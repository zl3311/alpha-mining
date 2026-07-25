---
field: anl4_netprofit_median
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.59
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2514
ann_vol: 0.0945
hit_rate: 0.5053
rolling_sharpe_min: -3.197
rolling_sharpe_max: 2.668
redundancy_cluster: 13
negated_best_sharpe: 0.72
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.13
---
# anl4_netprofit_median (analyst4)

*Net profit - Median of estimations*

## Signal Profile
- `rank(anl4_netprofit_median)`: S=0.39, F=0.24, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_netprofit_median / close)`: S=0.59, F=0.39, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netprofit_median, 5))`: S=0.20, F=0.03, T=36.8%, INFERIOR (TOP1000)
- `-rank(anl4_netprofit_median)`: S=-0.15, F=-0.06, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofit_median, 5))`: S=0.72, F=0.30, T=36.4%, INFERIOR (TOP3000)
- `ts_zscore(anl4_netprofit_median, 22)`: S=-0.18, F=-0.03, T=34.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_netprofit_median, 10)`: S=0.09, F=0.03, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netprofit_median, 22))`: S=-0.14, F=-0.03, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_median)`: S=0.04, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_median / close)`: S=0.07, F=0.02, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.12 (weak), ret=+0.5%
  - 2020: S=-2.41 (negative), ret=-14.6%
  - 2021: S=1.42 (moderate), ret=+16.5%
  - 2022: S=1.87 (strong), ret=+24.4%
  - 2023: S=0.02 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 25.14% over 805 days (recovered)
- Annualized: return +5.5%, volatility 9.4% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.02, excess kurtosis +1.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.20, max 2.67, latest -0.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.92%; worst month: -5.09%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.37
- Sideways: S=0.88
- Bear: S=-3.31

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netprofit_median, 5))` S=0.72, F=0.30, INFERIOR
Direction gap: +0.13 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_netprofit_median)`: S=0.04, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_median / close)`: S=0.07, F=0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofit_median, 5))`: S=0.72, F=0.30, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netprofit_median / close)` | TOP3000 | 0.58 | 0.39 | 25.1% | 80% | bull-only |
| `rank(anl4_netprofit_median)` | TOP3000 | 0.38 | 0.24 | 38.6% | 60% | bull-only |
| `rank(anl4_netprofit_median / close)` | TOP1000 | 0.25 | 0.12 | 28.9% | 60% | bull-only |
| `rank(anl4_netprofit_median / close)` | TOP500 | 0.15 | 0.06 | 39.7% | 60% | bull-only |
| `rank(anl4_netprofit_median)` | TOP1000 | 0.14 | 0.06 | 43.9% | 60% | bull-only |
| `rank(anl4_netprofit_median)` | TOP500 | 0.11 | 0.04 | 50.5% | 60% | bull-only |
| `rank(ts_delta(anl4_netprofit_median, 5))` | TOP1000 | 0.21 | 0.03 | 7.6% | 40% | mixed |

## Correlation Notes
Top correlates:
- anl4_netprofit_mean: 1.000 (strongly positively correlated)
- est_netprofit: 0.997 (strongly positively correlated)
- anl4_ptp_median: 0.996 (strongly positively correlated)
- anl4_ptp_mean: 0.995 (strongly positively correlated)
- anl4_netprofit_low: 0.994 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
