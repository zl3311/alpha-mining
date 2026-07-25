---
field: news_pct_5_min
dataset: news12
best_template: rank_level
best_sharpe: 0.74
best_fitness: 0.19
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1683
ann_vol: 0.0923
hit_rate: 0.5126
rolling_sharpe_min: -1.148
rolling_sharpe_max: 2.26
negated_best_sharpe: 0.43
negated_best_template: neg_rank
negated_best_fitness: 0.07
n_negated_sims: 4
direction_gap: -0.31
---
# news_pct_5_min (news12)

*Percent change in price during the first 5 minutes following the news release*

## Signal Profile
- `rank(news_pct_5_min)`: S=0.74, F=0.19, T=103.8%, INFERIOR (TOP200)
- `rank(news_pct_5_min / close)`: S=-0.46, F=-0.07, T=123.0%, INFERIOR (TOP3000)
- `rank(ts_delta(news_pct_5_min, 5))`: S=0.27, F=0.04, T=120.7%, INFERIOR (TOP200)
- `-rank(news_pct_5_min)`: S=0.43, F=0.07, T=122.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_5_min, 5))`: S=0.09, F=0.01, T=148.2%, INFERIOR (TOP3000)
- `-ts_zscore(news_pct_5_min, 63)`: S=0.64, F=0.12, T=118.2%, INFERIOR (TOP3000)
- `ts_mean(news_pct_5_min, 10)`: S=-0.38, F=-0.11, T=27.5%, INFERIOR (TOP3000)
- `rank(ts_rank(news_pct_5_min, 22))`: S=-0.57, F=-0.09, T=125.6%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_5_min)`: S=-0.40, F=-0.06, T=130.4%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_5_min / close)`: S=-0.32, F=-0.04, T=132.2%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.73, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.68 (strong), ret=+12.8%
  - 2020: S=0.20 (weak), ret=+2.0%
  - 2021: S=0.56 (moderate), ret=+6.5%
  - 2022: S=1.05 (moderate), ret=+8.9%
  - 2023: S=0.42 (weak), ret=+3.0%

## Risk & Drawdown
- Max drawdown: 16.83% over 279 days (recovered)
- Annualized: return +6.8%, volatility 9.2% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.33, excess kurtosis +2.40

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 2.26, latest 0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +6.64%; worst month: -7.37%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.31
- Sideways: S=1.10
- Bear: S=1.55

## Negated Direction
Best negated: `-rank(news_pct_5_min)` S=0.43, F=0.07, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_pct_5_min)`: S=-0.40, F=-0.06, T=130.4%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_5_min / close)`: S=-0.32, F=-0.04, T=132.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_5_min, 5))`: S=0.09, F=0.01, T=148.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_pct_5_min)` | TOP200 | 0.73 | 0.19 | 16.8% | 100% | mixed |
| `rank(news_pct_5_min)` | TOP3000 | 0.43 | 0.06 | 16.5% | 60% | mixed |
| `rank(ts_delta(news_pct_5_min, 5))` | TOP200 | 0.27 | 0.04 | 27.8% | 80% | bear-only |

## Correlation Notes
Top correlates:
- news_pct_10min: 0.658 (moderately positively correlated)
- news_pct_30min: 0.484 (moderately positively correlated)
- rp_ess_price: 0.150 (weakly positively correlated)
- fnd6_prcc: -0.123 (weakly negatively correlated)
- fnd6_prclq: -0.123 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
