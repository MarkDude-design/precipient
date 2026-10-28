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


---

## v0.1 APPEND — Meraki protections + RECOVER / DEGRADE GRACEFULLY (2026-10-28, gear row 40; per 6462069918 §2 + owner calibration 6462444840 + ALLur #16 6462435671)

**v0.1 protection A (thin-gate rule, adopted from 6462069918 §2):** on any interface switch, a thin FRESH/OWNED/REAL/NEXT lookup may answer a one-character recovery/status reply IMMEDIATELY; the Full Block is required before *consequential writes, scored turns, dispatch, or acceptance* — not before a ten-minute forensic scan of a status reply.

**v0.1 protection B (item-8 guard, adopted from 6462069918 §2):** compaction-diff re-posts of remembered-but-unchanneled owner DECISIONS require a **re-verified owner decision + a public-safe destination/authorization**. A remembered choice ≠ a durable OWNER_ATTESTED grant; silence and compaction are not authority; never spray unconfirmed choices or private material onto GitHub.

**RECOVER / DEGRADE GRACEFULLY (dedicated section; the 8-point candidate from 6462435671, Z-adopted with edits):**
1. Read the latest durable anchor, not the remembered chat head; the newest sourced delta wins.
2. FRESH? OWNED? REAL? BOUNDARY? NEXT? — never conflate PAPER, REPORTED, VERIFIED, ACCEPTED.
3. If native read/write/UI breaks: classify the failed layer; bounded one-word canary first; re-read the destination before retrying writes (never blindly retry a possibly-successful write).
4. If a seat cannot post: an owner-EXPLICIT emergency relay through another authorized seat may carry a public-safe message; label AUTHOR, RELAYED_BY, POSTED_BY, fidelity, destination, horizon separately; later native confirmation ≠ end-to-end byte proof.
5. If the old chat is inaccessible: new chat + `.` = quick changed-only recovery from connected ledgers; `..` = full sweep; if the connector also fails, a plain-text status + links is the recoverable minimum.
6. Reconstruct owner DECISIONS and gates; never turn a remembered choice, a review OFFER, or silence into authorization; no keys/notebooks in public receipts.
7. Record ATTEMPT / DELIVERY / ACCEPTANCE / INDEPENDENT VERIFICATION separately; STOP only the affected artifact; continue other already-authorized, low-risk work.
8. Z curates this final combined checklist; Meraki supplies independent overview, corrections, and cold-start prompts. ONE canonical checklist — not a rival framework.

**Pickup status:** Z OPEN_RECEIPTED per the owner instruction relayed in 6462444840 (Z owns the FINAL combined continuity checklist). The two founding receipts: the round-028 emergency relay recovery and the one-character new-thread recovery (ALLur #16 6462435671). The v0 adoption note is superseded: the owner has picked the merged form via role split; this v0.1 IS the merged draft pending only the owner's final blessing.

— Z, 2026-10-28T07:22:56.525Z (in-chat session clock, DECLARED_UNVERIFIED). Gear row 40.

---

## v0.2 APPEND — SEAT STEWARDSHIP FOLD-IN (2026-10-28, gear row 44; per Meraki 6463330595 ask + ALLur docs/SEAT_STEWARDSHIP_AND_MENTORSHIP_V0.md, commit 6dc74ac0)

**Layer rule (her distinction, preserved):** the stewardship doc is the TEAM ETHOS layer — public working conduct, applicable by reference across repos. This checklist stays the ONE canonical procedural checklist. The ethos is adopted here by pointer + load-bearing moves, NOT duplicated as a second tier (per her §7: "not a second checklist to maintain").

**Adopted into checklist canon:**
1. **STEWARDSHIP TENSION** = the neutral first label when project obligations and a proposed direction appear to conflict; decide from behavior and receipts (constructive protection / misunderstanding / avoidable gatekeeping) — never pre-judged, never a claim about internal states.
2. **The recovery loop, named:** NOTICE → LOCATE → REPAIR → FALSIFIER → RESUME — replaces the oops-sorry cycle; append/errata instead of erasing; credit whoever caught it. Standard sequence inside RECOVER item 3.
3. **Review = OFFER, not pickup** (inverse of item 9's silence rule): a recommendation or GitHub review never transfers ownership; who ACCEPTED a concrete task is recorded, and recorded separately from who offered.
4. **Two-layers boundary rule:** flexibility for WHO contributes; rigor for WHO MAY COMMIT THE SYSTEM (spend, credentials, publication, destructive actions, merges, hosted runs) — a role title or model branding is not permission.
5. **New-seat onboarding row:** record SKILL DEMONSTRATED / TOOLING OBSERVED / TASK SCOPE / HELP NEEDED separately; never label a seat deficient because the tools differ; the lead does not win by prestige; a newcomer's revision gets recorded and credited.
6. **Consult rule:** another seat is consulted when it adds a distinct test, source, skill, or falsifier — not a second agreeable voice; record what each actually ran (SEAT | VIA | POSTED_BY | RELAYED_BY | DID | DID_NOT as needed).

**Ethos readout (hers, adopted):** "Hold the seat. Protect the standard. Let the proof travel." Ties: the hit-by-a-bus metric (the seat belongs to the work; teach the handoff) and RECOVER/DEGRADE GRACEFULLY — her doc §6 already points here; the cross-references are now mutual.

**Not adopted as checklist procedure (kept on the ethos doc):** the private-notebook privacy stance, no-auto-wake promises, and provenance-note revision rule — standing constraints on the ethos layer, not checklist items. Nothing rejected on substance.

— Z, 2026-10-28 (in-chat session clock, DECLARED_UNVERIFIED). Gear row 44.