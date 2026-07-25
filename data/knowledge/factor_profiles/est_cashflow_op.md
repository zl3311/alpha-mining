---
field: est_cashflow_op
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.76
best_fitness: 0.55
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1812
ann_vol: 0.086
hit_rate: 0.5061
rolling_sharpe_min: -1.98
rolling_sharpe_max: 2.83
redundancy_cluster: 1
negated_best_sharpe: 0.17
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.59
---
# est_cashflow_op (analyst4)

*Cash Flow From Operations - mean of estimations*

## Signal Profile
- `rank(est_cashflow_op)`: S=0.44, F=0.28, T=1.1%, INFERIOR (TOP3000)
- `rank(est_cashflow_op / close)`: S=0.76, F=0.55, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(est_cashflow_op, 5))`: S=0.37, F=0.12, T=35.1%, INFERIOR (TOP200)
- `-rank(est_cashflow_op)`: S=-0.21, F=-0.10, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_cashflow_op, 5))`: S=0.17, F=0.02, T=36.6%, INFERIOR (TOP3000)
- `-ts_zscore(est_cashflow_op, 63)`: S=-0.31, F=-0.09, T=16.1%, INFERIOR (TOP3000)
- `ts_mean(est_cashflow_op, 10)`: S=0.25, F=0.12, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(est_cashflow_op, 22))`: S=-0.37, F=-0.12, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * est_cashflow_op)`: S=-0.44, F=-0.28, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * est_cashflow_op / close)`: S=-0.76, F=-0.55, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.76, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.42 (negative), ret=-1.9%
  - 2020: S=-1.48 (negative), ret=-10.1%
  - 2021: S=1.66 (strong), ret=+18.7%
  - 2022: S=1.99 (strong), ret=+22.7%
  - 2023: S=0.43 (weak), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 18.12% over 835 days (recovered)
- Annualized: return +6.5%, volatility 8.6% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.19, excess kurtosis +1.98

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.98, max 2.83, latest 0.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.04%; worst month: -3.35%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.75
- Sideways: S=0.24
- Bear: S=-2.70

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_cashflow_op, 5))` S=0.17, F=0.02, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * est_cashflow_op)`: S=-0.44, F=-0.28, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * est_cashflow_op / close)`: S=-0.76, F=-0.55, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_cashflow_op, 5))`: S=0.17, F=0.02, T=36.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_cashflow_op / close)` | TOP3000 | 0.76 | 0.55 | 18.1% | 60% | bull-only |
| `rank(est_cashflow_op)` | TOP3000 | 0.43 | 0.28 | 33.9% | 60% | bull-only |
| `rank(est_cashflow_op / close)` | TOP1000 | 0.33 | 0.18 | 19.3% | 40% | bull-only |
| `rank(ts_delta(est_cashflow_op, 5))` | TOP200 | 0.37 | 0.12 | 20.0% | 60% | all-weather |
| `rank(est_cashflow_op)` | TOP1000 | 0.20 | 0.10 | 38.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_cfo_mean: 0.984 (strongly positively correlated)
- anl4_cfo_median: 0.983 (strongly positively correlated)
- anl4_cfo_high: 0.979 (strongly positively correlated)
- anl4_cfo_low: 0.975 (strongly positively correlated)
- anl4_ebit_high: 0.963 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
