---
field: sales_estimate_median_quarterly
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.75
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1017
ann_vol: 0.0731
hit_rate: 0.4996
rolling_sharpe_min: -1.227
rolling_sharpe_max: 2.106
redundancy_cluster: 1
negated_best_sharpe: 0.66
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.09
---
# sales_estimate_median_quarterly (analyst4)

*Sales - median of estimations*

## Signal Profile
- `rank(sales_estimate_median_quarterly)`: S=0.64, F=0.47, T=1.0%, INFERIOR (TOP3000)
- `rank(sales_estimate_median_quarterly / close)`: S=0.75, F=0.50, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(sales_estimate_median_quarterly, 5))`: S=0.32, F=0.06, T=35.9%, INFERIOR (TOP1000)
- `-rank(sales_estimate_median_quarterly)`: S=-0.31, F=-0.17, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_median_quarterly, 5))`: S=0.66, F=0.25, T=36.5%, INFERIOR (TOP3000)
- `ts_zscore(sales_estimate_median_quarterly, 22)`: S=0.49, F=0.15, T=35.0%, INFERIOR (TOP3000)
- `ts_mean(sales_estimate_median_quarterly, 10)`: S=0.00, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_estimate_median_quarterly, 22))`: S=0.14, F=0.03, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_median_quarterly)`: S=0.05, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_median_quarterly / close)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.75, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.15 (negative), ret=-0.8%
  - 2020: S=0.20 (weak), ret=+1.7%
  - 2021: S=0.97 (moderate), ret=+8.7%
  - 2022: S=1.30 (moderate), ret=+9.1%
  - 2023: S=1.62 (strong), ret=+8.1%

## Risk & Drawdown
- Max drawdown: 10.17% over 245 days (recovered)
- Annualized: return +5.5%, volatility 7.3% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.46, excess kurtosis +2.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.23, max 2.11, latest 1.70

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +7.48%; worst month: -4.17%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.85
- Sideways: S=0.16
- Bear: S=-1.13

## Negated Direction
Best negated: `rank(-1 * ts_delta(sales_estimate_median_quarterly, 5))` S=0.66, F=0.25, INFERIOR
Direction gap: -0.09 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sales_estimate_median_quarterly)`: S=0.05, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_median_quarterly / close)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_median_quarterly, 5))`: S=0.66, F=0.25, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_estimate_median_quarterly / close)` | TOP3000 | 0.75 | 0.50 | 10.2% | 80% | bull-only |
| `rank(sales_estimate_median_quarterly)` | TOP3000 | 0.64 | 0.47 | 30.0% | 80% | bull-only |
| `rank(sales_estimate_median_quarterly / close)` | TOP1000 | 0.43 | 0.24 | 14.4% | 80% | bull-only |
| `rank(sales_estimate_median_quarterly / close)` | TOP500 | 0.37 | 0.20 | 18.6% | 80% | bull-only |
| `rank(sales_estimate_median_quarterly)` | TOP1000 | 0.30 | 0.17 | 34.3% | 60% | bull-only |
| `rank(sales_estimate_median_quarterly)` | TOP500 | 0.17 | 0.07 | 41.8% | 60% | bull-only |
| `rank(ts_delta(sales_estimate_median_quarterly, 5))` | TOP1000 | 0.32 | 0.06 | 11.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- sales_estimate_median_value: 1.000 (strongly positively correlated)
- sales_estimate_average_quarterly: 1.000 (strongly positively correlated)
- est_sales: 1.000 (strongly positively correlated)
- sales_estimate_maximum_quarterly: 0.999 (strongly positively correlated)
- sales_estimate_maximum: 0.999 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
