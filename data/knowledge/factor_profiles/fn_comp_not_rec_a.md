---
field: fn_comp_not_rec_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.89
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1327
ann_vol: 0.0753
hit_rate: 0.5077
rolling_sharpe_min: -1.071
rolling_sharpe_max: 2.717
redundancy_cluster: 46
negated_best_sharpe: 0.38
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.51
---
# fn_comp_not_rec_a (fundamental2)

*Unrecognized cost of unvested share-based compensation awards.*

## Signal Profile
- `rank(fn_comp_not_rec_a)`: S=0.49, F=0.24, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_comp_not_rec_a / close)`: S=0.54, F=0.31, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_comp_not_rec_a, 5))`: S=0.11, F=0.03, T=31.4%, INFERIOR (TOP200)
- `-rank(fn_comp_not_rec_a)`: S=-0.14, F=-0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_not_rec_a, 5))`: S=0.38, F=0.14, T=34.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_not_rec_a, 63)`: S=0.89, F=0.74, T=17.4%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_not_rec_a, 10)`: S=0.74, F=0.61, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_not_rec_a, 22))`: S=-0.05, F=-0.01, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_not_rec_a)`: S=-0.49, F=-0.24, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_not_rec_a / close)`: S=-0.54, F=-0.31, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.55, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.86 (moderate), ret=+3.6%
  - 2020: S=2.02 (strong), ret=+15.1%
  - 2021: S=0.49 (weak), ret=+2.1%
  - 2022: S=-0.49 (negative), ret=-5.1%
  - 2023: S=0.53 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 13.27% over 634 days (not yet recovered, ongoing at window end)
- Annualized: return +4.1%, volatility 7.5% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.48, excess kurtosis +2.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.07, max 2.72, latest 0.70

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +5.10%; worst month: -3.96%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.05
- Sideways: S=0.10
- Bear: S=1.55

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_not_rec_a, 5))` S=0.38, F=0.14, INFERIOR
Direction gap: -0.51 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_comp_not_rec_a)`: S=-0.49, F=-0.24, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_not_rec_a / close)`: S=-0.54, F=-0.31, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_not_rec_a, 5))`: S=0.38, F=0.14, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_not_rec_a / close)` | TOP3000 | 0.55 | 0.31 | 13.3% | 80% | mixed |
| `rank(fn_comp_not_rec_a / close)` | TOP1000 | 0.49 | 0.25 | 7.9% | 80% | mixed |
| `rank(fn_comp_not_rec_a)` | TOP3000 | 0.50 | 0.24 | 17.9% | 80% | bull-only |
| `rank(fn_comp_not_rec_a / close)` | TOP500 | 0.23 | 0.08 | 11.8% | 60% | bull-only |
| `rank(fn_comp_not_rec_a)` | TOP1000 | 0.14 | 0.04 | 25.1% | 80% | bull-only |
| `rank(ts_delta(fn_comp_not_rec_a, 5))` | TOP200 | 0.11 | 0.03 | 38.2% | 40% | weak |

## Correlation Notes
Top correlates:
- fn_allocated_share_based_compensation_expense_a: 0.968 (strongly positively correlated)
- fnd6_stkcpa: 0.869 (strongly positively correlated)
- fn_oth_comp_fair_value_a: 0.865 (strongly positively correlated)
- fn_comp_non_opt_grants_a: 0.854 (strongly positively correlated)
- fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a: 0.852 (strongly positively correlated)

Redundancy cluster #46: 6 similar fields, mean |rho| 0.737 (representative: fn_op_lease_min_pay_due_after_5y_a). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
