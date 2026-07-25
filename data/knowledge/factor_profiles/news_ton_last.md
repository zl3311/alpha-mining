---
field: news_ton_last
dataset: news12
best_template: rank_neg_delta
best_sharpe: 1.2
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4617
ann_vol: 0.1366
hit_rate: 0.5377
rolling_sharpe_min: -2.95
rolling_sharpe_max: 2.441
negated_best_sharpe: 1.2
negated_best_template: rank_neg_delta
negated_best_fitness: 0.37
n_negated_sims: 4
direction_gap: 0.14
---
# news_ton_last (news12)

*Price at the time of the news*

## Signal Profile
- `rank(news_ton_last)`: S=0.17, F=0.03, T=70.2%, INFERIOR (TOP3000)
- `rank(news_ton_last / close)`: S=1.06, F=0.26, T=111.2%, INFERIOR (TOP3000)
- `rank(ts_delta(news_ton_last, 5))`: S=-0.56, F=-0.14, T=88.1%, INFERIOR (TOP500)
- `-rank(news_ton_last)`: S=-0.05, F=0.00, T=60.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_ton_last, 5))`: S=1.20, F=0.37, T=107.4%, INFERIOR (TOP3000)
- `-ts_zscore(news_ton_last, 63)`: S=0.58, F=0.19, T=65.6%, INFERIOR (TOP3000)
- `ts_mean(news_ton_last, 10)`: S=-0.02, F=0.00, T=5.0%, INFERIOR (TOP3000)
- `rank(ts_rank(news_ton_last, 22))`: S=-0.62, F=-0.17, T=76.2%, INFERIOR (TOP3000)
- `rank(-1 * news_ton_last)`: S=-0.17, F=-0.03, T=70.2%, INFERIOR (TOP3000)
- `rank(-1 * news_ton_last / close)`: S=-0.23, F=-0.02, T=120.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 13F/8P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.16, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.12 (moderate), ret=+9.1%
  - 2020: S=-1.70 (negative), ret=-21.3%
  - 2021: S=0.86 (moderate), ret=+12.5%
  - 2022: S=0.76 (moderate), ret=+12.8%
  - 2023: S=-0.19 (negative), ret=-2.5%

## Risk & Drawdown
- Max drawdown: 46.17% over 1218 days (recovered)
- Annualized: return +2.1%, volatility 13.7% (fraction of booksize)
- Hit rate: 53.8% positive days
- Tail shape: skew -0.31, excess kurtosis +0.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.95, max 2.44, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +8.91%; worst month: -10.45%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.74
- Sideways: S=0.91
- Bear: S=-2.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_ton_last, 5))` S=1.20, F=0.37, INFERIOR
Direction gap: +0.14 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_ton_last)`: S=-0.17, F=-0.03, T=70.2%, INFERIOR (TOP3000)
- `rank(-1 * news_ton_last / close)`: S=-0.23, F=-0.02, T=120.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_ton_last, 5))`: S=1.20, F=0.37, T=107.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_ton_last)` | TOP3000 | 0.16 | 0.03 | 46.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_ton_low: 1.000 (strongly positively correlated)
- news_eod_close: 1.000 (strongly positively correlated)
- news_open: 1.000 (strongly positively correlated)
- news_ton_high: 1.000 (strongly positively correlated)
- news_eod_high: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
