---
field: news_eod_close
dataset: news12
best_template: rank_neg_delta
best_sharpe: 1.36
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4626
ann_vol: 0.1369
hit_rate: 0.5368
rolling_sharpe_min: -2.939
rolling_sharpe_max: 2.422
negated_best_sharpe: 1.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.46
n_negated_sims: 4
direction_gap: 0.77
---
# news_eod_close (news12)

*Session closing price*

## Signal Profile
- `rank(news_eod_close)`: S=0.16, F=0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(news_eod_close / close)`: S=0.48, F=0.08, T=114.0%, INFERIOR (TOP3000)
- `rank(ts_delta(news_eod_close, 5))`: S=-0.56, F=-0.17, T=74.8%, INFERIOR (TOP200)
- `-rank(news_eod_close)`: S=-0.04, F=0.00, T=60.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_eod_close, 5))`: S=1.36, F=0.46, T=108.2%, INFERIOR (TOP3000)
- `-ts_zscore(news_eod_close, 63)`: S=0.59, F=0.19, T=65.5%, INFERIOR (TOP3000)
- `ts_mean(news_eod_close, 10)`: S=-0.02, F=0.00, T=5.0%, INFERIOR (TOP3000)
- `rank(ts_rank(news_eod_close, 22))`: S=-0.75, F=-0.24, T=76.2%, INFERIOR (TOP3000)
- `rank(-1 * news_eod_close)`: S=-0.16, F=-0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(-1 * news_eod_close / close)`: S=-0.66, F=-0.11, T=122.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 13F/8P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.15, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.11 (moderate), ret=+9.1%
  - 2020: S=-1.69 (negative), ret=-21.2%
  - 2021: S=0.85 (moderate), ret=+12.4%
  - 2022: S=0.75 (moderate), ret=+12.6%
  - 2023: S=-0.18 (negative), ret=-2.5%

## Risk & Drawdown
- Max drawdown: 46.26% over 1218 days (recovered)
- Annualized: return +2.1%, volatility 13.7% (fraction of booksize)
- Hit rate: 53.7% positive days
- Tail shape: skew -0.31, excess kurtosis +0.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.94, max 2.42, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +8.93%; worst month: -10.58%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.72
- Sideways: S=0.92
- Bear: S=-2.41

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_eod_close, 5))` S=1.36, F=0.46, INFERIOR
Direction gap: +0.77 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * news_eod_close)`: S=-0.16, F=-0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(-1 * news_eod_close / close)`: S=-0.66, F=-0.11, T=122.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_eod_close, 5))`: S=1.36, F=0.46, T=108.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_eod_close)` | TOP3000 | 0.15 | 0.03 | 46.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_ton_low: 1.000 (strongly positively correlated)
- news_ton_high: 1.000 (strongly positively correlated)
- news_ton_last: 1.000 (strongly positively correlated)
- news_open: 1.000 (strongly positively correlated)
- news_eod_high: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
