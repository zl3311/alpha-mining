---
field: news_pct_120min
dataset: news12
best_template: neg_rank
best_sharpe: 1.05
best_fitness: 0.23
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.1123
ann_vol: 0.0503
hit_rate: 0.4996
rolling_sharpe_min: -1.331
rolling_sharpe_max: 4.103
redundancy_cluster: 89
negated_best_sharpe: 1.05
negated_best_template: neg_rank
negated_best_fitness: 0.23
n_negated_sims: 4
direction_gap: 0.35
---
# news_pct_120min (news12)

*Percent change in price during the first 120 minutes following the news release*

## Signal Profile
- `rank(news_pct_120min)`: S=0.62, F=0.10, T=123.9%, INFERIOR (TOP3000)
- `rank(news_pct_120min / close)`: S=-1.01, F=-0.22, T=114.1%, INFERIOR (TOP3000)
- `rank(ts_delta(news_pct_120min, 5))`: S=0.21, F=0.02, T=145.4%, INFERIOR (TOP3000)
- `-rank(news_pct_120min)`: S=1.05, F=0.23, T=114.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_120min, 5))`: S=-0.21, F=-0.02, T=145.4%, INFERIOR (TOP3000)
- `-ts_zscore(news_pct_120min, 63)`: S=0.70, F=0.13, T=111.5%, INFERIOR (TOP3000)
- `ts_mean(news_pct_120min, 10)`: S=-0.47, F=-0.17, T=26.1%, INFERIOR (TOP3000)
- `rank(ts_rank(news_pct_120min, 22))`: S=-1.01, F=-0.20, T=115.4%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_120min)`: S=-0.62, F=-0.10, T=123.9%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_120min / close)`: S=-0.65, F=-0.11, T=124.6%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.61, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.26 (moderate), ret=+6.2%
  - 2020: S=0.16 (weak), ret=+0.8%
  - 2021: S=0.59 (moderate), ret=+3.0%
  - 2022: S=1.55 (strong), ret=+8.4%
  - 2023: S=-0.79 (negative), ret=-3.4%

## Risk & Drawdown
- Max drawdown: 11.23% over 363 days (recovered)
- Annualized: return +3.0%, volatility 5.0% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.07, excess kurtosis +0.84

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.33, max 4.10, latest -0.71

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.13%; worst month: -3.47%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.40
- Sideways: S=0.49
- Bear: S=1.73

## Negated Direction
Best negated: `-rank(news_pct_120min)` S=1.05, F=0.23, INFERIOR
Direction gap: +0.35 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_pct_120min)`: S=-0.62, F=-0.10, T=123.9%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_120min / close)`: S=-0.65, F=-0.11, T=124.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_120min, 5))`: S=-0.21, F=-0.02, T=145.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_pct_120min)` | TOP3000 | 0.61 | 0.10 | 11.2% | 80% | mixed |
| `rank(ts_delta(news_pct_120min, 5))` | TOP3000 | 0.19 | 0.02 | 26.6% | 80% | mixed |

## Correlation Notes
Top correlates:
- news_pct_90min: 0.889 (strongly positively correlated)
- news_pct_60min: 0.788 (strongly positively correlated)
- rank(scl12_buzz * (-1 * returns)): -0.296 (weakly negatively correlated)
- rank(fnd6_acdo) * rank(-1 * returns): -0.280 (weakly negatively correlated)
- rank(fnd6_acdo) + rank(open/close - 1): -0.245 (weakly negatively correlated)

Redundancy cluster #89: 3 similar fields, mean |rho| 0.845 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
