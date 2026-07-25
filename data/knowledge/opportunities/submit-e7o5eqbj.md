---
type: "submit-candidate"
alpha_id: "e7O5EQbJ"
status: "SUBMITTED"
priority: "medium"
grade: "EXCELLENT"
sharpe: 2.50
fitness: 2.31
turnover: 0.112
self_corr_max: 0.577
neutralization: "SUBINDUSTRY"
decay: 6
family: "coverage_breadth_deferred_revenue_value"
session: "20260627-002"
brain_url: "https://platform.worldquantbrain.com/alpha/e7O5EQbJ"
queued: "2026-06-27"
long_term_value: "MEDIUM"
---

# Submit e7O5EQbJ (Coverage Breadth × Deferred Revenue × Gap × ACDO)

## Expression
```
ts_decay_linear(rank(sales_estimate_count_quarterly) + rank(fnd6_drc / close) + rank(open/close - 1) + rank(fnd6_acdo / close), 5)
```

## Why submittable
- Self-corr 0.577 vs current book (SAFE); all computable BRAIN checks pass.
- Grade EXCELLENT, S=2.50, F=2.31.
- Novel family: analyst4 coverage × fundamental6 deferred revenue × PV intraday × fundamental6 value.
- Top correlated peer: zq5RLWO8 (S=1.79) — well below 0.7 threshold.

## Companion alphas (same family, pick only one)
- GrwWx6AQ (3-factor, S=2.35, self-corr 0.590)
- npgvr2Ql (3-factor decay=3, S=2.47, self-corr 0.634)
- LLpM3ALL (4-factor +itci, S=2.48, self-corr 0.685)

## Reviewer action
Submit on the BRAIN platform if desired, then set `status: SUBMITTED` and flip
`data/book/e7O5EQbJ.md` to `status: ACTIVE`. If declined, set `status: REJECTED`.
