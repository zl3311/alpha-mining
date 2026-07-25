---
type: "submit-candidate"
alpha_id: "ZYpVLGZj"
status: "SUBMITTED"
priority: "high"
grade: "SPECTACULAR"
sharpe: 2.84
fitness: 3.21
turnover: 0.178
self_corr_max: 0.7943
neutralization: "SUBINDUSTRY"
decay: 8
family: "ppe_capital_intensity_revision"
session: "20260701-001"
brain_url: "https://platform.worldquantbrain.com/alpha/ZYpVLGZj"
queued: "2026-07-01"
long_term_value: "MEDIUM"
---

# Submit ZYpVLGZj (PP&E Capital Intensity + Revision)

## Expression

`ts_decay_linear(rank(fnd6_newqv1300_ppegtq / close) + rank(anl4_ptpr_flag) + rank(fnd6_itci / close) + rank(open/close - 1), 5)`

## Why submittable

- Self-corr 0.7943 vs MPbgqZ7o (SAFE via Sharpe premium: 2.84 >= 2.838); all 7 computable BRAIN checks pass.
- Grade SPECTACULAR, S=2.84, F=3.21.

## Risk

- Premium escape margin is razor-thin (+0.002). If MPbgqZ7o's Sharpe increases (e.g., via BRAIN recalculation), the premium escape could fail. Submit promptly.

## Reviewer action

Submit on the BRAIN platform if desired, then set `status: SUBMITTED` and flip
`data/book/ZYpVLGZj.md` to `status: ACTIVE`. If declined, set `status: REJECTED`.
