---
field: fn_proceeds_from_stock_options_exercised_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.56
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1461
ann_vol: 0.0998
hit_rate: 0.498
rolling_sharpe_min: -1.829
rolling_sharpe_max: 1.982
negated_best_sharpe: 0.56
negated_best_template: rank_neg_delta
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: 0.16
---
# fn_proceeds_from_stock_options_exercised_a (fundamental2)

*The cash inflow associated with the amount received from holders exercising their stock options. This item inherently excludes any excess tax benefit, which the entity may have realized and reported separately.*

## Signal Profile
- `rank(fn_proceeds_from_stock_options_exercised_a)`: S=0.09, F=0.03, T=2.2%, INFERIOR (TOP200)
- `rank(fn_proceeds_from_stock_options_exercised_a / close)`: S=0.40, F=0.23, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(fn_proceeds_from_stock_options_exercised_a, 5))`: S=0.22, F=0.08, T=31.5%, INFERIOR (TOP1000)
- `-rank(fn_proceeds_from_stock_options_exercised_a)`: S=0.22, F=0.08, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_stock_options_exercised_a, 5))`: S=0.56, F=0.32, T=28.6%, INFERIOR (TOP3000)
- `ts_zscore(fn_proceeds_from_stock_options_exercised_a, 22)`: S=0.17, F=0.08, T=15.8%, INFERIOR (TOP3000)
- `ts_mean(fn_proceeds_from_stock_options_exercised_a, 10)`: S=-0.15, F=-0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_proceeds_from_stock_options_exercised_a, 22))`: S=0.28, F=0.13, T=16.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_stock_options_exercised_a)`: S=0.30, F=0.13, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_stock_options_exercised_a / close)`: S=-0.02, F=0.00, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.40, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.83 (negative), ret=-4.6%
  - 2020: S=0.23 (weak), ret=+2.4%
  - 2021: S=1.10 (moderate), ret=+15.2%
  - 2022: S=1.05 (moderate), ret=+10.8%
  - 2023: S=-0.56 (negative), ret=-4.0%

## Risk & Drawdown
- Max drawdown: 14.61% over 780 days (recovered)
- Annualized: return +4.0%, volatility 10.0% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.27, excess kurtosis +3.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.83, max 1.98, latest -0.49

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.57%; worst month: -6.43%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.05
- Sideways: S=-0.94
- Bear: S=-0.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_proceeds_from_stock_options_exercised_a, 5))` S=0.56, F=0.32, INFERIOR
Direction gap: +0.16 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_proceeds_from_stock_options_exercised_a)`: S=0.30, F=0.13, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_stock_options_exercised_a / close)`: S=-0.02, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_stock_options_exercised_a, 5))`: S=0.56, F=0.32, T=28.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_proceeds_from_stock_options_exercised_a / close)` | TOP200 | 0.40 | 0.23 | 14.6% | 60% | mixed |
| `rank(ts_delta(fn_proceeds_from_stock_options_exercised_a, 5))` | TOP1000 | 0.22 | 0.08 | 28.1% | 60% | weak |
| `rank(fn_proceeds_from_stock_options_exercised_a)` | TOP200 | 0.10 | 0.03 | 26.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_loxdr: 0.609 (moderately positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: -0.576 (moderately negatively correlated)
- fnd6_ch: 0.573 (moderately positively correlated)
- enterprise_value: 0.571 (moderately positively correlated)
- fnd6_newa1v1300_che: 0.570 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
