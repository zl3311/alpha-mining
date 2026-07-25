---
field: fn_liab_fair_val_q
dataset: fundamental2
best_template: ts_mean
best_sharpe: 0.62
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 2
max_drawdown: 0.0857
ann_vol: 0.0433
hit_rate: 0.5028
rolling_sharpe_min: -1.506
rolling_sharpe_max: 2.477
negated_best_sharpe: 0.47
negated_best_template: neg_rank_level
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.15
---
# fn_liab_fair_val_q (fundamental2)

*Liabilities Fair Value, Recurring, Total*

## Signal Profile
- `rank(fn_liab_fair_val_q)`: S=0.38, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_liab_fair_val_q / close)`: S=0.39, F=0.14, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_liab_fair_val_q, 5))`: S=0.01, F=0.00, T=29.1%, INFERIOR (TOP200)
- `-rank(fn_liab_fair_val_q)`: S=0.06, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_liab_fair_val_q, 5))`: S=0.05, F=0.01, T=36.5%, INFERIOR (TOP3000)
- `-ts_zscore(fn_liab_fair_val_q, 63)`: S=0.00, F=0.00, T=15.5%, INFERIOR (TOP3000)
- `ts_mean(fn_liab_fair_val_q, 10)`: S=0.62, F=0.34, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_liab_fair_val_q, 22))`: S=-0.50, F=-0.24, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_q)`: S=0.47, F=0.22, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_q / close)`: S=0.22, F=0.07, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.38, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.40 (weak), ret=+1.2%
  - 2020: S=-0.07 (negative), ret=-0.3%
  - 2021: S=2.19 (strong), ret=+8.6%
  - 2022: S=-0.97 (negative), ret=-5.2%
  - 2023: S=0.86 (moderate), ret=+3.7%

## Risk & Drawdown
- Max drawdown: 8.57% over 639 days (not yet recovered, ongoing at window end)
- Annualized: return +1.6%, volatility 4.3% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.16, excess kurtosis +1.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.51, max 2.48, latest 1.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +2.74%; worst month: -4.04%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.82
- Sideways: S=-0.47
- Bear: S=0.71

## Negated Direction
Best negated: `rank(-1 * fn_liab_fair_val_q)` S=0.47, F=0.22, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_liab_fair_val_q)`: S=0.47, F=0.22, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_q / close)`: S=0.22, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_liab_fair_val_q, 5))`: S=0.05, F=0.01, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_liab_fair_val_q / close)` | TOP3000 | 0.38 | 0.14 | 8.6% | 60% | all-weather |
| `rank(fn_liab_fair_val_q)` | TOP3000 | 0.37 | 0.14 | 14.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_liab_fair_val_a: 0.820 (strongly positively correlated)
- fn_comp_not_rec_a: 0.643 (moderately positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.639 (moderately positively correlated)
- fn_business_combination_purchase_price_a: 0.631 (moderately positively correlated)
- fn_oth_comp_fair_value_a: 0.612 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
