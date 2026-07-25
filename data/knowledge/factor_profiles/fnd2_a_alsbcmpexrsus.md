---
field: fnd2_a_alsbcmpexrsus
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.72
best_fitness: 0.83
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1062
ann_vol: 0.0578
hit_rate: 0.5045
rolling_sharpe_min: -1.007
rolling_sharpe_max: 3.184
redundancy_cluster: 83
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: -0.2
---
# fnd2_a_alsbcmpexrsus (fundamental2)

*Allocated Share-Based Compensation Expense, Restricted Stock Units*

## Signal Profile
- `rank(fnd2_a_alsbcmpexrsus)`: S=0.26, F=0.08, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_a_alsbcmpexrsus / close)`: S=0.65, F=0.36, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_alsbcmpexrsus, 5))`: S=0.23, F=0.08, T=34.8%, INFERIOR (TOP3000)
- `-rank(fnd2_a_alsbcmpexrsus)`: S=0.19, F=0.06, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_alsbcmpexrsus, 5))`: S=-0.41, F=-0.32, T=15.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_alsbcmpexrsus, 63)`: S=0.72, F=0.83, T=11.2%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_alsbcmpexrsus, 10)`: S=0.04, F=0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_alsbcmpexrsus, 22))`: S=-0.26, F=-0.14, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_alsbcmpexrsus)`: S=0.52, F=0.40, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_alsbcmpexrsus / close)`: S=0.18, F=0.08, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.64, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.70 (moderate), ret=+2.7%
  - 2020: S=2.31 (strong), ret=+13.8%
  - 2021: S=0.42 (weak), ret=+1.8%
  - 2022: S=-0.55 (negative), ret=-3.9%
  - 2023: S=0.61 (moderate), ret=+3.8%

## Risk & Drawdown
- Max drawdown: 10.62% over 645 days (not yet recovered, ongoing at window end)
- Annualized: return +3.7%, volatility 5.8% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.64, excess kurtosis +2.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.01, max 3.18, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +5.74%; worst month: -4.02%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.12
- Sideways: S=0.01
- Bear: S=1.80

## Negated Direction
Best negated: `rank(-1 * fnd2_a_alsbcmpexrsus)` S=0.52, F=0.40, INFERIOR
Direction gap: -0.20 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_alsbcmpexrsus)`: S=0.52, F=0.40, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_alsbcmpexrsus / close)`: S=0.18, F=0.08, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_alsbcmpexrsus, 5))`: S=-0.41, F=-0.32, T=15.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_alsbcmpexrsus / close)` | TOP3000 | 0.64 | 0.36 | 10.6% | 80% | mixed |
| `rank(fnd2_a_alsbcmpexrsus / close)` | TOP1000 | 0.45 | 0.23 | 9.8% | 80% | mixed |
| `rank(fnd2_a_alsbcmpexrsus / close)` | TOP500 | 0.22 | 0.09 | 15.4% | 80% | mixed |
| `rank(fnd2_a_alsbcmpexrsus)` | TOP3000 | 0.25 | 0.08 | 11.9% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_alsbcmpexrsus, 5))` | TOP3000 | 0.25 | 0.08 | 32.3% | 40% | weak |

## Correlation Notes
Top correlates:
- fn_allocated_share_based_compensation_expense_a: 0.838 (strongly positively correlated)
- fn_comp_not_rec_a: 0.805 (strongly positively correlated)
- fn_comp_non_opt_vested_a: 0.781 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_5y_a: 0.774 (strongly positively correlated)
- fnd6_stkcpa: 0.763 (strongly positively correlated)

Redundancy cluster #83: 3 similar fields, mean |rho| 0.764 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
