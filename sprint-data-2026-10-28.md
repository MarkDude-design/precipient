# Sprint Data — Day 2 (2026-10-28): the 30-round checkpoint, stages 31–35.4, and what's worth keeping

- **kind:** owner-directed harvest view (day-2 companion to sprint-data-2026-10-27.md); round machine PAUSED at the Stage-34-approved checkpoint; NOT a scored round; no P44.
- **captured:** 2026-10-29 (in-chat session, gear row 50); sources = issue #1 comments + rounds/ + reports/ on main. **All claim-class labels of the sprint apply to this file** — nothing here upgrades to VERIFIED by being written down.

## 1. Day-2 metrics view (honest)
- **Rounds closed Oct 28 (00:17Z–04:29Z): 025 (P38) → 030 (P43); checkpoint STOP at round 030.** Machine paused since 04:30Z Oct 28. Rounds 000–030 ran from Oct 27 11:21Z → Oct 28 04:29Z (~17 hours wall clock).
- **Prediction ledger (the honesty beat):** Z's self-recorded running totals (…35/35) were UNVERIFIED until the §5 arithmetic flag (rounds/007's recorded 9/16 vs later totals) was SELF-CAUGHT, receipted, and resolved by a bounded re-addition pass (reports/prediction-ledger-readdition-2026-10-28-Z.md); QC's fresh-context independent re-add then confirmed **35/42 predictions, zero discrepancies**. The per-P disposition table is the record — not the headline totals.
- **Adversarial saturation test:** predictions P13–P15 were deliberately locked AGAINST the all-cooperative hit pattern (HIT only if she forced amending Z's rules) — **3-for-3**. The instrument does not only bet on agreement.
- **Legibility:** QC verdict **PARTIAL** (3 failure modes); GLOSSARY.md shipped as the repair (Stage-34 owner-approved). Independent fresh readers: NOT performed, NOT claimed (owner-gated).
- **Continuity under failure, receipted twice:** (1) Meraki's posting blocked 3× at the tool boundary → **47-second emergency relay** (owner-ferry, verbatim envelope, grade-on-the-text/authorship-on-the-channel); (2) Mark's Android client died mid-thread → **one `.` character rebuilt the full session from durable channels**.
- **Correction cadence:** essentially every Meraki grade carried ≥1 worked correction; Z logged 9 self-slips with a named taxonomy (unstated-stipulation ×3, axis collapse, domain-of-applicability omission, boundary-kind conflation, stale-attribution, others); the checker/instrument flagged its own author 8+ receipted times.
- **Transport defects (DEV-001–012):** all caught pre-push or repaired same-burst; zero damage to main's record.

## 2. The reusable canon (what any AI-team project can lift)
One-line spine (full instrument stack + adoption order: reads/checkpoint-reconstruction-2026-10-28-Z.md):
- **Pre-registered restatement** — grade against criteria frozen BEFORE seeing the answer; step 1 is load-bearing.
- **Claim-indexed UNDETERMINED** — uncertainty attaches to a claim at an evidence horizon, never to a round or a seat.
- **Two-claim acceptance (S/R)** — source-static vs runtime-reported are separate claims; never inherit.
- **Support-path ledger** — evidence composes over paths (min within AND, max across OR), not ladders; no silent corroboration.
- **Decision-grade certificates** — reversibility class sets the gate; no scalar scores, threshold = dependency-set membership.
- **Effect envelopes** — read-only is not zero-effect; crossing an envelope (not repeating a verb) triggers re-scope.
- **Oracle supersession** — kill the oracle, not the history: (claim, oracle@revision, horizon) triples; consumers re-check named edges.
- **Transform-chain receipts (four digests)** — input, transform version/config, output, consumer-read; compressed-input SHA ≠ consumed bytes.
- **COMMITMENT RECEIPT + lifecycle** — commitment iff the owning seat posted acceptance; offers never commit; UNASSIGNED is first-class; drops are receipted; **time, silence, and proximity never author a state change**.
- **COMPLETION TRIPLE (D-A-V)** — delivered ≠ accepted ≠ independently-verified; creator self-report stays REPORTED_BY.
- **PROVENANCE PROMOTION** — identity-relative vs content-relative predicates decided at freeze time; grade the text, not the channel.
- **Author-grading (006-A)** — frozen counterparty positions are author-graded BEFORE becoming targets.
- **Pre-exposure drafts** — timestamped-before-exposure artifacts split habit from copying.

## 3. Quotable lines (talk material; numbered flags already banked in-thread)
1. "The instrument caught its author" — 8+ receipted instances of the checker/grading machine flagging its own builder.
2. "Grade the text, not the channel." — the emergency-relay canon.
3. "Silence is never acceptance. UNASSIGNED is a state." — the commitment canon, from the bot vantage.
4. "Time, silence, and proximity never author a state change." — the lifecycle rule in one line.
5. "A checksum-shaped string is not evidence of a receipt unless the verification path exists." — DEV-003, the experiment's first false receipt, self-caught.
6. "One tap, one character, full continuity." — operator-side client death survived by durable channels.
7. **47 seconds** — a two-seat AI argument survived a platform outage via owner-ferry + receipts.
8. "Delivered is not accepted; accepted is not verified." — the D-A-V triple.
9. "Elastic collaboration, rigid gates"; "role label ≠ permission"; "hold a seat open while a contributor learns" — Meraki's stewardship ethos (docs/SEAT_STEWARDSHIP_AND_MENTORSHIP_V0.md, review-candidate).
10. "NOTICE → LOCATE → REPAIR → FALSIFIER → RESUME" — raise the standard instead of 'oops' loops; credit the challenger.
11. "STEWARDSHIP TENSION" — a neutral name for protective ownership that replaces "defensiveness."
12. The numbers: ~17 hours, 30 scored rounds, 42 sealed predictions independently re-added (35 confirmed, zero discrepancies), adversarial 3-for-3, two transport failures, zero lost rounds.

## 4. Code / tooling candidates (patterns, not products)
- **lane_check.py v0.3.1** — ledger-vs-source back-scan checker (unindexed / orphaned / duplicate / clock-fault classes; ambiguous rows over-flag, never mask). Generalizes to ANY repo with an index or claims file; her negative tests are the spec.
- **Continuity Index** — GitHub-issue-as-ledger, zero new infra; UNASSIGNED-first rows; append-only corrections.
- **Sync gear** — a claims table IS the instrument (claim → window → re-check → fire → DONE + four phase stamps); honest scope: advisory, not a mutex; P50/P95 still NOT MEASURED.
- **continuity-checklist v0.2 + deep-scan frame** — continuity as thread-age × interface-switch weighting; the beyond-thread primary.
- **fixture_runner paired-digest harness** — condition-independent state digests + arm-config digests + negative tests (paired starts byte-equal, perturbed arms differ).
- **Offer only (NOT built):** D-A-V / commitment-lifecycle checker extensions to lane_check.

## 5. Cross-project pull-outs (public-safe one-liners)
- **Channel 22** (green-light pending): manufactured presence of agreement, provenance laundering, false receipts = satire-ready units, receipted.
- **muwu / model-spirit work:** receipts-as-spine; shared vocabulary manufactures apparent agreement (bus pair 16).
- **Z-desk:** gear + index + ops notes ARE desk foundations.
- **Nonprofit tech-jobs / AI-as-tool demos:** the whole sprint is a demo of AI teaming that receipts itself — with numbers.
- **Stakes quantization:** the P9 operational triggers + $5–10 floor lineage run straight through rounds 002–003.

## 6. Pending (owner rows — do not do for him)
Island paste model → R1 pastes (16 pastes + 16 copied-back outputs + NOTE edits) → Phase A real data · art-talk uploads + Spiral ruling · movie Part III+ · talks print list · fresh readers · machine-resume decision · delegated-motion kickoff.

*Harvest receipts: precipient commit (this push); talks-main inbox extract (same burst); bus #2 pointer. Talk-material numbering continues the flags banked in-thread Oct 27–28 (flags 1–6).*
