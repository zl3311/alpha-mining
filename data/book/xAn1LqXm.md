---
alpha_id: "xAn1LqXm"
name: "vol_gated_leverage_netprofit"
tags:
  - "leverage"
  - "analyst4"
  - "netprofit"
  - "volatility_gate"
  - "session_20260610-001"
  - "excellent"
expression: "trade_when(ts_std_dev(returns, 30) > 0.025, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 30) < 0.012)"
sharpe: 2.00
fitness: 2.12
turnover: 0.039
grade: "EXCELLENT"
family: "leverage_analyst_revision"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.5022
self_corr_result: "PASS"
status: "ACTIVE"
session: "20260610-001"
brain_url: "https://platform.worldquantbrain.com/alpha/xAn1LqXm"
---

# xAn1LqXm

Volatility-gated leverage premium plus net profit revision zscore. EXCELLENT
grade and BRAIN self-correlation PASS.

## Expression

```
trade_when(ts_std_dev(returns, 30) > 0.025, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 30) < 0.012)
```

## Simulation Settings

| Setting | Value |
|---------|-------|
| Region | USA |
| Universe | TOP3000 |
| Delay | 1 |
| Decay | 6 |
| Neutralization | SUBINDUSTRY |
| Truncation | 0.08 |

## Pre-Submission Checks (2026-06-10)

| Check | Result |
|-------|--------|
| Sharpe | 2.00 (PASS, limit 1.25) |
| Fitness | 2.12 (PASS, limit 1.0) |
| Turnover | 3.9% (PASS) |
| All computable BRAIN checks | PASS |
| Self-corr vs book (BRAIN /check) | 0.5022 PASS |

## Mechanism

The expression combines capital-structure risk premium with positive analyst net
profit revisions, but only trades in higher realized volatility regimes. The
30-day volatility gate appears to concentrate the payoff into periods where
leverage risk is priced more aggressively while preserving low turnover and
moderate self-correlation.

## Post-Submission

BRAIN check reported this alpha as ACTIVE on 2026-06-17.

