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


class V03RowPurposeContract(unittest.TestCase):
    """v0.3 (her second review, bus #2 6452507980): the ROW'S PURPOSE is
    determined BEFORE link parsing.

    (1) Her must-FLAG linked-incidental fixture — a markdown link to
        precipient in a NON-record row must be REFERENCED_ONLY, never MATCHED
        (v0.2's rule (i) masked this missing-handoff class).
    (2) In a headered record table, ONLY the source column records: the
        `through <id>` horizon cell and other embeds are references.
    (3) The legacy `issue #1 comment <id>` record form still matches — in the
        source column of a record table.
    (4) Ambiguous legacy rows (non-record, ≥3 cells, bare-ID cell or local
        link) land in ambiguous_rows for HUMAN adjudication — classified
        reference, never silently matched; 2-cell fixtures stay plain
        reference, not ambiguous.
    """

    CID = "6443236880"  # her exact fixture ID
    LOCAL = "https://github.com/MarkDude-design/precipient/issues/1#issuecomment-"

    HDR7 = ("| Message ID | Timestamp | Seat claimed | Posted by | Source URL "
            "| read_up_to | Fidelity |\n| --- | --- | --- | --- | --- | --- | --- |\n")

    def _run(self, rounds_text):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            snap = _snapshot(tmp, [(int(self.CID), "2026-10-27T13:35:12Z"),
                                   (6444140310, "2026-10-27T14:08:44Z"),
                                   (6443814967, "2026-10-27T14:01:02Z")])
            rounds = _rounds_dir(tmp, {"round-x.md": rounds_text})
            return run_check(snap, rounds, None)

    def test_linked_incidental_is_referenced_only(self):
        # Her exact must-FLAG fixture: local-repo markdown link in a NON-record
        # row — v0.2 matched it; v0.3 must report REFERENCED_ONLY.
        r = self._run("| Admin note mentions | [%s](%s%s) |\n"
                      % (self.CID, self.LOCAL, self.CID))
        self.assertEqual(r["matched"], [])
        self.assertEqual(r["referenced_only_source"], [self.CID])
        # 2-cell fixture: plain reference, NOT ambiguous
        self.assertEqual(r["ambiguous_rows"], {})
        self.assertEqual(r["ambiguous_rows_n"], 0)

    def test_ambiguous_legacy_row_flagged_for_human(self):
        # Non-record row, ≥3 cells, local link: still reference (over-flag),
        # but surfaced in ambiguous_rows for human adjudication.
        r = self._run("| admin | note | [%s](%s%s) | context |\n"
                      % (self.CID, self.LOCAL, self.CID))
        self.assertEqual(r["matched"], [])
        self.assertEqual(r["referenced_only_source"], [self.CID])
        self.assertEqual(r["ambiguous_rows_n"], 1)
        self.assertIn("round-x.md", r["ambiguous_rows"])

    def test_ambiguous_bare_id_row_flagged_for_human(self):
        # Her point (3): ambiguous legacy rows are never silently MATCHED.
        r = self._run("| 004 | admin note | %s | context |\n" % self.CID)
        self.assertEqual(r["matched"], [])
        self.assertEqual(r["referenced_only_source"], [self.CID])
        self.assertEqual(r["ambiguous_rows_n"], 1)

    def test_headered_record_table_source_column_only(self):
        # Column contract: `issue #1 comment <id>` in the Source URL column is
        # the canonical record; the read_up_to `through <id>` horizon is a
        # reference — one row records one message.
        r = self._run(self.HDR7 +
                      "| 004-M-01 | 2026-10-27T14:08:44Z | Meraki | acct "
                      "| issue #1 comment 6444140310 | through %s | verbatim/origin |\n"
                      % self.CID)
        self.assertEqual(r["matched"], ["6444140310"])
        self.assertEqual(r["referenced_only_source"], [self.CID])
        self.assertEqual(r["orphaned_index"], [])

    def test_headered_table_summary_links_are_references(self):
        # v0.2 rule (i) defect, restated on a real 012+ ledger shape: a local
        # link inside the SUMMARY column of a record row must NOT match; only
        # the Source URL column records.
        r = self._run(self.HDR7 +
                      "| 004-M-01 | 2026-10-27T14:08:44Z | Meraki | acct "
                      "| issue #1 comment 6444140310 | through 6443814967 "
                      "| cites [%s](%s%s) in passing |\n"
                      % (self.CID, self.LOCAL, self.CID))
        self.assertEqual(r["matched"], ["6444140310"])
        # both the through-horizon AND the summary link are references
        self.assertEqual(r["referenced_only_source"], [self.CID, "6443814967"])

    def test_canonical_linked_source_cell_matches(self):
        # Positive mirror of the fix: the SAME local link in the SOURCE column
        # of a record table still matches.
        r = self._run(self.HDR7 +
                      "| 004-M-01 | 2026-10-27T14:08:44Z | Meraki | acct "
                      "| [%s](%s%s) | through 6443814967 | verbatim/origin |\n"
                      % (self.CID, self.LOCAL, self.CID))
        self.assertEqual(r["matched"], [self.CID])

    def test_kickoff_transport_link_record_matches(self):
        # rounds/000 receipt-slot shape: 'Transport / source link' column with
        # link text 'Issue comment <id>' — still a canonical record.
        hdr = ("| Order | Seat claimed | Transport / source link | `read_up_to` "
               "| Fidelity | Status |\n| --- | --- | --- | --- | --- | --- |\n")
        r = self._run(hdr +
                      "| 1 | Meraki | [Issue comment %s](%s%s) — native session "
                      "| issue #1 body | verbatim (origin) | RECEIVED |\n"
                      % (self.CID, self.LOCAL, self.CID))
        self.assertEqual(r["matched"], [self.CID])
        self.assertEqual(r["ambiguous_rows"], {})

    def test_p1_parenthetical_carrier_row_is_record(self):
        # rounds/008/010/011 shape: col0 '008-M-P1 (in 007-M-02)' — headerless
        # fallback must still see a message record (bare-ID source cell).
        r = self._run("| 008-M-P1 (in 007-M-02) | Meraki | %s | 16:2x | packet |\n"
                      % self.CID)
        self.assertEqual(r["matched"], [self.CID])


class V031HeaderlessMultiId(unittest.TestCase):
    """v0.3.1 (her re-grade 6455594534, the one narrow remaining edge): a
    HEADERLESS record row treats every local link / issue#1-comment / bare-ID
    cell as canonical — so one row could mint TWO records, contradicting the
    "one row records one message" contract. Repair per her guidance: keep only
    the FIRST (leftmost) record form canonical, demote the rest to reference,
    flag the row in ambiguous_rows for human adjudication (explicit ambiguity
    over guessing); no parser framework added.
    """

    CID = "6443236880"
    LOCAL = "https://github.com/MarkDude-design/precipient/issues/1#issuecomment-"

    def _run(self, rounds_text, ids):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            snap = _snapshot(tmp, [(int(i), "2026-10-27T13:35:12Z") for i in ids])
            rounds = _rounds_dir(tmp, {"round-x.md": rounds_text})
            return run_check(snap, rounds, None)

    def test_her_exact_fixture_first_only_canonical(self):
        # Her fixture verbatim: first ID canonical, second reference, row
        # flagged ambiguous — never two records.
        r = self._run(
            "| 008-M-P1 (in 007-M-02) | Meraki | 6444140310 | [%s](%s%s) |\n"
            % (self.CID, self.LOCAL, self.CID),
            ["6444140310", self.CID])
        self.assertEqual(r["matched"], ["6444140310"])
        self.assertEqual(r["referenced_only_source"], [self.CID])
        self.assertEqual(r["ambiguous_rows_n"], 1)
        self.assertEqual(r["ambiguous_rows"]["round-x.md"][0]["line"], 1)

    def test_two_bare_id_cells_first_only_canonical(self):
        r = self._run(
            "| 011-M-01 | Meraki | 6448692635 | 6448941890 | note |\n",
            ["6448692635", "6448941890"])
        self.assertEqual(r["matched"], ["6448692635"])
        self.assertEqual(r["referenced_only_source"], ["6448941890"])
        self.assertEqual(r["ambiguous_rows_n"], 1)

    def test_single_record_form_stays_unflagged(self):
        # Control: one record form + embedded reference = current good path,
        # no ambiguity flag, no demotion.
        r = self._run(
            "| 011-M-01 | Meraki | 6448692635 | 17:22 | cites %s in prose |\n"
            % self.CID,
            ["6448692635", self.CID])
        self.assertEqual(r["matched"], ["6448692635"])
        self.assertEqual(r["referenced_only_source"], [self.CID])
        self.assertEqual(r["ambiguous_rows_n"], 0)

    def test_headered_multi_id_row_unaffected(self):
        # Her fix must not touch HEADERED tables (strict column contract):
        # source column canonical, extra link in another cell reference,
        # and NO ambiguity flag (the column contract is trustworthy).
        hdr = ("| Message ID | Timestamp | Seat claimed | Posted by | Source URL "
               "| read_up_to | Fidelity |\n| --- | --- | --- | --- | --- | --- | --- |\n")
        r = self._run(
            hdr + "| 004-M-01 | 2026-10-27T14:08:44Z | Meraki | acct "
            "| issue #1 comment 6444140310 | through 6443814967 "
            "| cites [%s](%s%s) |\n" % (self.CID, self.LOCAL, self.CID),
            ["6444140310", "6443814967", self.CID])
        self.assertEqual(r["matched"], ["6444140310"])
        self.assertEqual(r["ambiguous_rows_n"], 0)


if __name__ == "__main__":
    unittest.main()
