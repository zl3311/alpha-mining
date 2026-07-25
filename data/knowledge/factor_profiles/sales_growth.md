---
field: sales_growth
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.76
best_fitness: 0.6
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.1697
ann_vol: 0.1019
hit_rate: 0.5174
rolling_sharpe_min: -1.263
rolling_sharpe_max: 2.783
negated_best_sharpe: 0.49
negated_best_template: neg_rank_level
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.27
---
# sales_growth (fundamental6)

*Growth in Sales (Quarterly)*

## Signal Profile
- `rank(sales_growth)`: S=0.64, F=0.47, T=6.7%, INFERIOR (TOP200)
- `rank(sales_growth / close)`: S=0.76, F=0.60, T=6.2%, INFERIOR (TOP200)
- `rank(ts_delta(sales_growth, 5))`: S=0.30, F=0.07, T=38.0%, INFERIOR (TOP500)
- `ts_decay_linear(rank(sales_growth), 5)`: S=-0.47, F=-0.20, T=4.5%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(sales_growth), ts_std_dev(returns,20)<0.01)`: S=-0.53, F=-0.24, T=5.0%, INFERIOR (TOP3000)
- `-rank(sales_growth)`: S=-0.18, F=-0.06, T=5.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_growth, 5))`: S=0.62, F=0.15, T=36.8%, INFERIOR (TOP3000)
- `ts_zscore(sales_growth, 22)`: S=0.28, F=0.06, T=36.5%, INFERIOR (TOP3000)
- `ts_mean(sales_growth, 10)`: S=0.14, F=0.06, T=6.0%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_growth, 22))`: S=0.11, F=0.02, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * sales_growth)`: S=0.49, F=0.22, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * sales_growth / close)`: S=0.42, F=0.18, T=4.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/35P
- LOW_FITNESS: 37F/0P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/22P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.66 (negative), ret=-3.5%
  - 2020: S=1.12 (moderate), ret=+12.0%
  - 2021: S=1.51 (strong), ret=+17.9%
  - 2022: S=-0.39 (negative), ret=-4.8%
  - 2023: S=2.21 (strong), ret=+17.0%

## Risk & Drawdown
- Max drawdown: 16.97% over 787 days (recovered)
- Annualized: return +7.9%, volatility 10.2% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.30, excess kurtosis +3.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 2.78, latest 2.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +8.83%; worst month: -7.15%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.28
- Sideways: S=0.59
- Bear: S=2.25

## Negated Direction
Best negated: `rank(-1 * sales_growth)` S=0.49, F=0.22, INFERIOR
Direction gap: -0.27 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sales_growth)`: S=0.49, F=0.22, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * sales_growth / close)`: S=0.42, F=0.18, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_growth, 5))`: S=0.62, F=0.15, T=36.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_growth / close)` | TOP200 | 0.77 | 0.60 | 17.0% | 60% | mixed |
| `rank(sales_growth)` | TOP200 | 0.64 | 0.47 | 18.9% | 60% | mixed |
| `rank(sales_growth / close)` | TOP500 | 0.53 | 0.28 | 13.0% | 60% | bear-only |
| `rank(sales_growth)` | TOP500 | 0.40 | 0.19 | 14.3% | 40% | bear-only |
| `rank(sales_growth / close)` | TOP1000 | 0.33 | 0.12 | 12.1% | 60% | bear-only |
| `rank(ts_delta(sales_growth, 5))` | TOP500 | 0.31 | 0.07 | 7.9% | 80% | mixed |
| `rank(sales_growth)` | TOP1000 | 0.20 | 0.06 | 10.8% | 60% | bear-only |
| `rank(ts_delta(sales_growth, 5))` | TOP200 | 0.20 | 0.04 | 17.5% | 60% | mixed |
| `rank(ts_delta(sales_growth, 5))` | TOP1000 | 0.24 | 0.04 | 10.1% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_accum_oth_income_loss_net_of_tax_q: 0.546 (moderately positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.540 (moderately positively correlated)
- anl4_cff_median: 0.536 (moderately positively correlated)
- est_cashflow_fin: 0.533 (moderately positively correlated)
- anl4_cff_low: 0.531 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
