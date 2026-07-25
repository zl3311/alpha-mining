---
field: rp_ess_labor
dataset: news18
best_template: ts_zscore
best_sharpe: 0.72
best_fitness: 0.18
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: all-weather
n_variations_with_pnl: 3
max_drawdown: 0.1708
ann_vol: 0.121
hit_rate: 0.5368
rolling_sharpe_min: -1.202
rolling_sharpe_max: 2.22
negated_best_sharpe: 0.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 4
direction_gap: -0.47
---
# rp_ess_labor (news18)

*Event sentiment score of labor issues news*

## Signal Profile
- `rank(rp_ess_labor)`: S=0.58, F=0.12, T=157.8%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_ess_labor, 5))`: S=0.11, F=0.01, T=147.1%, INFERIOR (TOP200)
- `-rank(rp_ess_labor)`: S=-0.27, F=-0.04, T=152.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_labor, 5))`: S=0.25, F=0.04, T=155.1%, INFERIOR (TOP3000)
- `ts_zscore(rp_ess_labor, 22)`: S=0.72, F=0.18, T=145.4%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_labor, 10)`: S=-0.17, F=-0.03, T=28.3%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_labor, 22))`: S=0.48, F=0.09, T=154.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_labor)`: S=-0.58, F=-0.12, T=157.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_labor / close)`: S=-0.35, F=-0.06, T=155.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.59, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.00 (moderate), ret=+14.5%
  - 2020: S=1.39 (moderate), ret=+15.9%
  - 2021: S=-0.70 (negative), ret=-6.8%
  - 2022: S=1.40 (moderate), ret=+15.3%
  - 2023: S=-0.32 (negative), ret=-3.9%

## Risk & Drawdown
- Max drawdown: 17.08% over 681 days (recovered)
- Annualized: return +7.1%, volatility 12.1% (fraction of booksize)
- Hit rate: 53.7% positive days
- Tail shape: skew +0.57, excess kurtosis +11.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.20, max 2.22, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +13.58%; worst month: -8.37%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.59
- Sideways: S=-0.15
- Bear: S=1.65

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_ess_labor, 5))` S=0.25, F=0.04, INFERIOR
Direction gap: -0.47 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_ess_labor)`: S=-0.58, F=-0.12, T=157.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_labor / close)`: S=-0.35, F=-0.06, T=155.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_labor, 5))`: S=0.25, F=0.04, T=155.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_ess_labor)` | TOP3000 | 0.59 | 0.12 | 17.1% | 60% | all-weather |
| `rank(rp_ess_labor)` | TOP1000 | 0.28 | 0.04 | 35.7% | 80% | mixed |
| `rank(rp_ess_labor)` | TOP200 | 0.22 | 0.03 | 27.7% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_oth_comp_fair_value_a: -0.208 (weakly negatively correlated)
- fn_oth_comp_forfeitures_fair_value_a: -0.204 (weakly negatively correlated)
- fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a: -0.203 (weakly negatively correlated)
- fn_allocated_share_based_compensation_expense_a: -0.202 (weakly negatively correlated)
- fn_comp_non_opt_vested_a: -0.202 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
