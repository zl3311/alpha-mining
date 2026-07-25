---
field: sales_estimate_maximum_quarterly
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.77
best_fitness: 0.52
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0998
ann_vol: 0.0727
hit_rate: 0.4964
rolling_sharpe_min: -1.278
rolling_sharpe_max: 2.113
redundancy_cluster: 1
negated_best_sharpe: 0.71
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.06
---
# sales_estimate_maximum_quarterly (analyst4)

*Sales - The highest estimation*

## Signal Profile
- `rank(sales_estimate_maximum_quarterly)`: S=0.66, F=0.49, T=1.0%, INFERIOR (TOP3000)
- `rank(sales_estimate_maximum_quarterly / close)`: S=0.77, F=0.52, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(sales_estimate_maximum_quarterly, 5))`: S=0.47, F=0.11, T=35.9%, INFERIOR (TOP1000)
- `-rank(sales_estimate_maximum_quarterly)`: S=-0.33, F=-0.18, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_maximum_quarterly, 5))`: S=0.71, F=0.29, T=36.5%, INFERIOR (TOP3000)
- `ts_zscore(sales_estimate_maximum_quarterly, 22)`: S=0.62, F=0.21, T=36.3%, INFERIOR (TOP3000)
- `ts_mean(sales_estimate_maximum_quarterly, 10)`: S=0.00, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_estimate_maximum_quarterly, 22))`: S=0.34, F=0.10, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_maximum_quarterly)`: S=0.04, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_maximum_quarterly / close)`: S=-0.09, F=-0.02, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.17 (negative), ret=-0.9%
  - 2020: S=0.27 (weak), ret=+2.4%
  - 2021: S=1.03 (moderate), ret=+9.0%
  - 2022: S=1.26 (moderate), ret=+8.8%
  - 2023: S=1.62 (strong), ret=+8.3%

## Risk & Drawdown
- Max drawdown: 9.98% over 244 days (recovered)
- Annualized: return +5.6%, volatility 7.3% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +0.48, excess kurtosis +2.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.28, max 2.11, latest 1.71

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +7.43%; worst month: -4.18%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.83
- Sideways: S=0.12
- Bear: S=-1.00

## Negated Direction
Best negated: `rank(-1 * ts_delta(sales_estimate_maximum_quarterly, 5))` S=0.71, F=0.29, INFERIOR
Direction gap: -0.06 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sales_estimate_maximum_quarterly)`: S=0.04, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_maximum_quarterly / close)`: S=-0.09, F=-0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_maximum_quarterly, 5))`: S=0.71, F=0.29, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_estimate_maximum_quarterly / close)` | TOP3000 | 0.77 | 0.52 | 10.0% | 80% | bull-only |
| `rank(sales_estimate_maximum_quarterly)` | TOP3000 | 0.65 | 0.49 | 29.4% | 80% | bull-only |
| `rank(sales_estimate_maximum_quarterly / close)` | TOP1000 | 0.46 | 0.26 | 14.1% | 80% | bull-only |
| `rank(sales_estimate_maximum_quarterly / close)` | TOP500 | 0.39 | 0.21 | 18.3% | 80% | bull-only |
| `rank(sales_estimate_maximum_quarterly)` | TOP1000 | 0.32 | 0.18 | 33.2% | 60% | bull-only |
| `rank(ts_delta(sales_estimate_maximum_quarterly, 5))` | TOP1000 | 0.48 | 0.11 | 10.2% | 80% | mixed |
| `rank(sales_estimate_maximum_quarterly)` | TOP500 | 0.19 | 0.09 | 40.0% | 60% | bull-only |
| `rank(ts_delta(sales_estimate_maximum_quarterly, 5))` | TOP3000 | 0.21 | 0.03 | 8.6% | 60% | bull-only |
| `rank(sales_estimate_maximum_quarterly / close)` | TOP200 | 0.09 | 0.02 | 29.1% | 80% | bull-only |

## Correlation Notes
Top correlates:
- sales_estimate_maximum: 1.000 (strongly positively correlated)
- sales_estimate_median_quarterly: 0.999 (strongly positively correlated)
- sales_estimate_median_value: 0.999 (strongly positively correlated)
- sales_estimate_average_quarterly: 0.999 (strongly positively correlated)
- est_sales: 0.999 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
