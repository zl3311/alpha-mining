---
id: "20260617-001-results"
session: "20260617-001"
total_expressions: 12
gate_passers: 0
best_sharpe: 1.19
best_fitness: 0.67
best_alpha_id: "wpRq06ev"
---

# Results: Session 20260617-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 12 |
| Gate-passers (S>=1.25, F>=1.0) | 0 |
| Best Sharpe | 1.19 |
| Best Fitness | 0.67 |
| Budget used | 12 |
| Batch tag | `connector_theme_r1` |

## Gate-Passers

None. No candidate met the aggregate Sharpe/Fitness gates, so no BRAIN checks,
self-correlation checks, metadata labeling, book entries, or submit queue entries
were created.

## All Expressions Tested

| # | Alpha ID | Expression | Sharpe | Fitness | Turnover | Status |
|---|----------|------------|--------|---------|----------|--------|
| 1 | `wpRq06ev` | `ts_decay_linear(rank(implied_volatility_mean_skew_180) * rank(anl4_rd_exp_flag), 5)` | 1.19 | 0.67 | 23.33% | BELOW_GATE |
| 2 | `zq9ZlgXo` | `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_180) * rank(anl4_rd_exp_flag), 5), ts_std_dev(returns, 20) < 0.01)` | 1.01 | 0.55 | 20.01% | BELOW_GATE |
| 3 | `9qwYNrQo` | `ts_decay_linear(rank(implied_volatility_mean_skew_180) + rank(anl4_rd_exp_flag) + rank(fnd6_txs / close), 5)` | 0.84 | 0.52 | 19.79% | BELOW_GATE |
| 4 | `E5w1dNgP` | `ts_decay_linear(rank(anl4_rd_exp_flag) + rank(fnd6_txs / close), 5)` | 0.79 | 0.47 | 2.23% | BELOW_GATE |
| 5 | `A1w9odKY` | `ts_decay_linear(rank(anl4_rd_exp_flag) + rank(fnd6_dn / close), 5)` | 0.81 | 0.46 | 2.11% | BELOW_GATE |
| 6 | `npg9LpXq` | `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(anl4_rd_exp_flag) + rank(fnd6_txs / close), 5), ts_std_dev(returns, 20) < 0.01)` | 0.70 | 0.40 | 2.91% | BELOW_GATE |
| 7 | `QPaMwVRM` | `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(anl4_rd_exp_flag) + rank(fnd6_dn / close), 5), ts_std_dev(returns, 20) < 0.01)` | 0.70 | 0.36 | 2.78% | BELOW_GATE |
| 8 | `QPaM8RlM` | `ts_decay_linear(rank(anl4_rd_exp_flag) * rank(fnd6_txs / close), 5)` | 0.58 | 0.33 | 2.26% | BELOW_GATE |
| 9 | `pw6m9x3X` | `ts_decay_linear(rank(pcr_vol_20) * rank(fnd2_dfdtxasoprlcarryfwd / close), 5)` | 0.74 | 0.28 | 31.55% | BELOW_GATE |
| 10 | `6Xw75NrG` | `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(pcr_vol_20) + rank(fnd2_dfdtxasoprlcarryfwd / close), 5), ts_std_dev(returns, 20) < 0.01)` | 0.67 | 0.28 | 27.17% | BELOW_GATE |
| 11 | `blLXegMZ` | `ts_decay_linear(rank(ts_delta(relative_valuation_rank_derivative, 5)) + rank(implied_volatility_mean_skew_180), 5)` | 0.67 | 0.24 | 30.38% | BELOW_GATE |
| 12 | `Jjpq699e` | `ts_decay_linear(rank(ts_corr(pcr_vol_20, fnd2_dfdtxasoprlcarryfwd, 20)), 5)` | -0.53 | -0.41 | 28.66% | BELOW_GATE |

## Interpretation

The only variant with any meaningful signal was the option-skew x R&D revision
product, but it still missed both submission gates by a wide margin. Volatility
gating reduced its Sharpe and fitness. R&D-tax and R&D-debt additive connectors
were low-turnover but too weak. Option9/deferred-tax wrappers preserved high
turnover without generating enough Sharpe. The model16/options connector remained
consistent with the model16 dead-zone rule.

