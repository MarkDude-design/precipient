# Round 009 — independence repair + cross-session collision (closed 2026-10-27)

## What was tested
Her adversarial packet: dual Z answers (009-M-P1) — grading whether two same-seat answer events count as independent corroboration, plus the independence-repair question (what repair makes R3's rubric-use independent of R2's rubric).

## Events (chronological)
- **009-Z-01 = 6447895921** (in-chat session, canonical after resolution)
- 009-Z-02 = 6447900009 (sprint-window session, renumbered from "009-Z-01"; posted within ~60s of the in-chat answer — DEV-010)
- **009-Z-03 = 6448162898** — collision resolution: canonical = earlier ID (in-chat); window post renumbered; window's P20 lock renumbered P21. Appendix correction: rounds/008-evidence-profiles.md cites "009-Z-01 (6447900009)" — should be 009-Z-01 = 6447895921, 009-Z-02 = 6447900009.
- **009-M-01 = 6448264628** — her grade: BOTH Z answers PASS all four criteria; graded once; **P19 HIT**; duplicates = two same-seat answer events, not double evidence. Round 009 CLOSED.

## Her worked answer (adopted in 010-Z-01)
- Independence is RELATIVE to the failure mode being tested: a shared rubric = comparability-feature under consistency-question, error-source under independence-question.
- Minimal repair = seal R3 from R2's rubric; R3 derives + timestamps its own rubric BEFORE reveal.
- Language refinement accepted: "independent-in-sourcing" withdrawn → "two access events, one shared upstream table, one borrowed rubric."

## Convergence datum (live-demonstrated on itself)
Two same-seat sessions converged on the same answer → same-source readings, NOT independent corroboration. Same-seat convergence measures the source's stability, not evidence strength.

## DEV-010 (self-caught)
Cross-session turn collision (in-chat + window both answered within ~60s; both did read-before-post at the same horizon — genuine race). Structural fix = sync gear v0 (z-turn-claims.md claim table, owner's interrupter-gear metaphor; installed 2026-10-27 on z/ledger-batch-2).

## Scores
P19: HIT (scored once). P20/P21 scored HIT in 010-Z-01 (6448331494). Running total after 010-Z-01: **13/21**.
