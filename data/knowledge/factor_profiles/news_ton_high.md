---
field: news_ton_high
dataset: news12
best_template: rank_neg_delta
best_sharpe: 1.16
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4644
ann_vol: 0.1362
hit_rate: 0.5385
rolling_sharpe_min: -2.962
rolling_sharpe_max: 2.459
negated_best_sharpe: 1.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.35
n_negated_sims: 4
direction_gap: 0.3
---
# news_ton_high (news12)

*Highest price reached during the session before the time of news*

## Signal Profile
- `rank(news_ton_high)`: S=0.16, F=0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(news_ton_high / close)`: S=0.86, F=0.24, T=103.5%, INFERIOR (TOP3000)
- `rank(ts_delta(news_ton_high, 5))`: S=-0.44, F=-0.10, T=89.4%, INFERIOR (TOP500)
- `-rank(news_ton_high)`: S=-0.05, F=-0.01, T=60.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_ton_high, 5))`: S=1.16, F=0.35, T=108.4%, INFERIOR (TOP3000)
- `-ts_zscore(news_ton_high, 63)`: S=0.55, F=0.17, T=66.1%, INFERIOR (TOP3000)
- `ts_mean(news_ton_high, 10)`: S=-0.02, F=0.00, T=5.0%, INFERIOR (TOP3000)
- `rank(ts_rank(news_ton_high, 22))`: S=-0.72, F=-0.21, T=76.8%, INFERIOR (TOP3000)
- `rank(-1 * news_ton_high)`: S=-0.16, F=-0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(-1 * news_ton_high / close)`: S=-0.11, F=-0.01, T=114.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 13F/8P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.16, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.10 (moderate), ret=+9.0%
  - 2020: S=-1.71 (negative), ret=-21.5%
  - 2021: S=0.86 (moderate), ret=+12.5%
  - 2022: S=0.76 (moderate), ret=+12.7%
  - 2023: S=-0.17 (negative), ret=-2.3%

## Risk & Drawdown
- Max drawdown: 46.44% over 1218 days (recovered)
- Annualized: return +2.1%, volatility 13.6% (fraction of booksize)
- Hit rate: 53.8% positive days
- Tail shape: skew -0.31, excess kurtosis +0.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.96, max 2.46, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +8.86%; worst month: -10.46%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.74
- Sideways: S=0.92
- Bear: S=-2.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_ton_high, 5))` S=1.16, F=0.35, INFERIOR
Direction gap: +0.30 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_ton_high)`: S=-0.16, F=-0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(-1 * news_ton_high / close)`: S=-0.11, F=-0.01, T=114.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_ton_high, 5))`: S=1.16, F=0.35, T=108.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_ton_high)` | TOP3000 | 0.16 | 0.03 | 46.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_open: 1.000 (strongly positively correlated)
- news_eod_close: 1.000 (strongly positively correlated)
- news_ton_last: 1.000 (strongly positively correlated)
- news_ton_low: 1.000 (strongly positively correlated)
- news_eod_high: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
