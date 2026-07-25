---
alpha_id: "JjpzQAze"
name: "ivaco_intraday_bvps_product"
tags:
  - "product_interaction"
  - "fnd6_ivaco"
  - "novel_structure"
  - "session_20260629-001"
submitted: "2026-06-30"
session: "20260629-001"
grade: "EXCELLENT"
sharpe: 2.30
fitness: 2.05
turnover: 0.117
expression: "ts_decay_linear(rank(fnd6_ivaco / close) * rank(open / close - 1) * rank(anl4_bvps_flag), 5)"
family: "investment_intraday_analyst_product"
neutralization: "SUBINDUSTRY"
decay: 6
self_corr_max: 0.6813
self_corr_method: "brain_check_authoritative"
self_corr_verdict: "PASS"
status: "ACTIVE"
brain_url: "https://platform.worldquantbrain.com/alpha/JjpzQAze"
---

# Alpha: JjpzQAze

## Expression
```
ts_decay_linear(rank(fnd6_ivaco / close) * rank(open / close - 1) * rank(anl4_bvps_flag), 5)
```

## Mechanism

Three-way multiplicative interaction that requires simultaneous agreement across
three orthogonal dimensions:

1. **fnd6_ivaco / close** (investment value): Companies with high investment in
   associated companies relative to price are undervalued conglomerates
   deploying capital into growth via subsidiaries.
2. **open / close - 1** (intraday momentum): Positive intraday return confirms
   near-term demand and price momentum.
3. **anl4_bvps_flag** (book value revision): Analyst upward revision of book
   value per share signals improving fundamentals recognized by the sell side.

The product structure only generates signal when ALL three factors agree,
creating a more selective position set than additive blends. This reduces noise
from stocks that score high on one dimension but not others.

## Self-Correlation Profile

| Peer | Correlation | Peer Sharpe |
|------|-------------|-------------|
| LLR0n261 (accrual_intraday_analyst_revision) | 0.6813 | 2.51 |
| 1YJagrVk (conglomerate_revision) | 0.6296 | 2.37 |
| vR56vdYd (analyst_revision) | 0.6153 | 2.86 |
| ZYpk2kx8 (iv60_fundamental_blend) | 0.6103 | 1.71 |
| 6Xzm6PQP (guidance_fundamental) | 0.5842 | 2.31 |

Max self-corr 0.6813 < 0.7 threshold → auto-PASS (no Sharpe premium needed).

## Post-Submission
After the human submits on BRAIN, flip status to ACTIVE and set the submitted date.
