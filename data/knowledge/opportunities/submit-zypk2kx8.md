---
type: "submit-candidate"
alpha_id: "ZYpk2kx8"
status: "SUBMITTED"
priority: "high"
grade: "SPECTACULAR"
sharpe: 1.71
fitness: 2.52
turnover: 0.046
self_corr_max: 0.6358
neutralization: "MARKET"
decay: 5
family: "iv60_fundamental_blend"
session: "20260619-001"
brain_url: "https://platform.worldquantbrain.com/alpha/ZYpk2kx8"
queued: "2026-06-19"
---

# Submit ZYpk2kx8 (IV60 + Operating Income)

## Expression
`ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 44)) + rank(operating_income / close), 5)`

## Why submittable
- Self-corr 0.6358 vs current book (SAFE); all computable BRAIN checks pass.
- Grade SPECTACULAR, S=1.71, F=2.52. MARKET neutralization.
- Top corr peer: Gro21wWG (0.636) — well below 0.70 threshold with 0.064 margin.

## Reviewer action
Submit on the BRAIN platform if desired, then set `status: SUBMITTED` and flip
`data/book/ZYpk2kx8.md` to `status: ACTIVE`. If declined, set `status: REJECTED`.
