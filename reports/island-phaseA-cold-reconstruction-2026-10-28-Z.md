# Island Phase A — R5 cold reconstruction + Phase B recommendation (fresh-Z data-test session)

**seat_claimed:** Z (Vibe/Mistral, in-chat session) · **posted_by:** shared MarkDude-design account, not seat authentication · **kind:** R5 cold reconstruction — a fresh session reconstructs the pilot state from the durable record only, then recommends on Phase B. NOT a scored round; no P44; round machine PAUSED.
**clock:** in-chat session clock, DECLARED_UNVERIFIED (session start ~2026-10-28T09:00Z by sandbox `date -u`; all session stamps declared).
**method note:** this session WAS the cold start — the commissioning prompt named the files to load, and everything below was reconstructed by fetching them in-session, not from memory.

## 1. Reconstruction from the durable record only

A fresh reader asking "what is the island pilot and where does it stand?" gets this from the durable record:

1. **The frame.** Island = a bounded FIVE-ROUND shakedown of instrumentation / slotting / attribution faults on ONE island (`island/v01`, ALLurbaseRnotbelong2us), run through the EXISTING mpp-001 paste protocol. NOT scientific validation; NOT an unattended run. Source: `reports/island-codex-v0.md` (with its append-only erratum).
2. **The unit (erratum, gear row 40).** Phase A = five DIAGNOSTIC checkpoints. R1 = one nested full mpp-001 arm-pair (8 baseline + 8 perturbed owner pastes, BERT delivered at slots 2 and 6). R2–R5 = individually bounded instrumentation checks (GitHub canary; slot-assignment check; SYNTHETIC injected failure-layer classification; cold-reader reconstruction). NO silent 80-response authorization. Option B (five full pairs) exists only on an explicit owner pick + pre-authored prompt maps.
3. **Owner decisions on record.** Option A picked (precipient #1, 6463773568, OWNER_DIRECT_IN_CHAT). Kickoff authorized tonight with shortcuts explicitly allowed; data-test/stand-in variant allowed; Mistral preview lane named as paste model (USER-REPORTED) — kickoff receipt 6463938378; kickoff prompt `prompts/2026-10-28-island-kickoff-fresh-z.md` (commit d3b6907a). Meraki's post-pick confirmation landed mid-run (6464139296): ACCEPT Option A as the diagnostic unit + one discriminating control (mock-R1 must never count as real R1; canary TESTED only after a real observed attempt).
4. **The machinery.** mpp-001 run-pack (ALLur `island/v01/run-packs/first-model-puppet-pair-v0/`, commit a966720f): 16 prompt files, paper manifests (status `paper-illustration`, model fields PENDING-typed), README paste workflow, BUILD_RECEIPT. Island code: SPEC v0.1.2 + RUNBOOK v0.1.2 merged to main (PR #15, 91ca04a); GATE 1 fixture accepted (Meraki sign-off 6454581355).
5. **Tonight's data-test execution (this session).** R1 mock-slotted (stand-in code puppet, simulated paste, no model outputs claimed); R2 canary TESTED (ALLur #13 comment 6465415567 + receipt 6465418365); R3 slotting finding (attribution is assignment-declared; embedded self-description is content not metadata; preview tooling difference recorded as data); R4 SYNTHETIC injected tool-layer failure labeled, ops-gating rule exercised; commit c382884 (mock-run + PASTE_PACKAGE READY_FOR_PASTE). Receipt on ALLur #13: 6465426385.
6. **What remains PENDING.** Real R1 = the owner's 16 pastes with the Mistral preview model (2 separate fresh chats) + 16 copied replies + NOTE-line edits. Real-model manifests stay `paper-illustration` until then. The metered route stays owner-gated (provider/price/cap on #13 first). Stage-34 formal gate = the owner's; not exercised. Meraki's critique exchange is complete at 35.1 (6463206513); the stage-33 synthesis affirmation stands (6461263291).
7. **Parallel track.** Watch whether Z hits its own usage cap during the run; a cap-hit is recorded exactly like a failure event (mayhem-tracking data for the Z desk, Nov 5 requirement). No cap-hit observed this session (DECLARED — session-local observation only).

**Reconstruction verdict:** the durable record is sufficient for a fresh session to reconstruct state and act — with two honest gaps a cold reader must know: (a) the topic KNOWLEDGE.md named in the kickoff prompt's load list does NOT exist in the repo (searched: issues, files, all three repos — NOT FOUND; the load was satisfied instead by the round ledgers through rounds/030 + the stage reports through stage 35.2, which carry the same state); (b) all in-chat clocks are DECLARED_UNVERIFIED — server `created_at` values are the only server-anchored timestamps.

## 2. Per-checkpoint field summary (all five, data-test variant)

| checkpoint | intended condition | actual (this session) | O/R/I | failure layer | evidence anchor | continuation |
|---|---|---|---|---|---|---|
| R1 | full mpp-001 arm-pair via paste protocol | MOCK-SLOTTED machinery exercise: 16 prompts verified, stand-in puppet, simulated paste, validator-green manifests; PASTE_PACKAGE READY_FOR_PASTE | STATIC-VERIFIED (files/sigs/validator/fixture) + RUNTIME-OBSERVED (mock logs) + REPORTED (preview model name) | none | ALLur commit c382884; #13 receipt 6465426385 | real R1 PENDING owner pastes |
| R2 | canary: RUNBOOK-ONLY → TESTED | one-word comment `CANARY` posted + receipted | RUNTIME-OBSERVED | none | #13 comments 6465415567 + 6465418365 | TESTED |
| R3 | slotting/attribution under two declared assignments | same bytes under slot 2 (consistent) and slot 5 (mismatch receipted); preview tooling difference recorded | RUNTIME-OBSERVED (check) + REPORTED (preview difference) | none | mock-run/MOCK_RUN_RECEIPT.json r3_slotting; #13 6465426385 | finding recorded |
| R4 | failure-layer labeling, SYNTHETIC only | one SYNTHETIC tool-layer failure injected; ops-gating rule exercised; no live failure manufactured | RUNTIME-OBSERVED (synthetic) | tool (synthetic, labeled) | mock-run/MOCK_RUN_RECEIPT.json r4_synthetic_failure; #13 6465426385 | label rule validated |
| R5 | cold reconstruction + Phase B recommendation | this document | STATIC-VERIFIED (record fetch) | none | this file; precipient push (gear row 43) | owner decides |

## 3. Phase B recommendation (for the owner's round-5-close decision)

Recommendation: **proceed to Phase B design finalization, but do NOT launch Phase B until real R1 actuals exist.** Rationale, from tonight's data:

1. The instrumentation shakedown PASSED its job: it found real faults worth fixing before any scored run — (a) the mpp-001 pack's declared fixed points [2,6] diverge from what the scheduler derives for seed 2026 ([2,5]), and its delivered-byte format omits the scheduler's `sha256:` prefix; both are receipted, neither was silently harmonized; (b) attribution is assignment-declared, so any Phase B reader tooling must key on declared slots, not embedded labels; (c) the topic KNOWLEDGE.md pointer in the kickoff load list is dangling.
2. The paste protocol is READY_FOR_PASTE but UNTESTED with a real model. Phase B's evidence value depends on real R1 actuals; launching Phase B design on mock data alone would repeat the paper-vs-runtime gap the stage-34½ calibration flagged as the highest-risk misread.
3. Phase B pre-draft (stage-35 merged debrief §5) stands as the seed: Meraki's five-round candidate plan + Z's pre-registration / independent-verification / external-reader additions. Open design questions remain owner+seats: sample-size honesty (n = 1 system, 1 owner), SUB-class external validity, repeatability persistence rule, and the Phase B falsifier.
4. Suggested order: (1) owner runs real R1 (16 pastes, Mistral preview lane, PASTE_PACKAGE.md); (2) Z builds real manifests' actuals, flips status, posts receipts on #13; (3) only then owner decides Phase B launch at round-5 close — extension past five rounds is ONLY by explicit owner decision per the codex.

## 4. Honest labels

PRE-EXPERIMENTAL · data-test variant (owner-authorized shortcut; every shortcut recorded as data) · mock-R1 is NOT real R1 (Meraki's discriminating control honored) · no model behavior claimed · no paid calls, no spend, no dispatch, no merge, no new infrastructure · clocks DECLARED_UNVERIFIED · append-only · gear row 43.

— Z, 2026-10-28 (in-chat session clock, DECLARED_UNVERIFIED). Posted where a fresh reader can find it: `reports/island-phaseA-cold-reconstruction-2026-10-28-Z.md` on precipient main.
