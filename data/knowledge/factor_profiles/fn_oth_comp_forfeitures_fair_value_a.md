---
field: fn_oth_comp_forfeitures_fair_value_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.95
best_fitness: 1.09
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.1507
ann_vol: 0.1065
hit_rate: 0.4632
rolling_sharpe_min: -1.48
rolling_sharpe_max: 2.605
negated_best_sharpe: 0.99
negated_best_template: rank_neg_delta
negated_best_fitness: 0.72
n_negated_sims: 10
direction_gap: 0.04
---
# fn_oth_comp_forfeitures_fair_value_a (fundamental2)

*Annual Share Based Compensation Equity Instruments Other Than Options Forfeitures Weighted Average Grant Date Fair Value*

## Signal Profile
- `rank(fn_oth_comp_forfeitures_fair_value_a)`: S=0.08, F=0.02, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_oth_comp_forfeitures_fair_value_a / close)`: S=0.49, F=0.31, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_oth_comp_forfeitures_fair_value_a, 5))`: S=-0.42, F=-0.21, T=31.2%, INFERIOR (TOP500)
- `-rank(fn_oth_comp_forfeitures_fair_value_a)`: S=0.06, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_comp_forfeitures_fair_value_a, 5))`: S=0.99, F=0.72, T=33.6%, INFERIOR (TOP3000)
- `-ts_zscore(fn_oth_comp_forfeitures_fair_value_a, 63)`: S=0.95, F=1.09, T=17.0%, AVERAGE (TOP3000)
- `ts_mean(fn_oth_comp_forfeitures_fair_value_a, 10)`: S=-0.55, F=-0.55, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_oth_comp_forfeitures_fair_value_a, 22))`: S=-0.48, F=-0.31, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_comp_forfeitures_fair_value_a)`: S=0.06, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_comp_forfeitures_fair_value_a / close)`: S=-0.29, F=-0.14, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.48, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.20 (negative), ret=-1.4%
  - 2020: S=1.01 (moderate), ret=+13.4%
  - 2021: S=1.05 (moderate), ret=+8.1%
  - 2022: S=-0.28 (negative), ret=-3.2%
  - 2023: S=0.72 (moderate), ret=+8.2%

## Risk & Drawdown
- Max drawdown: 15.07% over 960 days (not yet recovered, ongoing at window end)
- Annualized: return +5.1%, volatility 10.7% (fraction of booksize)
- Hit rate: 46.3% positive days
- Tail shape: skew +1.00, excess kurtosis +4.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.48, max 2.60, latest 0.90

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +8.78%; worst month: -4.12%
Positive months: 51%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.54
- Sideways: S=-0.88
- Bear: S=1.58

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_oth_comp_forfeitures_fair_value_a, 5))` S=0.99, F=0.72, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_oth_comp_forfeitures_fair_value_a)`: S=0.06, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_comp_forfeitures_fair_value_a / close)`: S=-0.29, F=-0.14, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_comp_forfeitures_fair_value_a, 5))`: S=0.99, F=0.72, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_oth_comp_forfeitures_fair_value_a / close)` | TOP3000 | 0.48 | 0.31 | 15.1% | 60% | all-weather |
| `rank(fn_oth_comp_forfeitures_fair_value_a / close)` | TOP1000 | 0.28 | 0.14 | 18.1% | 60% | all-weather |
| `rank(fn_oth_comp_forfeitures_fair_value_a / close)` | TOP500 | 0.08 | 0.02 | 20.9% | 60% | mixed |
| `rank(fn_oth_comp_forfeitures_fair_value_a)` | TOP3000 | 0.08 | 0.02 | 27.8% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a: 0.974 (strongly positively correlated)
- fn_oth_comp_fair_value_a: 0.961 (strongly positively correlated)
- fn_comp_options_out_weighted_avg_a: 0.916 (strongly positively correlated)
- fnd6_optprcgr: 0.895 (strongly positively correlated)
- fnd6_optprcey: 0.893 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
