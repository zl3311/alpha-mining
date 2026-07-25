---
field: news_ton_low
dataset: news12
best_template: rank_neg_delta
best_sharpe: 1.23
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4628
ann_vol: 0.1372
hit_rate: 0.5377
rolling_sharpe_min: -2.926
rolling_sharpe_max: 2.446
negated_best_sharpe: 1.23
negated_best_template: rank_neg_delta
negated_best_fitness: 0.38
n_negated_sims: 4
direction_gap: 0.22
---
# news_ton_low (news12)

*Lowest price reached during the session before the time of news*

## Signal Profile
- `rank(news_ton_low)`: S=0.17, F=0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(news_ton_low / close)`: S=1.01, F=0.27, T=104.6%, INFERIOR (TOP3000)
- `rank(ts_delta(news_ton_low, 5))`: S=-0.52, F=-0.12, T=90.0%, INFERIOR (TOP500)
- `-rank(news_ton_low)`: S=-0.05, F=-0.01, T=60.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_ton_low, 5))`: S=1.23, F=0.38, T=108.6%, INFERIOR (TOP3000)
- `-ts_zscore(news_ton_low, 63)`: S=0.62, F=0.20, T=66.3%, INFERIOR (TOP3000)
- `ts_mean(news_ton_low, 10)`: S=-0.02, F=0.00, T=5.0%, INFERIOR (TOP3000)
- `rank(ts_rank(news_ton_low, 22))`: S=-0.69, F=-0.20, T=77.2%, INFERIOR (TOP3000)
- `rank(-1 * news_ton_low)`: S=-0.17, F=-0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(-1 * news_ton_low / close)`: S=-0.97, F=-0.22, T=115.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 13F/8P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.16, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.09 (moderate), ret=+9.0%
  - 2020: S=-1.68 (negative), ret=-21.2%
  - 2021: S=0.88 (moderate), ret=+12.8%
  - 2022: S=0.75 (moderate), ret=+12.6%
  - 2023: S=-0.17 (negative), ret=-2.3%

## Risk & Drawdown
- Max drawdown: 46.28% over 1218 days (recovered)
- Annualized: return +2.2%, volatility 13.7% (fraction of booksize)
- Hit rate: 53.8% positive days
- Tail shape: skew -0.31, excess kurtosis +0.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.93, max 2.45, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +9.02%; worst month: -10.55%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.74
- Sideways: S=0.92
- Bear: S=-2.41

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_ton_low, 5))` S=1.23, F=0.38, INFERIOR
Direction gap: +0.22 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_ton_low)`: S=-0.17, F=-0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(-1 * news_ton_low / close)`: S=-0.97, F=-0.22, T=115.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_ton_low, 5))`: S=1.23, F=0.38, T=108.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_ton_low)` | TOP3000 | 0.16 | 0.03 | 46.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_open: 1.000 (strongly positively correlated)
- news_eod_close: 1.000 (strongly positively correlated)
- news_ton_last: 1.000 (strongly positively correlated)
- news_ton_high: 1.000 (strongly positively correlated)
- news_eod_low: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
