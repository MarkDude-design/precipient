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
| 2026-10-27T23:0XZ | Z in-chat | ISLAND: SPEC/RUNBOOK v0.1.2 push + #12 compare-notes/grade post | +10 min | HOT | pending |

## History
- 2026-10-27: first dogfood complete (claim row 1). Island burst row 2 (daf02bd, #13, 6448629635). Walkthrough row 3 (6448660056). Bus timing note row 4 (6448972620) — landed after Meraki's current-state checkpoint 6448885244; complementary admin-lane content, no collision.
