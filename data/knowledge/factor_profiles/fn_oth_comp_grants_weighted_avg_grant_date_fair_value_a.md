---
field: fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.72
best_fitness: 0.69
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1762
ann_vol: 0.1135
hit_rate: 0.4688
rolling_sharpe_min: -1.436
rolling_sharpe_max: 2.421
negated_best_sharpe: 1.0
negated_best_template: rank_neg_delta
negated_best_fitness: 0.68
n_negated_sims: 10
direction_gap: 0.28
---
# fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a (fundamental2)

*Annual Share-Based Compensation Equity Instruments Other Than Options Nonvested Weighted Average Grant Date Fair Value*

## Signal Profile
- `rank(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a)`: S=0.15, F=0.05, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a / close)`: S=0.41, F=0.25, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a, 5))`: S=-0.33, F=-0.16, T=29.3%, INFERIOR (TOP200)
- `-rank(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a)`: S=0.04, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a, 5))`: S=1.00, F=0.68, T=33.9%, INFERIOR (TOP3000)
- `-ts_zscore(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a, 63)`: S=0.72, F=0.69, T=17.8%, INFERIOR (TOP3000)
- `ts_mean(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a, 10)`: S=-0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a, 22))`: S=-0.84, F=-0.69, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a)`: S=-0.15, F=-0.05, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a / close)`: S=-0.41, F=-0.25, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.40, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.26 (negative), ret=-1.8%
  - 2020: S=1.22 (moderate), ret=+17.4%
  - 2021: S=0.74 (moderate), ret=+5.8%
  - 2022: S=-0.30 (negative), ret=-3.8%
  - 2023: S=0.42 (weak), ret=+5.0%

## Risk & Drawdown
- Max drawdown: 17.62% over 504 days (not yet recovered, ongoing at window end)
- Annualized: return +4.6%, volatility 11.3% (fraction of booksize)
- Hit rate: 46.9% positive days
- Tail shape: skew +1.06, excess kurtosis +4.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.44, max 2.42, latest 0.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +9.39%; worst month: -5.49%
Positive months: 46%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.17
- Sideways: S=-0.81
- Bear: S=1.68

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a, 5))` S=1.00, F=0.68, INFERIOR
Direction gap: +0.28 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a)`: S=-0.15, F=-0.05, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a / close)`: S=-0.41, F=-0.25, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a, 5))`: S=1.00, F=0.68, T=33.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a / close)` | TOP3000 | 0.40 | 0.25 | 17.6% | 60% | mixed |
| `rank(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a / close)` | TOP1000 | 0.23 | 0.10 | 17.0% | 60% | mixed |
| `rank(fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a)` | TOP3000 | 0.15 | 0.05 | 26.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fn_oth_comp_fair_value_a: 0.978 (strongly positively correlated)
- fn_oth_comp_forfeitures_fair_value_a: 0.974 (strongly positively correlated)
- fnd6_optprcgr: 0.913 (strongly positively correlated)
- fn_comp_options_out_weighted_avg_a: 0.907 (strongly positively correlated)
- fnd6_optprcey: 0.883 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
