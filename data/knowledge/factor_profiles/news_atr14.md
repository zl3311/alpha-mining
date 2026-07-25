---
field: news_atr14
dataset: news12
cluster: news12_other
coverage: 0.8947
community_alphas: 3682
best_template: ts_zscore
best_sharpe: 0.25
best_fitness: 0.05
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 23
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.3237
ann_vol: 0.0897
hit_rate: 0.5231
rolling_sharpe_min: -2.442
rolling_sharpe_max: 2.469
negated_best_sharpe: 0.01
negated_best_template: neg_rank
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.24
---
# news_atr14 (news12)

*14-day Average True Range*

## Signal Profile
- `rank(news_atr14)`: S=0.18, F=0.03, T=71.5%, INFERIOR (TOP3000)
- `rank(news_atr14 / close)`: S=0.08, F=0.01, T=59.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_atr14, 5))`: S=0.15, F=0.01, T=105.3%, INFERIOR (TOP3000)
- `-rank(news_atr14)`: S=0.01, F=0.00, T=60.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_atr14, 5))`: S=-0.15, F=-0.01, T=105.3%, INFERIOR (TOP3000)
- `-ts_zscore(news_atr14, 63)`: S=0.25, F=0.05, T=67.1%, INFERIOR (TOP3000)
- `ts_mean(news_atr14, 10)`: S=0.09, F=0.02, T=5.5%, INFERIOR (TOP3000)
- `rank(ts_rank(news_atr14, 22))`: S=-0.11, F=-0.01, T=76.0%, INFERIOR (TOP3000)
- `rank(-1 * news_atr14)`: S=-0.18, F=-0.03, T=71.5%, INFERIOR (TOP3000)
- `rank(-1 * news_atr14 / close)`: S=-0.04, F=0.00, T=71.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 23F/0P
- HIGH_TURNOVER: 14F/9P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 23F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.17, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.33 (moderate), ret=+8.1%
  - 2020: S=-0.89 (negative), ret=-8.9%
  - 2021: S=0.54 (moderate), ret=+4.8%
  - 2022: S=0.38 (weak), ret=+3.5%
  - 2023: S=-0.01 (negative), ret=-0.1%

## Risk & Drawdown
- Max drawdown: 32.37% over 1362 days (not yet recovered, ongoing at window end)
- Annualized: return +1.5%, volatility 9.0% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew -0.35, excess kurtosis +1.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.44, max 2.47, latest -0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +5.74%; worst month: -6.09%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=0.99
- Sideways: S=1.01
- Bear: S=-1.44

## Negated Direction
Best negated: `-rank(news_atr14)` S=0.01, F=0.00, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_atr14)`: S=-0.18, F=-0.03, T=71.5%, INFERIOR (TOP3000)
- `rank(-1 * news_atr14 / close)`: S=-0.04, F=0.00, T=71.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_atr14, 5))`: S=-0.15, F=-0.01, T=105.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_atr14)` | TOP3000 | 0.17 | 0.03 | 32.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- call_breakeven_1080: 0.885 (strongly positively correlated)
- call_breakeven_720: 0.885 (strongly positively correlated)
- call_breakeven_360: 0.885 (strongly positively correlated)
- call_breakeven_270: 0.883 (strongly positively correlated)
- call_breakeven_150: 0.880 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
