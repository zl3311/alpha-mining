---
field: sales_estimate_average_annual
dataset: analyst4
best_template: rank_level
best_sharpe: 0.6
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2786
ann_vol: 0.0985
hit_rate: 0.519
rolling_sharpe_min: -2.967
rolling_sharpe_max: 2.633
redundancy_cluster: 13
negated_best_sharpe: 0.86
negated_best_template: rank_neg_delta
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: 0.26
---
# sales_estimate_average_annual (analyst4)

*Sales - mean of estimations*

## Signal Profile
- `rank(sales_estimate_average_annual)`: S=0.60, F=0.41, T=1.0%, INFERIOR (TOP3000)
- `rank(sales_estimate_average_annual / close)`: S=0.55, F=0.31, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(sales_estimate_average_annual, 5))`: S=0.20, F=0.03, T=34.8%, INFERIOR (TOP3000)
- `-rank(sales_estimate_average_annual)`: S=-0.34, F=-0.19, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_average_annual, 5))`: S=0.86, F=0.36, T=35.8%, INFERIOR (TOP3000)
- `ts_zscore(sales_estimate_average_annual, 22)`: S=0.27, F=0.06, T=34.3%, INFERIOR (TOP3000)
- `ts_mean(sales_estimate_average_annual, 10)`: S=-0.04, F=-0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_estimate_average_annual, 22))`: S=0.19, F=0.04, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_average_annual)`: S=0.12, F=0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_average_annual / close)`: S=0.00, F=0.00, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.60, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.76 (moderate), ret=+3.9%
  - 2020: S=-1.83 (negative), ret=-13.8%
  - 2021: S=0.80 (moderate), ret=+10.8%
  - 2022: S=2.02 (strong), ret=+23.2%
  - 2023: S=0.60 (moderate), ret=+5.0%

## Risk & Drawdown
- Max drawdown: 27.86% over 787 days (recovered)
- Annualized: return +5.9%, volatility 9.8% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew -0.02, excess kurtosis +1.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.97, max 2.63, latest 0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.45%; worst month: -5.70%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.16
- Sideways: S=1.27
- Bear: S=-3.06

## Negated Direction
Best negated: `rank(-1 * ts_delta(sales_estimate_average_annual, 5))` S=0.86, F=0.36, INFERIOR
Direction gap: +0.26 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * sales_estimate_average_annual)`: S=0.12, F=0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_average_annual / close)`: S=0.00, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_average_annual, 5))`: S=0.86, F=0.36, T=35.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_estimate_average_annual)` | TOP3000 | 0.60 | 0.41 | 27.9% | 80% | bull-only |
| `rank(sales_estimate_average_annual / close)` | TOP3000 | 0.55 | 0.31 | 11.4% | 80% | bull-only |
| `rank(sales_estimate_average_annual / close)` | TOP1000 | 0.50 | 0.29 | 14.5% | 100% | bull-only |
| `rank(sales_estimate_average_annual)` | TOP1000 | 0.34 | 0.19 | 32.6% | 60% | bull-only |
| `rank(sales_estimate_average_annual / close)` | TOP500 | 0.36 | 0.18 | 18.9% | 60% | bull-only |
| `rank(sales_estimate_average_annual)` | TOP500 | 0.15 | 0.06 | 40.3% | 60% | bull-only |
| `rank(ts_delta(sales_estimate_average_annual, 5))` | TOP3000 | 0.20 | 0.03 | 8.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- median_sales_estimate: 1.000 (strongly positively correlated)
- highest_sales_estimate: 0.999 (strongly positively correlated)
- lowest_sales_estimate: 0.998 (strongly positively correlated)
- fnd6_cptmfmq_actq: 0.975 (strongly positively correlated)
- fnd6_cptnewqv1300_actq: 0.975 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
