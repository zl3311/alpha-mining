---
alpha_id: "3q7edgEQ"
name: "iv60_guidance_coverage_epsr_cshtr_cfi"
grade: "SPECTACULAR"
sharpe: 2.53
fitness: 3.29
turnover: 0.058
returns: null
status: "PENDING"
family: "iv60_guidance_analyst_revenue_blend"
tags:
  - "options"
  - "analyst4"
  - "fundamental6"
  - "guidance"
  - "implied_volatility_call_60"
  - "anl4_epsr_flag"
  - "anl4_cfi_flag"
  - "fnd6_cshtr"
  - "session_20260624-001"
  - "spectacular"
session: "20260624-001"
expression: "ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 44)) + rank(max_adjusted_net_income_guidance) + rank(sales_estimate_count_quarterly) + rank(anl4_epsr_flag) + rank(fnd6_cshtr) + rank(anl4_cfi_flag), 5)"
settings:
  decay: 6
  neutralization: "SUBINDUSTRY"
  universe: "TOP3000"
  region: "USA"
brain_checks:
  LOW_SHARPE: "PASS (2.53 vs 1.25)"
  LOW_FITNESS: "PASS (3.29 vs 1.00)"
  LOW_TURNOVER: "PASS (0.058 vs 0.01)"
  HIGH_TURNOVER: "PASS (0.058 vs 0.70)"
  CONCENTRATED_WEIGHT: "PASS"
  LOW_SUB_UNIVERSE_SHARPE: "PASS"
  SELF_CORRELATION: "PASS (BRAIN corr 0.6013 < 0.70)"
  MATCHES_COMPETITION: "PASS"
self_correlation:
  max_corr: 0.6013
  top_peer: "kq33Gjqk (Depreciation×IV60×Capital)"
  vs_88z7MM37: 0.5135
  margin: 0.099
  verdict: "PASS (auto below 0.70 threshold)"
discovered: "20260624"
session: "20260624-001"
url: "https://platform.worldquantbrain.com/alpha/3q7edgEQ"
---

# Alpha 3q7edgEQ — IV60 × Guidance × Analyst Coverage × Revenue Quality

## Expression

```
ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 44)) + rank(max_adjusted_net_income_guidance) + rank(sales_estimate_count_quarterly) + rank(anl4_epsr_flag) + rank(fnd6_cshtr) + rank(anl4_cfi_flag), 5)
```

## Mechanism

6-factor additive blend combining signals from 4 orthogonal economic families:

1. **zscore(ts_mean(IV60_call - IV60_put, 44))** — 44-day smoothed cross-sectional
   z-score of 60-day implied volatility call-put skew. Captures options market
   directional sentiment: positive skew indicates bullish options flow from informed
   traders.

2. **rank(max_adjusted_net_income_guidance)** — Maximum adjusted net income guidance
   issued by management. Companies with higher earnings guidance demonstrate management
   confidence in forward earnings trajectory. Sparse coverage creates concentrated
   signal among guidance-issuing firms.

3. **rank(sales_estimate_count_quarterly)** — Number of analyst estimates for quarterly
   sales. High coverage indicates institutional interest and analyst attention, which
   correlates with information efficiency and reduces downside surprise risk.

4. **rank(anl4_epsr_flag)** — EPS revision flag indicating upward consensus estimate
   revisions. Captures earnings momentum — stocks with rising analyst estimates tend
   to outperform as the market slowly incorporates new information (post-earnings-
   announcement drift).

5. **rank(fnd6_cshtr)** — Cash-to-total-revenue ratio. High cash conversion indicates
   superior revenue quality — firms that convert revenue to cash efficiently have
   better earnings sustainability and lower accounting manipulation risk.

6. **rank(anl4_cfi_flag)** — Cash flow from investment revision flag. Captures changes
   in analyst expectations about capital allocation efficiency. Rising CFI estimates
   signal improving investment returns.

## Why It Works

The combination exploits four distinct market inefficiencies simultaneously:
- **Options sentiment** (fast-moving, daily) captures informed flow before price impact
- **Management guidance** (event-driven, sparse) captures insider confidence asymmetry
- **Analyst attention** (slow-moving) proxies for institutional demand pressure
- **Fundamental quality** (quarterly) captures earnings sustainability mispricing

The structural diversity (options + guidance + coverage + revision + fundamentals)
creates natural decorrelation from the balance-sheet-focused book entries (88z7MM37
uses itci/drlt/acdo; xAxxVG7N uses dpactq/dlto/tlcf). None of these legs overlap
with existing book entries' non-IV60 components.

## BRAIN Checks

| Check | Result | Value | Limit |
|-------|--------|-------|-------|
| LOW_SHARPE | PASS | 2.53 | 1.25 |
| LOW_FITNESS | PASS | 3.29 | 1.0 |
| LOW_TURNOVER | PASS | 5.8% | 1% |
| HIGH_TURNOVER | PASS | 5.8% | 70% |
| CONCENTRATED_WEIGHT | PASS | — | — |
| LOW_SUB_UNIVERSE_SHARPE | PASS | — | — |
| SELF_CORRELATION | PASS | 0.6013 | 0.70 |
| MATCHES_COMPETITION | PASS | — | — |

## Self-Correlation Breakdown (BRAIN /correlations/self)

| Book Entry | Correlation | Status |
|------------|-------------|--------|
| kq33Gjqk (Depreciation×IV60×Capital) | 0.6013 | Below threshold |
| Gro21wWG (iv90_vol_gated_spread) | 0.5839 | Safe |
| omY3pZq2 (buzz×iv_skew) | 0.5570 | Safe |
| vRm07LP3 (iv_spread_zscore) | 0.5274 | Safe |
| 88z7MM37 (itci_iv60_drlt_acdo) | 0.5135 | Safe |

## Platform URL

https://platform.worldquantbrain.com/alpha/3q7edgEQ
