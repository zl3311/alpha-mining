---
field: anl4_cfo_median
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.78
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1883
ann_vol: 0.0942
hit_rate: 0.5053
rolling_sharpe_min: -1.949
rolling_sharpe_max: 2.866
redundancy_cluster: 1
negated_best_sharpe: 0.23
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.55
---
# anl4_cfo_median (analyst4)

*Cash Flow From Operations - median of estimations*

## Signal Profile
- `rank(anl4_cfo_median)`: S=0.46, F=0.31, T=1.5%, INFERIOR (TOP3000)
- `rank(anl4_cfo_median / close)`: S=0.78, F=0.60, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_cfo_median, 5))`: S=0.11, F=0.02, T=35.0%, INFERIOR (TOP200)
- `-rank(anl4_cfo_median)`: S=-0.21, F=-0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfo_median, 5))`: S=0.23, F=0.04, T=37.1%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_cfo_median, 63)`: S=-0.11, F=-0.02, T=16.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_cfo_median, 10)`: S=0.14, F=0.05, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cfo_median, 22))`: S=-0.30, F=-0.09, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_median)`: S=-0.21, F=-0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_median / close)`: S=-0.29, F=-0.14, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.23 (negative), ret=-1.1%
  - 2020: S=-1.60 (negative), ret=-12.0%
  - 2021: S=1.78 (strong), ret=+21.6%
  - 2022: S=1.86 (strong), ret=+23.2%
  - 2023: S=0.60 (moderate), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 18.83% over 837 days (recovered)
- Annualized: return +7.3%, volatility 9.4% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.23, excess kurtosis +1.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.95, max 2.87, latest 0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.86%; worst month: -3.76%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.74
- Sideways: S=0.22
- Bear: S=-2.69

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cfo_median, 5))` S=0.23, F=0.04, INFERIOR
Direction gap: -0.55 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_cfo_median)`: S=-0.21, F=-0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_median / close)`: S=-0.29, F=-0.14, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfo_median, 5))`: S=0.23, F=0.04, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cfo_median / close)` | TOP3000 | 0.77 | 0.60 | 18.8% | 60% | bull-only |
| `rank(anl4_cfo_median)` | TOP3000 | 0.45 | 0.31 | 35.9% | 60% | bull-only |
| `rank(anl4_cfo_median / close)` | TOP1000 | 0.28 | 0.14 | 22.8% | 40% | bull-only |
| `rank(anl4_cfo_median)` | TOP1000 | 0.20 | 0.10 | 37.5% | 60% | bull-only |
| `rank(anl4_cfo_median)` | TOP500 | 0.10 | 0.04 | 47.1% | 60% | bull-only |
| `rank(ts_delta(anl4_cfo_median, 5))` | TOP200 | 0.11 | 0.02 | 25.1% | 60% | mixed |
| `rank(anl4_cfo_median / close)` | TOP500 | 0.08 | 0.02 | 37.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_cfo_mean: 1.000 (strongly positively correlated)
- anl4_cfo_high: 0.995 (strongly positively correlated)
- anl4_cfo_low: 0.992 (strongly positively correlated)
- est_cashflow_op: 0.983 (strongly positively correlated)
- anl4_ebit_mean: 0.952 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
