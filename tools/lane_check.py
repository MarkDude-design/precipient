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

v0.3 (Meraki's second review, bus #2 6452507980): row-purpose/column contract
BEFORE link parsing.
  Defect fixed: v0.2 rule (i) treated ANY bare-digit markdown link to
  MarkDude-design/precipient as a canonical message record, so a
  LINKED-INCIDENTAL citation (her must-FLAG fixture
  `| Admin note mentions | [6443236880](…#issuecomment-6443236880) |`) was
  matched instead of reported REFERENCED_ONLY — masking a missing handoff.
  v0.2 rule (iii) likewise matched any `issue #1 comment <id>` anywhere.
  Repair: determine the ROW'S PURPOSE FIRST, then read IDs against it:
  - A table with a header row declaring a SOURCE COLUMN (a header cell matching
    source-url / comment / comment-id / transport-source-link) is a MESSAGE
    RECORD TABLE: only IDs in the designated source column are canonical
    (bare ID, `issue #1 comment <id>`, local-repo link, or `Issue comment <id>`
    link text). Every other ID in the row — read_up_to / `through <id>`
    horizons, summary embeds — is a REFERENCE (one row records one message).
  - Headerless pipe blocks fall back to a per-row contract: a row is a record
    row iff column 0 is a compact message-label token (011-M-01 / 020/020-Z-01 /
    006-M-choice / 008-M-P1 (in 007-M-02) shapes); canonical = bare-ID cell,
    `issue #1 comment <id>` form, or local-repo link; other IDs reference.
  - Any OTHER row containing IDs is a non-record row: every ID in it is a
    REFERENCE, and — when it has ≥3 cells and holds a bare-ID cell or a
    local-repo bare-digit link — it is additionally listed in the
    ambiguous_rows bucket FOR HUMAN ADJUDICATION (over-flag, never silently
    matched; 2-cell fixtures stay plain reference, not ambiguous).
  v0.3 also ships the one real repair her review called for: an append-only
  canonical row for 004-Z-01 (comment 6443982750) in rounds/004 — see
  reports/adjudications-2026-10-27.md. Other v0.2 dispositions stand
  (6443236880 = EXCLUDED_NONROUND; 6444169721 / 6445766848 =
  FOREIGN_SOURCE_REFERENCE — the rounds/004 admin-row locator flag stands until
  an author appendix corrects the locator; 6448264628 = bullets-vs-tables
  coverage limitation, a ledger-format question, not a checker fix).

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


LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://[^\s)]+)\)")
LOCAL_REPO = "MarkDude-design/precipient"
# Explicit record form used by real message tables when the ID is embedded:
ISSUE1_COMMENT_RE = re.compile(r"issue\s*#?1?\s*comment\s+(\d{10,11})", re.IGNORECASE)
# v0.3: header cell that declares a SOURCE COLUMN — table purpose contract.
SOURCE_COL_RE = re.compile(
    r"^(source(\s*url)?|comment(\s*id)?|transport(\s*/\s*source\s*link)?)$", re.IGNORECASE)
# v0.3: message-label token in column 0 for HEADERLESS record rows
# (011-M-01 / 020/020-Z-01 / 000/Z-01 / 006-M-choice / 008-M-P1 (in 007-M-02)).
MSG_LABEL_RE = re.compile(
    r"^(?:\d{3}/)?(?:\d{3}-)?[MZ]-[A-Za-z0-9][A-Za-z0-9-]*(?:\s+\(in\s+[\w./-]+\))?$")
SEP_ROW_RE = re.compile(r"^\|[\s\-:|]+\|?$")


def _link_repo(url: str):
    m = re.search(r"github\.com/([^/\s]+)/([^/\s]+)/", url)
    return "/".join(m.groups()) if m else None


def _link_local_ids(text: str, url: str):
    """IDs carried by one markdown link: digits in the link text or the URL
    fragment (covers both `[6454176799](…)` and `[Issue comment 6440653310](…)`)."""
    ids = set(COMMENT_ID_RE.findall(text)) | set(COMMENT_ID_RE.findall(url))
    return sorted(ids)


def classify_record_cell(cell: str):
    """Canonical record IDs inside a SOURCE-column cell (v0.3 contract).
    Bare ID, `issue #1 comment <id>`, or a local-repo markdown link. Any OTHER
    digits in the cell are references (an honest source cell carries one)."""
    out = []
    consumed = set()
    for m in LINK_RE.finditer(cell):
        repo = _link_repo(m.group(2))
        if repo is None or repo == LOCAL_REPO:
            for cid in _link_local_ids(m.group(1), m.group(2)):
                out.append((cid, "canonical", repo))
                consumed.add(cid)
        else:
            for cid in _link_local_ids(m.group(1), m.group(2)):
                out.append((cid, "reference", repo))
    for m in ISSUE1_COMMENT_RE.finditer(cell):
        out.append((m.group(1), "canonical", None))
        consumed.add(m.group(1))
    rest = cell
    for m in LINK_RE.finditer(cell):
        rest = rest.replace(m.group(0), " ")
    for m in ISSUE1_COMMENT_RE.finditer(cell):
        rest = rest.replace(m.group(0), " ")
    for cid in set(COMMENT_ID_RE.findall(rest)):
        kind = "canonical" if (rest.strip() == cid and cid not in consumed) else "reference"
        out.append((cid, kind, None))
    return out


def classify_row_cells(row: str, source_col=None):
    """Split a table row into cells; classify every comment ID found.

    v0.3 row-purpose contract (bus #2 6452507980):
    - RECORD row (source_col given = headered message table, or headerless row
      whose column 0 is a message-label token): the source-column cell's record
      forms are CANONICAL; every other ID in the row is a REFERENCE — one row
      records one message; horizons/summaries never upgrade to records.
    - NON-record row: every ID is a REFERENCE (foreign links stay repo-tagged);
      rows with ≥3 cells holding a bare-ID cell or local-repo bare-digit link
      are ALSO reported in ambiguous_rows for human adjudication — over-flag,
      never silently matched.
    """
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    strict = source_col is not None
    headerless_record = len(cells) >= 3 and bool(MSG_LABEL_RE.match(cells[0]))
    is_record = strict or headerless_record
    out = []
    ambiguous = False
    for i, cell in enumerate(cells):
        if strict and i == source_col:
            out.extend(classify_record_cell(cell))
            continue
        if strict:
            # Column contract: in a headered record table ONLY the source
            # column records; every other cell (read horizons, summaries,
            # admin notes) is a reference — the linked-incidental fix.
            for m in LINK_RE.finditer(cell):
                repo = _link_repo(m.group(2))
                for cid in _link_local_ids(m.group(1), m.group(2)):
                    out.append((cid, "reference", repo))
            rest = LINK_RE.sub(" ", cell)
            for m in ISSUE1_COMMENT_RE.finditer(rest):
                out.append((m.group(1), "reference", None))
            rest = ISSUE1_COMMENT_RE.sub(" ", rest)
            for cid in set(COMMENT_ID_RE.findall(rest)):
                out.append((cid, "reference", None))
            continue
        for m in LINK_RE.finditer(cell):
            repo = _link_repo(m.group(2))
            for cid in _link_local_ids(m.group(1), m.group(2)):
                if repo is None or repo == LOCAL_REPO:
                    if is_record:
                        out.append((cid, "canonical", repo))
                    else:
                        out.append((cid, "reference", repo))
                        ambiguous = True
                else:
                    out.append((cid, "reference", repo))
        if LINK_RE.search(cell):
            continue
        for m in ISSUE1_COMMENT_RE.finditer(cell):
            if is_record:
                out.append((m.group(1), "canonical", None))
            else:
                out.append((m.group(1), "reference", None))
        rest = ISSUE1_COMMENT_RE.sub(" ", cell)
        for cid in set(COMMENT_ID_RE.findall(rest)):
            if rest.strip() == cid and is_record:
                # headerless record row: bare-ID cell = the message record
                # (v0.2 rule (ii), retained for the column-less fallback)
                out.append((cid, "canonical", None))
            else:
                out.append((cid, "reference", None))
                if rest.strip() == cid:
                    ambiguous = True
    if not is_record and len(cells) >= 3 and ambiguous:
        return out, True
    return out, False


def parse_rounds_index(rounds_dir: Path):
    """Parse every rounds/*.md table; return ({comment_id: [provenance]},
    {filename: [{line, row}]} ambiguous rows) with the v0.3 row-purpose
    classification (record table via source-column header, else reference)."""
    index: dict[str, list[dict]] = {}
    ambiguous: dict[str, list[dict]] = {}
    files = sorted(p for p in rounds_dir.glob("*.md")) if rounds_dir.is_dir() else []
    if not files:
        raise LaneCheckError(f"no rounds .md files found under {rounds_dir}")
    for f in files:
        text = load_content_file(f)
        lines = text.splitlines()
        i = 0
        while i < len(lines):
            if not lines[i].strip().startswith("|"):
                i += 1
                continue
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append((i + 1, lines[i].strip()))
                i += 1
            # Header + separator present? → column contract table.
            source_col = None
            body = block
            if len(block) >= 2 and SEP_ROW_RE.match(block[1][1]):
                header_cells = [c.strip().strip("`") for c in
                                block[0][1].strip().strip("|").split("|")]
                for k, hc in enumerate(header_cells):
                    if SOURCE_COL_RE.match(hc):
                        source_col = k
                        break
                body = block[2:]
            for lineno, stripped in body:
                if set(stripped.replace("|", "").strip()) <= {"-", " "}:
                    continue
                classified, is_amb = classify_row_cells(stripped, source_col)
                seen_in_row = set()
                for cid, kind, repo in classified:
                    if (cid, kind) in seen_in_row:
                        continue
                    seen_in_row.add((cid, kind))
                    index.setdefault(cid, []).append(
                        {"file": f.name, "line": lineno, "kind": kind, "repo": repo,
                         "row": stripped[:160]}
                    )
                if source_col is None and is_amb:
                    ambiguous.setdefault(f.name, []).append(
                        {"line": lineno, "row": stripped[:160],
                         "why": "non-record row with bare-ID cell or local link"})
    return index, ambiguous


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
    index, ambiguous_rows = parse_rounds_index(rounds_dir)
    source_ids = set(source)
    canonical_ids = {cid for cid, prov in index.items()
                     if any(p.get("kind") == "canonical" for p in prov)}
    referenced_ids = set(index) - canonical_ids
    report = {
        "tool": "lane_check v0.3 (Meraki's second review 6452507980: "
                "row-purpose/column contract BEFORE link parsing; "
                "source-column record tables; linked-incidental citations are "
                "REFERENCED_ONLY; ambiguous legacy rows flagged for human "
                "adjudication, never silently matched)",
        "scope_honesty": "advisory consistency check; authenticates nothing; "
                        "declared claim times are DECLARED_UNVERIFIED (Appendix A)",
        "source_n": len(source_ids),
        "index_n": len(index),
        "canonical_index_n": len(canonical_ids),
        # matched ONLY on canonical message records (her case C)
        "matched": sorted(source_ids & canonical_ids),
        # source cited ONLY incidentally (her case B) — reported, never matched
        "referenced_only_source": sorted((source_ids & referenced_ids)
                                         - canonical_ids),
        # source in NO table row at all (her case A; prose/bullet events are
        # outside row scope — documented limitation)
        "unindexed_source": sorted(source_ids - set(index)),
        # canonical rows claiming a record the source does not have —
        # the true missing-record class
        "orphaned_index": sorted(canonical_ids - source_ids),
        # ids cited only incidentally and absent from source: foreign pointers,
        # cross-thread cites — informational, NOT orphan-labeled
        "reference_only_index": {
            cid: {"files": sorted({p["file"] for p in index[cid]}),
                  "repos": sorted({p["repo"] for p in index[cid]
                                   if p.get("repo")}) or ["(no URL in row)"]}
            for cid in sorted((referenced_ids - source_ids) - canonical_ids)
        },
        # v0.3: non-record rows where purpose is genuinely ambiguous — human
        # adjudication; still classified reference (over-flag, never mask)
        "ambiguous_rows": ambiguous_rows,
        "ambiguous_rows_n": sum(len(v) for v in ambiguous_rows.values()),
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
    lines += [f"  - {c}" for c in r['unindexed_source']]
    lines.append(f"orphaned_index (CANONICAL rows, NOT in source — missing-record class): "
                 f"{len(r['orphaned_index'])}")
    lines += [f"  - {c}" for c in r['orphaned_index']]
    lines.append(f"referenced_only_source (in thread, ONLY incidental citations — "
                 f"her case B, never matched): {len(r['referenced_only_source'])}")
    lines += [f"  - {c}" for c in r['referenced_only_source']]
    lines.append(f"reference_only_index (incidental cites, NOT in source — foreign/"
                 f"cross-thread pointers, informational): {len(r['reference_only_index'])}")
    for c, d in r['reference_only_index'].items():
        lines.append(f"  - {c}  rows in: {', '.join(d['files'])}"
                     f"  repo-hint: {', '.join(d['repos'])}")
    amb = r.get("ambiguous_rows", {})
    lines.append(f"ambiguous_rows (non-record rows with ID cells — HUMAN ADJUDICATION, "
                 f"classified reference, never silently matched): {r.get('ambiguous_rows_n', 0)}")
    for fname, rows in amb.items():
        for row in rows:
            lines.append(f"  - {fname}:{row['line']}  {row['row']}")
    lines.append(f"duplicate_index_ids (flagged for review, not asserted errors): "
                 f"{len(r['duplicate_index_ids'])}")
    for cid, d in r['duplicate_index_ids'].items():
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
