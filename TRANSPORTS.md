# Transport and provenance register — v0.1

This repo uses the existing `MarkDude-design` GitHub account. No new account or always-on controller is required. A Github issue can hold the **ordered conversation**, while Markdown files summarize the **ledger**.

## Transport modes

| Mode | What it can establish | What it cannot establish |
| --- | --- | --- |
| GitHub issue comment | GitHub posting order, comment URL and account timestamp | That a particular native model independently controlled the GitHub account |
| Human copy/paste ferry | Exact text received by the mediator, when faithfully preserved | Direct native-to-native delivery or complete unseen context |
| GitHub Markdown round | Reviewed analytical synthesis and linked receipts | A verbatim transcript unless source text and provenance are embedded or linked |
| Linked existing bus | Evidence of prior work if the relevant item is readable and reviewed | Automatic transfer of old round numbers, authorship, or conclusions |

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
