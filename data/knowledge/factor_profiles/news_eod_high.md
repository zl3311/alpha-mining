---
field: news_eod_high
dataset: news12
best_template: rank_neg_delta
best_sharpe: 1.36
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4647
ann_vol: 0.138
hit_rate: 0.536
rolling_sharpe_min: -2.955
rolling_sharpe_max: 2.381
negated_best_sharpe: 1.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.44
n_negated_sims: 4
direction_gap: 0.73
---
# news_eod_high (news12)

*Highest price from the time of news to end of session*

## Signal Profile
- `rank(news_eod_high)`: S=0.16, F=0.03, T=76.8%, INFERIOR (TOP3000)
- `rank(news_eod_high / close)`: S=0.10, F=0.01, T=109.3%, INFERIOR (TOP3000)
- `rank(ts_delta(news_eod_high, 5))`: S=-0.66, F=-0.18, T=91.2%, INFERIOR (TOP500)
- `-rank(news_eod_high)`: S=0.02, F=0.00, T=64.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_eod_high, 5))`: S=1.36, F=0.44, T=113.5%, INFERIOR (TOP3000)
- `-ts_zscore(news_eod_high, 63)`: S=0.63, F=0.20, T=69.8%, INFERIOR (TOP3000)
- `ts_mean(news_eod_high, 10)`: S=-0.02, F=0.00, T=5.1%, INFERIOR (TOP3000)
- `rank(ts_rank(news_eod_high, 22))`: S=-0.73, F=-0.22, T=81.0%, INFERIOR (TOP3000)
- `rank(-1 * news_eod_high)`: S=-0.16, F=-0.03, T=76.8%, INFERIOR (TOP3000)
- `rank(-1 * news_eod_high / close)`: S=0.13, F=0.01, T=120.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 13F/8P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.15, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.10 (moderate), ret=+9.2%
  - 2020: S=-1.67 (negative), ret=-21.2%
  - 2021: S=0.78 (moderate), ret=+11.4%
  - 2022: S=0.72 (moderate), ret=+12.1%
  - 2023: S=-0.10 (negative), ret=-1.4%

## Risk & Drawdown
- Max drawdown: 46.47% over 1498 days (recovered)
- Annualized: return +2.1%, volatility 13.8% (fraction of booksize)
- Hit rate: 53.6% positive days
- Tail shape: skew -0.31, excess kurtosis +0.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.96, max 2.38, latest -0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +8.83%; worst month: -10.71%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.68
- Sideways: S=0.92
- Bear: S=-2.38

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_eod_high, 5))` S=1.36, F=0.44, INFERIOR
Direction gap: +0.73 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * news_eod_high)`: S=-0.16, F=-0.03, T=76.8%, INFERIOR (TOP3000)
- `rank(-1 * news_eod_high / close)`: S=0.13, F=0.01, T=120.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_eod_high, 5))`: S=1.36, F=0.44, T=113.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_eod_high)` | TOP3000 | 0.15 | 0.03 | 46.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_eod_low: 1.000 (strongly positively correlated)
- news_eod_vwap: 0.999 (strongly positively correlated)
- news_eod_close: 0.999 (strongly positively correlated)
- news_ton_high: 0.999 (strongly positively correlated)
- news_open: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
