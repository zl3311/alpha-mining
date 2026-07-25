---
field: median_sales_estimate
dataset: analyst4
best_template: rank_level
best_sharpe: 0.61
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2762
ann_vol: 0.098
hit_rate: 0.519
rolling_sharpe_min: -2.951
rolling_sharpe_max: 2.643
redundancy_cluster: 13
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.03
---
# median_sales_estimate (analyst4)

*Sales - median of estimations*

## Signal Profile
- `rank(median_sales_estimate)`: S=0.61, F=0.42, T=1.0%, INFERIOR (TOP3000)
- `rank(median_sales_estimate / close)`: S=0.56, F=0.32, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(median_sales_estimate, 5))`: S=0.26, F=0.05, T=35.9%, INFERIOR (TOP1000)
- `-rank(median_sales_estimate)`: S=-0.35, F=-0.20, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(median_sales_estimate, 5))`: S=0.58, F=0.20, T=36.8%, INFERIOR (TOP3000)
- `ts_zscore(median_sales_estimate, 22)`: S=0.28, F=0.06, T=35.4%, INFERIOR (TOP3000)
- `ts_mean(median_sales_estimate, 10)`: S=-0.06, F=-0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(median_sales_estimate, 22))`: S=0.28, F=0.08, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * median_sales_estimate)`: S=0.10, F=0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * median_sales_estimate / close)`: S=-0.03, F=-0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.61, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.79 (moderate), ret=+4.1%
  - 2020: S=-1.81 (negative), ret=-13.6%
  - 2021: S=0.80 (moderate), ret=+10.9%
  - 2022: S=2.03 (strong), ret=+23.1%
  - 2023: S=0.61 (moderate), ret=+5.0%

## Risk & Drawdown
- Max drawdown: 27.62% over 787 days (recovered)
- Annualized: return +6.0%, volatility 9.8% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew -0.01, excess kurtosis +1.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.95, max 2.64, latest 0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.41%; worst month: -5.75%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.18
- Sideways: S=1.27
- Bear: S=-3.05

## Negated Direction
Best negated: `rank(-1 * ts_delta(median_sales_estimate, 5))` S=0.58, F=0.20, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * median_sales_estimate)`: S=0.10, F=0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * median_sales_estimate / close)`: S=-0.03, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(median_sales_estimate, 5))`: S=0.58, F=0.20, T=36.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(median_sales_estimate)` | TOP3000 | 0.61 | 0.42 | 27.6% | 80% | bull-only |
| `rank(median_sales_estimate / close)` | TOP3000 | 0.56 | 0.32 | 11.4% | 80% | mixed |
| `rank(median_sales_estimate / close)` | TOP1000 | 0.52 | 0.31 | 14.2% | 100% | bull-only |
| `rank(median_sales_estimate)` | TOP1000 | 0.34 | 0.20 | 32.5% | 60% | bull-only |
| `rank(median_sales_estimate / close)` | TOP500 | 0.37 | 0.20 | 18.8% | 60% | bull-only |
| `rank(median_sales_estimate)` | TOP500 | 0.16 | 0.06 | 40.0% | 60% | bull-only |
| `rank(ts_delta(median_sales_estimate, 5))` | TOP1000 | 0.26 | 0.05 | 7.7% | 80% | bull-only |
| `rank(ts_delta(median_sales_estimate, 5))` | TOP3000 | 0.25 | 0.04 | 9.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- sales_estimate_average_annual: 1.000 (strongly positively correlated)
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
