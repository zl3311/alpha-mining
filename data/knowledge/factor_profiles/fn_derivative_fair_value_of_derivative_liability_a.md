---
field: fn_derivative_fair_value_of_derivative_liability_a
dataset: fundamental2
best_template: ts_mean
best_sharpe: 0.99
best_fitness: 0.89
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.0741
ann_vol: 0.0403
hit_rate: 0.502
rolling_sharpe_min: -2.066
rolling_sharpe_max: 2.212
negated_best_sharpe: 0.44
negated_best_template: neg_rank_level
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.55
---
# fn_derivative_fair_value_of_derivative_liability_a (fundamental2)

*Fair value, before effects of master netting arrangements, of a financial liability or contract with one or more underlyings, notional amount or payment provision or both, and the contract can be net settled by means outside the contract or delivery of an asset. Includes liabilities elected not to be offset. Excludes liabilities not subject to a master netting arrangement.*

## Signal Profile
- `rank(fn_derivative_fair_value_of_derivative_liability_a)`: S=0.25, F=0.08, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_derivative_fair_value_of_derivative_liability_a / close)`: S=0.61, F=0.27, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_derivative_fair_value_of_derivative_liability_a, 5))`: S=0.23, F=0.08, T=32.3%, INFERIOR (TOP500)
- `-rank(fn_derivative_fair_value_of_derivative_liability_a)`: S=0.06, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_derivative_fair_value_of_derivative_liability_a, 5))`: S=-0.20, F=-0.06, T=32.0%, INFERIOR (TOP3000)
- `ts_zscore(fn_derivative_fair_value_of_derivative_liability_a, 22)`: S=0.25, F=0.11, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(fn_derivative_fair_value_of_derivative_liability_a, 10)`: S=0.99, F=0.89, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_derivative_fair_value_of_derivative_liability_a, 22))`: S=-0.82, F=-0.59, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_fair_value_of_derivative_liability_a)`: S=0.44, F=0.21, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_fair_value_of_derivative_liability_a / close)`: S=0.33, F=0.13, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.60, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.20 (moderate), ret=+3.5%
  - 2020: S=0.77 (moderate), ret=+4.4%
  - 2021: S=1.47 (moderate), ret=+5.2%
  - 2022: S=-0.59 (negative), ret=-2.2%
  - 2023: S=0.36 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 7.41% over 585 days (not yet recovered, ongoing at window end)
- Annualized: return +2.4%, volatility 4.0% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.66, excess kurtosis +5.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.07, max 2.21, latest 0.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +2.58%; worst month: -4.66%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.74
- Sideways: S=0.37
- Bear: S=-0.29

## Negated Direction
Best negated: `rank(-1 * fn_derivative_fair_value_of_derivative_liability_a)` S=0.44, F=0.21, INFERIOR
Direction gap: -0.55 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_derivative_fair_value_of_derivative_liability_a)`: S=0.44, F=0.21, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_fair_value_of_derivative_liability_a / close)`: S=0.33, F=0.13, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_derivative_fair_value_of_derivative_liability_a, 5))`: S=-0.20, F=-0.06, T=32.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_derivative_fair_value_of_derivative_liability_a / close)` | TOP3000 | 0.60 | 0.27 | 7.4% | 80% | mixed |
| `rank(ts_delta(fn_derivative_fair_value_of_derivative_liability_a, 5))` | TOP500 | 0.25 | 0.08 | 34.3% | 60% | mixed |
| `rank(fn_derivative_fair_value_of_derivative_liability_a)` | TOP3000 | 0.24 | 0.08 | 11.2% | 80% | bull-only |
| `rank(fn_derivative_fair_value_of_derivative_liability_a / close)` | TOP1000 | 0.20 | 0.07 | 8.9% | 60% | bull-only |
| `rank(ts_delta(fn_derivative_fair_value_of_derivative_liability_a, 5))` | TOP1000 | 0.20 | 0.06 | 25.1% | 40% | mixed |
| `rank(ts_delta(fn_derivative_fair_value_of_derivative_liability_a, 5))` | TOP200 | 0.09 | 0.02 | 47.7% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_derivative_notional_amount_a: 0.735 (strongly positively correlated)
- fn_derivative_notional_amount_q: 0.722 (strongly positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_a: 0.697 (moderately positively correlated)
- fn_op_lease_rent_exp_a: 0.695 (moderately positively correlated)
- est_tot_assets: 0.694 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
