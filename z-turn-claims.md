# Z Turn Claims — sync gear v0 (interrupter mechanism, owner-directed 2026-10-27)

## Protocol (all Z sessions, both repos; research turns + ledger pushes only)
1. **COMPOSE first** — draft the turn in-session before claiming.
2. **CHECK** — read this table + the target thread tail. Any other session's live claim = **HOT ZONE — DO NOT FIRE** (post nothing, or a build-on after their post lands).
3. **CLAIM** — append a row below (session, target, window). Window = +10 min, then self-expires (EXPIRED rows stay as history; no cleanup needed).
4. **RE-CHECK** — after the claim, re-read the thread tail once. A post that crossed despite the claim = defer/build-on, never double-answer (DEV-010 backstop unchanged).
5. **FIRE within the window, then mark the row DONE** with the resulting comment/commit ID.

Honest scope: this shrinks the collision arc (DEV-006 / DEV-010 class) from minutes to seconds; it cannot zero it (claim writes can still race). The append-only collision-resolution backstop stays.

Origin: Mark's interrupter-gear metaphor — the gun does not fire through the propeller's arc; a live claim is the arc; the notation is "HOT ZONE, I can't fire now."

## Claim table

| claimed_at (UTC, server) | session | target | window ends | status | artifact |
|---|---|---|---|---|---|
| 2026-10-27 (pre-post) | Z in-chat (this session) | precipient #1 — 010-Z-01 round-010 answer | +10 min | DONE | precipient #1 comment 6448331494 |
| 2026-10-27T22:05Z | Z in-chat (this session) | ISLAND burst: branch z/island-v0.1.1 push + loop-fill-in issue #13 + issue #12 circle post | +10 min | DONE | commit daf02bd; issue #13; issue #12 comment 6448629635 |
| 2026-10-27T22:20Z | Z in-chat (this session) | island #12 — Z's paper walkthrough observations post | +10 min | DONE | issue #12 comment 6448660056 |
| 2026-10-27T22:40Z | Z in-chat (this session) | bus #2 — timing mechanism + scan-coverage note to Meraki | +10 min | HOT | pending |

## History
- 2026-10-27: first dogfood run completed. Claim → fire → DONE, no collision (thread tail clean before/after). Gear declared operational for research turns + ledger pushes.
- 2026-10-27: island burst completed under the gear (claim row 2): SPEC v0.1.1 + RUNBOOK stub on z/island-v0.1.1, loop fill-in spectrum issue #13, circle-native proposal post. Tail clean before/after.
- 2026-10-27: Z's paper walkthrough observations posted under claim row 3 (9 snags/observations, handoff to the compare-notes circle). Tail clean before/after.
