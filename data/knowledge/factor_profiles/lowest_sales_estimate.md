---
field: lowest_sales_estimate
dataset: analyst4
best_template: rank_level
best_sharpe: 0.58
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2848
ann_vol: 0.1012
hit_rate: 0.5158
rolling_sharpe_min: -2.994
rolling_sharpe_max: 2.591
redundancy_cluster: 13
negated_best_sharpe: 0.33
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.25
---
# lowest_sales_estimate (analyst4)

*Sales - The lowest estimation for the annual period*

## Signal Profile
- `rank(lowest_sales_estimate)`: S=0.58, F=0.40, T=1.0%, INFERIOR (TOP3000)
- `rank(lowest_sales_estimate / close)`: S=0.56, F=0.32, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(lowest_sales_estimate, 5))`: S=0.38, F=0.08, T=35.5%, INFERIOR (TOP3000)
- `-rank(lowest_sales_estimate)`: S=-0.32, F=-0.18, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(lowest_sales_estimate, 5))`: S=0.33, F=0.07, T=36.7%, INFERIOR (TOP3000)
- `ts_zscore(lowest_sales_estimate, 22)`: S=0.35, F=0.09, T=35.9%, INFERIOR (TOP3000)
- `ts_mean(lowest_sales_estimate, 10)`: S=-0.02, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(lowest_sales_estimate, 22))`: S=0.16, F=0.03, T=14.1%, INFERIOR (TOP3000)
- `rank(-1 * lowest_sales_estimate)`: S=-0.13, F=-0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * lowest_sales_estimate / close)`: S=-0.28, F=-0.13, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.70 (moderate), ret=+3.6%
  - 2020: S=-1.84 (negative), ret=-14.0%
  - 2021: S=0.78 (moderate), ret=+10.7%
  - 2022: S=1.97 (strong), ret=+23.6%
  - 2023: S=0.56 (moderate), ret=+4.8%

## Risk & Drawdown
- Max drawdown: 28.48% over 788 days (recovered)
- Annualized: return +5.9%, volatility 10.1% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew -0.02, excess kurtosis +1.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.99, max 2.59, latest 0.35

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.76%; worst month: -5.50%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.11
- Sideways: S=1.26
- Bear: S=-3.09

## Negated Direction
Best negated: `rank(-1 * ts_delta(lowest_sales_estimate, 5))` S=0.33, F=0.07, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * lowest_sales_estimate)`: S=-0.13, F=-0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * lowest_sales_estimate / close)`: S=-0.28, F=-0.13, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(lowest_sales_estimate, 5))`: S=0.33, F=0.07, T=36.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(lowest_sales_estimate)` | TOP3000 | 0.58 | 0.40 | 28.5% | 80% | bull-only |
| `rank(lowest_sales_estimate / close)` | TOP3000 | 0.56 | 0.32 | 11.4% | 80% | bull-only |
| `rank(lowest_sales_estimate / close)` | TOP1000 | 0.47 | 0.27 | 15.1% | 80% | bull-only |
| `rank(lowest_sales_estimate)` | TOP1000 | 0.32 | 0.18 | 33.1% | 60% | bull-only |
| `rank(lowest_sales_estimate / close)` | TOP500 | 0.28 | 0.13 | 19.8% | 60% | bull-only |
| `rank(ts_delta(lowest_sales_estimate, 5))` | TOP3000 | 0.38 | 0.08 | 10.2% | 60% | bull-only |
| `rank(ts_delta(lowest_sales_estimate, 5))` | TOP1000 | 0.34 | 0.07 | 6.5% | 60% | bull-only |
| `rank(lowest_sales_estimate)` | TOP500 | 0.12 | 0.05 | 41.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- sales_estimate_average_annual: 0.998 (strongly positively correlated)
- median_sales_estimate: 0.998 (strongly positively correlated)
- highest_sales_estimate: 0.995 (strongly positively correlated)
- fnd6_cptmfmq_actq: 0.975 (strongly positively correlated)
- fnd6_cptnewqv1300_actq: 0.975 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
