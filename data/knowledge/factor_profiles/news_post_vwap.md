---
field: news_post_vwap
dataset: news12
best_template: rank_value_norm
best_sharpe: 1.54
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4087
ann_vol: 0.1357
hit_rate: 0.5336
rolling_sharpe_min: -2.627
rolling_sharpe_max: 2.492
negated_best_sharpe: 1.14
negated_best_template: rank_neg_delta
negated_best_fitness: 0.35
n_negated_sims: 4
direction_gap: -0.4
---
# news_post_vwap (news12)

*Post-session volume-weighted average price*

## Signal Profile
- `rank(news_post_vwap)`: S=0.30, F=0.07, T=70.3%, INFERIOR (TOP3000)
- `rank(news_post_vwap / close)`: S=1.54, F=0.49, T=115.2%, INFERIOR (TOP3000)
- `rank(ts_delta(news_post_vwap, 5))`: S=-0.48, F=-0.11, T=86.9%, INFERIOR (TOP500)
- `-rank(news_post_vwap)`: S=-0.13, F=-0.02, T=60.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_post_vwap, 5))`: S=1.14, F=0.35, T=106.2%, INFERIOR (TOP3000)
- `-ts_zscore(news_post_vwap, 63)`: S=0.59, F=0.19, T=65.4%, INFERIOR (TOP3000)
- `ts_mean(news_post_vwap, 10)`: S=-0.11, F=-0.03, T=6.6%, INFERIOR (TOP3000)
- `rank(ts_rank(news_post_vwap, 22))`: S=-0.70, F=-0.21, T=75.9%, INFERIOR (TOP3000)
- `rank(-1 * news_post_vwap)`: S=-0.30, F=-0.07, T=70.3%, INFERIOR (TOP3000)
- `rank(-1 * news_post_vwap / close)`: S=-0.86, F=-0.19, T=124.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 13F/8P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.29, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.53 (strong), ret=+11.7%
  - 2020: S=-1.66 (negative), ret=-21.0%
  - 2021: S=1.23 (moderate), ret=+17.4%
  - 2022: S=0.77 (moderate), ret=+13.0%
  - 2023: S=-0.14 (negative), ret=-1.9%

## Risk & Drawdown
- Max drawdown: 40.87% over 767 days (recovered)
- Annualized: return +3.9%, volatility 13.6% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.30, excess kurtosis +0.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.63, max 2.49, latest -0.32

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +8.65%; worst month: -10.57%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.93
- Sideways: S=0.86
- Bear: S=-2.18

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_post_vwap, 5))` S=1.14, F=0.35, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_post_vwap)`: S=-0.30, F=-0.07, T=70.3%, INFERIOR (TOP3000)
- `rank(-1 * news_post_vwap / close)`: S=-0.86, F=-0.19, T=124.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_post_vwap, 5))`: S=1.14, F=0.35, T=106.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_post_vwap)` | TOP3000 | 0.29 | 0.07 | 40.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_all_vwap: 1.000 (strongly positively correlated)
- news_pre_vwap: 0.992 (strongly positively correlated)
- news_ton_high: 0.991 (strongly positively correlated)
- news_eod_close: 0.991 (strongly positively correlated)
- news_ton_low: 0.991 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
