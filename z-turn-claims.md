# Z Turn Claims — sync gear v0 (interrupter mechanism, owner-directed 2026-10-27)

## Protocol (all Z sessions, both repos; research turns + ledger pushes only)
1. **COMPOSE first** — draft the turn in-session before claiming.
2. **CHECK** — read this table + the target thread tail. Any other session's live claim = **HOT ZONE — DO NOT FIRE**.
3. **CLAIM** — append a row below (session, target, window). Window = +10 min, then self-expires (EXPIRED rows stay as history).
4. **RE-CHECK** — after the claim, re-read the thread tail once. A post that crossed despite the claim = defer/build-on, never double-answer (DEV-010 backstop unchanged).
5. **FIRE within the window, then mark the row DONE** with the resulting comment/commit ID.

Honest scope: shrinks the collision arc (DEV-006/DEV-010 class) from minutes to seconds; cannot zero it; append-only collision-resolution backstop stays.

Origin: Mark's interrupter-gear metaphor — the gun does not fire through the propeller's arc; a live claim is the arc; notation: "HOT ZONE, I can't fire now."

## Claim table

| claimed_at (UTC, server) | session | target | window ends | status | artifact |
|---|---|---|---|---|---|
| 2026-10-27 (pre-post) | Z in-chat | precipient #1 — 010-Z-01 | +10 min | DONE | precipient #1 comment 6448331494 |
| 2026-10-27T22:05Z | Z in-chat | ISLAND burst: z/island-v0.1.1 push + issue #13 + #12 circle post | +10 min | DONE | commit daf02bd; issue #13; #12 comment 6448629635 |
| 2026-10-27T22:20Z | Z in-chat | island #12 — Z's paper walkthrough | +10 min | DONE | #12 comment 6448660056 |
| 2026-10-27T22:40Z | Z in-chat | bus #2 — timing mechanism + scan-coverage note | +10 min | DONE | bus #2 comment 6448972620 |
| 2026-10-27T23:0XZ | Z in-chat | ISLAND: SPEC/RUNBOOK v0.1.2 push + #12 compare-notes post | +10 min | DONE | commit b4f4d95; #12 comment 6449023216 |
| 2026-10-27T23:2XZ | Z in-chat | precipient: PR #3 reconciliation push (4 errata appends) + PR review response | +10 min | DONE | commit e12f075 + repair commit (this push); PR #3 comment 6449101523 |

| 2026-10-27T17:43Z | Z in-chat | ISLAND GATE 1: v01 fixture+tests push to z/island-v0.1.1 + #13 fixture-acceptance post | +10 min (17:53Z) | DONE | island commit 71560ba; #13 comment 6449337601 |

| 8 | claimed_at_declared: 2026-10-27T17:58Z (in-chat session bash clock, unverified vs server) | PRECIP round 011 close: rounds/011 ledger push + 012-Z-01 post + Appendix A (this file) | advisory +10 min (unverified clock — see Appendix A scope) | DONE | rounds/011 pushed; #1 comment 6449687553 |

## APPENDIX A — CLAIM-TIME ERRATUM (append-only; response to Meraki's PR #3 review 6449562140 + bus #2 lead review 6449523930 §1)

**Correction adopted by Z, 2026-10-27.** The claim-table header says `claimed_at (UTC, server)`, but rows 1–6 claim times are NOT server-receipted: they are DECLARED times transcribed from Z-session clocks without server cross-check, and rows 2–5's declared times are AFTER their fired comments' server creation times — impossible as literal pre-post UTC. No row values are rewritten (append-only); rows 1–6 claim times are labeled **DECLARED_UNVERIFIED**. Exact cause of the ~5h offset: UNDETERMINED (not preserved); the labels and fire receipts are the correction.

**Role split going forward (her four roles, adopted):** `claimed_at_declared` (clock source declared) · `claim_receipt_created_at_server` (only when a server-receipted claim write exists — none does yet) · `expires_at_utc` (only when grounded; a bare "+10 min" from an unverified clock is not) · `fire_created_at_server` (fired artifact's GitHub receipt).

**Server-observed fire receipts (GitHub `created_at`):**

| row | claimed_at_declared | target | fire artifact | fire_created_at_server |
|---|---|---|---|---|
| 1 | 2026-10-27 (pre-post, no time) | precipient #1 010-Z-01 | comment 6448331494 | 2026-10-27T17:05:25Z |
| 2 | 2026-10-27T22:05Z — DECLARED_UNVERIFIED (impossible vs fire) | island burst + issue #13 + #12 circle post | comment 6448629635 | 2026-10-27T17:19:20Z |
| 3 | 2026-10-27T22:20Z — DECLARED_UNVERIFIED | island #12 walkthrough | comment 6448660056 | 2026-10-27T17:20:46Z |
| 4 | 2026-10-27T22:40Z — DECLARED_UNVERIFIED | bus #2 timing note | comment 6448972620 | 2026-10-27T17:31:53Z |
| 5 | 2026-10-27T23:0XZ — DECLARED_UNVERIFIED (not machine-comparable) | SPEC/RUNBOOK v0.1.2 + #12 compare post | commit b4f4d95; comment 6449023216 | comment 2026-10-27T17:33:33Z |
| 6 | 2026-10-27T23:2XZ — DECLARED_UNVERIFIED | PR #3 reconciliation | comments 6449101523 / 6449169341 | 2026-10-27T17:36:07Z / 17:38:19Z |
| 7 | 2026-10-27T17:43Z (session clock; consistent with fire) | GATE 1 fixture burst | commit 71560ba; comment 6449337601 | comment 2026-10-27T17:44:05Z |

**Scope statement (adopted verbatim from her review):** until a real server-receipted compare-and-swap claim write exists, this table is an **advisory collision-reduction convention, not enforceable mutual exclusion** — not a proven 10-minute lease, not a mutex. Row 7's plausible agreement of declared time with fire time is not a lock verification.

| 9 | claimed_at_declared: 2026-10-27T18:00Z (in-chat session bash clock, unverified vs server) | ISLAND §7: EKO primary-source citation push (docs/EKO_PRIMARY_SOURCE.md + SPEC §7 fill) + #12 citation post | advisory +10 min (unverified clock — Appendix A scope) | DONE | island commit c75c85c; #12 comment 6449727714 |

| 10 | claimed_at_declared: 2026-10-27T18:06Z (in-chat session bash clock, unverified vs server) | BUS #2 §3 librarian checker deliverable: push tools/lane_check.py + tests + snapshot fixture + run report to precipient z/ledger-batch-2 + bus #2 reply to her lead review 6449523930 | advisory +10 min (unverified clock — Appendix A scope) | DONE | precipient commit 702f4b5 (tools/lane_check.py, tests, fixture, report); bus #2 comment 6449857781 |

| 11 | claimed_at_declared: 2026-10-27T18:58Z (in-chat session bash clock, unverified vs server) | PRECIP round 012 close: 013-Z-01 post (author grade of her two boundary refinements + P25 score + handoff answer + round 013 answer + P26 lock) + rounds/012 ledger push to main (post-PR#3-merge) | advisory +10 min (unverified clock — Appendix A scope) | DONE | #1 comment 6450952905; rounds/012-marker-regrade.md on main |

| 12 | claimed_at_declared: 2026-10-27T18:59Z (in-chat session bash clock, unverified vs server) | CHECKER v0.2: push her false-negative fix (row-kind contract) + adjudications doc + v0.2 report to precipient main + bus #2 reply to her review 6450082179 | advisory +10 min (unverified clock — Appendix A scope) | DONE | precipient main: tools v0.2, tests, report v0.2, adjudications; bus #2 comment 6450972812 |

| 13 | claimed_at_declared: 2026-10-27T19:00Z (in-chat session bash clock, unverified vs server) | BUS #2 design answer: owner 11-min prefetch-first gear question (reply to her 6450120597) — paper position, no new timer/bot | advisory +10 min (unverified clock — Appendix A scope) | DONE | bus #2 comment 6450984269 (paper position; phase-timestamp columns = first implementation candidate, Mark-gated) |

| 14 | claimed_at_declared: 2026-10-27T19:28Z (in-chat session bash clock, unverified vs server) | PRECIP round 013 close: 014-Z-01 post (author grade of 013-M-01 + P26 score + round 014 answer + P27 lock) + rounds/013 ledger push to main | advisory +10 min (unverified clock — Appendix A scope) | DONE | #1 comment 6451536263; rounds/013-visibility-receipt.md on main |

| 15 | claimed_at_declared: 2026-10-27T20:05Z (in-chat session bash clock, unverified vs server) | BUS #2 owner-relayed note: PUPPF ask + txt-failsafe convention proposal (chat attachments failed; repo = durable channel) | advisory +10 min (unverified clock — Appendix A scope) | DONE | bus #2 comment 6451891613 (PUPPF ask + txt-failsafe proposal) |

| 16 | claimed_at_declared: 2026-10-27T20:12Z (in-chat session bash clock, unverified vs server) | PRECIP round 014 close: 015-Z-01 post (author grade of 014-M-01 + P27 score + round 015 answer + P28 lock) + rounds/014 ledger push to main | advisory +10 min (unverified clock — Appendix A scope) | DONE | #1 comment 6452205990; rounds/014-trustworthy-boundary.md on main |


| 17 | claimed_at_declared: 2026-10-27T20:07Z (in-chat session bash clock, unverified vs server) | GEAR v0.1 phase-stamping: implement Appendix B (phase-timestamp columns) in z-turn-claims.md per owner green-light + bus #2 implementation note (reply to design answer 6450984269) | advisory +10 min (unverified clock — Appendix A scope) | DONE | bus #2 comment 6452363902; Appendix B on main (this push) |


| 18 | claimed_at_declared: 2026-10-27T20:26Z (in-chat session bash clock, unverified vs server) | BUS #2 seat-continuity ask: Meraki handoff MD request (her thread hit context limit; notebook-continuity transfer try-1, owner-directed) | advisory +10 min (unverified clock — Appendix A scope) | DONE | bus #2 comment 6452774439 (seat-continuity ask) |

| 19 | claimed_at_declared: 2026-10-27T20:26Z (in-chat session bash clock, unverified vs server) | PRECIP round 015 close: 016-Z-01 post (author grade of 015-M-01 VERIFIED tuple correction + AXIS COLLAPSE log + P28 score + round 016 answer + P29 lock) + rounds/015 ledger push to main | advisory +10 min (unverified clock — Appendix A scope) | DONE | #1 comment 6452778003 (016-Z-01); rounds/015-attestation-axes.md on main (this push) |


| 20 | claimed_at_declared: 2026-10-27T20:38Z (in-chat session bash clock, unverified vs server) | PRECIP round 016 close: 017-Z-01 post (author grade of 016-M-01 + P29 score + author-check CORRECTED/VERIFIED + round 017 answer + P30 lock) + rounds/016 ledger push to main | advisory +10 min (unverified clock — Appendix A scope) | IN FLIGHT | claim push (this push) |

## APPENDIX B — PHASE TIMESTAMPS (implemented 2026-10-27; owner green-light on bus #2 design answer 6450984269 §2; implementation note bus #2 comment 6452363902)

**Instrumentation:** four declared phase timestamps per gear row; the claim table IS the instrument; no new tooling, no timer, no bot.

**Phases (mapped to protocol steps):**
- `prefetch_start` — COMPOSE begins: session clock read at start of turn processing (target thread fetch begins).
- `sources_in_hand` — CHECK complete: target thread tail + this table read; no hot zone.
- `re_read_done` — RE-CHECK complete: post-claim re-read of target tail done.
- `fired` — FIRE complete: fired artifact posted/pushed.

**Rules (from the design answer, adopted 2026-10-27):**
- Clock source declared in every stamp; all values DECLARED_UNVERIFIED (Appendix A scope). Server fire receipts (`fire_created_at_server`, Appendix A) remain the only server-anchored evidence.
- 11-minute phases = advisory preference only — not a lease, not a mutex, not enforceable.
- P50/P95: NOT MEASURED until ≥10 phase-stamped rows exist; then computed from declared clocks only, labeled declared-clock estimates. No fabricated distributions.
- Append-only: rows 1–16 stay unstamped (history); phase stamps begin with row 17.

**Phase stamps (declared — in-chat session bash clock, unverified vs server):**

| row | prefetch_start | sources_in_hand | re_read_done | fired | clock source |
|---|---|---|---|---|---|
| 17 | 2026-10-27T20:05Z | 2026-10-27T20:07Z | 2026-10-27T20:07Z | 2026-10-27T20:08Z | in-chat session bash clock, DECLARED_UNVERIFIED |
| 18 | 2026-10-27T20:25Z | 2026-10-27T20:25Z | 2026-10-27T20:27Z | 2026-10-27T20:28Z | in-chat session bash clock, DECLARED_UNVERIFIED |
| 19 | 2026-10-27T20:25Z | 2026-10-27T20:26Z | 2026-10-27T20:27Z | 2026-10-27T20:28Z | in-chat session bash clock, DECLARED_UNVERIFIED |

Row 17 note: same-minute claimed_at/re_read_done values = clock minute resolution, not a compression claim.

## History
- **DEV-011 (self-caught, 2026-10-27):** the reconciliation push e12f075 DESTROYED file contents — get_file_contents returned a status line ("successfully downloaded text file (SHA: …)") as the text payload, and the errata were appended to that line, replacing five files (rounds/009, 010, 001, 002, z-turn-claims). Caught by post-push verification within minutes. Repair: originals re-fetched from last-good commit 574fc52d via the working extraction path (resource envelope text), errata re-applied, all five files restored + appended correctly in the repair commit. Main untouched throughout (damage lived only on this branch). Standing rule added to transport discipline: NEVER append to fetched text without verifying it starts with the expected content header.
- 2026-10-27: dogfood runs 1–5 all DONE, collision-free. Round 011 answered by sprint-window Z (011-Z-02 6448941890) — in-chat Z built on, did not double-answer. Bus timing note landed after Meraki's checkpoint 6448885244 (complementary admin-lane, no collision).
