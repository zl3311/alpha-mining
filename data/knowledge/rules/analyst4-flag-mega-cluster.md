---
rule: "Nearly all anl4_*_flag fields belong to one 127-member redundancy mega-cluster; picking a different flag does not meaningfully escape correlation with the analyst-revision-heavy book"
category: "rule"
severity: "high"
discovered: "20260715-002"
confidence: "medium"
evidence: "factor-themes-redundancy.md cluster #13 (127 members, mean |rho| 0.82) lists anl4_bvps_flag, anl4_ptpr_flag, anl4_netdebt_flag alongside anl4_cfi_flag/anl4_cff_flag/anl4_cfo_flag/anl4_capex_flag/anl4_fcf_flag/anl4_fcfps_flag/anl4_totassets_flag (cluster #18, itself correlated with #13) as members; empirically, swapping anl4_fcf_flag for anl4_cfi_flag or anl4_capex_flag in an otherwise-identical blend did not reduce local self-corr below ~0.69-0.81 in session 20260715-002."
---

# Rule: The Analyst4 Flag Universe Is Effectively One Correlation Cluster

## The rule

Choosing a "fresh" `anl4_*_flag` field (one never used verbatim in a book
entry) is NOT sufficient to escape correlation with the book's existing
analyst-revision alphas. `data/knowledge/opportunities/factor-themes-redundancy.md`
cluster #13 (127 members, mean |rho| 0.82) and cluster #18 (7 members,
mean |rho| 0.82, itself correlated with #13) together span nearly the entire
`anl4_*_flag` universe: `anl4_bvps_flag`, `anl4_ptpr_flag`,
`anl4_netdebt_flag`, `anl4_cff_flag` (all already ACTIVE in the book) sit in
the same broad cluster as `anl4_cfi_flag`, `anl4_cfo_flag`, `anl4_capex_flag`,
`anl4_fcf_flag`, `anl4_fcfps_flag`, `anl4_totassets_flag` — fields that
LOOK fresh (zero prior book usage) but are statistically redundant with
fields that ARE already in the book.

## Evidence (session 20260715-002)

Four candidates using different analyst4 flags in an otherwise near-identical
5-factor blend (`guidance/event-magnitude anchor + ivaco + drlt-or-fatl +
FLAG + buzz*(-ret)`) all landed in the 0.69-0.81 local self-corr range
regardless of which specific flag was used:

| Flag used | Local self-corr vs book |
|-----------|--------------------------|
| `anl4_fcf_flag` (`N1rlJ7mq`) | 0.691 |
| `anl4_cfi_flag` (`oml0kV52`) | 0.796 |
| `anl4_cfi_flag` (`kq06YLrd`, `fatl` variant) | 0.813 |

Removing the flag leg entirely (`np25lW8a`, drlt+fatl only, no flag) still
showed 0.803 local corr — suggesting the flag choice is a secondary driver at
best; the dominant driver may be `buzz*(-ret)` and/or `ivaco`/`drlt`
themselves (see pattern note in session `20260715-002` learnings).

## Implication for mining

Do not treat "this specific `anl4_*_flag` has never appeared in a book
entry" as evidence of low correlation risk. Check the field's redundancy
cluster membership in `factor-themes-redundancy.md` first — if it lands in
cluster #13 or #18, treat it as functionally equivalent (for self-corr
purposes) to whichever member of that cluster is already ACTIVE.
