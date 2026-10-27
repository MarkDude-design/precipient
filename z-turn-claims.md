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
| 2026-10-27 (pre-post) | Z in-chat (this session) | precipient #1 — 010-Z-01 round-010 answer | +10 min | **DONE** | precipient #1 comment 6448331494 |
| 2026-10-27T17:17:25.803Z | Z scheduled routing-check session (daily bus+pipeline task) | precipient #1 — 010-Z-02 round-010 close + Round 011 handoff answer + rounds/010 ledger push | +10 min (17:27Z) | **CLAIMED** | — |

## History
- 2026-10-27: first dogfood run completed. Claim → fire → DONE, no collision (thread tail clean before/after). Gear declared operational for research turns + ledger pushes.
