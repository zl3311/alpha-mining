---
field: capital_expenditure_guidance_value
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.88
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1133
ann_vol: 0.0651
hit_rate: 0.4996
rolling_sharpe_min: -1.064
rolling_sharpe_max: 2.861
redundancy_cluster: 46
negated_best_sharpe: 0.88
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.74
n_negated_sims: 10
direction_gap: 0.29
---
# capital_expenditure_guidance_value (analyst4)

*Capital Expenditures - Total value for the annual guidance*

## Signal Profile
- `rank(capital_expenditure_guidance_value)`: S=0.47, F=0.24, T=1.3%, INFERIOR (TOP3000)
- `rank(capital_expenditure_guidance_value / close)`: S=0.59, F=0.33, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(capital_expenditure_guidance_value, 5))`: S=0.23, F=0.05, T=36.1%, INFERIOR (TOP1000)
- `-rank(capital_expenditure_guidance_value)`: S=0.00, F=0.00, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(capital_expenditure_guidance_value, 5))`: S=1.03, F=0.59, T=32.8%, INFERIOR (TOP3000)
- `ts_zscore(capital_expenditure_guidance_value, 22)`: S=0.41, F=0.15, T=34.1%, INFERIOR (TOP3000)
- `ts_mean(capital_expenditure_guidance_value, 10)`: S=-0.03, F=0.00, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(capital_expenditure_guidance_value, 22))`: S=0.15, F=0.03, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * capital_expenditure_guidance_value)`: S=0.87, F=0.72, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * capital_expenditure_guidance_value / close)`: S=0.88, F=0.74, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 7F/25P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.56 (negative), ret=-2.9%
  - 2020: S=1.86 (strong), ret=+15.2%
  - 2021: S=0.98 (moderate), ret=+4.7%
  - 2022: S=0.22 (weak), ret=+1.5%
  - 2023: S=0.07 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 11.33% over 450 days (recovered)
- Annualized: return +3.9%, volatility 6.5% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.66, excess kurtosis +3.48

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.06, max 2.86, latest 0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +5.59%; worst month: -4.75%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.57
- Sideways: S=-0.00
- Bear: S=0.13

## Negated Direction
Best negated: `rank(-1 * capital_expenditure_guidance_value / close)` S=0.88, F=0.74, INFERIOR
Direction gap: +0.29 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * capital_expenditure_guidance_value)`: S=0.87, F=0.72, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * capital_expenditure_guidance_value / close)`: S=0.88, F=0.74, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(capital_expenditure_guidance_value, 5))`: S=1.03, F=0.59, T=32.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(capital_expenditure_guidance_value / close)` | TOP3000 | 0.59 | 0.33 | 11.3% | 80% | mixed |
| `rank(capital_expenditure_guidance_value)` | TOP3000 | 0.46 | 0.24 | 13.0% | 80% | bull-only |
| `rank(ts_delta(capital_expenditure_guidance_value, 5))` | TOP1000 | 0.23 | 0.05 | 15.5% | 60% | bull-only |
| `rank(ts_delta(capital_expenditure_guidance_value, 5))` | TOP500 | 0.13 | 0.02 | 23.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- est_sga: 0.785 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_5y_a: 0.772 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.771 (strongly positively correlated)
- fnd2_oprlsfmpdcurr: 0.770 (strongly positively correlated)
- fnd2_a_seniornotes: 0.770 (strongly positively correlated)

Redundancy cluster #46: 6 similar fields, mean |rho| 0.737 (representative: fn_op_lease_min_pay_due_after_5y_a). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
