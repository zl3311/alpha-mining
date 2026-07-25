---
field: sales_estimate_average_quarterly
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.75
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1023
ann_vol: 0.0732
hit_rate: 0.498
rolling_sharpe_min: -1.238
rolling_sharpe_max: 2.119
redundancy_cluster: 1
negated_best_sharpe: 0.56
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.19
---
# sales_estimate_average_quarterly (analyst4)

*Sales - mean of estimations*

## Signal Profile
- `rank(sales_estimate_average_quarterly)`: S=0.63, F=0.46, T=1.0%, INFERIOR (TOP3000)
- `rank(sales_estimate_average_quarterly / close)`: S=0.75, F=0.49, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(sales_estimate_average_quarterly, 5))`: S=-0.08, F=-0.01, T=35.0%, INFERIOR (TOP3000)
- `-rank(sales_estimate_average_quarterly)`: S=-0.30, F=-0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_average_quarterly, 5))`: S=0.56, F=0.20, T=36.1%, INFERIOR (TOP3000)
- `ts_zscore(sales_estimate_average_quarterly, 22)`: S=0.25, F=0.05, T=34.2%, INFERIOR (TOP3000)
- `ts_mean(sales_estimate_average_quarterly, 10)`: S=0.00, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_estimate_average_quarterly, 22))`: S=-0.16, F=-0.03, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_average_quarterly)`: S=0.06, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_average_quarterly / close)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.16 (negative), ret=-0.8%
  - 2020: S=0.20 (weak), ret=+1.7%
  - 2021: S=0.96 (moderate), ret=+8.6%
  - 2022: S=1.31 (moderate), ret=+9.1%
  - 2023: S=1.63 (strong), ret=+8.1%

## Risk & Drawdown
- Max drawdown: 10.23% over 245 days (recovered)
- Annualized: return +5.5%, volatility 7.3% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.46, excess kurtosis +2.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.24, max 2.12, latest 1.70

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +7.49%; worst month: -4.20%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.85
- Sideways: S=0.17
- Bear: S=-1.15

## Negated Direction
Best negated: `rank(-1 * ts_delta(sales_estimate_average_quarterly, 5))` S=0.56, F=0.20, INFERIOR
Direction gap: -0.19 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sales_estimate_average_quarterly)`: S=0.06, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_average_quarterly / close)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_average_quarterly, 5))`: S=0.56, F=0.20, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_estimate_average_quarterly / close)` | TOP3000 | 0.74 | 0.49 | 10.2% | 80% | bull-only |
| `rank(sales_estimate_average_quarterly)` | TOP3000 | 0.63 | 0.46 | 30.0% | 80% | bull-only |
| `rank(sales_estimate_average_quarterly / close)` | TOP1000 | 0.42 | 0.24 | 14.4% | 60% | bull-only |
| `rank(sales_estimate_average_quarterly / close)` | TOP500 | 0.37 | 0.20 | 18.6% | 80% | bull-only |
| `rank(sales_estimate_average_quarterly)` | TOP1000 | 0.30 | 0.16 | 34.3% | 60% | bull-only |
| `rank(sales_estimate_average_quarterly)` | TOP500 | 0.16 | 0.06 | 42.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- est_sales: 1.000 (strongly positively correlated)
- sales_estimate_median_quarterly: 1.000 (strongly positively correlated)
- sales_estimate_median_value: 1.000 (strongly positively correlated)
- sales_estimate_maximum_quarterly: 0.999 (strongly positively correlated)
- sales_estimate_maximum: 0.999 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
