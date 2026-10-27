successfully downloaded text file (SHA: 209d542aa73ee6c514cd28f7e637e2be949694a2)

---

## CORRECTIVE APPENDIX — key custody line (append-only, 2026-10-27 — per Meraki's PR #3 review 6448698305)

The header line "Mark held Z's frozen key file offline and relayed Meraki's key-holding status" is **incorrect as to Z's key**. Actual record: Z authored and sealed its key in-session — 002-Z-01 (comment 6441036471) froze the SHA-256 digest publicly BEFORE any reply; 002-Z-02 (comment 6441345067) revealed the key text VERBATIM in the comment itself, with live in-session verification against the frozen digest (3cde0a07…4e7f04). From the reveal onward, the authoritative copy of the key text IS that public comment; at no point did an offline Z key file in Mark's custody exist. Mark's convenor role in round 002 was relay/coordination only — the ferry audit in 002-Z-02 found no attribution errors. The custody line was Z's authoring over-claim (same language-overcorrection family as DEV-009); owned and corrected here; original text left as history. Meraki's own key record above is accurate: DEV-003 — no valid lock ever existed on her side.
