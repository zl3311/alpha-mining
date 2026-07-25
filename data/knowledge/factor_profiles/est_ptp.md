---
field: est_ptp
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.57
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.2624
ann_vol: 0.0941
hit_rate: 0.5036
rolling_sharpe_min: -3.301
rolling_sharpe_max: 2.605
redundancy_cluster: 13
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: 0.01
---
# est_ptp (analyst4)

*Pretax income - mean of estimations*

## Signal Profile
- `rank(est_ptp)`: S=0.38, F=0.23, T=1.1%, INFERIOR (TOP3000)
- `rank(est_ptp / close)`: S=0.57, F=0.37, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(est_ptp, 5))`: S=0.09, F=0.01, T=36.5%, INFERIOR (TOP500)
- `-rank(est_ptp)`: S=-0.12, F=-0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_ptp, 5))`: S=0.58, F=0.20, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(est_ptp, 63)`: S=-0.11, F=-0.02, T=15.1%, INFERIOR (TOP3000)
- `ts_mean(est_ptp, 10)`: S=0.07, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(est_ptp, 22))`: S=-0.44, F=-0.15, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * est_ptp)`: S=-0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * est_ptp / close)`: S=-0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.11 (weak), ret=+0.5%
  - 2020: S=-2.55 (negative), ret=-15.9%
  - 2021: S=1.33 (moderate), ret=+15.7%
  - 2022: S=1.94 (strong), ret=+24.9%
  - 2023: S=0.10 (weak), ret=+0.8%

## Risk & Drawdown
- Max drawdown: 26.24% over 806 days (recovered)
- Annualized: return +5.3%, volatility 9.4% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.03, excess kurtosis +1.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.30, max 2.60, latest -0.11

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.05%; worst month: -5.25%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.41
- Sideways: S=0.88
- Bear: S=-3.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_ptp, 5))` S=0.58, F=0.20, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * est_ptp)`: S=-0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * est_ptp / close)`: S=-0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_ptp, 5))`: S=0.58, F=0.20, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_ptp / close)` | TOP3000 | 0.56 | 0.37 | 26.2% | 80% | bull-only |
| `rank(est_ptp)` | TOP3000 | 0.38 | 0.23 | 40.1% | 60% | bull-only |
| `rank(est_ptp / close)` | TOP1000 | 0.23 | 0.11 | 29.5% | 60% | bull-only |
| `rank(est_ptp / close)` | TOP500 | 0.15 | 0.07 | 39.9% | 60% | bull-only |
| `rank(est_ptp)` | TOP1000 | 0.11 | 0.04 | 44.9% | 60% | bull-only |
| `rank(est_ptp)` | TOP500 | 0.11 | 0.04 | 51.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ptp_mean: 0.997 (strongly positively correlated)
- anl4_ptp_median: 0.997 (strongly positively correlated)
- est_netprofit: 0.995 (strongly positively correlated)
- anl4_netprofit_mean: 0.994 (strongly positively correlated)
- anl4_netprofit_median: 0.994 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
