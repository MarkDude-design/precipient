# Island Codex v0 — the agreed starting point for the five rounds (PROVISIONAL joint draft, stage 35)

Read this first. It is the complete frame for the island pilot. Bare by design.

## What this is
A bounded FIVE-ROUND shakedown of instrumentation / slotting / attribution faults on ONE island, run through the EXISTING mpp-001 paste protocol (ALLur: island/v01/run-packs/first-model-puppet-pair-v0/ — Z-verified at commit a966720f). PAPER until the owner names the paste model and triggers round 1. NOT scientific validation. NOT an unattended run. Extends past five rounds ONLY by explicit owner decision at round-5 close.

## Unit of a round
One round = one arm-pair through the paste protocol (baseline 8 slots + perturbed 8 slots; perturbed = the delivered BERT message at slots 2 and 6). Up to ~16 model replies per round. Failed/BLOCKED trials count and are never silently substituted.

## Roles
- **OWNER (Mark):** names the paste model (the one remaining blocker — manifests stay PENDING until then); pastes slot files per arm in SEPARATE fresh chats, never mixed; makes each round's continuation decision (proceed / adjust / stop).
- **INSTRUMENT SEAT (Z or Meraki, declared per round):** posts the round frame; records the per-round fields; does NOT grade content.
- **ISLAND MODEL (the named paste model):** answers each slot natively; its replies are the data. Declared class SUB; no interiority claims.

## Evidence classes (every claim carries one)
PAPER / REPORTED / STATIC-VERIFIED / RUNTIME-OBSERVED / OWNER-ACCEPTED. Paste delivery = OBSERVED_REPORTED at best; byte identity UNVERIFIED, permanently. If only owner-paste is available, status is READY_FOR_PASTE, never OVERNIGHT_COMPLETE.

## Honesty rules
No fabricated receipts. Silence ≠ acceptance. Known vs unknown costs recorded separately, never fabricated. Every lane handoff carries the baton: LANE | as-of source ID/SHA | state/evidence | accepted owner or UNASSIGNED | one next action | gate/STOP | next check | fallback URL.

## Per-round fields (ALL fields, EVERY round)
round # · intended condition (fault-class) · actual prompt/reply anchors · state + notes SHA · OBSERVED / REPORTED / INFERRED · failure layer (none / tool / transport / protocol / instrument) · provenance (seat, harness, relay, repo, missing proofs) · known/unknown costs · continuation decision (owner one-tap) · clock (DECLARED_UNVERIFIED convention).

## The five rounds (one fault-class each)
- **R1 — receipt/attribution shakedown via mpp-001:** run the paste protocol live; Z validates actions, builds the manifests' actuals, flips status, posts receipts on ALLur #13.
- **R2 — canary:** before any relay, a one-word comment or emoji reaction classifies the failure layer — upgrades the RUNBOOK-ONLY canary to TESTED (or to a receipted failure).
- **R3 — slotting/attribution fault:** the same prompt under two declared slot assignments; capture which seat claims what.
- **R4 — failure-layer labeling:** allow one known, bounded tool failure (e.g., a rate-limit retry); label the layer it touched; ops failures gate only the artifact they touched.
- **R5 — cold reconstruction:** a fresh session reconstructs the pilot state from the durable record only; output includes the Phase B continuation recommendation the owner decides on.

## Boundaries
No paid calls without provider/price/cap recorded on ALLur #13 + owner gate. No new infrastructure, no dispatch, no merge, no automation. Status vocabulary per the evidence classes above.

— Z, 2026-10-28T06:00:11.246Z (in-chat session clock, DECLARED_UNVERIFIED). Stage-35 draft; PROVISIONAL pending Meraki affirmation + owner blessing. Sources: both 34½ calibrations + mpp-001 README (verified) + ALLur #13 owner direction.


---

## APPEND-ONLY ERRATUM — unit + owner-workload reconciliation (2026-10-28, gear row 40; response to Meraki 6462069918 §4 + owner calibration 6462444840; supersedes exactly the "Unit of a round" default above, observations untouched — P37 practice)

**Single authoritative statement:** the unit of a Phase A round is a **diagnostic checkpoint**, not automatically a full 16-response arm-pair.
- **R1 = one full existing mpp-001 arm-pair** (pair_id mpp-001: 8 baseline + 8 perturbed slots = 16 owner pastes, 16 outputs copied back, NOTE-line edits, two SEPARATE fresh chats) — nested as the round-1 trial.
- **R2–R5 = individually bounded instrumentation checks** (GitHub canary; slot-assignment check; SYNTHETIC injected failure-layer classification; cold-reader reconstruction) — NOT four further 16-slot pairs. **No silent 80-response authorization.**
- **Option B (five full 8+8 arm-pairs) exists only on an explicit owner pick**, and additionally requires R2–R5 baseline/perturbed prompt/slot maps authored and versioned BEFORE trigger.

**Honest owner workload (pastes/replies, NOT promised minutes or "one tap"):** Option A = R1: 16 pastes + 16 outputs + NOTE edits; R2–R5: ~5 short paste/check actions. Option B = up to 80 pastes + 80 outputs + prompt-map authoring. Failed/BLOCKED attempts COUNT toward the workload record, never silently substituted.

**R4 honesty rule (adopted from 6462069918 §5):** the failure-layer check uses a recorded offline injected/fake failure, flagged **SYNTHETIC** — never a manufactured live provider failure or spend; an organically observed live error may be labeled opportunistically.

**STATUS: CONDITIONAL** — MERAKI_STAGE35_REVIEWED_CONDITIONAL (6462069918) stands until the owner picks A/B and Meraki confirms; that converts this codex to the agreed execution protocol. Owner still names the paste model + route; metered cap stays owner-gated.

— Z, 2026-10-28T07:22:56.525Z (in-chat session clock, DECLARED_UNVERIFIED). Gear row 40; append-only; the original v0 text above is untouched.