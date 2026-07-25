---
type: "submit-candidate"
alpha_id: "LLR0n261"
status: "SUBMITTED"
priority: "high"
grade: "EXCELLENT"
sharpe: 2.51
fitness: 2.35
turnover: 0.1835
self_corr_max: 0.6094
self_corr_method: "brain_self_correlation_breakdown"
self_corr_verdict: "SAFE"
neutralization: "SUBINDUSTRY"
decay: 6
family: "accrual_intraday_analyst_revision"
session: "20260615-002"
brain_url: "https://platform.worldquantbrain.com/alpha/LLR0n261"
queued: "2026-06-15"
---

# Submit LLR0n261 (Accrual Intraday Analyst Revision)

## Expression

`ts_decay_linear(rank(fnd6_acdo) + rank(open / close - 1) + rank(anl4_netdebt_flag), 5)`

## Why Submittable

- BRAIN self-correlation check PASS at 0.6094, below the 0.70 threshold.
- All computable BRAIN checks PASS.
- EXCELLENT grade, S=2.51, F=2.35, turnover 18.35%.
- Re-verified after `GrwrVP5G` was marked ACTIVE locally; `GrwrVP5G` did not
  enter the top correlated peer set for this candidate.

## Risk Assessment

Top observed peer is `vR56vdYd` at 0.6094, safely below the raw threshold.
`88LMONJa` is a current-book-passing backup from the same backbone, but likely
too redundant to submit after `LLR0n261` is activated.

## Reviewer Action

BRAIN check reported this alpha as ACTIVE on 2026-06-17, and the user confirmed
it was submitted. `data/book/LLR0n261.md` has been flipped to `status: ACTIVE`.
