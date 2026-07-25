---
field: fn_proceeds_from_issuance_of_common_stock_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.45
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.3446
ann_vol: 0.212
hit_rate: 0.4874
rolling_sharpe_min: -1.257
rolling_sharpe_max: 1.418
negated_best_sharpe: 0.51
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: 0.06
---
# fn_proceeds_from_issuance_of_common_stock_a (fundamental2)

*The cash inflow from the additional capital contribution to the entity.*

## Signal Profile
- `rank(fn_proceeds_from_issuance_of_common_stock_a)`: S=-0.01, F=0.00, T=1.7%, INFERIOR (TOP500)
- `rank(fn_proceeds_from_issuance_of_common_stock_a / close)`: S=0.09, F=0.02, T=1.9%, INFERIOR (TOP500)
- `rank(ts_delta(fn_proceeds_from_issuance_of_common_stock_a, 5))`: S=0.23, F=0.10, T=27.2%, INFERIOR (TOP500)
- `-rank(fn_proceeds_from_issuance_of_common_stock_a)`: S=0.05, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_issuance_of_common_stock_a, 5))`: S=0.51, F=0.31, T=32.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_proceeds_from_issuance_of_common_stock_a, 63)`: S=0.45, F=0.48, T=13.9%, INFERIOR (TOP3000)
- `ts_mean(fn_proceeds_from_issuance_of_common_stock_a, 10)`: S=0.06, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_proceeds_from_issuance_of_common_stock_a, 22))`: S=-0.41, F=-0.27, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_issuance_of_common_stock_a)`: S=0.50, F=0.20, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_issuance_of_common_stock_a / close)`: S=0.48, F=0.22, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.23, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.12 (negative), ret=-2.1%
  - 2020: S=1.20 (moderate), ret=+24.6%
  - 2021: S=-0.36 (negative), ret=-8.8%
  - 2022: S=0.43 (weak), ret=+10.9%
  - 2023: S=-0.05 (negative), ret=-0.7%

## Risk & Drawdown
- Max drawdown: 34.46% over 613 days (recovered)
- Annualized: return +4.9%, volatility 21.2% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.17, excess kurtosis +7.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 1.42, latest -0.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +12.51%; worst month: -21.20%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.46
- Sideways: S=-0.97
- Bear: S=0.92

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_proceeds_from_issuance_of_common_stock_a, 5))` S=0.51, F=0.31, INFERIOR
Direction gap: +0.06 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_proceeds_from_issuance_of_common_stock_a)`: S=0.50, F=0.20, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_issuance_of_common_stock_a / close)`: S=0.48, F=0.22, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_issuance_of_common_stock_a, 5))`: S=0.51, F=0.31, T=32.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_proceeds_from_issuance_of_common_stock_a, 5))` | TOP500 | 0.23 | 0.10 | 34.5% | 40% | mixed |
| `rank(ts_delta(fn_proceeds_from_issuance_of_common_stock_a, 5))` | TOP1000 | 0.17 | 0.06 | 43.4% | 80% | mixed |
| `rank(fn_proceeds_from_issuance_of_common_stock_a / close)` | TOP500 | 0.08 | 0.02 | 16.2% | 40% | mixed |

## Correlation Notes
Top correlates:
- fn_new_shares_issued_a: 0.183 (weakly positively correlated)
- fn_repurchased_shares_value_a: 0.181 (weakly positively correlated)
- fnd6_newa1v1300_dcom: 0.171 (weakly positively correlated)
- fnd2_ebitdm: 0.171 (weakly positively correlated)
- fn_debt_instrument_interest_rate_stated_percentage_a: -0.170 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
