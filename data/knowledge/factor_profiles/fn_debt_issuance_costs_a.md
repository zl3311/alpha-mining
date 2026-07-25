---
field: fn_debt_issuance_costs_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.59
best_fitness: 0.36
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.0923
ann_vol: 0.0426
hit_rate: 0.4704
rolling_sharpe_min: -2.238
rolling_sharpe_max: 1.992
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: 0.43
---
# fn_debt_issuance_costs_a (fundamental2)

*Amount of debt issuance costs (for example, but not limited to, legal, accounting, broker, and regulatory fees).*

## Signal Profile
- `rank(fn_debt_issuance_costs_a)`: S=-0.06, F=-0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_debt_issuance_costs_a / close)`: S=0.18, F=0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_debt_issuance_costs_a, 5))`: S=-0.19, F=-0.10, T=13.2%, INFERIOR (TOP200)
- `-rank(fn_debt_issuance_costs_a)`: S=0.48, F=0.20, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_issuance_costs_a, 5))`: S=0.59, F=0.36, T=28.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_debt_issuance_costs_a, 22)`: S=0.16, F=0.08, T=10.5%, INFERIOR (TOP3000)
- `ts_mean(fn_debt_issuance_costs_a, 10)`: S=-0.35, F=-0.17, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_debt_issuance_costs_a, 22))`: S=0.07, F=0.02, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_issuance_costs_a)`: S=0.48, F=0.20, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_issuance_costs_a / close)`: S=0.16, F=0.04, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.15, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.75 (negative), ret=-2.9%
  - 2020: S=0.21 (weak), ret=+1.1%
  - 2021: S=-0.26 (negative), ret=-1.0%
  - 2022: S=0.32 (weak), ret=+1.4%
  - 2023: S=1.28 (moderate), ret=+4.7%

## Risk & Drawdown
- Max drawdown: 9.23% over 824 days (recovered)
- Annualized: return +0.7%, volatility 4.3% (fraction of booksize)
- Hit rate: 47.0% positive days
- Tail shape: skew +0.37, excess kurtosis +1.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.24, max 1.99, latest 1.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +3.32%; worst month: -2.73%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.88
- Sideways: S=-0.67
- Bear: S=0.24

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_debt_issuance_costs_a, 5))` S=0.59, F=0.36, INFERIOR
Direction gap: +0.43 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_debt_issuance_costs_a)`: S=0.48, F=0.20, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_issuance_costs_a / close)`: S=0.16, F=0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_issuance_costs_a, 5))`: S=0.59, F=0.36, T=28.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_debt_issuance_costs_a / close)` | TOP3000 | 0.15 | 0.04 | 9.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd2_oprlsfmpdcurr: 0.718 (strongly positively correlated)
- est_sga: 0.715 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_5y_a: 0.701 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.693 (moderately positively correlated)
- selling_general_admin_expense_actual_value: 0.691 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
