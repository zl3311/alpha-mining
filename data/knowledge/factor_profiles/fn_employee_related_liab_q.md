---
field: fn_employee_related_liab_q
dataset: fundamental2
best_template: rank_level
best_sharpe: 0.75
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.3007
ann_vol: 0.1173
hit_rate: 0.5231
rolling_sharpe_min: -2.889
rolling_sharpe_max: 2.696
redundancy_cluster: 13
negated_best_sharpe: 0.51
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.24
---
# fn_employee_related_liab_q (fundamental2)

*Total of the carrying values as of the balance sheet date of obligations incurred through that date and payable for obligations related to services received from employees, such as accrued salaries and bonuses, payroll taxes and fringe benefits. For classified balance sheets, used to reflect the current portion of the liabilities (due within 1 year or within the normal operating cycle if longer); for unclassified balance sheets, used to reflect the total liabilities (regardless of due date).*

## Signal Profile
- `rank(fn_employee_related_liab_q)`: S=0.75, F=0.63, T=1.1%, INFERIOR (TOP3000)
- `rank(fn_employee_related_liab_q / close)`: S=0.80, F=0.57, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_employee_related_liab_q, 5))`: S=0.52, F=0.20, T=36.4%, INFERIOR (TOP3000)
- `-rank(fn_employee_related_liab_q)`: S=-0.63, F=-0.53, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_employee_related_liab_q, 5))`: S=0.51, F=0.25, T=36.5%, INFERIOR (TOP3000)
- `-ts_zscore(fn_employee_related_liab_q, 63)`: S=-0.20, F=-0.06, T=18.2%, INFERIOR (TOP3000)
- `ts_mean(fn_employee_related_liab_q, 10)`: S=0.43, F=0.27, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_employee_related_liab_q, 22))`: S=-0.16, F=-0.04, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_employee_related_liab_q)`: S=0.20, F=0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_employee_related_liab_q / close)`: S=0.25, F=0.14, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.75, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+3.7%
  - 2020: S=-1.59 (negative), ret=-12.5%
  - 2021: S=1.36 (moderate), ret=+21.2%
  - 2022: S=1.53 (strong), ret=+23.7%
  - 2023: S=0.73 (moderate), ret=+6.8%

## Risk & Drawdown
- Max drawdown: 30.07% over 781 days (recovered)
- Annualized: return +8.8%, volatility 11.7% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew +0.03, excess kurtosis +1.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.89, max 2.70, latest 0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.35%; worst month: -6.13%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.03
- Sideways: S=1.14
- Bear: S=-2.66

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_employee_related_liab_q, 5))` S=0.51, F=0.25, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_employee_related_liab_q)`: S=0.20, F=0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_employee_related_liab_q / close)`: S=0.25, F=0.14, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_employee_related_liab_q, 5))`: S=0.51, F=0.25, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_employee_related_liab_q)` | TOP3000 | 0.75 | 0.63 | 30.1% | 80% | bull-only |
| `rank(fn_employee_related_liab_q / close)` | TOP3000 | 0.79 | 0.57 | 11.8% | 100% | mixed |
| `rank(fn_employee_related_liab_q)` | TOP1000 | 0.62 | 0.53 | 33.2% | 60% | bull-only |
| `rank(fn_employee_related_liab_q / close)` | TOP1000 | 0.61 | 0.47 | 14.3% | 60% | bull-only |
| `rank(fn_employee_related_liab_q)` | TOP500 | 0.39 | 0.27 | 41.9% | 60% | bull-only |
| `rank(fn_employee_related_liab_q / close)` | TOP500 | 0.38 | 0.25 | 23.2% | 60% | bull-only |
| `rank(ts_delta(fn_employee_related_liab_q, 5))` | TOP3000 | 0.48 | 0.20 | 18.2% | 80% | all-weather |
| `rank(ts_delta(fn_employee_related_liab_q, 5))` | TOP1000 | 0.15 | 0.03 | 19.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_xoprq: 0.965 (strongly positively correlated)
- operating_expense: 0.965 (strongly positively correlated)
- fnd6_newqv1300_icaptq: 0.957 (strongly positively correlated)
- invested_capital: 0.957 (strongly positively correlated)
- fnd6_newqv1300_acoq: 0.952 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
