---
field: news_tot_ticks
dataset: news12
cluster: news12_news
coverage: 0.9691
community_alphas: 2162
best_template: neg_rank_value_norm
best_sharpe: 0.48
best_fitness: 0.1
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 22
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1563
ann_vol: 0.0744
hit_rate: 0.4939
rolling_sharpe_min: -1.823
rolling_sharpe_max: 2.876
negated_best_sharpe: 0.48
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.1
n_negated_sims: 4
direction_gap: 0.05
---
# news_tot_ticks (news12)

*Total number of ticks during the trading day*

## Signal Profile
- `rank(news_tot_ticks)`: S=0.13, F=0.02, T=61.0%, INFERIOR (TOP200)
- `rank(ts_delta(news_tot_ticks, 5))`: S=0.43, F=0.07, T=118.2%, INFERIOR (TOP500)
- `-rank(news_tot_ticks)`: S=0.17, F=0.02, T=89.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_tot_ticks, 5))`: S=-0.03, F=0.00, T=136.6%, INFERIOR (TOP3000)
- `ts_zscore(news_tot_ticks, 22)`: S=0.32, F=0.04, T=114.8%, INFERIOR (TOP3000)
- `ts_mean(news_tot_ticks, 10)`: S=0.02, F=0.00, T=10.4%, INFERIOR (TOP3000)
- `rank(ts_rank(news_tot_ticks, 22))`: S=0.25, F=0.03, T=116.1%, INFERIOR (TOP3000)
- `rank(-1 * news_tot_ticks)`: S=0.43, F=0.07, T=102.4%, INFERIOR (TOP3000)
- `rank(-1 * news_tot_ticks / close)`: S=0.48, F=0.10, T=101.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 22F/0P
- HIGH_TURNOVER: 20F/2P
- LOW_FITNESS: 22F/0P
- LOW_SHARPE: 22F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.42, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.26 (moderate), ret=+7.0%
  - 2020: S=-1.12 (negative), ret=-8.0%
  - 2021: S=0.73 (moderate), ret=+5.7%
  - 2022: S=2.20 (strong), ret=+20.4%
  - 2023: S=-1.65 (negative), ret=-9.8%

## Risk & Drawdown
- Max drawdown: 15.63% over 946 days (recovered)
- Annualized: return +3.1%, volatility 7.4% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.69, excess kurtosis +5.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.82, max 2.88, latest -1.70

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +6.23%; worst month: -3.86%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.57
- Sideways: S=0.48
- Bear: S=-1.05

## Negated Direction
Best negated: `rank(-1 * news_tot_ticks / close)` S=0.48, F=0.10, INFERIOR
Direction gap: +0.05 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_tot_ticks)`: S=0.43, F=0.07, T=102.4%, INFERIOR (TOP3000)
- `rank(-1 * news_tot_ticks / close)`: S=0.48, F=0.10, T=101.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_tot_ticks, 5))`: S=-0.03, F=0.00, T=136.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_tot_ticks, 5))` | TOP500 | 0.42 | 0.07 | 15.6% | 60% | bull-only |
| `rank(ts_delta(news_tot_ticks, 5))` | TOP1000 | 0.30 | 0.04 | 15.8% | 60% | mixed |
| `rank(news_tot_ticks)` | TOP200 | 0.13 | 0.02 | 21.4% | 60% | mixed |
| `rank(ts_delta(news_tot_ticks, 5))` | TOP200 | 0.14 | 0.02 | 28.8% | 60% | mixed |

## Correlation Notes
Top correlates:
- news_vol_stddev: 0.530 (moderately positively correlated)
- news_ratio_vol: 0.459 (moderately positively correlated)
- news_session_range: 0.424 (moderately positively correlated)
- news_range_stddev: 0.424 (moderately positively correlated)
- news_atr_ratio: 0.390 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
