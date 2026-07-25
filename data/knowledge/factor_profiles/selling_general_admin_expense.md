---
field: selling_general_admin_expense
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.72
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1095
ann_vol: 0.0782
hit_rate: 0.4802
rolling_sharpe_min: -1.294
rolling_sharpe_max: 2.494
redundancy_cluster: 1
negated_best_sharpe: 0.33
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.39
---
# selling_general_admin_expense (analyst4)

*Selling, General & Administrative Expense Value*

## Signal Profile
- `rank(selling_general_admin_expense)`: S=0.36, F=0.21, T=1.0%, INFERIOR (TOP3000)
- `rank(selling_general_admin_expense / close)`: S=0.52, F=0.30, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(selling_general_admin_expense, 5))`: S=0.01, F=0.00, T=36.4%, INFERIOR (TOP1000)
- `-rank(selling_general_admin_expense)`: S=-0.08, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(selling_general_admin_expense, 5))`: S=0.33, F=0.10, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(selling_general_admin_expense, 63)`: S=0.72, F=0.39, T=21.1%, INFERIOR (TOP3000)
- `ts_mean(selling_general_admin_expense, 10)`: S=0.02, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(selling_general_admin_expense, 22))`: S=0.06, F=0.01, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * selling_general_admin_expense)`: S=0.08, F=0.02, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * selling_general_admin_expense / close)`: S=0.07, F=0.02, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/2P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.51, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.55 (negative), ret=-3.0%
  - 2020: S=0.63 (moderate), ret=+5.6%
  - 2021: S=1.32 (moderate), ret=+11.1%
  - 2022: S=0.49 (weak), ret=+3.9%
  - 2023: S=0.31 (weak), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 10.95% over 589 days (not yet recovered, ongoing at window end)
- Annualized: return +4.0%, volatility 7.8% (fraction of booksize)
- Hit rate: 48.0% positive days
- Tail shape: skew +0.55, excess kurtosis +1.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 2.49, latest 0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.00%; worst month: -4.61%
Positive months: 42%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.28
- Sideways: S=-0.72
- Bear: S=-0.48

## Negated Direction
Best negated: `rank(-1 * ts_delta(selling_general_admin_expense, 5))` S=0.33, F=0.10, INFERIOR
Direction gap: -0.39 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * selling_general_admin_expense)`: S=0.08, F=0.02, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * selling_general_admin_expense / close)`: S=0.07, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(selling_general_admin_expense, 5))`: S=0.33, F=0.10, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(selling_general_admin_expense / close)` | TOP3000 | 0.51 | 0.30 | 10.9% | 80% | mixed |
| `rank(selling_general_admin_expense)` | TOP3000 | 0.36 | 0.21 | 33.8% | 60% | bull-only |
| `rank(selling_general_admin_expense / close)` | TOP1000 | 0.14 | 0.04 | 14.3% | 40% | bull-only |
| `rank(selling_general_admin_expense / close)` | TOP500 | 0.13 | 0.04 | 22.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- selling_general_admin_expense_actual_value: 0.963 (strongly positively correlated)
- selling_general_admin_expense_reported_value: 0.963 (strongly positively correlated)
- est_sga: 0.947 (strongly positively correlated)
- fnd6_xopr: 0.932 (strongly positively correlated)
- fnd6_newa1v1300_aco: 0.929 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
