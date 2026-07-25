---
field: news_pct_90min
dataset: news12
best_template: neg_rank
best_sharpe: 0.84
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.0953
ann_vol: 0.0508
hit_rate: 0.4899
rolling_sharpe_min: -1.294
rolling_sharpe_max: 3.785
redundancy_cluster: 89
negated_best_sharpe: 0.84
negated_best_template: neg_rank
negated_best_fitness: 0.17
n_negated_sims: 4
direction_gap: 0.24
---
# news_pct_90min (news12)

*Percent change in price during the first 90 minutes following the news release*

## Signal Profile
- `rank(news_pct_90min)`: S=0.60, F=0.09, T=124.0%, INFERIOR (TOP3000)
- `rank(news_pct_90min / close)`: S=-0.86, F=-0.18, T=114.3%, INFERIOR (TOP3000)
- `rank(ts_delta(news_pct_90min, 5))`: S=0.34, F=0.04, T=145.6%, INFERIOR (TOP3000)
- `-rank(news_pct_90min)`: S=0.84, F=0.17, T=114.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_90min, 5))`: S=-0.34, F=-0.04, T=145.6%, INFERIOR (TOP3000)
- `-ts_zscore(news_pct_90min, 63)`: S=0.39, F=0.06, T=111.4%, INFERIOR (TOP3000)
- `ts_mean(news_pct_90min, 10)`: S=-0.23, F=-0.06, T=26.2%, INFERIOR (TOP3000)
- `rank(ts_rank(news_pct_90min, 22))`: S=-0.85, F=-0.16, T=115.6%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_90min)`: S=-0.60, F=-0.09, T=124.0%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_90min / close)`: S=-0.59, F=-0.09, T=124.8%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.59, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.14 (moderate), ret=+5.4%
  - 2020: S=-0.25 (negative), ret=-1.3%
  - 2021: S=0.73 (moderate), ret=+3.6%
  - 2022: S=1.56 (strong), ret=+8.7%
  - 2023: S=-0.39 (negative), ret=-1.8%

## Risk & Drawdown
- Max drawdown: 9.53% over 369 days (recovered)
- Annualized: return +3.0%, volatility 5.1% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.18, excess kurtosis +1.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 3.79, latest -0.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +6.03%; worst month: -4.05%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.05
- Sideways: S=0.66
- Bear: S=1.11

## Negated Direction
Best negated: `-rank(news_pct_90min)` S=0.84, F=0.17, INFERIOR
Direction gap: +0.24 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_pct_90min)`: S=-0.60, F=-0.09, T=124.0%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_90min / close)`: S=-0.59, F=-0.09, T=124.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_90min, 5))`: S=-0.34, F=-0.04, T=145.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_pct_90min)` | TOP3000 | 0.59 | 0.09 | 9.5% | 60% | mixed |
| `rank(ts_delta(news_pct_90min, 5))` | TOP3000 | 0.30 | 0.04 | 23.0% | 60% | bear-only |

## Correlation Notes
Top correlates:
- news_pct_120min: 0.889 (strongly positively correlated)
- news_pct_60min: 0.859 (strongly positively correlated)
- rank(scl12_buzz * (-1 * returns)): -0.248 (weakly negatively correlated)
- rank(fnd6_acdo) * rank(-1 * returns): -0.231 (weakly negatively correlated)
- rank(fnd6_acdo) + rank(open/close - 1): -0.197 (weakly negatively correlated)

Redundancy cluster #89: 3 similar fields, mean |rho| 0.845 (representative: news_pct_120min). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
