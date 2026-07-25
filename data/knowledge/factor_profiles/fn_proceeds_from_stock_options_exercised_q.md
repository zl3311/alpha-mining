---
field: fn_proceeds_from_stock_options_exercised_q
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.65
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.2097
ann_vol: 0.1254
hit_rate: 0.5036
rolling_sharpe_min: -1.287
rolling_sharpe_max: 1.71
negated_best_sharpe: 0.65
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: 0.31
---
# fn_proceeds_from_stock_options_exercised_q (fundamental2)

*The cash inflow associated with the amount received from holders exercising their stock options. This item inherently excludes any excess tax benefit, which the entity may have realized and reported separately.*

## Signal Profile
- `rank(fn_proceeds_from_stock_options_exercised_q)`: S=0.12, F=0.04, T=3.3%, INFERIOR (TOP200)
- `rank(fn_proceeds_from_stock_options_exercised_q / close)`: S=0.34, F=0.20, T=3.5%, INFERIOR (TOP200)
- `rank(ts_delta(fn_proceeds_from_stock_options_exercised_q, 5))`: S=-0.05, F=-0.01, T=36.5%, INFERIOR (TOP500)
- `-rank(fn_proceeds_from_stock_options_exercised_q)`: S=0.26, F=0.09, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_stock_options_exercised_q, 5))`: S=0.65, F=0.29, T=35.6%, INFERIOR (TOP3000)
- `-ts_zscore(fn_proceeds_from_stock_options_exercised_q, 63)`: S=-0.37, F=-0.16, T=17.5%, INFERIOR (TOP3000)
- `ts_mean(fn_proceeds_from_stock_options_exercised_q, 10)`: S=0.07, F=0.02, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_proceeds_from_stock_options_exercised_q, 22))`: S=0.02, F=0.00, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_stock_options_exercised_q)`: S=0.23, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_stock_options_exercised_q / close)`: S=0.32, F=0.12, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.37, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.27 (moderate), ret=+9.5%
  - 2020: S=0.74 (moderate), ret=+9.7%
  - 2021: S=0.74 (moderate), ret=+11.1%
  - 2022: S=-0.47 (negative), ret=-6.4%
  - 2023: S=-0.12 (negative), ret=-1.3%

## Risk & Drawdown
- Max drawdown: 20.97% over 939 days (not yet recovered, ongoing at window end)
- Annualized: return +4.6%, volatility 12.5% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.26, excess kurtosis +2.77

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 1.71, latest -0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +11.22%; worst month: -7.02%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.93
- Sideways: S=-0.02
- Bear: S=0.15

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_proceeds_from_stock_options_exercised_q, 5))` S=0.65, F=0.29, INFERIOR
Direction gap: +0.31 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_proceeds_from_stock_options_exercised_q)`: S=0.23, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_stock_options_exercised_q / close)`: S=0.32, F=0.12, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_stock_options_exercised_q, 5))`: S=0.65, F=0.29, T=35.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_proceeds_from_stock_options_exercised_q / close)` | TOP200 | 0.37 | 0.20 | 21.0% | 60% | mixed |
| `rank(fn_proceeds_from_stock_options_exercised_q)` | TOP200 | 0.13 | 0.04 | 17.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_optexd: 0.532 (moderately positively correlated)
- fnd6_optex: 0.524 (moderately positively correlated)
- fn_comp_options_out_number_q: 0.498 (moderately positively correlated)
- fn_proceeds_from_stock_options_exercised_a: 0.416 (moderately positively correlated)
- fn_comp_options_out_intrinsic_value_a: 0.406 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
