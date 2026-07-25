---
field: fn_def_income_tax_expense_q
dataset: fundamental2
best_template: neg_rank_value_norm
best_sharpe: 0.88
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.3556
ann_vol: 0.1447
hit_rate: 0.4947
rolling_sharpe_min: -1.423
rolling_sharpe_max: 1.496
negated_best_sharpe: 0.88
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.47
n_negated_sims: 10
direction_gap: 0.66
---
# fn_def_income_tax_expense_q (fundamental2)

*Income Tax Expense, Deferred*

## Signal Profile
- `rank(fn_def_income_tax_expense_q)`: S=-0.53, F=-0.21, T=2.9%, INFERIOR (TOP1000)
- `rank(fn_def_income_tax_expense_q / close)`: S=-0.56, F=-0.23, T=3.1%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_def_income_tax_expense_q, 5))`: S=0.22, F=0.06, T=36.8%, INFERIOR (TOP500)
- `-rank(fn_def_income_tax_expense_q)`: S=0.53, F=0.21, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_income_tax_expense_q, 5))`: S=-0.20, F=-0.06, T=37.0%, INFERIOR (TOP3000)
- `-ts_zscore(fn_def_income_tax_expense_q, 63)`: S=0.07, F=0.01, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(fn_def_income_tax_expense_q, 10)`: S=-0.44, F=-0.20, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_def_income_tax_expense_q, 22))`: S=-0.40, F=-0.15, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_income_tax_expense_q)`: S=0.71, F=0.35, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_income_tax_expense_q / close)`: S=0.88, F=0.47, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.21, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.01 (moderate), ret=+10.0%
  - 2020: S=0.53 (moderate), ret=+8.2%
  - 2021: S=0.85 (moderate), ret=+14.1%
  - 2022: S=-1.25 (negative), ret=-20.7%
  - 2023: S=0.29 (weak), ret=+3.1%

## Risk & Drawdown
- Max drawdown: 35.56% over 827 days (not yet recovered, ongoing at window end)
- Annualized: return +3.0%, volatility 14.5% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.70, excess kurtosis +7.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.42, max 1.50, latest 0.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +7.85%; worst month: -16.67%
Positive months: 54%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.02
- Sideways: S=0.34
- Bear: S=0.31

## Negated Direction
Best negated: `rank(-1 * fn_def_income_tax_expense_q / close)` S=0.88, F=0.47, INFERIOR
Direction gap: +0.66 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fn_def_income_tax_expense_q)`: S=0.71, F=0.35, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_income_tax_expense_q / close)`: S=0.88, F=0.47, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_income_tax_expense_q, 5))`: S=-0.20, F=-0.06, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_def_income_tax_expense_q, 5))` | TOP500 | 0.21 | 0.06 | 35.6% | 80% | weak |
| `rank(ts_delta(fn_def_income_tax_expense_q, 5))` | TOP200 | 0.12 | 0.03 | 46.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_propplteqmuflmeqmt: -0.121 (weakly negatively correlated)
- fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q: -0.118 (weakly negatively correlated)
- snt_buzz_ret: 0.111 (weakly positively correlated)
- fn_line_of_credit_facility_amount_out_q: 0.109 (weakly positively correlated)
- fnd2_dfdfeditxexp: 0.107 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
