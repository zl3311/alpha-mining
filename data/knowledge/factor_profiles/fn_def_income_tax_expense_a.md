---
field: fn_def_income_tax_expense_a
dataset: fundamental2
best_template: neg_rank_value_norm
best_sharpe: 0.78
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.3178
ann_vol: 0.1447
hit_rate: 0.5085
rolling_sharpe_min: -1.512
rolling_sharpe_max: 2.803
negated_best_sharpe: 0.78
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: 0.3
---
# fn_def_income_tax_expense_a (fundamental2)

*Income Tax Expense, Deferred*

## Signal Profile
- `rank(fn_def_income_tax_expense_a)`: S=-0.37, F=-0.10, T=1.1%, INFERIOR (TOP3000)
- `rank(fn_def_income_tax_expense_a / close)`: S=-0.20, F=-0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_def_income_tax_expense_a, 5))`: S=0.48, F=0.21, T=34.6%, INFERIOR (TOP500)
- `-rank(fn_def_income_tax_expense_a)`: S=0.63, F=0.26, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_income_tax_expense_a, 5))`: S=-0.44, F=-0.19, T=34.5%, INFERIOR (TOP3000)
- `ts_zscore(fn_def_income_tax_expense_a, 22)`: S=-0.19, F=-0.07, T=24.9%, INFERIOR (TOP3000)
- `ts_mean(fn_def_income_tax_expense_a, 10)`: S=-0.13, F=-0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_def_income_tax_expense_a, 22))`: S=-0.61, F=-0.35, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_income_tax_expense_a)`: S=0.73, F=0.37, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_income_tax_expense_a / close)`: S=0.78, F=0.40, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.46, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.81 (strong), ret=+21.9%
  - 2020: S=-0.25 (negative), ret=-3.6%
  - 2021: S=-0.38 (negative), ret=-5.7%
  - 2022: S=0.59 (moderate), ret=+9.5%
  - 2023: S=0.82 (moderate), ret=+10.8%

## Risk & Drawdown
- Max drawdown: 31.78% over 1231 days (recovered)
- Annualized: return +6.7%, volatility 14.5% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.05, excess kurtosis +2.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.51, max 2.80, latest 0.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +9.55%; worst month: -8.37%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.09
- Sideways: S=0.71
- Bear: S=-0.46

## Negated Direction
Best negated: `rank(-1 * fn_def_income_tax_expense_a / close)` S=0.78, F=0.40, INFERIOR
Direction gap: +0.30 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_def_income_tax_expense_a)`: S=0.73, F=0.37, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_income_tax_expense_a / close)`: S=0.78, F=0.40, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_income_tax_expense_a, 5))`: S=-0.44, F=-0.19, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_def_income_tax_expense_a, 5))` | TOP500 | 0.46 | 0.21 | 31.8% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd2_dfdfeditxexp: 0.475 (moderately positively correlated)
- fnd2_dfdfritxexp: 0.208 (weakly positively correlated)
- fnd2_dfdlocalitxexp: 0.171 (weakly positively correlated)
- fnd6_txdi: 0.167 (weakly positively correlated)
- fnd6_txdfed: 0.161 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
