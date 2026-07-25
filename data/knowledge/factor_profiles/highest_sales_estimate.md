---
field: highest_sales_estimate
dataset: analyst4
best_template: rank_level
best_sharpe: 0.63
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2689
ann_vol: 0.0952
hit_rate: 0.5239
rolling_sharpe_min: -2.923
rolling_sharpe_max: 2.689
redundancy_cluster: 13
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.04
---
# highest_sales_estimate (analyst4)

*Sales - The highest estimation for the annual period*

## Signal Profile
- `rank(highest_sales_estimate)`: S=0.63, F=0.44, T=1.0%, INFERIOR (TOP3000)
- `rank(highest_sales_estimate / close)`: S=0.55, F=0.33, T=1.8%, INFERIOR (TOP1000)
- `rank(ts_delta(highest_sales_estimate, 5))`: S=0.19, F=0.03, T=35.0%, INFERIOR (TOP3000)
- `-rank(highest_sales_estimate)`: S=-0.37, F=-0.21, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(highest_sales_estimate, 5))`: S=0.59, F=0.21, T=36.6%, INFERIOR (TOP3000)
- `ts_zscore(highest_sales_estimate, 22)`: S=0.36, F=0.09, T=36.5%, INFERIOR (TOP3000)
- `ts_mean(highest_sales_estimate, 10)`: S=-0.08, F=-0.02, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(highest_sales_estimate, 22))`: S=0.19, F=0.04, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * highest_sales_estimate)`: S=0.08, F=0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * highest_sales_estimate / close)`: S=-0.10, F=-0.03, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.84 (moderate), ret=+4.2%
  - 2020: S=-1.79 (negative), ret=-13.2%
  - 2021: S=0.80 (moderate), ret=+10.6%
  - 2022: S=2.07 (strong), ret=+22.6%
  - 2023: S=0.67 (moderate), ret=+5.3%

## Risk & Drawdown
- Max drawdown: 26.89% over 787 days (recovered)
- Annualized: return +6.0%, volatility 9.5% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew -0.01, excess kurtosis +1.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.92, max 2.69, latest 0.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.15%; worst month: -5.87%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.20
- Sideways: S=1.30
- Bear: S=-3.02

## Negated Direction
Best negated: `rank(-1 * ts_delta(highest_sales_estimate, 5))` S=0.59, F=0.21, INFERIOR
Direction gap: -0.04 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * highest_sales_estimate)`: S=0.08, F=0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * highest_sales_estimate / close)`: S=-0.10, F=-0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(highest_sales_estimate, 5))`: S=0.59, F=0.21, T=36.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(highest_sales_estimate)` | TOP3000 | 0.63 | 0.44 | 26.9% | 80% | bull-only |
| `rank(highest_sales_estimate / close)` | TOP1000 | 0.55 | 0.33 | 13.7% | 100% | bull-only |
| `rank(highest_sales_estimate / close)` | TOP3000 | 0.56 | 0.32 | 11.3% | 100% | mixed |
| `rank(highest_sales_estimate / close)` | TOP500 | 0.43 | 0.24 | 18.0% | 60% | bull-only |
| `rank(highest_sales_estimate)` | TOP1000 | 0.36 | 0.21 | 31.7% | 60% | bull-only |
| `rank(highest_sales_estimate)` | TOP500 | 0.19 | 0.08 | 38.4% | 60% | bull-only |
| `rank(ts_delta(highest_sales_estimate, 5))` | TOP3000 | 0.19 | 0.03 | 8.7% | 60% | bull-only |
| `rank(highest_sales_estimate / close)` | TOP200 | 0.10 | 0.03 | 25.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- median_sales_estimate: 0.999 (strongly positively correlated)
- sales_estimate_average_annual: 0.999 (strongly positively correlated)
- lowest_sales_estimate: 0.995 (strongly positively correlated)
- fnd6_cptnewqv1300_actq: 0.973 (strongly positively correlated)
- assets_curr: 0.973 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
