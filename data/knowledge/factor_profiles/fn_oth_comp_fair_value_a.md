---
field: fn_oth_comp_fair_value_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.89
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.1935
ann_vol: 0.1133
hit_rate: 0.4599
rolling_sharpe_min: -1.656
rolling_sharpe_max: 2.064
negated_best_sharpe: 0.89
negated_best_template: rank_neg_delta
negated_best_fitness: 0.57
n_negated_sims: 10
direction_gap: 0.34
---
# fn_oth_comp_fair_value_a (fundamental2)

*Annual share-based compensation equity instruments other than options grants in period weighted average grant date fair value*

## Signal Profile
- `rank(fn_oth_comp_fair_value_a)`: S=0.01, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_oth_comp_fair_value_a / close)`: S=0.29, F=0.15, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_oth_comp_fair_value_a, 5))`: S=0.06, F=0.01, T=32.3%, INFERIOR (TOP500)
- `-rank(fn_oth_comp_fair_value_a)`: S=0.13, F=0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_comp_fair_value_a, 5))`: S=0.89, F=0.57, T=33.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_oth_comp_fair_value_a, 22)`: S=0.55, F=0.49, T=15.4%, INFERIOR (TOP3000)
- `ts_mean(fn_oth_comp_fair_value_a, 10)`: S=-0.22, F=-0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_oth_comp_fair_value_a, 22))`: S=-0.61, F=-0.42, T=14.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_comp_fair_value_a)`: S=-0.01, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_comp_fair_value_a / close)`: S=-0.29, F=-0.15, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.28, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.08 (negative), ret=-0.6%
  - 2020: S=0.95 (moderate), ret=+13.5%
  - 2021: S=0.74 (moderate), ret=+5.2%
  - 2022: S=-0.67 (negative), ret=-9.0%
  - 2023: S=0.59 (moderate), ret=+6.6%

## Risk & Drawdown
- Max drawdown: 19.35% over 960 days (not yet recovered, ongoing at window end)
- Annualized: return +3.2%, volatility 11.3% (fraction of booksize)
- Hit rate: 46.0% positive days
- Tail shape: skew +1.05, excess kurtosis +5.30

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.66, max 2.06, latest 0.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +7.38%; worst month: -5.34%
Positive months: 48%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.02
- Sideways: S=-0.90
- Bear: S=1.59

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_oth_comp_fair_value_a, 5))` S=0.89, F=0.57, INFERIOR
Direction gap: +0.34 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_oth_comp_fair_value_a)`: S=-0.01, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_comp_fair_value_a / close)`: S=-0.29, F=-0.15, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_comp_fair_value_a, 5))`: S=0.89, F=0.57, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_oth_comp_fair_value_a / close)` | TOP3000 | 0.28 | 0.15 | 19.4% | 60% | mixed |
| `rank(fn_oth_comp_fair_value_a / close)` | TOP1000 | 0.18 | 0.07 | 17.1% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a: 0.978 (strongly positively correlated)
- fn_oth_comp_forfeitures_fair_value_a: 0.961 (strongly positively correlated)
- fnd6_optprcgr: 0.922 (strongly positively correlated)
- fn_comp_options_out_weighted_avg_a: 0.879 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.875 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
