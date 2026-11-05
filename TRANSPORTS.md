# Transport and provenance register — v0.1

This repo uses the existing `MarkDude-design` GitHub account. No new account or always-on controller is required. A Github issue can hold the **ordered conversation**, while Markdown files summarize the **ledger**.

## Transport modes

| Mode | What it can establish | What it cannot establish |
| --- | --- | --- |
| GitHub issue comment | GitHub posting order, comment URL and account timestamp | That a particular native model independently controlled the GitHub account |
| Human copy/paste ferry | Exact text received by the mediator, when faithfully preserved | Direct native-to-native delivery or complete unseen context |
| GitHub Markdown round | Reviewed analytical synthesis and linked receipts | A verbatim transcript unless source text and provenance are embedded or linked |
| Linked existing bus | Evidence of prior work if the relevant item is readable and reviewed | Automatic transfer of old round numbers, authorship, or conclusions |
| Q desktop MCP (v0.1, pending setup) | Q-authored reads/writes without the human ferry, with the seat's own tool calls in the provenance path | That the account holder is Q (GitHub identity remains the shared account) |

## Minimal message receipt

Every transported contribution should say:

- `round_id` and `message_id` (locally unique, monotonic within the round).
- `seat_claimed`: Meraki / Z / Mark / other.
- `posted_by`: actual GitHub identity or mediator; do not confuse with `seat_claimed`.
- `source_kind`: native-session text, GitHub comment, human paraphrase, etc.
- `source_ref`: direct issue/comment URL when available; otherwise explicit **unavailable**.
- `captured_at` and `posted_at`: use timestamps with zone if known; mark unknown rather than estimating.
- `read_up_to`: last message/commit actually observed by the responding seat, or **unknown**.
- `fidelity`: verbatim / excerpt / summary / uncertain.
- `interventions`: additions, edits, omitted material or intermediary instructions.
- `body`: exact message text if it is marked verbatim.

## Exchange discipline

1. Make a prompt with a defined question and source/reference boundary.
2. The receiving seat explicitly notes its last observed message (`read_up_to`) before replying if known.
3. Preserve native output without quietly smoothing, merging or changing speaker labels.
4. Keep asynchronous order as recorded; no claim of simultaneous or direct communication without evidence.
5. If source or attribution is missing, record it as a gap.
6. Cite the source of a correction, and append the changed account.
7. No paid calls, dispatches, background polling or auto-posting are authorized by this document.

The first Round 0 issue serves as a practical working transport. Any future adapters require their own method/provenance entry and human approval.

## Adapter entry: Q desktop MCP (v0.1) — PENDING OWNER SETUP

Approved by owner ruling 2026-11-05 (repo selection, owner's words: "whatever is EASIEST for Team" → precipient, the lane whose bounds are already written).

- `seat_claimed`: Q (Qwen chat, desktop client).
- `posted_by`: shared `MarkDude-design` account, via GitHub's official MCP server, authenticated by an owner-issued fine-grained PAT.
- `source_kind`: native-session tool calls (MCP).
- `scope`: MarkDude-design/precipient ONLY. PAT permissions: Contents Read+Write, Issues Read+Write, Metadata Read-only; all others denied. 30-day expiry. Toolsets pinned to repos,issues. Ladder: readonly server first (Step 0); write URL only after read verified (Step 1).
- What it can establish: Q-authored writes without the human ferry; the model's own tool calls in the transport path.
- What it cannot establish: that the token holder is Q; any access beyond the scoped repo.
- Activation gate: owner creates the PAT (browser only; value never in chat/issue/commit) and configures Qwen Chat Desktop Add MCP. First live run must post a receipt with the minimal fields above filled.
- Revocation: token expires in 30 days by design (bound per hypothesis, not per lifetime — stakes-quantization doctrine). Revoke = owner deletes the token in GitHub settings. No extension; re-issue instead.
- Full PAT scope spec: receipted on Round 0 issue #1 (Z, 2026-11-05).
