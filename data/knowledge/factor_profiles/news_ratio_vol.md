---
field: news_ratio_vol
dataset: news12
best_template: rank_level
best_sharpe: 0.37
best_fitness: 0.07
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 3
max_drawdown: 0.1145
ann_vol: 0.0632
hit_rate: 0.5053
rolling_sharpe_min: -1.035
rolling_sharpe_max: 2.118
negated_best_sharpe: 0.43
negated_best_template: neg_rank_level
negated_best_fitness: 0.06
n_negated_sims: 4
direction_gap: 0.06
---
# news_ratio_vol (news12)

*Ratio of current session volume to 30-day moving average volume*

## Signal Profile
- `rank(news_ratio_vol)`: S=0.37, F=0.07, T=87.0%, INFERIOR (TOP200)
- `rank(news_ratio_vol / close)`: S=-0.13, F=-0.02, T=87.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_ratio_vol, 5))`: S=0.29, F=0.03, T=122.6%, INFERIOR (TOP1000)
- `-rank(news_ratio_vol)`: S=0.13, F=0.01, T=104.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_ratio_vol, 5))`: S=-0.13, F=-0.01, T=134.1%, INFERIOR (TOP3000)
- `ts_zscore(news_ratio_vol, 22)`: S=0.27, F=0.03, T=106.0%, INFERIOR (TOP3000)
- `ts_mean(news_ratio_vol, 10)`: S=0.24, F=0.07, T=25.2%, INFERIOR (TOP3000)
- `rank(ts_rank(news_ratio_vol, 22))`: S=-0.42, F=-0.06, T=108.7%, INFERIOR (TOP3000)
- `rank(-1 * news_ratio_vol)`: S=0.43, F=0.06, T=115.4%, INFERIOR (TOP3000)
- `rank(-1 * news_ratio_vol / close)`: S=0.29, F=0.05, T=103.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.42, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.01 (weak), ret=+0.0%
  - 2020: S=1.01 (moderate), ret=+5.2%
  - 2021: S=-0.44 (negative), ret=-3.3%
  - 2022: S=0.73 (moderate), ret=+5.8%
  - 2023: S=1.02 (moderate), ret=+5.3%

## Risk & Drawdown
- Max drawdown: 11.45% over 553 days (recovered)
- Annualized: return +2.7%, volatility 6.3% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.86, excess kurtosis +7.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.03, max 2.12, latest 0.98

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +4.65%; worst month: -3.66%
Positive months: 44%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.97
- Sideways: S=-1.10
- Bear: S=1.13

## Negated Direction
Best negated: `rank(-1 * news_ratio_vol)` S=0.43, F=0.06, INFERIOR
Direction gap: +0.06 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_ratio_vol)`: S=0.43, F=0.06, T=115.4%, INFERIOR (TOP3000)
- `rank(-1 * news_ratio_vol / close)`: S=0.29, F=0.05, T=103.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_ratio_vol, 5))`: S=-0.13, F=-0.01, T=134.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_ratio_vol)` | TOP200 | 0.36 | 0.07 | 13.5% | 60% | mixed |
| `rank(news_ratio_vol)` | TOP500 | 0.42 | 0.07 | 11.5% | 80% | all-weather |
| `rank(ts_delta(news_ratio_vol, 5))` | TOP1000 | 0.28 | 0.03 | 9.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- news_tot_ticks: 0.459 (moderately positively correlated)
- news_curr_vol: 0.375 (weakly positively correlated)
- parkinson_volatility_150: 0.373 (weakly positively correlated)
- historical_volatility_150: 0.372 (weakly positively correlated)
- news_open_vol: 0.371 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
