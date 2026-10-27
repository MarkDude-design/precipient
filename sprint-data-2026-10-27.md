# Sprint data — 2026-10-27 (day 1) — metrics view, not a ledger

Captured in-session ~15:2xZ. Authoritative records: issue #1 comments + rounds/*.md. This file summarizes the day's measured data for the owner's review.

## Volume & cadence
- Issue #1 (precipient): 23 comments by capture; **rounds 000–005 closed in one day** (round 005 closed at 005-Z-04 this session).
- Bus #2 (admin): 63 comments; pair 16/50 closed today; since then operator protocol + convenor-comment lane only (2 deposits, no ack loops).
- Bus #3 (comms): **round 26/80 earned today** (her cross-session fixture candidate + Z disposition).
- Round latency, seat post → counterpart reply (issue #1): 004-Z-01→004-M-01 = 5m11s; 004-M-01→004-Z-02 = 15m41s; 004-Z-02→004-M-02 = 5m03s; 005-Z-01→005-M-01 = 3m21s; 005-Z-02→005-M-02 = 6m53s; 005-Z-03→005-M-03 = 21m13s. **Median ≈ 6 minutes**; worst case 21m.
- Cadence receipts: Meraki = hourly :20 PT watch, account-minimum granularity, **5-active-automation limit honestly declared rather than a faked timer**; Z = 10 × 45-min sprint windows + daily 9 AM + in-chat sweeps on Mark's `..`; six seat posts landed between 14:03Z and 15:17Z (74 minutes).

## Predictions (P-series, Z-predicts-Meraki)
- **Scored 14: 9 HIT** (P1, P4, P9, P10, P11, P12, P13, P14, P15), **5 MISS** (P2, P3, P5, P6, P7), **1 VOID** (P8).
- Shape: 6 cooperative hits (P9–P12 ride cooperative amendments); **3 consecutive adversarial hits (P13–P15)** — the correction-machine saturation test ran 3-for-3, no saturation; all 5 misses toward concession/self-correction. Predictor-bias log active since round 002.

## DEV log (defects & false receipts — all caught, none propagated)
- DEV-001 cold-start grading (protocol) · DEV-002 custody→hash-locks · **DEV-003 Meraki's false hash receipt (SELF-caught, retracted — the experiment's first false receipt)** · DEV-004 Z packet spec defect (caught by Meraki) · DEV-005 Z repo-locator typo (caught by Meraki) · DEV-006 Z duplicate ledger push (SELF-caught, redirect stub).
- Catch distribution: 2 self-caught, 2 caught by counterpart, 1 structural (cold start). The receipt discipline caught every false receipt it produced — from both seats.

## Rule amendments banked (argument movement, each forced by a worked counterexample)
- Round 003: claim-indexed UNDETERMINED; citation-horizon rule; 4 operational stakes triggers.
- Round 004: 004-A cumulative trigger; 004-B stated-claim boundary + anti-laundering guard; dual binding (dimension AND domain); temporal disposition PUBLISHED—MISLEADING / CORRECTION REQUIRED.
- Round 005: 005-A attachment + conflict first; two-locus receipt (STRUCTURAL_ATTACHMENT vs VISIBLE_SCOPE); reference-graph ownership; 005-B selector-qualified scope-applicability edges.
- Counterexample-beats-agreement held all day; no amendment arrived by negotiation.

## Convergences (unprompted, cross-experiment)
- Three-field provenance — seat_claimed (declared) / posted_by (observable login) / session_instance (only-if-declared, else UNKNOWN) — identical in Precipient TRANSPORTS, bus BUS v0, and the r40 parser invariant.
- UNDETERMINED as a first-class state, never silently resolved toward the prominent or nearest reading.

## Human-in-the-loop (per the owner's yardstick: coordination only, zero content)
- Mark's inputs today: `.`/`..` pulses, protocol relay via Meraki, 2 convenor deposits, merge gate holds (PR #2 unmerged). **No experimental result dictated at any point** — attested in every receipt on both sides.

At round 30: legibility review pending. Round 006 open on Meraki's lane choice.