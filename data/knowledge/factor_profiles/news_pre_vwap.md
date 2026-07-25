---
field: news_pre_vwap
dataset: news12
best_template: rank_value_norm
best_sharpe: 1.04
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4192
ann_vol: 0.1468
hit_rate: 0.5255
rolling_sharpe_min: -2.549
rolling_sharpe_max: 2.697
negated_best_sharpe: 0.92
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 4
direction_gap: -0.12
---
# news_pre_vwap (news12)

*Pre-session volume-weighted average price*

## Signal Profile
- `rank(news_pre_vwap)`: S=0.37, F=0.10, T=80.2%, INFERIOR (TOP3000)
- `rank(news_pre_vwap / close)`: S=1.04, F=0.26, T=117.3%, INFERIOR (TOP3000)
- `rank(ts_delta(news_pre_vwap, 5))`: S=-0.61, F=-0.16, T=89.4%, INFERIOR (TOP500)
- `-rank(news_pre_vwap)`: S=-0.12, F=-0.02, T=65.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pre_vwap, 5))`: S=0.92, F=0.26, T=109.9%, INFERIOR (TOP3000)
- `-ts_zscore(news_pre_vwap, 63)`: S=0.67, F=0.22, T=70.9%, INFERIOR (TOP3000)
- `ts_mean(news_pre_vwap, 10)`: S=-0.12, F=-0.04, T=9.1%, INFERIOR (TOP3000)
- `rank(ts_rank(news_pre_vwap, 22))`: S=-0.70, F=-0.20, T=82.6%, INFERIOR (TOP3000)
- `rank(-1 * news_pre_vwap)`: S=-0.37, F=-0.10, T=80.2%, INFERIOR (TOP3000)
- `rank(-1 * news_pre_vwap / close)`: S=-0.48, F=-0.08, T=128.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 14F/7P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.36, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.64 (strong), ret=+14.7%
  - 2020: S=-1.53 (negative), ret=-20.5%
  - 2021: S=1.22 (moderate), ret=+18.4%
  - 2022: S=0.81 (moderate), ret=+14.8%
  - 2023: S=-0.10 (negative), ret=-1.4%

## Risk & Drawdown
- Max drawdown: 41.92% over 766 days (recovered)
- Annualized: return +5.3%, volatility 14.7% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew -0.29, excess kurtosis +0.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.55, max 2.70, latest -0.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +9.80%; worst month: -11.49%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.92
- Sideways: S=0.91
- Bear: S=-2.02

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_pre_vwap, 5))` S=0.92, F=0.26, INFERIOR
Direction gap: -0.12 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_pre_vwap)`: S=-0.37, F=-0.10, T=80.2%, INFERIOR (TOP3000)
- `rank(-1 * news_pre_vwap / close)`: S=-0.48, F=-0.08, T=128.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pre_vwap, 5))`: S=0.92, F=0.26, T=109.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_pre_vwap)` | TOP3000 | 0.36 | 0.10 | 41.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_all_vwap: 0.992 (strongly positively correlated)
- news_post_vwap: 0.992 (strongly positively correlated)
- news_eod_vwap: 0.986 (strongly positively correlated)
- news_eod_low: 0.985 (strongly positively correlated)
- news_eod_high: 0.985 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
