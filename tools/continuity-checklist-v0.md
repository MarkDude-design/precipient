# Continuity Checklist v0 — thread-age × interface-switch weighted

**Provenance:** owner ask (stage-34½ identical-prompt assignment, in-chat, 2026-10-28): a simple continuity checklist that weights thread age and interface switches. Born from the run's own continuity receipts: the round-028 emergency relay, the round-029 one-character operator recovery (ALLur #16 comment 6460602301), and Meraki's stage-34½ main result — **preserved GitHub receipts ≠ recovered owner/action** (comment 6461406076, accepted). PRE-EXPERIMENTAL; v0; amendments append. Complements (does not replace) Meraki's FRESH / OWNED / REAL / BOUNDARY / NEXT artifact breath check — hers runs per-artifact; this runs per-cadence.

## Risk weight (seconds to compute)
**R = D + I + M**
- **D** = whole days since the LAST DURABLE ANCHOR on the active lane (comment ID or commit sha). Anchors, not raw thread age, are the denominator — a hot old thread with fresh anchors is safer than a cold new one.
- **I** = 1 if any interface switch since the last check (new thread, client swap, app restart, connector change, model/session handoff), else 0. Context loss clusters at switches.
- **M** = number of additional repos touched since the last check.

**Reading:** R = 0 → nothing due · R ≥ 1 → Quick Block · R ≥ 3 OR any interface switch → Full Block BEFORE any new work · overnight gap or before-bed handoff → Overnight Block regardless of R.

## Quick Block (every pulse; ≤ 1 min)
1. Latest anchor written down (comment ID + commit sha of the active lane)?
2. Horizon set ("anything newer than X = unprocessed")?
3. No silently-open claims — every gear row closed or explicitly LIVE with a timestamp?
4. Quoted totals in canonical anchored form (hits/scored, e.g. 35/42) — never a bare N/N form?
5. Waiting-on list current (whose lane, waiting since when)?

## Full Block (session start; any interface switch; R ≥ 3; ≤ 10 min)
6. Re-read the durable channel tail BEFORE acting on memory.
7. Gear/claims audit — every row's artifacts resolve (comment IDs exist; files are on main).
8. **Compaction diff** — reconstruct the plan from the durable record; anything remembered but NOT on-channel gets re-posted immediately. This includes owner DECISIONS (picks, scope choices, go/no-go calls): receipts preserve what was posted, not what was chosen in a chat head — that is the receipts-≠-owner-action gap.
9. UNASSIGNED offers re-indexed (silence is never acceptance).
10. Cross-repo pulse — every repo in the experiment has a known last-activity stamp.
11. Clock source labeled (DECLARED_UNVERIFIED unless server-anchored).
12. Other-seat action pending > 24h → flag to owner; never act unilaterally in her lane.

## Overnight Block (before bed / on wake)
13. Before bed: everything needed for cold reconstruction is on the durable channel (the one-character test) — including the decisions made tonight.
14. On wake: re-anchor from the durable channel only — not from memory or any summary.
15. Loose-end ledger re-read (stage-34½ calibration report §2) before resuming any lane.

**Adoption note:** owner + both seats may adopt v0 as the standing pre-pulse/pre-session check for future threads. Meraki's five-check breath + this cadence frame are both v0 candidates for a merged v1 — owner picks.

— Z, 2026-10-28T05:38:02.430Z (in-chat session clock, DECLARED_UNVERIFIED). Stage 34½, gear row 38.
