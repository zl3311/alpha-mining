---
field: sales_estimate_minimum
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.73
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1039
ann_vol: 0.0734
hit_rate: 0.4907
rolling_sharpe_min: -1.126
rolling_sharpe_max: 2.213
redundancy_cluster: 1
negated_best_sharpe: 0.51
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.22
---
# sales_estimate_minimum (analyst4)

*Sales - The lowest estimation*

## Signal Profile
- `rank(sales_estimate_minimum)`: S=0.61, F=0.44, T=1.0%, INFERIOR (TOP3000)
- `rank(sales_estimate_minimum / close)`: S=0.73, F=0.48, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(sales_estimate_minimum, 5))`: S=0.08, F=0.01, T=36.3%, INFERIOR (TOP1000)
- `-rank(sales_estimate_minimum)`: S=-0.27, F=-0.14, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_minimum, 5))`: S=0.51, F=0.17, T=36.7%, INFERIOR (TOP3000)
- `-ts_zscore(sales_estimate_minimum, 63)`: S=0.31, F=0.09, T=16.7%, INFERIOR (TOP3000)
- `ts_mean(sales_estimate_minimum, 10)`: S=-0.02, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_estimate_minimum, 22))`: S=-0.15, F=-0.03, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_minimum)`: S=0.13, F=0.05, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_minimum / close)`: S=0.03, F=0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.73, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.10 (negative), ret=-0.5%
  - 2020: S=0.12 (weak), ret=+1.1%
  - 2021: S=0.86 (moderate), ret=+7.9%
  - 2022: S=1.44 (moderate), ret=+10.0%
  - 2023: S=1.63 (strong), ret=+7.9%

## Risk & Drawdown
- Max drawdown: 10.39% over 245 days (recovered)
- Annualized: return +5.4%, volatility 7.3% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.45, excess kurtosis +2.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.13, max 2.21, latest 1.69

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +7.50%; worst month: -4.13%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.88
- Sideways: S=0.28
- Bear: S=-1.34

## Negated Direction
Best negated: `rank(-1 * ts_delta(sales_estimate_minimum, 5))` S=0.51, F=0.17, INFERIOR
Direction gap: -0.22 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sales_estimate_minimum)`: S=0.13, F=0.05, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_minimum / close)`: S=0.03, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_minimum, 5))`: S=0.51, F=0.17, T=36.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_estimate_minimum / close)` | TOP3000 | 0.73 | 0.48 | 10.4% | 80% | bull-only |
| `rank(sales_estimate_minimum)` | TOP3000 | 0.61 | 0.44 | 30.7% | 80% | bull-only |
| `rank(sales_estimate_minimum / close)` | TOP1000 | 0.39 | 0.21 | 14.8% | 60% | bull-only |
| `rank(sales_estimate_minimum / close)` | TOP500 | 0.31 | 0.16 | 19.9% | 80% | bull-only |
| `rank(sales_estimate_minimum)` | TOP1000 | 0.27 | 0.14 | 36.3% | 60% | bull-only |
| `rank(sales_estimate_minimum)` | TOP500 | 0.12 | 0.05 | 45.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- sales_estimate_minimum_quarterly: 1.000 (strongly positively correlated)
- sales_estimate_average_quarterly: 0.998 (strongly positively correlated)
- est_sales: 0.998 (strongly positively correlated)
- sales_estimate_median_quarterly: 0.997 (strongly positively correlated)
- sales_estimate_median_value: 0.997 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
