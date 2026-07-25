---
alpha_id: "LLR0Xjz2"
name: "exp20260615-001_acdo_dlto_salescount_decorr"
tags:
  - "session_20260615-001"
  - "ortho-theme"
  - "clean-decorrelated"
submitted: null
session: "20260615-001"
grade: "AVERAGE"
sharpe: 1.75
fitness: 1.48
turnover: 0.058
expression: "ts_decay_linear(rank(fnd6_acdo) + rank(fnd6_dlto / close) + rank(sales_estimate_count), 10)"
family: "fundamental_analyst_coverage"
neutralization: "SUBINDUSTRY"
decay: 10
self_corr_max: 0.675
status: "PENDING"
brain_url: "https://platform.worldquantbrain.com/alpha/LLR0Xjz2"
---

# Alpha: LLR0Xjz2

## Expression
```
ts_decay_linear(rank(fnd6_acdo) + rank(fnd6_dlto / close) + rank(sales_estimate_count), 10)
```

## Mechanism

Clean fundamental + analyst-coverage blend with NO `itci`, IV-spread, or
`flag*(-ret)` components: accrued/deferred items (`fnd6_acdo`), long-term debt
value (`fnd6_dlto / close`), and analyst sales-estimate breadth
(`sales_estimate_count`). All three legs individually pass `LOW_SUB_UNIVERSE_SHARPE`
(broad coverage), so the blend clears all 8 IS checks at AVERAGE grade and low
turnover (5.8%).

## Self-Correlation Profile

Max self-corr 0.675 vs the fundamental book (`pw8wNe76` 0.675, `6Xzm6PQP` 0.670,
`0mzQQvX8` 0.670). Below BRAIN's 0.70 gate (PASS) but above the conservative 0.65
buffer -> RISKY. Submission is a judgment call: it grinds points as a decorrelated
AVERAGE filler (book-saturation path #1) but the IS/OS gap could push OS self-corr
over 0.70.

## Post-Submission

PENDING. Human decides whether to submit given the borderline self-corr. If
submitted, flip status to ACTIVE and set the submitted date.
