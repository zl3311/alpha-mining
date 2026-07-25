---
field: fn_business_combination_purchase_price_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.68
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.0882
ann_vol: 0.0444
hit_rate: 0.4794
rolling_sharpe_min: -1.497
rolling_sharpe_max: 1.617
negated_best_sharpe: 0.68
negated_best_template: rank_neg_delta
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: 0.42
---
# fn_business_combination_purchase_price_a (fundamental2)

*Business Combination, Purchase Price*

## Signal Profile
- `rank(fn_business_combination_purchase_price_a)`: S=0.20, F=0.05, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_business_combination_purchase_price_a / close)`: S=0.26, F=0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_business_combination_purchase_price_a, 5))`: S=-0.01, F=0.00, T=32.6%, INFERIOR (TOP1000)
- `-rank(fn_business_combination_purchase_price_a)`: S=0.06, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_business_combination_purchase_price_a, 5))`: S=0.68, F=0.37, T=33.2%, INFERIOR (TOP3000)
- `-ts_zscore(fn_business_combination_purchase_price_a, 63)`: S=0.11, F=0.05, T=13.1%, INFERIOR (TOP3000)
- `ts_mean(fn_business_combination_purchase_price_a, 10)`: S=-0.04, F=-0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_business_combination_purchase_price_a, 22))`: S=0.11, F=0.03, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_business_combination_purchase_price_a)`: S=-0.20, F=-0.05, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_business_combination_purchase_price_a / close)`: S=-0.26, F=-0.08, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.26, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=1.11 (moderate), ret=+3.2%
  - 2020: S=0.81 (moderate), ret=+4.3%
  - 2021: S=-0.28 (negative), ret=-1.0%
  - 2022: S=-0.17 (negative), ret=-0.8%
  - 2023: S=-0.01 (negative), ret=-0.1%

## Risk & Drawdown
- Max drawdown: 8.82% over 963 days (not yet recovered, ongoing at window end)
- Annualized: return +1.1%, volatility 4.4% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.72, excess kurtosis +2.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.50, max 1.62, latest 0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +2.91%; worst month: -3.35%
Positive months: 48%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.78
- Sideways: S=-0.19
- Bear: S=0.13

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_business_combination_purchase_price_a, 5))` S=0.68, F=0.37, INFERIOR
Direction gap: +0.42 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_business_combination_purchase_price_a)`: S=-0.20, F=-0.05, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_business_combination_purchase_price_a / close)`: S=-0.26, F=-0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_business_combination_purchase_price_a, 5))`: S=0.68, F=0.37, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_business_combination_purchase_price_a / close)` | TOP3000 | 0.26 | 0.08 | 8.8% | 40% | mixed |
| `rank(fn_business_combination_purchase_price_a)` | TOP3000 | 0.19 | 0.05 | 12.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_op_lease_min_pay_due_in_5y_a: 0.859 (strongly positively correlated)
- fnd2_oprlsfmpdcurr: 0.854 (strongly positively correlated)
- fnd2_a_ptoacqbnsesg: 0.846 (strongly positively correlated)
- fn_op_lease_min_pay_due_a: 0.844 (strongly positively correlated)
- fn_op_lease_min_pay_due_after_5y_a: 0.827 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
