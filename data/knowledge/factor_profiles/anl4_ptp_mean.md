---
field: anl4_ptp_mean
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.56
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.286
ann_vol: 0.0994
hit_rate: 0.5085
rolling_sharpe_min: -3.53
rolling_sharpe_max: 2.689
redundancy_cluster: 13
negated_best_sharpe: 0.69
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: 0.13
---
# anl4_ptp_mean (analyst4)

*Pretax income - mean of estimations*

## Signal Profile
- `rank(anl4_ptp_mean)`: S=0.39, F=0.25, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_ptp_mean / close)`: S=0.56, F=0.37, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ptp_mean, 5))`: S=-0.04, F=0.00, T=35.9%, INFERIOR (TOP3000)
- `-rank(anl4_ptp_mean)`: S=-0.15, F=-0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptp_mean, 5))`: S=0.69, F=0.26, T=36.4%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ptp_mean, 22)`: S=-0.07, F=-0.01, T=33.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_ptp_mean, 10)`: S=0.13, F=0.05, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ptp_mean, 22))`: S=-0.30, F=-0.08, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_mean)`: S=0.00, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_mean / close)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.55, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.01 (weak), ret=+0.1%
  - 2020: S=-2.78 (negative), ret=-17.6%
  - 2021: S=1.44 (moderate), ret=+17.7%
  - 2022: S=1.94 (strong), ret=+26.6%
  - 2023: S=0.02 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 28.60% over 805 days (recovered)
- Annualized: return +5.5%, volatility 9.9% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.02, excess kurtosis +1.52

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.53, max 2.69, latest -0.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.59%; worst month: -5.76%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.45
- Sideways: S=0.78
- Bear: S=-3.43

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ptp_mean, 5))` S=0.69, F=0.26, INFERIOR
Direction gap: +0.13 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_ptp_mean)`: S=0.00, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_mean / close)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptp_mean, 5))`: S=0.69, F=0.26, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ptp_mean / close)` | TOP3000 | 0.55 | 0.37 | 28.6% | 80% | bull-only |
| `rank(anl4_ptp_mean)` | TOP3000 | 0.38 | 0.25 | 41.8% | 60% | bull-only |
| `rank(anl4_ptp_mean / close)` | TOP1000 | 0.27 | 0.14 | 29.6% | 60% | bull-only |
| `rank(anl4_ptp_mean / close)` | TOP500 | 0.14 | 0.06 | 41.2% | 60% | bull-only |
| `rank(anl4_ptp_mean)` | TOP1000 | 0.14 | 0.06 | 45.2% | 60% | bull-only |
| `rank(anl4_ptp_mean)` | TOP500 | 0.10 | 0.04 | 52.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ptp_median: 1.000 (strongly positively correlated)
- est_ptp: 0.997 (strongly positively correlated)
- anl4_netprofit_mean: 0.996 (strongly positively correlated)
- anl4_netprofit_median: 0.995 (strongly positively correlated)
- anl4_ptp_low: 0.995 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
