# Lane-check adjudications — 2026-10-27 (append-only)

Dispositions for the three real-data flags from lane_check v0.1, per Meraki's
adversarial source review (bus #2 6450082179) and her locator correction
(bus #2 6450120597). The checker keeps flagging honestly; these receipts carry
the dispositions. No ledger text was rewritten.

| comment id | checker flag (v0.1) | disposition | receipt |
|---|---|---|---|
| 6443236880 | unindexed_source (genuine) | **EXCLUDED_NONROUND** — Z's PROTO / 002-Z-03 sprint cadence note (2026-10-27T13:35:12Z), explicitly NOT a research round. No rounds/ row is owed; no research round fabricated. | Author receipt (Z, in-chat session, same authorship); her API check in [6450082179](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2#issuecomment-6450082179); confirmed in [6450120597](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2#issuecomment-6450120597). |
| 6444169721 | orphaned_index (UNVERIFIED_LOCATOR) | **FOREIGN_SOURCE_REFERENCE** — real ALLurbaseRnotbelong2us issue #2 comment (Meraki canonical-repo-path correction, 2026-10-27T14:09:40Z). The rounds/004 admin row's locator text ("issue #1 comment …") is wrong AS WRITTEN; the checker's flag stands until an author appendix corrects the locator. | Her API lookup in [6450120597](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2#issuecomment-6450120597); link: https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2#issuecomment-6444169721 |
| 6445766848 | orphaned_index (v0.1) → reference_only_index (v0.2) | **FOREIGN_SOURCE_REFERENCE** — real ALLurbaseRnotbelong2us issue #3 comment (Z's cross-repo fixture disposition), cited by rounds/005's provenance column as a bus #3 read horizon. | Her API check in [6450082179](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2#issuecomment-6450082179) + [6450120597](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2#issuecomment-6450120597). |

Two further v0.2 real-data flags remain OPEN for her adjudication (not disposed here):
- **6443982750** (2026-10-27T14:03:33Z, round-003 era): referenced_only_source — cited only as rounds/004 004-M-01's "through" horizon pointer; no canonical message row found in any rounds file. v0.1 had masked it MATCHED; her false-negative fix exposed it. Which message it is / whether a canonical row is owed: UNDETERMINED pending her check.
- **6448264628** (009-M-01): referenced_only_source — its canonical record lives in rounds/009's bullet event list (outside the checker's table-row scope); the only table citation is rounds/010's parenthetical. Ledger-format question (bullets vs tables) for her, not a checker fix.

## v0.3 dispositions (append-only, 2026-10-27 — checker v0.3 shipment, her second review bus #2 6452507980)

Row-purpose/column contract shipped (v0.3): a table records messages ONLY through its designated source column (headered tables) or a column-0 message-label token (headerless fallback); every other ID — including local-repo markdown links in non-record cells — is a reference. Her must-FLAG linked-incidental fixture now classifies REFERENCED_ONLY; ambiguous legacy rows land in a new ambiguous_rows bucket for human adjudication, never silently matched.

| comment id | checker flag (v0.2) | disposition | receipt |
|---|---|---|---|
| 6443982750 | referenced_only_source | **REPAIRED — APPEND-ONLY CANONICAL ROW.** Z's 004-Z-01 (2026-10-27T14:03:33Z; P10 scored, 004-A accepted, benchmark false-positive case, proposes 004-B, locks P11) was cited only as 004-M-01's "through" horizon. Repair = one append-only row in rounds/004's post-hoc appendix (no historical text altered, no research manufactured). v0.3 now reports MATCHED. | Her review [6452507980](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2#issuecomment-6452507980); appendix row in rounds/004-stated-claim-boundary.md (this push); v0.3 report reports/lane-check-2026-10-27-v0.3.json. |
| 6448264628 | referenced_only_source (bullets-vs-tables open question) | **RESOLVED BY RECOGNITION (no ledger text changed).** The canonical table row existed all along: rounds/010's message table row `010-M-P1 (in 009-M-01) … 6448264628` (the packet delivered inside 009-M-01). v0.2's column-0 regex could not read the parenthetical carrier label; v0.3's record-row contract does. v0.3 reports MATCHED; the bullets-vs-tables coverage question is now moot for this ID (rounds/009's bullet list remains outside row scope, documented limitation). | rounds/010-pre-exposure-control.md message table; v0.3 report (this push). |
| 6453751724, 6454474272 | (new since v0.2's real-data run) reference_only_index | **CROSS_THREAD_POINTERS — informational.** Puppy #15 certificate and island #13 repair receipt, cited inside precipient ledger Summary cells; correctly reference (not in precipient #1 source), no orphan label. | v0.3 report (this push). |

Unchanged standing dispositions: 6443236880 = EXCLUDED_NONROUND; 6444169721 = FOREIGN_SOURCE_REFERENCE — the rounds/004 admin-row locator flag stands until an author appendix corrects the locator; 6445766848 = FOREIGN_SOURCE_REFERENCE. The 009-collision trio (6447895921 / 6447900009 / 6448162898) remains unindexed_source by format (bullet list, outside row scope — documented limitation, cross-checked by hand in rounds/009).
