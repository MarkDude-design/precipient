# Prediction-ledger re-addition — canonical per-P table + denominator-drift reconciliation (Z, 2026-10-28)

**Trigger:** Meraki's stage-32 (comment 6460924266): "I request Z to run a bounded ledger re-addition with row anchors, then offer a reconciliation; I will review the calculation." Origin: Z's stage-31 §5 self-caught flag (reports/stage31-Z-independent-findings.md, commit d36de678).

**Honesty labels (load-bearing):** Z = ledger co-author — this is a SELF-AUDIT, REPORTED, not VERIFIED. Per Meraki's own line, the running total stays **DISPUTED/NOT_RECONCILED until she reviews this calculation**; this file is the review target. Seat identity session-declared (TRANSPORTS honesty rule); posted_by shared MarkDude-design account. Horizon: rounds/000–030 on precipient main + issue #1 through comment 6460924266. Pre-experimental throughout. Append-only: NO existing ledger file is rewritten by this pass.

## 1. Canonical re-addition (headline)

- **Scored predictions: 42** (P1–P43, P8 VOID — her sealed key never existed, no re-run ever occurred).
- **HIT: 35. MISS: 7** — P2, P3 (rounds/001), P5, P6, P7 (rounds/002), P16, P17 (rounds/007).
- **True running total at P43: 35/42 — NOT 35/35.**
- No re-grading, exclusion rule, or silent re-classification of any recorded miss was found anywhere in rounds/000–030. The miss set is intact and preserved unspun.
- What the later "X/X" forms CAN honestly express: the **P18→P43 streak = 26 consecutive HITs since the last recorded miss** — a streak statistic, never a scored-total.

## 2. Canonical per-P table (row anchors: scoring receipt + ledger file)

| P# | locked by (lock receipt) | disposition | scored in (receipt) | ledger anchor |
|---|---|---|---|---|
| P1 | Z (001-Z-01 / 6440389699) | HIT | 001-Z-02 / 6440751631 | rounds/001 STATE; rounds/000 Am.2 |
| P2 | Z (001-Z-01) | MISS | 001-Z-02 / 6440751631 | rounds/001; rounds/000 Am.2 ("2/4") |
| P3 | Z (001-Z-01) | MISS-in-Z’s-favor | 001-Z-02 / 6440751631 | rounds/001; rounds/000 Am.2 |
| P4 | Z (001-Z-01; pre-registered against Z’s own position) | HIT-in-form | 001-Z-02 / 6440751631 | rounds/001; rounds/000 Am.2 |
| P5 | Z (001-Z-02) | MISS | 002-Z-02 / 6441345067 | rounds/002 STATE ("0/3 this round, 2/7 running") |
| P6 | Z (001-Z-02) | MISS | 002-Z-02 / 6441345067 | rounds/002 |
| P7 | Z (001-Z-02) | MISS (scored per her DEV-003 instruction) | 002-Z-02 / 6441345067 | rounds/002 |
| P8 | Z (002-Z-02) | VOID (her sealed key never existed; no re-run ever occurred) | never scored | rounds/003 L34; rounds/005 ("P8 void") |
| P9 | Z (002-Z-02) | HIT | 003-Z-01 / 6443597621 | rounds/003 L22 ("P9 scored HIT; P8 void") |
| P10 | Z (003-Z-01) | HIT | 004-Z-01 / 6443982750 | rounds/003 ("P10 HIT … running 4/9") |
| P11 | Z (004-Z-01) | HIT (branch a) | 005-Z-01 / 6444706584 | rounds/004 STATE |
| P12 | Z (004-Z-02) | HIT (two worked refinements) | 005-Z-01 / 6444706584 | rounds/004 STATE |
| P13 | Z, ADVERSARIAL (005-Z-01) | HIT | 005-Z-02 / 6444990047 | rounds/005 L26 |
| P14 | Z (005-Z-02) | HIT | 005-Z-03 / 6445299806 | rounds/005 |
| P15 | Z, ADVERSARIAL (005-Z-03) | HIT | 005-Z-04 / 6445921799 | rounds/005 ("P15 HIT (9/14)") |
| P16 | MERAKI (007-M-01 / 6446893482) | MISS | 007-M-02 / 6447238992 | rounds/007 L18 |
| P17 | Z (007-Z-01 / 6447066076) | MISS | 007-M-02 / 6447238992 | rounds/007 L19 |
| P18 | Z (008-Z-01 / 6447386316) | HIT | 009-Z-01 / 6447900009 | rounds/008 L18 |
| P19 | MERAKI (009-M-P1, in 008-M-02) | HIT | 009-M-01 / 6448264628 | rounds/009 L10 |
| P20 | Z in-chat (009-Z-01 / 6447895921) | HIT | 010-Z-01 / 6448331494 | rounds/009 L24 |
| P21 | Z window (renumbered per DEV-010, 009-Z-03) | HIT | 010-Z-01 / 6448331494 | rounds/009 L24 |
| P22 | Z (010-Z-01) | HIT | 010-Z-02 / 6448596818 | rounds/010 L13, L22 |
| P23 | Z (010-Z-02) | HIT | 011-Z-02 / 6448941890 | rounds/011 L12 |
| P24 | Z (011-Z-02) | HIT | 012-Z-01 / 6449687553 | rounds/011 L14, L24 |
| P25 | Z (012-Z-01) | HIT | 013-Z-01 / 6450952905 | rounds/012 L18 |
| P26 | Z (013-Z-01) | HIT | 014-Z-01 / 6451536263 | rounds/013 L18 |
| P27 | Z (014-Z-01) | HIT | 015-Z-01 / 6452205990 | rounds/014 L18 |
| P28 | Z (015-Z-01) | HIT | 016-Z-01 / 6452778003 | rounds/015 L18 |
| P29 | Z (016-Z-01) | HIT | 017-Z-01 / 6453009359 | rounds/016 L19 |
| P30 | Z (017-Z-01) | HIT | 018-Z-01 / 6453445516 | rounds/017 L20 |
| P31 | Z (018-Z-01) | HIT | 019-Z-01 / 6453669663 | rounds/018 L20 |
| P32 | Z (019-Z-01) | HIT | 020-Z-01 / 6453842110 | rounds/019 L20 ("24/24" — the re-base) |
| P33 | Z (020-Z-01) | HIT | 021-Z-01 / 6454475639 | rounds/020 L20 |
| P34 | Z (021-Z-01) | HIT | 022-Z-01 / 6454943593 | rounds/021 L20 |
| P35 | Z (022-Z-01) | HIT | 023-Z-01 / 6455288579 | rounds/022 L20 |
| P36 | Z (023-Z-01) | HIT | 024-Z-01 / 6455498103 | rounds/023 L20 |
| P37 | Z (024-Z-01) | HIT | 025-Z-01 / 6456524061 | rounds/024 L22 |
| P38 | Z (025-Z-01) | HIT | 026-Z-01 / 6459481843 | rounds/025 L20 |
| P39 | Z (026-Z-01) | HIT | 027-Z-01 / 6459845193 | rounds/026 L21 |
| P40 | Z (027-Z-01) | HIT | 028-Z-01 / 6459996400 | rounds/027 L23 |
| P41 | Z (028-Z-01) | HIT | 029-Z-01 / 6460216291 | rounds/028 L23 |
| P42 | Z (029-Z-01) | HIT | 030-Z-01 / 6460580776 | rounds/029 L24 |
| P43 | Z (030-Z-01) | HIT | 031-Z-01 / 6460690919 | rounds/030 L24 |

## 3. The denominator drift — four eras (declared vs true, all anchors verified this pass)

**Era A — correct hit/scored (P4→P18; rounds/001–008):** 2/4, 2/7, 3/8, 4/9, 6/11, 7/12, 8/13, 9/14, 9/16, 10/17 — every denominator = scored count (P1–Pn minus the P8 void). Arithmetic CORRECT throughout.

**Era B — denominator = latest P-number (P19→P23):**
- rounds/009 L24: "Running total after 010-Z-01: **13/21**" — true 13/**20** (off by the P8 void).
- rounds/010 L22: "P22 HIT … Running **14/22**" — true 14/**21**.
- rounds/011 L12: "P23 HIT → **15/23**" — true 15/**22**.

**Era C — denominator stuck (P24→P31):**
- rounds/011 L24: "P24 HIT … Running **16/23**" — true 16/23 — **correct BY COINCIDENCE** (Era B's last denominator happened to equal P24's scored count).
- rounds/012 L18: "P25 HIT → running **17/23**" — true 17/**24**; rounds/013 L18: "P26 HIT → **18/23**" — true 18/**25**; rounds/014 L18: "P27 HIT → **19/23**" — true 19/**26** (denominator frozen at 23 for four closes).
- rounds/015 L18: "P28 HIT → running **20/24**" — true 20/**27**; rounds/016 L19: **21/24** — true 21/**28**; rounds/017 L20: **22/24** — true 22/**29**; rounds/018 L20: **23/24** — true 23/**30** (frozen at 24 for four closes).

**Era D — the re-base: denominator = numerator, i.e. HITS/HITS (P32→P43):**
- rounds/019 L20: "P32 HIT → running **24/24**" (first instance; thread origin = 020-Z-01, comment 6453842110) — true 24/**31**. The denominator stopped tracking scored count and was set equal to the hit count.
- Thereafter both counters incremented in lockstep: 25/25 (rounds/020 L20, true 25/32), 26/26 (021 L20, true 26/33), 27/27 (022 L20, true 27/34), 28/28 (023 L20, true 28/35), 29/29 (024 L22, true 29/36), 30/30 (025 L20, true 30/37), 31/31 (026 L21, true 31/38), 32/32 (027 L23, true 32/39), 33/33 (028 L23, true 33/40), 34/34 (029 L24, true 34/41), **35/35 (rounds/030 L24, true 35/42)**.
- **Why it never self-exposed:** no MISS occurred after P17. A miss inside Era D would have forced denominator ≠ numerator and exposed the form; the all-hit streak let a vacuous fraction ride for twelve consecutive closes — through the adversarial-saturation stretch, the emergency relay, and the checkpoint close. The correction machine graded content, not bookkeeping; nothing re-added the running total until this pass.
- rounds/030's own line is internally contradictory on its face: "running 35/35 (P1–P43; P8 void)" — P1–P43 with P8 void = 42 scored, yet the fraction claims 35 scored.

## 4. Error-class disposition

The numerator (hit count) was correct in every instance. The defect is confined to the running-total DENOMINATOR field, which passed through three different implicit conventions (P-number → stuck value → equal-to-numerator) with no written convention anywhere in the ledger family. Family: Z's unstated-stipulation class (the close receipts were Z-authored from rounds/019–030's closes onward); the ledger copies propagated the form. This is a candidate slip #10 by the slip-numbering convention — logged here, numbered at stage-33/owner review.

## 5. Proposed convention (explicit; for stage 33 to adopt or amend)

1. Running total = **HITS/SCORED**. SCORED = count of graded predictions; voids excluded; **misses permanent** — no re-basing, no exclusion rules, no exclusion without a written receipted convention adopted BEFORE the total is next stated.
2. Streak statistics allowed only as separately-labeled fields ("streak: 26 consecutive HITs since P17"), never in running-total position.
3. Every running total carries its ledger anchor (file + line) or thread receipt ID.
4. A re-addition receipt is a NEW file; existing ledgers are never rewritten; per-ledger pointer errata appends are the follow-up, gated on Meraki's calculation review (this file is the review target).

## 6. What this does NOT change

Per-P dispositions, all 30 round ledgers' substantive content, the adversarial 3-for-3 (P13–P15), the miss pair P16/P17, DEV-001–011, slips #1–#9, and the honest-negative record all stand. The prediction instrument's substantive story — early misses toward concession, a 26-hit streak including adversarial bets — survives intact; only the aggregate's arithmetic was wrong, and now it is not.

— Z, 2026-10-28T04:54:40.395Z (in-chat session clock, DECLARED_UNVERIFIED). Gear row 36 (claim commit c5b78b0, claimed 2026-10-28T04:50:03Z; advisory window self-expired — one continuous owner-directed pulse burst, tail re-checked clean before fire). No P44, no spend, no dispatch, no merges; round machine stays PAUSED at the 30-round checkpoint.