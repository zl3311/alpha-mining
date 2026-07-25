---
field: fn_income_tax_expense_a
dataset: fundamental2
best_template: neg_rank_level
best_sharpe: 0.52
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.189
ann_vol: 0.0809
hit_rate: 0.5093
rolling_sharpe_min: -3.044
rolling_sharpe_max: 2.176
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.38
n_negated_sims: 10
direction_gap: 0.04
---
# fn_income_tax_expense_a (fundamental2)

*Income Tax Expense (Benefit)*

## Signal Profile
- `rank(fn_income_tax_expense_a)`: S=0.26, F=0.12, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_income_tax_expense_a / close)`: S=0.48, F=0.27, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_income_tax_expense_a, 5))`: S=0.16, F=0.04, T=34.5%, INFERIOR (TOP1000)
- `-rank(fn_income_tax_expense_a)`: S=-0.02, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_income_tax_expense_a, 5))`: S=0.36, F=0.17, T=31.2%, INFERIOR (TOP3000)
- `-ts_zscore(fn_income_tax_expense_a, 63)`: S=-0.16, F=-0.06, T=17.6%, INFERIOR (TOP3000)
- `ts_mean(fn_income_tax_expense_a, 10)`: S=0.13, F=0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_income_tax_expense_a, 22))`: S=-0.17, F=-0.05, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_tax_expense_a)`: S=0.52, F=0.38, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_tax_expense_a / close)`: S=0.44, F=0.29, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.46, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.74 (strong), ret=+6.5%
  - 2020: S=-1.80 (negative), ret=-9.7%
  - 2021: S=0.54 (moderate), ret=+4.8%
  - 2022: S=1.33 (moderate), ret=+16.2%
  - 2023: S=0.07 (weak), ret=+0.5%

## Risk & Drawdown
- Max drawdown: 18.90% over 806 days (recovered)
- Annualized: return +3.7%, volatility 8.1% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew -0.06, excess kurtosis +1.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.04, max 2.18, latest -0.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +5.68%; worst month: -4.12%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.73
- Sideways: S=1.29
- Bear: S=-3.34

## Negated Direction
Best negated: `rank(-1 * fn_income_tax_expense_a)` S=0.52, F=0.38, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_income_tax_expense_a)`: S=0.52, F=0.38, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_tax_expense_a / close)`: S=0.44, F=0.29, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_income_tax_expense_a, 5))`: S=0.36, F=0.17, T=31.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_income_tax_expense_a / close)` | TOP3000 | 0.46 | 0.27 | 18.9% | 80% | bull-only |
| `rank(fn_income_tax_expense_a)` | TOP3000 | 0.25 | 0.12 | 32.2% | 60% | bull-only |
| `rank(fn_income_tax_expense_a / close)` | TOP1000 | 0.17 | 0.07 | 21.5% | 60% | bull-only |
| `rank(ts_delta(fn_income_tax_expense_a, 5))` | TOP1000 | 0.16 | 0.04 | 28.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_txt: 0.983 (strongly positively correlated)
- fnd2_a_curritxexp: 0.960 (strongly positively correlated)
- net_income_adjusted: 0.952 (strongly positively correlated)
- pretax_income_total: 0.950 (strongly positively correlated)
- operating_profit_before_interest_tax: 0.948 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
