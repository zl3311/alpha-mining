---
field: news_eod_vwap
dataset: news12
best_template: rank_neg_delta
best_sharpe: 1.33
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4653
ann_vol: 0.141
hit_rate: 0.532
rolling_sharpe_min: -2.92
rolling_sharpe_max: 2.388
negated_best_sharpe: 1.33
negated_best_template: rank_neg_delta
negated_best_fitness: 0.44
n_negated_sims: 4
direction_gap: 0.71
---
# news_eod_vwap (news12)

*VWAP from the time of news to the end of the session*

## Signal Profile
- `rank(news_eod_vwap)`: S=0.18, F=0.03, T=81.2%, INFERIOR (TOP3000)
- `rank(news_eod_vwap / close)`: S=0.64, F=0.12, T=118.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_eod_vwap, 5))`: S=-0.75, F=-0.22, T=91.0%, INFERIOR (TOP500)
- `-rank(news_eod_vwap)`: S=0.03, F=0.00, T=66.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_eod_vwap, 5))`: S=1.33, F=0.44, T=115.4%, INFERIOR (TOP3000)
- `-ts_zscore(news_eod_vwap, 63)`: S=0.62, F=0.20, T=71.1%, INFERIOR (TOP3000)
- `ts_mean(news_eod_vwap, 10)`: S=-0.01, F=0.00, T=5.2%, INFERIOR (TOP3000)
- `rank(ts_rank(news_eod_vwap, 22))`: S=-0.72, F=-0.21, T=82.1%, INFERIOR (TOP3000)
- `rank(-1 * news_eod_vwap)`: S=-0.18, F=-0.03, T=81.2%, INFERIOR (TOP3000)
- `rank(-1 * news_eod_vwap / close)`: S=-0.92, F=-0.18, T=131.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 14F/7P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.17, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.16 (moderate), ret=+9.9%
  - 2020: S=-1.63 (negative), ret=-21.1%
  - 2021: S=0.80 (moderate), ret=+11.9%
  - 2022: S=0.74 (moderate), ret=+12.9%
  - 2023: S=-0.12 (negative), ret=-1.7%

## Risk & Drawdown
- Max drawdown: 46.53% over 998 days (recovered)
- Annualized: return +2.4%, volatility 14.1% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.32, excess kurtosis +0.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.92, max 2.39, latest -0.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +9.12%; worst month: -11.17%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.68
- Sideways: S=0.93
- Bear: S=-2.32

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_eod_vwap, 5))` S=1.33, F=0.44, INFERIOR
Direction gap: +0.71 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * news_eod_vwap)`: S=-0.18, F=-0.03, T=81.2%, INFERIOR (TOP3000)
- `rank(-1 * news_eod_vwap / close)`: S=-0.92, F=-0.18, T=131.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_eod_vwap, 5))`: S=1.33, F=0.44, T=115.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_eod_vwap)` | TOP3000 | 0.17 | 0.03 | 46.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_eod_low: 0.999 (strongly positively correlated)
- news_eod_high: 0.999 (strongly positively correlated)
- news_eod_close: 0.998 (strongly positively correlated)
- news_ton_low: 0.998 (strongly positively correlated)
- news_open: 0.998 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
