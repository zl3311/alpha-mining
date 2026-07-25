---
field: fn_allocated_share_based_compensation_expense_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.59
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1581
ann_vol: 0.0869
hit_rate: 0.4939
rolling_sharpe_min: -1.129
rolling_sharpe_max: 3.398
redundancy_cluster: 46
negated_best_sharpe: 0.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.43
---
# fn_allocated_share_based_compensation_expense_a (fundamental2)

*Represents the expense recognized during the period arising from equity-based compensation arrangements (for example, shares of stock, unit, stock options or other equity instruments) with employees, directors and certain consultants qualifying for treatment as employees.*

## Signal Profile
- `rank(fn_allocated_share_based_compensation_expense_a)`: S=0.49, F=0.26, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_allocated_share_based_compensation_expense_a / close)`: S=0.53, F=0.32, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_allocated_share_based_compensation_expense_a, 5))`: S=-0.02, F=0.00, T=34.4%, INFERIOR (TOP1000)
- `-rank(fn_allocated_share_based_compensation_expense_a)`: S=-0.03, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_allocated_share_based_compensation_expense_a, 5))`: S=0.16, F=0.04, T=34.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_allocated_share_based_compensation_expense_a, 63)`: S=0.59, F=0.42, T=18.0%, INFERIOR (TOP3000)
- `ts_mean(fn_allocated_share_based_compensation_expense_a, 10)`: S=0.43, F=0.27, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_allocated_share_based_compensation_expense_a, 22))`: S=-1.09, F=-0.90, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_allocated_share_based_compensation_expense_a)`: S=-0.03, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_allocated_share_based_compensation_expense_a / close)`: S=-0.42, F=-0.22, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.54, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.31 (weak), ret=+1.5%
  - 2020: S=2.43 (strong), ret=+20.0%
  - 2021: S=0.71 (moderate), ret=+3.5%
  - 2022: S=-0.66 (negative), ret=-7.8%
  - 2023: S=0.55 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 15.81% over 634 days (not yet recovered, ongoing at window end)
- Annualized: return +4.7%, volatility 8.7% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.53, excess kurtosis +2.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.13, max 3.40, latest 0.72

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +6.47%; worst month: -4.80%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.08
- Sideways: S=-0.20
- Bear: S=1.78

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_allocated_share_based_compensation_expense_a, 5))` S=0.16, F=0.04, INFERIOR
Direction gap: -0.43 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_allocated_share_based_compensation_expense_a)`: S=-0.03, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_allocated_share_based_compensation_expense_a / close)`: S=-0.42, F=-0.22, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_allocated_share_based_compensation_expense_a, 5))`: S=0.16, F=0.04, T=34.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_allocated_share_based_compensation_expense_a / close)` | TOP3000 | 0.54 | 0.32 | 15.8% | 80% | mixed |
| `rank(fn_allocated_share_based_compensation_expense_a)` | TOP3000 | 0.49 | 0.26 | 16.8% | 100% | bull-only |
| `rank(fn_allocated_share_based_compensation_expense_a / close)` | TOP500 | 0.43 | 0.22 | 11.8% | 80% | bull-only |
| `rank(fn_allocated_share_based_compensation_expense_a / close)` | TOP1000 | 0.39 | 0.19 | 7.9% | 80% | mixed |
| `rank(fn_allocated_share_based_compensation_expense_a / close)` | TOP200 | 0.20 | 0.07 | 19.8% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fn_comp_not_rec_a: 0.968 (strongly positively correlated)
- fnd6_stkcpa: 0.906 (strongly positively correlated)
- fn_comp_non_opt_grants_a: 0.876 (strongly positively correlated)
- fn_oth_comp_fair_value_a: 0.875 (strongly positively correlated)
- fn_comp_non_opt_vested_a: 0.869 (strongly positively correlated)

Redundancy cluster #46: 6 similar fields, mean |rho| 0.737 (representative: fn_op_lease_min_pay_due_after_5y_a). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
