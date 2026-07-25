---
field: news_eod_low
dataset: news12
best_template: rank_neg_delta
best_sharpe: 1.24
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4596
ann_vol: 0.1394
hit_rate: 0.536
rolling_sharpe_min: -2.894
rolling_sharpe_max: 2.357
negated_best_sharpe: 1.24
negated_best_template: rank_neg_delta
negated_best_fitness: 0.39
n_negated_sims: 4
direction_gap: 0.65
---
# news_eod_low (news12)

*Lowest price from the time of news to end of session*

## Signal Profile
- `rank(news_eod_low)`: S=0.17, F=0.03, T=76.7%, INFERIOR (TOP3000)
- `rank(news_eod_low / close)`: S=0.53, F=0.10, T=113.2%, INFERIOR (TOP3000)
- `rank(ts_delta(news_eod_low, 5))`: S=-0.64, F=-0.17, T=91.7%, INFERIOR (TOP500)
- `-rank(news_eod_low)`: S=0.02, F=0.00, T=64.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_eod_low, 5))`: S=1.24, F=0.39, T=113.7%, INFERIOR (TOP3000)
- `-ts_zscore(news_eod_low, 63)`: S=0.59, F=0.19, T=70.0%, INFERIOR (TOP3000)
- `ts_mean(news_eod_low, 10)`: S=-0.01, F=0.00, T=5.1%, INFERIOR (TOP3000)
- `rank(ts_rank(news_eod_low, 22))`: S=-0.65, F=-0.18, T=81.6%, INFERIOR (TOP3000)
- `rank(-1 * news_eod_low)`: S=-0.17, F=-0.03, T=76.7%, INFERIOR (TOP3000)
- `rank(-1 * news_eod_low / close)`: S=-0.90, F=-0.20, T=125.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 13F/8P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.16, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.10 (moderate), ret=+9.3%
  - 2020: S=-1.62 (negative), ret=-20.7%
  - 2021: S=0.79 (moderate), ret=+11.6%
  - 2022: S=0.71 (moderate), ret=+12.1%
  - 2023: S=-0.11 (negative), ret=-1.5%

## Risk & Drawdown
- Max drawdown: 45.96% over 1497 days (recovered)
- Annualized: return +2.2%, volatility 13.9% (fraction of booksize)
- Hit rate: 53.6% positive days
- Tail shape: skew -0.32, excess kurtosis +0.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.89, max 2.36, latest -0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +8.93%; worst month: -10.84%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.68
- Sideways: S=0.93
- Bear: S=-2.37

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_eod_low, 5))` S=1.24, F=0.39, INFERIOR
Direction gap: +0.65 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * news_eod_low)`: S=-0.17, F=-0.03, T=76.7%, INFERIOR (TOP3000)
- `rank(-1 * news_eod_low / close)`: S=-0.90, F=-0.20, T=125.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_eod_low, 5))`: S=1.24, F=0.39, T=113.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_eod_low)` | TOP3000 | 0.16 | 0.03 | 46.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_eod_high: 1.000 (strongly positively correlated)
- news_eod_vwap: 0.999 (strongly positively correlated)
- news_ton_low: 0.999 (strongly positively correlated)
- news_eod_close: 0.999 (strongly positively correlated)
- news_open: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
