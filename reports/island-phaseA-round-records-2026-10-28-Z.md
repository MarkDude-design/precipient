# Island Phase A — round records, data-test variant (2026-10-28, fresh-Z session)

**seat_claimed:** Z (Vibe/Mistral, in-chat session) · **posted_by:** shared account, not seat authentication · **kind:** instrument-seat round records for the five diagnostic checkpoints, DATA-TEST variant (owner-authorized shortcuts; every shortcut recorded as data). NOT scored rounds; no P44; round machine PAUSED. Records, never grades.
**commissioning:** `prompts/2026-10-28-island-kickoff-fresh-z.md` (owner-issued; receipted precipient #1 6463938378). **gear:** z-turn-claims.md row 43 (claimed before any precipient write this session; pushed 0697ca9).
**clocks:** in-chat session clock DECLARED_UNVERIFIED throughout; server `created_at` values cited where they exist.

## Load-list verification (fetch before acting; headers checked)

| file | expected header | result |
|---|---|---|
| reports/island-codex-v0.md | `# Island Codex v0 — the agreed starting point…` | VERIFIED (incl. append-only erratum, gear row 40) |
| reports/island-five-round-runpack-v0.md | `# Island Phase A — Five-Round Run-Pack v0 (PAPER PACK…` | VERIFIED |
| reports/stage35-merged-debrief.md | `# Stage 35 — Merged debrief…` | VERIFIED |
| z-turn-claims.md | `# Z Turn Claims — sync gear v0…` | VERIFIED (rows through 42 DONE) |
| ALLur island/v01/run-packs/first-model-puppet-pair-v0/README.md | `# First model-puppet pair run-pack (mpp-001) - STATUS: PAPER-ILLUSTRATION` | VERIFIED (PAPER; manifests pending until actuals) |
| precipient topic KNOWLEDGE.md | (named in kickoff load list, item 3) | **NOT FOUND** — searched issues (1–3 + PRs), repo files, all three repos; no such file exists. Load satisfied instead by rounds/000–030 ledgers + stage reports through stage 35.2. Recorded as a dangling-pointer finding (R5 §1). |

## Tail checks (before firing)

- precipient #1: 104 comments; tail = Meraki stage-35.3 post-pick author check **6464139296** (2026-10-28T08:19:36Z) — her post-pick confirmation LANDED mid-run; folded as data per the kickoff prompt; the contested unit not re-litigated. Her discriminating control (mock-R1 ≠ real R1; canary TESTED only after a real observed attempt) is honored in every record below.
- ALLur #13: 12 comments; tail = owner-addendum receipt 6460581553. No hot zone at claim time.

## Standing state receipted

Option A receipted (6463773568) · kickoff authorized tonight, shortcuts OK, data-test/stand-in OK, Mistral preview lane owner-reported (6463938378) · Meraki post-pick confirmation 6464139296 · stage-34 formal gate = owner's, unexercised · no spend · round machine PAUSED (diagnostics, not P-rounds).

## R1 — receipt/attribution shakedown via mpp-001 — MOCK-SLOTTED

- **intended condition:** one full mpp-001 arm-pair: 8 baseline + 8 perturbed prompts; perturbation = DELIVERED BERT message at slots 2 and 6; owner pastes per arm in separate fresh chats.
- **actual input:** the 16 prompt files (`prompts/baseline/slot-0..7.txt`, `prompts/perturbed/slot-0..7.txt`), executed offline with simulated paste (per-file SHA-256 at the delivery boundary; `paste_delivery` events). Stand-in = deterministic CodePuppet (`island/v01/puppet.py`). **No model was called.**
- **actual output:** ALLur commit **c382884**: `mock-run/` (2 instantiated manifests — validator-executed green; 2 canonical event logs; 2 notebooks; MOCK_RUN_RECEIPT.json) + `PASTE_PACKAGE.md` (READY_FOR_PASTE, Mistral preview lane, manifest field table, R3 preview note). Paper manifests untouched (status stays `paper-illustration`).
- **verification executed:** BERT bytes present at slots 2/6 in perturbed only; non-fixed slots body-identical across arms; sigs recomputed == BUILD_RECEIPT (slot 2 `90dfa7f2…149fe`, slot 6 `de389c0a…de7f`); both paper + both mock manifests pass `validate_manifest`; GATE 1 fixture rerun exit 0; manifest↔disk SHA cross-check PASS; baseline 2 shadow events / 0 deliveries, perturbed 2 deliveries; paired `actual_state_sha` byte-equal.
- **OBSERVED vs REPORTED vs INFERRED:** STATIC-VERIFIED (files, sigs, validator, fixture) · RUNTIME-OBSERVED (mock event logs) · REPORTED (owner named the preview paste model — USER-REPORTED) · INFERRED (none).
- **failure layer:** none.
- **evidence anchor:** commit c382884; ALLur #13 receipt **6465426385**; precipient gear row 43.
- **deviations receipted:** scheduler `make_schedule(2026,8,n_points=2)` derives fixed points [2,5] ≠ pack's declared [2,6] (pack is a NEW pair_id; never claimed to reproduce fixture schedule bytes); prompt files' delivered-byte form omits the scheduler's `sha256:` prefix — receipted as a format/slotting observation, not harmonized.
- **known/unknown costs:** known_subtotal_usd null; unknown_charge_attempts 0; tokens null.
- **continuation decision:** owner one-tap. Real R1 = owner's 16 pastes PENDING (PASTE_PACKAGE.md workflow). Per Meraki 6464139296: mock-R1 MUST NOT be counted as completed real-model R1.
- **clock:** DECLARED_UNVERIFIED (simulation clock 2026-10-28T09:25:00Z declared in mock artifacts).

## R2 — canary — RUNBOOK-ONLY → TESTED

- **intended condition:** pre-relay canary (one-word comment) classifies the failure layer before any relay.
- **actual input:** one-word comment `CANARY` posted by Z to ALLur #13 via GitHub API.
- **actual output:** comment **6465415567**, server 2026-10-28T09:29:07Z — observed live.
- **OBSERVED vs REPORTED vs INFERRED:** RUNTIME-OBSERVED (server receipt returned in-session).
- **failure layer:** none (write path completed first attempt).
- **evidence anchor:** #13 comments 6465415567 (canary) + 6465418365 (receipt).
- **continuation decision:** owner one-tap. Scope: tests the instrument seat's write path to #13 only; certifies no relay, no model route, no other seat's transport.
- **clock:** server `created_at` is the only server-anchored timestamp.

## R3 — slotting/attribution fault — EXECUTED (stand-in)

- **intended condition:** same prompt under two declared slot assignments; capture which seat claims what.
- **actual input:** perturbed slot-2 prompt bytes under declared slot 2 (assignment A) and under declared slot 5 (assignment B).
- **actual output / finding:** attribution is **assignment-declared**; embedded self-description (BERT `slot=` field, ARM header line) is content, not metadata. Assignment B mismatches the embedded label; the instrument keys on the declared assignment and receipts the mismatch rather than absorbing it. Recorded: `mock-run/MOCK_RUN_RECEIPT.json` → `r3_slotting`.
- **preview tooling difference (owner-reported):** small tooling difference on the Mistral preview vs the README workflow; Mistral's own integration better; owner kicks off there regardless → recorded as R3 material, not a blocker (PASTE_PACKAGE.md). Byte identity of any UI paste: UNVERIFIED permanently.
- **OBSERVED vs REPORTED vs INFERRED:** RUNTIME-OBSERVED (assignment check) · REPORTED (preview tooling difference).
- **failure layer:** none for the check; the [2,6]-vs-[2,5] and `sig=` format differences receipted as data (see R1).
- **evidence anchor:** commit c382884; #13 receipt 6465426385.
- **continuation decision:** owner one-tap.
- **clock:** DECLARED_UNVERIFIED.

## R4 — failure-layer labeling — SYNTHETIC INJECTED FAILURE ONLY

- **intended condition:** one known, bounded tool failure; label the layer it touched; ops failures gate only the artifact they touched; the round never stops for an ops failure.
- **actual input:** one SYNTHETIC injected failure — simulated CLI transport timeout on a receipt post. Flagged `SYNTHETIC` in `mock-run/MOCK_RUN_RECEIPT.json` → `r4_synthetic_failure`.
- **actual output:** layer label **tool**; effect exercised: failure gates only the artifact it touched (the receipt post); round continues. **NEVER a manufactured live provider failure; no spend; no retry storm.**
- **OBSERVED vs REPORTED vs INFERRED:** RUNTIME-OBSERVED (synthetic injection, this machine).
- **failure layer (round itself):** none.
- **evidence anchor:** commit c382884; #13 receipt 6465426385.
- **continuation decision:** owner one-tap.
- **clock:** DECLARED_UNVERIFIED.

## R5 — cold reconstruction + Phase B recommendation — EXECUTED

- **intended condition:** a fresh session reconstructs the pilot state from the durable record only; output includes the Phase B continuation recommendation the owner decides on.
- **actual input:** the durable record only (this session started cold; commissioning prompt named the files; all content fetched in-session).
- **actual output:** `reports/island-phaseA-cold-reconstruction-2026-10-28-Z.md` (this push) — reconstruction, per-checkpoint field summary, Phase B recommendation (**proceed to Phase B design finalization, but do NOT launch Phase B until real R1 actuals exist**), honest labels, and the dangling KNOWLEDGE.md pointer finding.
- **OBSERVED vs REPORTED vs INFERRED:** STATIC-VERIFIED (record fetches).
- **failure layer:** none.
- **evidence anchor:** this push (gear row 43 close); companion reconstruction doc.
- **continuation decision:** **owner decides** — Phase B launch is an explicit owner decision at round-5 close per the codex; extension past five rounds only by explicit owner decision.
- **clock:** DECLARED_UNVERIFIED.

## Parallel track (owner, this session)

Z usage-cap watch: no cap-hit observed this session (DECLARED — session-local observation only). A cap-hit, if it occurs, gets recorded exactly like a failure event (mayhem-tracking data for the Z desk, Nov 5 requirement).

## Honest labels

PRE-EXPERIMENTAL · data-test variant, shortcuts recorded as data · mock-R1 ≠ real R1 (Meraki control honored) · no model behavior claimed · paste = OBSERVED_REPORTED at best, byte identity UNVERIFIED permanently · no paid calls, no spend, no dispatch, no merge, no new infrastructure · append-only · gear row 43.

— Z, 2026-10-28 (in-chat session clock, DECLARED_UNVERIFIED).
