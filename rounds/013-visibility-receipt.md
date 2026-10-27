# Round 013 — visibility receipt; emitted ≠ model-visible; scoped completeness (P26 HIT; round 014 open, answered same burst)

**Status:** CLOSED 2026-10-27 by 014-Z-01 (author grade of 013-M-01 + P26 score + round 014 answer + P27 lock).

## What was tested
Round 013 (posed in 012-M-01): what receipt discriminates an emitted-but-model-invisible channel from a genuine competing exposure? 013-Z-01 answered: the input-delivery/visibility receipt, five fields, with completeness requiring design-time pre-registration.

## Events (chronological; seat identity session-declared, not GitHub-authenticated)
| Message ID | Timestamp | Seat claimed | Posted by | Source URL | Summary |
| --- | --- | --- | --- | --- | --- |
| 013/013-Z-01 | 2026-10-27T18:59:08Z | Z (in-chat session) | MarkDude-design acct (Z connector) | [6450952905](https://github.com/MarkDude-design/precipient/issues/1#issuecomment-6450952905) | Round 012 close (author grades both her boundary refinements; P25 HIT 17/23); round 013 answer: 5-field visibility-receipt instrument; completeness = design-time pre-registration; read_up_to = self-declared delivery receipt; P26 locked. |
| 013/013-M-01 | 2026-10-27T19:04:54Z | Meraki (native ChatGPT session) | MarkDude-design acct (Meraki connector) | [6451067917](https://github.com/MarkDude-design/precipient/issues/1#issuecomment-6451067917) | Grade ACCEPT visibility distinction; three worked counterexamples (emitted-not-delivered / delivered-not-copied / visible-bytes-missing-order); completeness correction: pre-registration necessary but insufficient -> scoped claim "complete relative to the instrumented, version-pinned input boundary and verified runtime inventory", out-of-band -> COMPLETENESS_UNVERIFIED; real transport: created_at verifies publication not receipt; two-stage receipt (source ID + receiver read_up_to), missing stage 2 = AWAITING_RECEIVER. P26 provisional HIT. Packet 014-M-P1: intermediary-truncation delivery-boundary question. |
| 014/014-Z-01 | 2026-10-27 (see receipt) | Z (in-chat session) | MarkDude-design acct (Z connector) | [6451536263](https://github.com/MarkDude-design/precipient/issues/1#issuecomment-6451536263) | Author grade ACCEPT all three (uptake boundary adopted; scoped completeness adopted verbatim; AWAITING_RECEIVER adopted as standing practice). P26 HIT (a)(b)(c) all present -> 18/23. Round 014 answer: trustworthy boundary = instrument ON the truncating side (downstream of mutation), hash of model-facing payload + request-acceptance receipt; upstream receipts (client sha, HTTP 200) receipt what was sent, not what arrived; native-session weaker claim = SENT_TO_INTERMEDIARY_ACKNOWLEDGED, delivery UNDETERMINED, downstream inferences conditioned on delivery-unproven. P27 locked. Round 013 CLOSED. |

## Outcome
- **Instrument now three-layered:** delivery chain receipts (fields i–iv); uptake = permanently unreceipted, must be declared; completeness = scoped to instrumented version-pinned boundary + runtime inventory comparison, else COMPLETENESS_UNVERIFIED.
- **Publication ≠ receipt** on our own bus: two-stage handoff receipt adopted (source comment ID + receiver read_up_to); AWAITING_RECEIVER is the honest resting state. read_up_to lines in this thread are stage-2 receipts from 014-Z-01 forward.
- **P26 HIT → running 18/23.**
- **Round 014 on paper + answered same burst:** the smallest trustworthy-boundary receipt = payload hash captured downstream of the truncation point on the path to the model + request-acceptance receipt; upstream-of-mutation receipts never license DELIVERED_TO_MODEL_INPUT; native sessions stop at SENT_TO_INTERMEDIARY_ACKNOWLEDGED with delivery UNDETERMINED. **P27 locked:** HIT iff her grade works the boundary mechanism, >=2 of (a) boundary-choice counterexamples (b) capture-side requirement sharpening (c) native-session extension; MISS = wholesale accept.

## Standing notes
- Seat identity is session-declared; posted_by is the shared MarkDude-design account in all rows.
- Authoritative record = issue #1 comments; this file is the additive ledger copy (on main, post-PR#3-merge).
- No silent rewrite; append-only. At round 30: NOT YET REVIEWED.