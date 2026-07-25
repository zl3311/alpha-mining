---
field: news_all_vwap
dataset: news12
best_template: rank_neg_delta
best_sharpe: 1.24
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4121
ann_vol: 0.1355
hit_rate: 0.5352
rolling_sharpe_min: -2.663
rolling_sharpe_max: 2.631
negated_best_sharpe: 1.24
negated_best_template: rank_neg_delta
negated_best_fitness: 0.4
n_negated_sims: 4
direction_gap: 0.15
---
# news_all_vwap (news12)

*VWAP across all sessions (pre, main, post)*

## Signal Profile
- `rank(news_all_vwap)`: S=0.30, F=0.07, T=70.1%, INFERIOR (TOP3000)
- `rank(news_all_vwap / close)`: S=1.09, F=0.27, T=114.9%, INFERIOR (TOP3000)
- `rank(ts_delta(news_all_vwap, 5))`: S=-0.62, F=-0.17, T=86.2%, INFERIOR (TOP500)
- `-rank(news_all_vwap)`: S=-0.13, F=-0.02, T=59.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_all_vwap, 5))`: S=1.24, F=0.40, T=105.9%, INFERIOR (TOP3000)
- `-ts_zscore(news_all_vwap, 63)`: S=0.64, F=0.22, T=64.9%, INFERIOR (TOP3000)
- `ts_mean(news_all_vwap, 10)`: S=-0.03, F=0.00, T=5.4%, INFERIOR (TOP3000)
- `rank(ts_rank(news_all_vwap, 22))`: S=-0.80, F=-0.26, T=75.2%, INFERIOR (TOP3000)
- `rank(-1 * news_all_vwap)`: S=-0.30, F=-0.07, T=70.1%, INFERIOR (TOP3000)
- `rank(-1 * news_all_vwap / close)`: S=-0.82, F=-0.16, T=124.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 13F/8P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.29, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.67 (strong), ret=+12.7%
  - 2020: S=-1.69 (negative), ret=-21.3%
  - 2021: S=1.21 (moderate), ret=+17.1%
  - 2022: S=0.77 (moderate), ret=+12.8%
  - 2023: S=-0.16 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 41.21% over 768 days (recovered)
- Annualized: return +3.9%, volatility 13.6% (fraction of booksize)
- Hit rate: 53.5% positive days
- Tail shape: skew -0.30, excess kurtosis +0.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.66, max 2.63, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +8.83%; worst month: -10.56%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.91
- Sideways: S=0.91
- Bear: S=-2.21

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_all_vwap, 5))` S=1.24, F=0.40, INFERIOR
Direction gap: +0.15 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_all_vwap)`: S=-0.30, F=-0.07, T=70.1%, INFERIOR (TOP3000)
- `rank(-1 * news_all_vwap / close)`: S=-0.82, F=-0.16, T=124.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_all_vwap, 5))`: S=1.24, F=0.40, T=105.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_all_vwap)` | TOP3000 | 0.29 | 0.07 | 41.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_post_vwap: 1.000 (strongly positively correlated)
- news_pre_vwap: 0.992 (strongly positively correlated)
- news_eod_close: 0.991 (strongly positively correlated)
- news_ton_high: 0.991 (strongly positively correlated)
- news_ton_low: 0.991 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
