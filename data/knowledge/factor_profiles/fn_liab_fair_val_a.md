---
field: fn_liab_fair_val_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 1.11
best_fitness: 0.91
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.0483
ann_vol: 0.0393
hit_rate: 0.5296
rolling_sharpe_min: -0.856
rolling_sharpe_max: 2.18
negated_best_sharpe: 1.11
negated_best_template: rank_neg_delta
negated_best_fitness: 0.91
n_negated_sims: 10
direction_gap: -0.04
---
# fn_liab_fair_val_a (fundamental2)

*Liabilities Fair Value, Recurring, Total*

## Signal Profile
- `rank(fn_liab_fair_val_a)`: S=0.37, F=0.14, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_liab_fair_val_a / close)`: S=0.75, F=0.36, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_liab_fair_val_a, 5))`: S=0.55, F=0.32, T=27.6%, INFERIOR (TOP500)
- `-rank(fn_liab_fair_val_a)`: S=0.33, F=0.12, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_liab_fair_val_a, 5))`: S=1.11, F=0.91, T=31.2%, INFERIOR (TOP3000)
- `ts_zscore(fn_liab_fair_val_a, 22)`: S=0.61, F=0.60, T=13.0%, INFERIOR (TOP3000)
- `ts_mean(fn_liab_fair_val_a, 10)`: S=1.15, F=0.88, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_liab_fair_val_a, 22))`: S=-0.26, F=-0.13, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_a)`: S=-0.37, F=-0.14, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_a / close)`: S=-0.75, F=-0.36, T=1.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 9F/23P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.74, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.13 (strong), ret=+5.9%
  - 2020: S=-0.42 (negative), ret=-1.8%
  - 2021: S=1.42 (moderate), ret=+5.1%
  - 2022: S=-0.24 (negative), ret=-1.1%
  - 2023: S=1.56 (strong), ret=+6.0%

## Risk & Drawdown
- Max drawdown: 4.83% over 565 days (recovered)
- Annualized: return +2.9%, volatility 3.9% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +0.14, excess kurtosis +1.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.86, max 2.18, latest 1.66

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +2.48%; worst month: -3.17%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.48
- Sideways: S=0.41
- Bear: S=0.33

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_liab_fair_val_a, 5))` S=1.11, F=0.91, INFERIOR
Direction gap: -0.04 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_liab_fair_val_a)`: S=-0.37, F=-0.14, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_a / close)`: S=-0.75, F=-0.36, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_liab_fair_val_a, 5))`: S=1.11, F=0.91, T=31.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_liab_fair_val_a / close)` | TOP3000 | 0.74 | 0.36 | 4.8% | 60% | mixed |
| `rank(ts_delta(fn_liab_fair_val_a, 5))` | TOP500 | 0.55 | 0.32 | 18.9% | 80% | mixed |
| `rank(ts_delta(fn_liab_fair_val_a, 5))` | TOP200 | 0.33 | 0.19 | 29.1% | 60% | weak |
| `rank(fn_liab_fair_val_a)` | TOP3000 | 0.36 | 0.14 | 18.5% | 80% | bull-only |
| `rank(ts_delta(fn_liab_fair_val_a, 5))` | TOP1000 | 0.29 | 0.13 | 36.8% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_liab_fair_val_q: 0.820 (strongly positively correlated)
- fn_business_combination_purchase_price_a: 0.643 (moderately positively correlated)
- est_sga: 0.624 (moderately positively correlated)
- selling_general_admin_expense_actual_value: 0.617 (moderately positively correlated)
- selling_general_admin_expense_reported_value: 0.617 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
