---
field: fn_employee_related_liab_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.87
best_fitness: 0.78
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0771
ann_vol: 0.0771
hit_rate: 0.4826
rolling_sharpe_min: -1.098
rolling_sharpe_max: 2.598
redundancy_cluster: 1
negated_best_sharpe: 0.17
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.7
---
# fn_employee_related_liab_a (fundamental2)

*Total of the carrying values as of the balance sheet date of obligations incurred through that date and payable for obligations related to services received from employees, such as accrued salaries and bonuses, payroll taxes and fringe benefits. For classified balance sheets, used to reflect the current portion of the liabilities (due within 1 year or within the normal operating cycle if longer); for unclassified balance sheets, used to reflect the total liabilities (regardless of due date).*

## Signal Profile
- `rank(fn_employee_related_liab_a)`: S=0.55, F=0.39, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_employee_related_liab_a / close)`: S=0.78, F=0.54, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_employee_related_liab_a, 5))`: S=0.29, F=0.13, T=30.0%, INFERIOR (TOP200)
- `-rank(fn_employee_related_liab_a)`: S=-0.36, F=-0.22, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_employee_related_liab_a, 5))`: S=0.17, F=0.05, T=34.5%, INFERIOR (TOP3000)
- `-ts_zscore(fn_employee_related_liab_a, 63)`: S=0.87, F=0.78, T=17.8%, INFERIOR (TOP3000)
- `ts_mean(fn_employee_related_liab_a, 10)`: S=0.26, F=0.12, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_employee_related_liab_a, 22))`: S=-0.08, F=-0.02, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_employee_related_liab_a)`: S=-0.36, F=-0.22, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_employee_related_liab_a / close)`: S=-0.53, F=-0.36, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.23 (weak), ret=+1.3%
  - 2020: S=0.22 (weak), ret=+2.1%
  - 2021: S=1.44 (moderate), ret=+13.4%
  - 2022: S=1.30 (moderate), ret=+9.2%
  - 2023: S=0.56 (moderate), ret=+2.9%

## Risk & Drawdown
- Max drawdown: 7.71% over 100 days (recovered)
- Annualized: return +5.9%, volatility 7.7% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.60, excess kurtosis +3.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.10, max 2.60, latest 0.69

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.29%; worst month: -3.77%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.86
- Sideways: S=0.11
- Bear: S=-1.13

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_employee_related_liab_a, 5))` S=0.17, F=0.05, INFERIOR
Direction gap: -0.70 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_employee_related_liab_a)`: S=-0.36, F=-0.22, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_employee_related_liab_a / close)`: S=-0.53, F=-0.36, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_employee_related_liab_a, 5))`: S=0.17, F=0.05, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_employee_related_liab_a / close)` | TOP3000 | 0.77 | 0.54 | 7.7% | 100% | bull-only |
| `rank(fn_employee_related_liab_a)` | TOP3000 | 0.55 | 0.39 | 33.7% | 80% | bull-only |
| `rank(fn_employee_related_liab_a / close)` | TOP1000 | 0.52 | 0.36 | 21.1% | 80% | bull-only |
| `rank(fn_employee_related_liab_a)` | TOP1000 | 0.35 | 0.22 | 39.8% | 80% | bull-only |
| `rank(ts_delta(fn_employee_related_liab_a, 5))` | TOP200 | 0.29 | 0.13 | 64.4% | 60% | weak |
| `rank(fn_employee_related_liab_a / close)` | TOP500 | 0.23 | 0.11 | 35.7% | 80% | bull-only |
| `rank(ts_delta(fn_employee_related_liab_a, 5))` | TOP3000 | 0.27 | 0.08 | 23.7% | 60% | mixed |
| `rank(fn_employee_related_liab_a)` | TOP500 | 0.05 | 0.02 | 55.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_xopr: 0.950 (strongly positively correlated)
- liabilities: 0.948 (strongly positively correlated)
- fnd6_cptnewqv1300_ltq: 0.948 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.948 (strongly positively correlated)
- fnd6_newqv1300_ltmibq: 0.948 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
