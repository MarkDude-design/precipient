#!/usr/bin/env python3
"""lane_check — offline bidirectional lane checker (read-only, stdlib only).

Bus #2 (6449523930 §3) "smallest first deliverable": an OFFLINE, read-only
Python stdlib checker against the EXISTING 009 collision + 001/002 corrections
+ DEV-011 example, outputting a short matched / missing / duplicate /
unverifiable report. No new bot, no scheduler, no network, no spend.

What it checks:
  1. BACK-SCAN (bidirectional): every source message ID vs every rounds-ledger
     index ID — flags unindexed_source AND orphaned_index. A tail-only
     read_up_to cannot do this; this can (it is the whole point).
  2. DUPLICATES: the same comment ID claimed by more than one ledger row.
  3. CLOCK FAULTS on the sync-gear claim table: malformed / future /
     declared-after-fire / unverifiable-expiry / overlapping-window rows —
     flagged, never accepted as proof of exclusivity.
  4. DEV-011 CLASS: any fetched content file that is a transport status line
     ("successfully downloaded text file (SHA: …)") is REJECTED before parsing,
     exactly the failure mode that destroyed five branch files on 2026-10-27.

Honest scope: this is an advisory consistency checker over files that exist;
it does NOT authenticate seats, verify merges, or create a lease. Per Appendix A
(z-turn-claims.md): declared claim times are DECLARED_UNVERIFIED until a
server-receipted claim write exists.

Usage:
  python3 tools/lane_check.py --snapshot snapshot.json --rounds-dir rounds \
      --claims z-turn-claims.md [--out report.json]

Snapshot format: JSON array of {"id": "<10+ digit str>", "created_at": "<RFC3339>"}.
For the precipient research thread: any export of GET /repos/{owner}/{repo}/issues/1/comments
(id + created_at fields suffice). The checker is source-agnostic.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

STATUS_LINE_RE = re.compile(r"^\s*successfully downloaded text file", re.IGNORECASE)
COMMENT_ID_RE = re.compile(r"\b(\d{10,11})\b")
TS_RE = re.compile(r"(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2})(?::(\d{2}))?Z?")


class LaneCheckError(Exception):
    """Fatal input problem (e.g. DEV-011-class contamination)."""


def load_content_file(path: Path) -> str:
    """Read a repo-content file; REJECT transport status lines (DEV-011 class)."""
    text = path.read_text(encoding="utf-8")
    if STATUS_LINE_RE.match(text):
        raise LaneCheckError(
            f"DEV-011 class: {path} contains a transport STATUS LINE, not file "
            "content ('successfully downloaded text file (SHA: …)'). Refusing to "
            "parse; re-fetch via the resource envelope (res[1].resource.text)."
        )
    return text


def parse_timestamp(s: str):
    """Parse an RFC3339-ish UTC timestamp; return aware datetime or None."""
    if not s or any(ch in s.upper() for ch in ("X",)):
        return None
    m = TS_RE.search(s)
    if not m:
        return None
    h, mi = int(m.group(2).split(":")[0]), int(m.group(2).split(":")[1])
    sec = int(m.group(3) or 0)
    try:
        return datetime(
            int(m.group(1)[:4]), int(m.group(1)[5:7]), int(m.group(1)[8:10]),
            h, mi, sec, tzinfo=timezone.utc,
        )
    except ValueError:
        return None


def load_snapshot(path: Path):
    """Load + validate the source snapshot; returns {id: created_at}."""
    data = json.loads(load_content_file(path).strip() or "[]")
    if not isinstance(data, list):
        raise LaneCheckError("snapshot must be a JSON array")
    source: dict[str, str] = {}
    malformed = []
    for item in data:
        cid = str(item.get("id", ""))
        ts = item.get("created_at", "")
        if not COMMENT_ID_RE.fullmatch(cid):
            malformed.append({"id": cid, "why": "id not a 10-11 digit comment id"})
            continue
        if parse_timestamp(ts) is None:
            malformed.append({"id": cid, "why": f"created_at unparseable: {ts!r}"})
            continue
        source[cid] = ts
    return source, malformed


def parse_rounds_index(rounds_dir: Path):
    """Parse every rounds/*.md message table; return {comment_id: [provenance]}."""
    index: dict[str, list[dict]] = {}
    files = sorted(p for p in rounds_dir.glob("*.md")) if rounds_dir.is_dir() else []
    if not files:
        raise LaneCheckError(f"no rounds .md files found under {rounds_dir}")
    for f in files:
        text = load_content_file(f)
        for lineno, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            if not stripped.startswith("|"):
                continue
            for cid in COMMENT_ID_RE.findall(stripped):
                index.setdefault(cid, []).append(
                    {"file": f.name, "line": lineno, "row": stripped[:160]}
                )
    return index


def parse_claims(claims_path: Path):
    """Parse the sync-gear claim table + Appendix A fire receipts."""
    text = load_content_file(claims_path)
    rows = []
    appendix_fires = {}
    in_appendix = False
    for lineno, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if s.startswith("## "):
            in_appendix = "APPENDIX" in s.upper()
            continue
        if not s.startswith("|") or set(s.replace("|", "").strip()) <= {"-", " "}:
            continue
        cols = [c.strip() for c in s.strip("|").split("|")]
        if "claimed" in cols[0].lower() or set(cols[0].lower()) <= {"-", " ", ":"}:
            continue  # header / separator row
        if in_appendix and len(cols) == 5 and "Z" in cols[-1]:
            # Appendix A fire-receipt row: [row, declared, target, artifact, fire_ts]
            appendix_fires[cols[0]] = {"declared": cols[1], "fire_ts": cols[-1]}
        elif len(cols) >= 6:
            # Declared time = FIRST column that parses as a timestamp (handles both
            # legacy "time-first" rows and new "row-number, claimed_at_declared" rows).
            declared = next((c for c in cols if TS_RE.search(c)), cols[0])
            rows.append({"line": lineno, "claimed": declared, "target": cols[2],
                         "window": cols[-3], "status": cols[-2], "artifact": cols[-1]})
    return rows, appendix_fires


def clock_faults(claims_rows, appendix_fires, source):
    """Flag clock faults: malformed, future, declared-after-fire, unverifiable
    expiry, overlapping windows. Flagged, never accepted as proof."""
    horizon = max((parse_timestamp(ts) for ts in source.values()), default=None)
    faults = []
    declared_list = []
    for row in claims_rows:
        declared_raw = row["claimed"]
        declared = parse_timestamp(declared_raw)
        entry = {"row": declared_raw[:44], "line": row["line"]}
        if "X" in declared_raw.upper() or declared is None:
            faults.append({**entry, "fault": "MALFORMED_OR_UNPARSEABLE_DECLARED_TIME",
                           "detail": declared_raw})
            continue
        if horizon and declared > horizon + timedelta(minutes=15):
            faults.append({**entry, "fault": "FUTURE_DECLARED_BEYOND_SOURCE_HORIZON",
                           "detail": f"declared {declared_raw} vs latest source {horizon.isoformat()}"})
        if "X" in row["window"] or "+10" in row["window"] or "advisory" in row["window"].lower():
            faults.append({**entry, "fault": "EXPIRY_UNVERIFIABLE",
                           "detail": f"window {row['window']!r} is not a grounded UTC expiry"})
        declared_list.append({**row, "dt": declared})
    # declared-after-fire (Appendix A receipts): the mislabel class she caught.
    for key, rec in appendix_fires.items():
        d, f = parse_timestamp(rec["declared"]), parse_timestamp(rec["fire_ts"])
        if d and f and d > f:
            faults.append({"row": key, "fault": "DECLARED_AFTER_FIRE",
                           "detail": f"declared {rec['declared']} > fire {rec['fire_ts']}"})
        elif d is None:
            faults.append({"row": key, "fault": "MALFORMED_OR_UNPARSEABLE_DECLARED_TIME",
                           "detail": rec["declared"]})
    # overlapping windows on the same target (declared times only; advisory).
    for i in range(len(declared_list)):
        for j in range(i + 1, len(declared_list)):
            a, b = declared_list[i], declared_list[j]
            if a["target"].split(":")[0] != b["target"].split(":")[0]:
                continue
            start_a, start_b = a["dt"], b["dt"]
            if abs((start_a - start_b).total_seconds()) <= 10 * 60:
                faults.append({"row": f"rows@L{a['line']}+L{b['line']}",
                               "fault": "OVERLAPPING_WINDOW_SAME_TARGET",
                               "detail": f"{a['target'][:60]} vs {b['target'][:60]}"})
    return faults


def run_check(snapshot: Path, rounds_dir: Path, claims: Path | None):
    source, snap_malformed = load_snapshot(snapshot)
    index = parse_rounds_index(rounds_dir)
    source_ids, index_ids = set(source), set(index)
    report = {
        "tool": "lane_check v0 (bus #2 6449523930 §3 smallest first deliverable)",
        "scope_honesty": "advisory consistency check; authenticates nothing; "
                        "declared claim times are DECLARED_UNVERIFIED (Appendix A)",
        "source_n": len(source_ids),
        "index_n": len(index_ids),
        "matched": sorted(source_ids & index_ids),
        "unindexed_source": sorted(source_ids - index_ids),
        "orphaned_index": sorted(index_ids - source_ids),
        # Duplicates are FLAGGED FOR REVIEW, not asserted as errors: same-file
        # repeats are normal citation practice (message table + prose cross-ref);
        # true double-claims would be the same ID in two different round tables.
        "duplicate_index_ids": {
            cid: {"rows": len(prov), "files": sorted({p["file"] for p in prov}),
                  "provenance": prov}
            for cid, prov in index.items() if len(prov) > 1
        },
        "duplicate_index_ids_cross_file_only": {
            cid: v for cid, v in
            sorted({c: p for c, p in index.items()
                    if len(p) > 1 and len({q["file"] for q in p}) > 1}.items())
        },
        "snapshot_malformed_entries": snap_malformed,
    }
    if claims and claims.exists():
        rows, appendix = parse_claims(claims)
        report["claims_clock_faults"] = clock_faults(rows, appendix, source)
    report["matched_n"] = len(report["matched"])
    return report


def human_report(r: dict) -> str:
    lines = [
        "LANE CHECK — matched / missing / duplicate / unverifiable",
        f"source comments: {r['source_n']}   ledger-index ids: {r['index_n']}",
        f"matched: {r['matched_n']}",
        f"unindexed_source (in thread, NOT in any ledger): {len(r['unindexed_source'])}",
    ]
    lines += [f"  - {c}" for c in r["unindexed_source"]]
    lines.append(f"orphaned_index (in ledger, NOT in source): {len(r['orphaned_index'])}")
    lines += [f"  - {c}" for c in r["orphaned_index"]]
    lines.append(f"duplicate_index_ids (flagged for review, not asserted errors): "
                 f"{len(r['duplicate_index_ids'])}")
    for cid, d in r["duplicate_index_ids"].items():
        cross = "CROSS-FILE" if len(d["files"]) > 1 else "same-file citation"
        lines.append(f"  - {cid}: {d['rows']} rows in {', '.join(d['files'])} [{cross}]")
    crossf = r.get("duplicate_index_ids_cross_file_only", {})
    lines.append(f"  of which CROSS-FILE (the class worth a human look): {len(crossf)}")
    for cid, d in crossf.items():
        lines.append(f"    - {cid}: {', '.join(sorted({p['file'] for p in d}))}")
    faults = r.get("claims_clock_faults", [])
    lines.append(f"claims clock faults: {len(faults)}")
    for f_ in faults:
        lines.append(f"  - [{f_['fault']}] {f_.get('row','')} :: {f_.get('detail','')[:110]}")
    lines.append("unverifiable-as-lease: every declared claim time (no server-receipted "
                 "claim write exists); rows flagged above, not accepted as exclusivity proof.")
    lines.append("known limitation: index parse covers message-table rows and appendix "
                 "tables; events recorded ONLY in prose/bullet lists (e.g. the 009 "
                 "collision event list) are outside its row scope — cross-check by hand.")
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="lane_check")
    ap.add_argument("--snapshot", required=True, type=Path)
    ap.add_argument("--rounds-dir", required=True, type=Path)
    ap.add_argument("--claims", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args(argv)
    try:
        report = run_check(args.snapshot, args.rounds_dir, args.claims)
    except LaneCheckError as e:
        print(f"FATAL: {e}", file=sys.stderr)
        return 2
    print(human_report(report))
    if args.out:
        args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n",
                            encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
