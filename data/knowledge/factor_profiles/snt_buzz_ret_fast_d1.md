---
field: snt_buzz_ret_fast_d1
dataset: socialmedia12
best_template: ts_zscore
best_sharpe: 0.63
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.1089
ann_vol: 0.0482
hit_rate: 0.5126
rolling_sharpe_min: -1.717
rolling_sharpe_max: 3.143
negated_best_sharpe: 0.54
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.09
---
# snt_buzz_ret_fast_d1 (socialmedia12)

*negative return of relative sentiment volume*

## Signal Profile
- `rank(snt_buzz_ret_fast_d1)`: S=0.28, F=0.04, T=40.1%, INFERIOR (TOP3000)
- `rank(ts_delta(snt_buzz_ret_fast_d1, 5))`: S=0.33, F=0.06, T=52.6%, INFERIOR (TOP500)
- `-rank(snt_buzz_ret_fast_d1)`: S=0.09, F=0.01, T=44.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_buzz_ret_fast_d1, 5))`: S=0.54, F=0.08, T=58.6%, INFERIOR (TOP3000)
- `-ts_zscore(snt_buzz_ret_fast_d1, 63)`: S=0.63, F=0.16, T=47.9%, INFERIOR (TOP3000)
- `ts_mean(snt_buzz_ret_fast_d1, 10)`: S=0.19, F=0.08, T=18.8%, INFERIOR (TOP3000)
- `rank(ts_rank(snt_buzz_ret_fast_d1, 22))`: S=-0.63, F=-0.14, T=47.2%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_ret_fast_d1)`: S=-0.28, F=-0.04, T=40.1%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_ret_fast_d1 / close)`: S=-0.08, F=-0.01, T=39.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/25P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/19P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.33, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.04 (negative), ret=-0.1%
  - 2020: S=1.76 (strong), ret=+7.7%
  - 2021: S=1.33 (moderate), ret=+7.4%
  - 2022: S=-1.35 (negative), ret=-8.1%
  - 2023: S=0.22 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 10.89% over 686 days (not yet recovered, ongoing at window end)
- Annualized: return +1.6%, volatility 4.8% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.75, excess kurtosis +6.30

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.72, max 3.14, latest 0.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +2.90%; worst month: -3.79%
Positive months: 59%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.07
- Sideways: S=1.14
- Bear: S=0.08

## Negated Direction
Best negated: `rank(-1 * ts_delta(snt_buzz_ret_fast_d1, 5))` S=0.54, F=0.08, INFERIOR
Direction gap: -0.09 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * snt_buzz_ret_fast_d1)`: S=-0.28, F=-0.04, T=40.1%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_ret_fast_d1 / close)`: S=-0.08, F=-0.01, T=39.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_buzz_ret_fast_d1, 5))`: S=0.54, F=0.08, T=58.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(snt_buzz_ret_fast_d1, 5))` | TOP500 | 0.33 | 0.06 | 10.9% | 60% | weak |
| `rank(snt_buzz_ret_fast_d1)` | TOP3000 | 0.28 | 0.04 | 7.8% | 40% | mixed |

## Correlation Notes
Top correlates:
- scl12_buzz_fast_d1: -0.212 (weakly negatively correlated)
- implied_volatility_mean_1080: -0.197 (weakly negatively correlated)
- snt_buzz: 0.196 (weakly positively correlated)
- implied_volatility_mean_720: -0.196 (weakly negatively correlated)
- implied_volatility_call_60: -0.195 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
