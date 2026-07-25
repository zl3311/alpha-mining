---
type: "submit-candidate"
alpha_id: "vRmlGnkv"
status: "SUBMITTED"
priority: "high"
grade: "EXCELLENT"
sharpe: 1.72
fitness: 2.21
turnover: 0.081
self_corr_max: 0.593
neutralization: "SUBINDUSTRY"
decay: 6
family: "analyst_revision_zscore"
session: "20260608-001"
brain_url: "https://platform.worldquantbrain.com/alpha/vRmlGnkv"
queued: "2026-06-08"
---

# Submit vRmlGnkv (netprofit revision zscore)

## Expression
`ts_decay_linear(zscore(ts_sum(anl4_netprofit_flag, 22)), 3)`

## Why submittable
- Self-corr 0.593 vs current book (SAFE — well below 0.70 threshold).
- All 8 BRAIN checks PASS (verified via /alphas/{id}/check endpoint).
- EXCELLENT grade, S=1.72, F=2.21. Would be the 5th SPECTACULAR/EXCELLENT-tier alpha.
- Uses anl4_netprofit_flag which has ZERO overlap with any existing book entry field.

## Risk assessment
- Top correlated peer is vR56vdYd (analyst_revision, corr=0.593). Both use analyst4
  dataset but different fields (netprofit_flag vs other analyst flags). The
  correlation is from shared underlying analyst behavior, not field overlap.
- After submission, other netprofit variants (E5KEzxzR, GroLXj95, etc.) will
  likely fail self-corr (they're the same signal).

## Reviewer action
BRAIN check reported this alpha as ACTIVE on 2026-06-17. `data/book/vRmlGnkv.md`
is already `status: ACTIVE`.
