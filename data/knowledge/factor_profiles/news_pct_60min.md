---
field: news_pct_60min
dataset: news12
best_template: neg_rank
best_sharpe: 1.0
best_fitness: 0.21
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1246
ann_vol: 0.0529
hit_rate: 0.5004
rolling_sharpe_min: -1.903
rolling_sharpe_max: 3.15
redundancy_cluster: 89
negated_best_sharpe: 1.0
negated_best_template: neg_rank
negated_best_fitness: 0.21
n_negated_sims: 4
direction_gap: 0.36
---
# news_pct_60min (news12)

*Percent change in price during the first 60 minutes following the news release*

## Signal Profile
- `rank(news_pct_60min)`: S=0.57, F=0.09, T=123.8%, INFERIOR (TOP3000)
- `rank(news_pct_60min / close)`: S=-0.88, F=-0.18, T=114.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_pct_60min, 5))`: S=-0.24, F=-0.03, T=145.1%, INFERIOR (TOP3000)
- `-rank(news_pct_60min)`: S=1.00, F=0.21, T=114.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_60min, 5))`: S=0.24, F=0.03, T=145.1%, INFERIOR (TOP3000)
- `-ts_zscore(news_pct_60min, 63)`: S=0.64, F=0.11, T=111.8%, INFERIOR (TOP3000)
- `ts_mean(news_pct_60min, 10)`: S=-0.57, F=-0.21, T=26.3%, INFERIOR (TOP3000)
- `rank(ts_rank(news_pct_60min, 22))`: S=-1.00, F=-0.20, T=116.1%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_60min)`: S=-0.57, F=-0.09, T=123.8%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_60min / close)`: S=-0.67, F=-0.12, T=124.6%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.10 (moderate), ret=+5.5%
  - 2020: S=0.57 (moderate), ret=+3.2%
  - 2021: S=0.16 (weak), ret=+0.8%
  - 2022: S=1.13 (moderate), ret=+6.3%
  - 2023: S=-0.28 (negative), ret=-1.3%

## Risk & Drawdown
- Max drawdown: 12.46% over 632 days (recovered)
- Annualized: return +2.9%, volatility 5.3% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.23, excess kurtosis +1.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.90, max 3.15, latest -0.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +6.07%; worst month: -3.48%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.16
- Sideways: S=0.79
- Bear: S=1.00

## Negated Direction
Best negated: `-rank(news_pct_60min)` S=1.00, F=0.21, INFERIOR
Direction gap: +0.36 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_pct_60min)`: S=-0.57, F=-0.09, T=123.8%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_60min / close)`: S=-0.67, F=-0.12, T=124.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_60min, 5))`: S=0.24, F=0.03, T=145.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_pct_60min)` | TOP3000 | 0.56 | 0.09 | 12.5% | 80% | mixed |

## Correlation Notes
Top correlates:
- news_pct_90min: 0.859 (strongly positively correlated)
- news_pct_120min: 0.788 (strongly positively correlated)
- rank(scl12_buzz * (-1 * returns)): -0.205 (weakly negatively correlated)
- rank(fnd6_acdo) * rank(-1 * returns): -0.192 (weakly negatively correlated)
- rank(fnd6_acdo) + rank(open/close - 1): -0.168 (weakly negatively correlated)

Redundancy cluster #89: 3 similar fields, mean |rho| 0.845 (representative: news_pct_120min). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
