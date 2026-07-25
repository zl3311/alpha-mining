---
field: selling_general_admin_expense_reported_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.44
best_fitness: 0.23
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.1255
ann_vol: 0.0782
hit_rate: 0.4713
rolling_sharpe_min: -1.437
rolling_sharpe_max: 2.571
negated_best_sharpe: 0.62
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: 0.18
---
# selling_general_admin_expense_reported_value (analyst4)

*Selling, General & Administrative Expense value*

## Signal Profile
- `rank(selling_general_admin_expense_reported_value)`: S=0.36, F=0.21, T=1.8%, INFERIOR (TOP3000)
- `rank(selling_general_admin_expense_reported_value / close)`: S=0.44, F=0.23, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(selling_general_admin_expense_reported_value, 5))`: S=0.13, F=0.02, T=36.7%, INFERIOR (TOP200)
- `-rank(selling_general_admin_expense_reported_value)`: S=-0.09, F=-0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(selling_general_admin_expense_reported_value, 5))`: S=0.62, F=0.17, T=37.5%, INFERIOR (TOP3000)
- `ts_zscore(selling_general_admin_expense_reported_value, 22)`: S=0.60, F=0.22, T=39.3%, INFERIOR (TOP3000)
- `ts_mean(selling_general_admin_expense_reported_value, 10)`: S=0.19, F=0.08, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(selling_general_admin_expense_reported_value, 22))`: S=0.34, F=0.11, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * selling_general_admin_expense_reported_value)`: S=-0.36, F=-0.21, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * selling_general_admin_expense_reported_value / close)`: S=-0.44, F=-0.23, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.43, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.36 (negative), ret=-2.1%
  - 2020: S=0.49 (weak), ret=+4.3%
  - 2021: S=1.40 (moderate), ret=+11.9%
  - 2022: S=-0.10 (negative), ret=-0.8%
  - 2023: S=0.46 (weak), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 12.55% over 589 days (not yet recovered, ongoing at window end)
- Annualized: return +3.4%, volatility 7.8% (fraction of booksize)
- Hit rate: 47.1% positive days
- Tail shape: skew +0.47, excess kurtosis +1.68

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.44, max 2.57, latest 0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.61%; worst month: -4.36%
Positive months: 44%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.04
- Sideways: S=-0.80
- Bear: S=-0.30

## Negated Direction
Best negated: `rank(-1 * ts_delta(selling_general_admin_expense_reported_value, 5))` S=0.62, F=0.17, INFERIOR
Direction gap: +0.18 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * selling_general_admin_expense_reported_value)`: S=-0.36, F=-0.21, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * selling_general_admin_expense_reported_value / close)`: S=-0.44, F=-0.23, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(selling_general_admin_expense_reported_value, 5))`: S=0.62, F=0.17, T=37.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(selling_general_admin_expense_reported_value / close)` | TOP3000 | 0.43 | 0.23 | 12.6% | 60% | mixed |
| `rank(selling_general_admin_expense_reported_value)` | TOP3000 | 0.36 | 0.21 | 34.2% | 80% | bull-only |
| `rank(selling_general_admin_expense_reported_value / close)` | TOP500 | 0.12 | 0.04 | 21.6% | 80% | bull-only |
| `rank(selling_general_admin_expense_reported_value)` | TOP1000 | 0.08 | 0.03 | 37.9% | 60% | bull-only |
| `rank(selling_general_admin_expense_reported_value / close)` | TOP1000 | 0.11 | 0.03 | 11.8% | 40% | bull-only |
| `rank(ts_delta(selling_general_admin_expense_reported_value, 5))` | TOP500 | 0.12 | 0.02 | 10.7% | 60% | mixed |
| `rank(ts_delta(selling_general_admin_expense_reported_value, 5))` | TOP200 | 0.14 | 0.02 | 16.9% | 40% | weak |

## Correlation Notes
Top correlates:
- selling_general_admin_expense_actual_value: 1.000 (strongly positively correlated)
- est_sga: 0.966 (strongly positively correlated)
- selling_general_admin_expense: 0.963 (strongly positively correlated)
- fnd6_newqv1300_lseq: 0.911 (strongly positively correlated)
- fnd6_cptnewqv1300_atq: 0.911 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
