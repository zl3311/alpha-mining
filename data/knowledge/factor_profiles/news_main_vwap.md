---
field: news_main_vwap
dataset: news12
best_template: rank_value_norm
best_sharpe: 1.12
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4373
ann_vol: 0.1376
hit_rate: 0.5279
rolling_sharpe_min: -2.811
rolling_sharpe_max: 2.807
negated_best_sharpe: 0.86
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 4
direction_gap: -0.26
---
# news_main_vwap (news12)

*Main session volume-weighted average price*

## Signal Profile
- `rank(news_main_vwap)`: S=0.30, F=0.06, T=118.7%, INFERIOR (TOP3000)
- `rank(news_main_vwap / close)`: S=1.12, F=0.30, T=143.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_main_vwap, 5))`: S=-0.48, F=-0.12, T=101.5%, INFERIOR (TOP200)
- `-rank(news_main_vwap)`: S=-0.06, F=-0.01, T=102.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_main_vwap, 5))`: S=0.86, F=0.21, T=141.0%, INFERIOR (TOP3000)
- `-ts_zscore(news_main_vwap, 63)`: S=0.58, F=0.15, T=104.9%, INFERIOR (TOP3000)
- `ts_mean(news_main_vwap, 10)`: S=0.00, F=0.00, T=5.9%, INFERIOR (TOP3000)
- `rank(ts_rank(news_main_vwap, 22))`: S=-0.73, F=-0.19, T=115.2%, INFERIOR (TOP3000)
- `rank(-1 * news_main_vwap)`: S=-0.30, F=-0.06, T=118.7%, INFERIOR (TOP3000)
- `rank(-1 * news_main_vwap / close)`: S=-1.39, F=-0.38, T=155.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 19F/2P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.30, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.79 (strong), ret=+13.7%
  - 2020: S=-1.73 (negative), ret=-22.6%
  - 2021: S=1.11 (moderate), ret=+16.2%
  - 2022: S=0.75 (moderate), ret=+12.7%
  - 2023: S=0.01 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 43.73% over 768 days (recovered)
- Annualized: return +4.1%, volatility 13.8% (fraction of booksize)
- Hit rate: 52.8% positive days
- Tail shape: skew -0.34, excess kurtosis +0.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.81, max 2.81, latest -0.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +9.22%; worst month: -12.45%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.85
- Sideways: S=0.86
- Bear: S=-2.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_main_vwap, 5))` S=0.86, F=0.21, INFERIOR
Direction gap: -0.26 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_main_vwap)`: S=-0.30, F=-0.06, T=118.7%, INFERIOR (TOP3000)
- `rank(-1 * news_main_vwap / close)`: S=-1.39, F=-0.38, T=155.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_main_vwap, 5))`: S=0.86, F=0.21, T=141.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_main_vwap)` | TOP3000 | 0.30 | 0.06 | 43.7% | 80% | bull-only |

## Correlation Notes
Top correlates:
- news_all_vwap: 0.984 (strongly positively correlated)
- news_post_vwap: 0.984 (strongly positively correlated)
- news_pre_vwap: 0.982 (strongly positively correlated)
- news_eod_vwap: 0.976 (strongly positively correlated)
- news_eod_low: 0.976 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
