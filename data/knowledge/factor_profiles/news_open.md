---
field: news_open
dataset: news12
best_template: rank_value_norm
best_sharpe: 1.55
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4632
ann_vol: 0.1367
hit_rate: 0.5385
rolling_sharpe_min: -2.94
rolling_sharpe_max: 2.465
negated_best_sharpe: 1.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.35
n_negated_sims: 4
direction_gap: -0.39
---
# news_open (news12)

*Price at the session open*

## Signal Profile
- `rank(news_open)`: S=0.17, F=0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(news_open / close)`: S=1.55, F=0.50, T=115.0%, INFERIOR (TOP3000)
- `rank(ts_delta(news_open, 5))`: S=-0.38, F=-0.08, T=88.1%, INFERIOR (TOP500)
- `-rank(news_open)`: S=-0.05, F=-0.01, T=60.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_open, 5))`: S=1.16, F=0.35, T=107.5%, INFERIOR (TOP3000)
- `-ts_zscore(news_open, 63)`: S=0.56, F=0.18, T=65.7%, INFERIOR (TOP3000)
- `ts_mean(news_open, 10)`: S=-0.02, F=0.00, T=5.0%, INFERIOR (TOP3000)
- `rank(ts_rank(news_open, 22))`: S=-0.65, F=-0.19, T=76.3%, INFERIOR (TOP3000)
- `rank(-1 * news_open)`: S=-0.17, F=-0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(-1 * news_open / close)`: S=-0.99, F=-0.23, T=125.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 13F/8P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.17, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.09 (moderate), ret=+9.0%
  - 2020: S=-1.69 (negative), ret=-21.3%
  - 2021: S=0.88 (moderate), ret=+12.8%
  - 2022: S=0.76 (moderate), ret=+12.7%
  - 2023: S=-0.16 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 46.32% over 1218 days (recovered)
- Annualized: return +2.2%, volatility 13.7% (fraction of booksize)
- Hit rate: 53.8% positive days
- Tail shape: skew -0.31, excess kurtosis +0.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.94, max 2.46, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +8.92%; worst month: -10.49%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.75
- Sideways: S=0.93
- Bear: S=-2.41

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_open, 5))` S=1.16, F=0.35, INFERIOR
Direction gap: -0.39 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_open)`: S=-0.17, F=-0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(-1 * news_open / close)`: S=-0.99, F=-0.23, T=125.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_open, 5))`: S=1.16, F=0.35, T=107.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_open)` | TOP3000 | 0.17 | 0.03 | 46.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_ton_low: 1.000 (strongly positively correlated)
- news_ton_high: 1.000 (strongly positively correlated)
- news_ton_last: 1.000 (strongly positively correlated)
- news_eod_close: 1.000 (strongly positively correlated)
- news_eod_high: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
