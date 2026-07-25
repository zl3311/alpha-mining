---
field: snt_buzz_bfl_fast_d1
dataset: socialmedia12
best_template: ts_mean
best_sharpe: 0.37
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.092
ann_vol: 0.0447
hit_rate: 0.5061
rolling_sharpe_min: -1.938
rolling_sharpe_max: 1.852
negated_best_sharpe: 0.38
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: 0.01
---
# snt_buzz_bfl_fast_d1 (socialmedia12)

*Negative relative sentiment volume measure for current day, with missing values filled as 1*

## Signal Profile
- `rank(snt_buzz_bfl_fast_d1)`: S=0.21, F=0.03, T=45.6%, INFERIOR (TOP1000)
- `rank(ts_delta(snt_buzz_bfl_fast_d1, 5))`: S=0.16, F=0.01, T=70.3%, INFERIOR (TOP3000)
- `-rank(snt_buzz_bfl_fast_d1)`: S=-0.21, F=-0.03, T=45.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_buzz_bfl_fast_d1, 5))`: S=0.19, F=0.03, T=62.3%, INFERIOR (TOP3000)
- `-ts_zscore(snt_buzz_bfl_fast_d1, 63)`: S=0.28, F=0.05, T=54.1%, INFERIOR (TOP3000)
- `ts_mean(snt_buzz_bfl_fast_d1, 10)`: S=0.37, F=0.17, T=20.1%, INFERIOR (TOP3000)
- `rank(ts_rank(snt_buzz_bfl_fast_d1, 22))`: S=0.09, F=0.01, T=60.6%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_bfl_fast_d1)`: S=0.52, F=0.14, T=55.5%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_bfl_fast_d1 / close)`: S=0.38, F=0.16, T=24.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/25P
- HIGH_TURNOVER: 1F/25P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.21, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.64 (moderate), ret=+1.8%
  - 2020: S=1.29 (moderate), ret=+5.0%
  - 2021: S=-0.91 (negative), ret=-5.4%
  - 2022: S=1.52 (strong), ret=+7.0%
  - 2023: S=-0.90 (negative), ret=-3.7%

## Risk & Drawdown
- Max drawdown: 9.20% over 617 days (recovered)
- Annualized: return +0.9%, volatility 4.5% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew -0.62, excess kurtosis +7.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.94, max 1.85, latest -0.84

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +3.71%; worst month: -5.95%
Positive months: 56%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.40
- Sideways: S=0.94
- Bear: S=-0.49

## Negated Direction
Best negated: `rank(-1 * snt_buzz_bfl_fast_d1 / close)` S=0.38, F=0.16, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * snt_buzz_bfl_fast_d1)`: S=0.52, F=0.14, T=55.5%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz_bfl_fast_d1 / close)`: S=0.38, F=0.16, T=24.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_buzz_bfl_fast_d1, 5))`: S=0.19, F=0.03, T=62.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(snt_buzz_bfl_fast_d1)` | TOP1000 | 0.21 | 0.03 | 9.2% | 60% | weak |
| `rank(snt_buzz_bfl_fast_d1)` | TOP3000 | 0.17 | 0.02 | 6.1% | 60% | weak |

## Correlation Notes
Top correlates:
- snt_buzz_bfl: 0.520 (moderately positively correlated)
- news_open_vol: -0.459 (moderately negatively correlated)
- implied_volatility_call_270 - implied_volatility_put_270: 0.431 (moderately positively correlated)
- implied_volatility_mean_skew_1080: 0.379 (weakly positively correlated)
- implied_volatility_mean_skew_720: 0.379 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
