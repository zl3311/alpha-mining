---
field: anl4_ptp_median
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.58
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 31
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2822
ann_vol: 0.0991
hit_rate: 0.5061
rolling_sharpe_min: -3.491
rolling_sharpe_max: 2.711
redundancy_cluster: 13
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: 0.01
---
# anl4_ptp_median (analyst4)

*Pretax income - median of estimations*

## Signal Profile
- `rank(anl4_ptp_median)`: S=0.40, F=0.25, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_ptp_median / close)`: S=0.58, F=0.39, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ptp_median, 5))`: S=0.25, F=0.05, T=36.8%, INFERIOR (TOP1000)
- `-rank(anl4_ptp_median)`: S=-0.15, F=-0.06, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptp_median, 5))`: S=0.59, F=0.22, T=36.3%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ptp_median, 22)`: S=-0.10, F=-0.01, T=34.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_ptp_median, 10)`: S=0.12, F=0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ptp_median, 22))`: S=-0.03, F=0.00, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_median)`: S=0.00, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_median / close)`: S=0.03, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 31F/0P
- LOW_SHARPE: 31F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.00 (weak), ret=+0.0%
  - 2020: S=-2.74 (negative), ret=-17.4%
  - 2021: S=1.45 (moderate), ret=+17.8%
  - 2022: S=2.00 (strong), ret=+27.3%
  - 2023: S=0.02 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 28.22% over 805 days (recovered)
- Annualized: return +5.7%, volatility 9.9% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.02, excess kurtosis +1.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.49, max 2.71, latest -0.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.56%; worst month: -5.75%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.47
- Sideways: S=0.79
- Bear: S=-3.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ptp_median, 5))` S=0.59, F=0.22, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_ptp_median)`: S=0.00, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_median / close)`: S=0.03, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptp_median, 5))`: S=0.59, F=0.22, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ptp_median / close)` | TOP3000 | 0.58 | 0.39 | 28.2% | 80% | bull-only |
| `rank(anl4_ptp_median)` | TOP3000 | 0.39 | 0.25 | 41.6% | 60% | bull-only |
| `rank(anl4_ptp_median / close)` | TOP1000 | 0.28 | 0.15 | 29.0% | 60% | bull-only |
| `rank(anl4_ptp_median / close)` | TOP500 | 0.14 | 0.06 | 40.7% | 60% | bull-only |
| `rank(anl4_ptp_median)` | TOP1000 | 0.14 | 0.06 | 45.0% | 60% | bull-only |
| `rank(ts_delta(anl4_ptp_median, 5))` | TOP1000 | 0.26 | 0.05 | 8.7% | 40% | weak |
| `rank(anl4_ptp_median)` | TOP500 | 0.10 | 0.04 | 52.2% | 60% | bull-only |
| `rank(ts_delta(anl4_ptp_median, 5))` | TOP3000 | 0.17 | 0.02 | 7.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_ptp_mean: 1.000 (strongly positively correlated)
- est_ptp: 0.997 (strongly positively correlated)
- anl4_netprofit_median: 0.996 (strongly positively correlated)
- anl4_netprofit_mean: 0.995 (strongly positively correlated)
- anl4_ptp_low: 0.994 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
