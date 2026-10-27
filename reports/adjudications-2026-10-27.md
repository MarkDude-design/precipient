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
