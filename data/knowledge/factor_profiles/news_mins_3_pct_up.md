---
field: news_mins_3_pct_up
dataset: news12
best_template: rank_delta
best_sharpe: 0.43
best_fitness: 0.16
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.5267
ann_vol: 0.4357
hit_rate: 0.4097
rolling_sharpe_min: -0.909
rolling_sharpe_max: 1.934
negated_best_sharpe: 0.42
negated_best_template: neg_rank
negated_best_fitness: 0.09
n_negated_sims: 4
direction_gap: -0.01
---
# news_mins_3_pct_up (news12)

*Number of minutes before the price increased by at least 3 percent after the news release*

## Signal Profile
- `rank(news_mins_3_pct_up)`: S=0.28, F=0.05, T=155.9%, INFERIOR (TOP500)
- `rank(ts_delta(news_mins_3_pct_up, 5))`: S=0.43, F=0.16, T=137.7%, INFERIOR (TOP500)
- `-rank(news_mins_3_pct_up)`: S=0.42, F=0.09, T=155.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_3_pct_up, 5))`: S=-0.31, F=-0.08, T=173.9%, INFERIOR (TOP3000)
- `-ts_zscore(news_mins_3_pct_up, 63)`: S=0.53, F=0.12, T=157.7%, INFERIOR (TOP3000)
- `ts_mean(news_mins_3_pct_up, 10)`: S=-0.08, F=-0.01, T=32.5%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_3_pct_up, 22))`: S=0.10, F=0.01, T=158.9%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_3_pct_up)`: S=0.08, F=0.01, T=152.7%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_3_pct_up / close)`: S=-0.07, F=-0.01, T=146.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.43, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.31 (weak), ret=+7.8%
  - 2020: S=1.66 (strong), ret=+75.1%
  - 2021: S=0.27 (weak), ret=+17.4%
  - 2022: S=0.09 (weak), ret=+2.9%
  - 2023: S=-0.32 (negative), ret=-11.7%

## Risk & Drawdown
- Max drawdown: 52.67% over 287 days (recovered)
- Annualized: return +18.7%, volatility 43.6% (fraction of booksize)
- Hit rate: 41.0% positive days
- Tail shape: skew +2.29, excess kurtosis +20.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.91, max 1.93, latest -0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +60.22%; worst month: -33.02%
Positive months: 44%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.81
- Sideways: S=-0.42
- Bear: S=-0.50

## Negated Direction
Best negated: `-rank(news_mins_3_pct_up)` S=0.42, F=0.09, INFERIOR
Direction gap: -0.01 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_mins_3_pct_up)`: S=0.08, F=0.01, T=152.7%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_3_pct_up / close)`: S=-0.07, F=-0.01, T=146.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_3_pct_up, 5))`: S=-0.31, F=-0.08, T=173.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_mins_3_pct_up, 5))` | TOP500 | 0.43 | 0.16 | 52.7% | 80% | mixed |
| `rank(ts_delta(news_mins_3_pct_up, 5))` | TOP200 | 0.37 | 0.13 | 71.3% | 40% | mixed |
| `rank(ts_delta(news_mins_3_pct_up, 5))` | TOP1000 | 0.38 | 0.13 | 67.3% | 60% | all-weather |
| `rank(ts_delta(news_mins_3_pct_up, 5))` | TOP3000 | 0.33 | 0.08 | 76.8% | 40% | mixed |
| `rank(news_mins_3_pct_up)` | TOP500 | 0.30 | 0.05 | 40.3% | 60% | bear-only |

## Correlation Notes
Top correlates:
- news_mins_4_pct_up: 0.165 (weakly positively correlated)
- news_mins_10_chg: 0.111 (weakly positively correlated)
- news_vol_stddev: -0.093 (weakly negatively correlated)
- fnd6_cptnewqv1300_nopiq: -0.092 (weakly negatively correlated)
- rp_ess_price: -0.080 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
