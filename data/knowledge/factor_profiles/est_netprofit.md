---
field: est_netprofit
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.56
best_fitness: 0.36
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.2367
ann_vol: 0.0913
hit_rate: 0.5061
rolling_sharpe_min: -3.014
rolling_sharpe_max: 2.653
redundancy_cluster: 13
negated_best_sharpe: 0.44
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.12
---
# est_netprofit (analyst4)

*Net profit - mean of estimations*

## Signal Profile
- `rank(est_netprofit)`: S=0.38, F=0.23, T=1.1%, INFERIOR (TOP3000)
- `rank(est_netprofit / close)`: S=0.56, F=0.36, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(est_netprofit, 5))`: S=0.05, F=0.00, T=36.2%, INFERIOR (TOP1000)
- `-rank(est_netprofit)`: S=-0.13, F=-0.05, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_netprofit, 5))`: S=0.44, F=0.14, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(est_netprofit, 63)`: S=-0.02, F=0.00, T=15.0%, INFERIOR (TOP3000)
- `ts_mean(est_netprofit, 10)`: S=0.09, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(est_netprofit, 22))`: S=-0.43, F=-0.14, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * est_netprofit)`: S=0.03, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * est_netprofit / close)`: S=0.04, F=0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.55, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.15 (weak), ret=+0.7%
  - 2020: S=-2.25 (negative), ret=-13.6%
  - 2021: S=1.33 (moderate), ret=+15.1%
  - 2022: S=1.84 (strong), ret=+23.0%
  - 2023: S=-0.06 (negative), ret=-0.5%

## Risk & Drawdown
- Max drawdown: 23.67% over 805 days (recovered)
- Annualized: return +5.0%, volatility 9.1% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.02, excess kurtosis +1.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.01, max 2.65, latest -0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.71%; worst month: -4.98%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.36
- Sideways: S=0.88
- Bear: S=-3.36

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_netprofit, 5))` S=0.44, F=0.14, INFERIOR
Direction gap: -0.12 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * est_netprofit)`: S=0.03, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * est_netprofit / close)`: S=0.04, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_netprofit, 5))`: S=0.44, F=0.14, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_netprofit / close)` | TOP3000 | 0.55 | 0.36 | 23.7% | 60% | bull-only |
| `rank(est_netprofit)` | TOP3000 | 0.37 | 0.23 | 37.9% | 60% | bull-only |
| `rank(est_netprofit / close)` | TOP1000 | 0.22 | 0.10 | 28.3% | 60% | bull-only |
| `rank(est_netprofit / close)` | TOP500 | 0.16 | 0.07 | 39.1% | 60% | bull-only |
| `rank(est_netprofit)` | TOP1000 | 0.12 | 0.05 | 43.4% | 60% | bull-only |
| `rank(est_netprofit)` | TOP500 | 0.11 | 0.04 | 50.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_netprofit_mean: 0.998 (strongly positively correlated)
- anl4_netprofit_median: 0.997 (strongly positively correlated)
- est_ptp: 0.995 (strongly positively correlated)
- anl4_ptp_mean: 0.993 (strongly positively correlated)
- anl4_ptp_median: 0.993 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
