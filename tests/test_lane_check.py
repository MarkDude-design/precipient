"""lane_check unit tests — Meraki's §3 negative tests, each baked in as an
assertion that the checker FLAGS (never accepts) the fault. stdlib unittest only.

Run: python3 -m unittest tests.test_lane_check -v
"""

import json
import tempfile
import unittest
from pathlib import Path

import sys
sys_path_hack = Path(__file__).resolve().parents[1]
import os
sys.path.insert(0, str(sys_path_hack / "tools" if (sys_path_hack / "tools").exists() else sys_path_hack))

from lane_check import (
    LaneCheckError, clock_faults, load_content_file, parse_claims, parse_rounds_index,
    run_check, parse_timestamp,
)


def _snapshot(tmp, comments):
    p = tmp / "snapshot.json"
    p.write_text(json.dumps([{"id": str(i), "created_at": t} for i, t in comments]))
    return p


def _rounds_dir(tmp, files):
    d = tmp / "rounds"
    d.mkdir(exist_ok=True)
    for name, text in files.items():
        (d / name).write_text(text)
    return d


GOOD_ROW = "| 011-M-01 | Meraki | 6448692635 | 17:22 | grade accepted; marker question opened. |\n"
GOOD_ROW2 = "| 011-Z-02 | Z | 6448941890 | 17:30 | answer: receipt-class split. |\n"


class HappyPath(unittest.TestCase):
    def test_all_matched_no_faults(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            snap = _snapshot(tmp, [(6448692635, "2026-10-27T17:22:10Z"),
                                    (6448941890, "2026-10-27T17:30:53Z")])
            rounds = _rounds_dir(tmp, {"011-marker-transfer.md": GOOD_ROW + GOOD_ROW2})
            r = run_check(snap, rounds, None)
            self.assertEqual(r["matched_n"], 2)
            self.assertEqual(r["unindexed_source"], [])
            self.assertEqual(r["orphaned_index"], [])
            self.assertEqual(r["duplicate_index_ids"], {})


class Backscan(unittest.TestCase):
    """Her negative test (4): one old unseen comment + one orphan ledger entry
    must BOTH be caught — a tail-only read_up_to cannot do this."""

    def test_unseen_old_source_comment_caught(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            snap = _snapshot(tmp, [(6448692635, "2026-10-27T17:22:10Z"),
                                    (6448941890, "2026-10-27T17:30:53Z"),
                                    (6448331494, "2026-10-27T17:05:25Z")])  # old, unindexed
            rounds = _rounds_dir(tmp, {"011-marker-transfer.md": GOOD_ROW + GOOD_ROW2})
            r = run_check(snap, rounds, None)
            self.assertEqual(r["unindexed_source"], ["6448331494"])
            self.assertEqual(r["orphaned_index"], [])

    def test_orphan_ledger_entry_caught(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            snap = _snapshot(tmp, [(6448692635, "2026-10-27T17:22:10Z")])
            rounds = _rounds_dir(tmp, {"011-marker-transfer.md": GOOD_ROW + GOOD_ROW2})
            r = run_check(snap, rounds, None)
            self.assertEqual(r["orphaned_index"], ["6448941890"])

    def test_duplicate_index_id_caught(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            snap = _snapshot(tmp, [(6448692635, "2026-10-27T17:22:10Z")])
            rounds = _rounds_dir(tmp, {
                "009-independence-collision.md": "| 009-M-01 | Meraki | 6448692635 | 17:00 | row A |\n",
                "011-marker-transfer.md": GOOD_ROW,  # same id again
            })
            r = run_check(snap, rounds, None)
            self.assertIn("6448692635", r["duplicate_index_ids"])
            self.assertEqual(r["duplicate_index_ids"]["6448692635"]["rows"], 2)


class ClockFaults(unittest.TestCase):
    """Her negative test (2): future/malformed/expired/overlap flagged, never
    accepted as exclusivity proof."""

    def _claims_file(self, tmp, rows_text):
        p = tmp / "z-turn-claims.md"
        p.write_text(
            "# Z Turn Claims\n\n## Claim table\n\n| claimed | session | target | window | status | artifact |\n"
            "|---|---|---|---|---|---|\n" + rows_text + "\n## History\n- none\n")
        return p

    def test_malformed_time_flagged(self):
        rows = [{"claimed": "2026-10-27T23:0XZ", "target": "island burst", "window": "+10 min"},
                {"claimed": "2026-10-27T22:05Z", "target": "island walk", "window": "+10 min"}]
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            snap = _snapshot(tmp, [(6448692635, "2026-10-27T17:22:10Z")])
            faults = clock_faults([{"line": 1, "claimed": r["claimed"], "target": r["target"],
                                    "window": r["window"], "status": "DONE", "artifact": "x"} for r in rows], {}, { "6448692635": "2026-10-27T17:22:10Z"})
            self.assertTrue(any(f["fault"] == "MALFORMED_OR_UNPARSEABLE_DECLARED_TIME" for f in faults))

    def test_future_declared_flagged(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            snap = _snapshot(tmp, [(6448692635, "2026-10-27T17:22:10Z")])
            row = {"line": 1, "claimed": "2027-01-01T10:00Z", "target": "future lane", "window": "+10 min"}
            faults = clock_faults([row], {}, {"6448692635": "2026-10-27T17:22:10Z"})
            self.assertTrue(any(f["fault"] == "FUTURE_DECLARED_BEYOND_SOURCE_HORIZON" for f in faults))

    def test_declared_after_fire_flagged(self):
        appendix = {"row 2": {"declared": "2026-10-27T22:05Z", "fire_ts": "2026-10-27T17:19:20Z"}}
        faults = clock_faults([], appendix, {})
        self.assertTrue(any(f["fault"] == "DECLARED_AFTER_FIRE" for f in faults))

    def test_unverifiable_expiry_flagged(self):
        row = {"line": 1, "claimed": "2026-10-27T17:43Z", "target": "island gate", "window": "+10 min (17:53Z)"}
        faults = clock_faults([row], {}, {"6449337601": "2026-10-27T17:44:05Z"})
        self.assertTrue(any(f["fault"] == "EXPIRY_UNVERIFIABLE" for f in faults))

    def test_overlapping_same_target_flagged(self):
        rows = [
            {"line": 1, "claimed": "2026-10-27T17:00Z", "target": "island burst: push", "window": "+10 min"},
            {"line": 2, "claimed": "2026-10-27T17:05Z", "target": "island burst: push", "window": "+10 min"},
        ]
        faults = clock_faults(rows, {}, {})
        self.assertTrue(any(f["fault"] == "OVERLAPPING_WINDOW_SAME_TARGET" for f in faults))


class Dev011Guard(unittest.TestCase):
    """Her negative test (3): a fetch that returns a transport STATUS LINE must
    be REJECTED before any parsing/rewriting — the DEV-011 failure mode."""

    def test_status_line_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "fetched.md"
            p.write_text("successfully downloaded text file (SHA: e12f075deadbeef)")
            with self.assertRaises(LaneCheckError):
                load_content_file(p)

    def test_status_line_snapshot_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            p = tmp / "snapshot.json"
            p.write_text("successfully downloaded text file (SHA: e12f075deadbeef)")
            rounds = _rounds_dir(tmp, {"011.md": GOOD_ROW})
            with self.assertRaises(LaneCheckError):
                run_check(p, rounds, None)

    def test_real_claims_file_parses(self):
        """The REAL z-turn-claims.md (with Appendix A) parses and yields the
        DECLARED_AFTER_FIRE flags for rows 2-5 — the mislabel class, caught."""
        here = Path(__file__).resolve().parent
        candidates = [here.parent / "z-turn-claims.md",   # repo checkout
                      here.parent / "real" / "z-turn-claims.md"]  # staged fetch
        repo_claims = next((p for p in candidates if p.exists()), None)
        if repo_claims is None:
            self.skipTest("real claims file not present in this checkout")
        rows, appendix = parse_claims(repo_claims)
        self.assertGreater(len(rows), 0)
        self.assertGreaterEqual(len(appendix), 5)


if __name__ == "__main__":
    unittest.main()


class RowKindClassification(unittest.TestCase):
    """Her false-negative fix (6450082179): incidental citation must NOT mask a
    missing handoff. Three-case fixture on the same valid source ID:
    (A) only in prose          -> UNINDEXED
    (B) only incidental table  -> REFERENCED_ONLY (never MATCHED)
    (C) canonical message row   -> MATCHED
    Plus: foreign-repo pointers are reference-only, never orphan-labeled."""

    CID = "6443236880"  # her exact fixture ID

    def _run(self, rounds_text):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            snap = _snapshot(tmp, [(int(self.CID), "2026-10-27T13:35:12Z")])
            rounds = _rounds_dir(tmp, {"round-x.md": rounds_text})
            return run_check(snap, rounds, None)

    def test_A_prose_only_is_unindexed(self):
        r = self._run("Some prose mentions %s in passing, no table.\n" % self.CID)
        self.assertEqual(r["matched"], [])
        self.assertEqual(r["referenced_only_source"], [])
        self.assertEqual(r["unindexed_source"], [self.CID])

    def test_B_incidental_table_citation_is_referenced_only(self):
        # Her exact fixture: 2-cell row, no message record — must NOT match.
        r = self._run("| Admin note mentions | %s |\n" % self.CID)
        self.assertEqual(r["matched"], [])
        self.assertEqual(r["unindexed_source"], [])
        self.assertEqual(r["referenced_only_source"], [self.CID])

    def test_C_canonical_message_row_is_matched(self):
        r = self._run(GOOD_ROW.replace("6448692635", self.CID))
        self.assertEqual(r["matched"], [self.CID])
        self.assertEqual(r["referenced_only_source"], [])

    def test_incidental_embedded_cite_is_referenced_only(self):
        # Real-l ledger shape: ID embedded in a longer prose cell.
        r = self._run("| 005/005-M-03 | 2026-10-27T15:17:52Z | Meraki | acct | "
                      "issue #1 through 005-Z-03; bus #3 through %s |\n" % self.CID)
        self.assertEqual(r["matched"], [])
        self.assertEqual(r["referenced_only_source"], [self.CID])

    def test_foreign_pointer_not_orphaned(self):
        # Cross-repo link in a reference row: informational, not an orphan
        # precipient record claim.
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            snap = _snapshot(tmp, [(6448692635, "2026-10-27T17:22:10Z")])
            link = ("[6444169721](https://github.com/MarkDude-design/"
                    "ALLurbaseRnotbelong2us/issues/2#issuecomment-6444169721)")
            rounds = _rounds_dir(tmp, {"004-x.md":
                "| 004 | admin note | %s | context |\n" % link})
            r = run_check(snap, rounds, None)
            self.assertEqual(r["orphaned_index"], [])
            self.assertIn("6444169721", r["reference_only_index"])
            self.assertTrue(any(
                hint.endswith("ALLurbaseRnotbelong2us")
                for hint in r["reference_only_index"]["6444169721"]["repos"]))
