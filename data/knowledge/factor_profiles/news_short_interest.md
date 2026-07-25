---
field: news_short_interest
dataset: news12
best_template: rank_level
best_sharpe: 1.16
best_fitness: 0.72
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.2461
ann_vol: 0.1183
hit_rate: 0.1862
rolling_sharpe_min: -1.916
rolling_sharpe_max: 2.969
negated_best_sharpe: 0.6
negated_best_template: rank_neg_delta
negated_best_fitness: 0.19
n_negated_sims: 4
direction_gap: -0.56
---
# news_short_interest (news12)

*Ratio of total number of shares sold short to total shares outstanding*

## Signal Profile
- `rank(news_short_interest)`: S=1.16, F=0.72, T=54.8%, INFERIOR (TOP200)
- `rank(ts_delta(news_short_interest, 5))`: S=0.05, F=0.01, T=94.7%, INFERIOR (TOP500)
- `-rank(news_short_interest)`: S=-0.22, F=-0.05, T=86.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_short_interest, 5))`: S=0.60, F=0.19, T=119.9%, INFERIOR (TOP3000)
- `ts_zscore(news_short_interest, 22)`: S=0.61, F=0.27, T=92.0%, INFERIOR (TOP3000)
- `ts_mean(news_short_interest, 10)`: S=-0.30, F=-0.19, T=18.2%, INFERIOR (TOP3000)
- `rank(ts_rank(news_short_interest, 22))`: S=0.75, F=0.27, T=101.5%, INFERIOR (TOP3000)
- `rank(-1 * news_short_interest)`: S=-0.89, F=-0.34, T=96.7%, INFERIOR (TOP3000)
- `rank(-1 * news_short_interest / close)`: S=-1.13, F=-0.52, T=95.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 17F/3P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.75, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=2.19 (strong), ret=+29.7%
  - 2020: S=2.12 (strong), ret=+21.1%
  - 2021: S=-0.36 (negative), ret=-7.2%
  - 2022: S=0.00 (negative), ret=+0.0%
  - 2023: S=0.00 (negative), ret=+0.0%

## Risk & Drawdown
- Max drawdown: 24.61% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +8.9%, volatility 11.8% (fraction of booksize)
- Hit rate: 18.6% positive days
- Tail shape: skew -0.53, excess kurtosis +84.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.92, max 2.97, latest 0.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +9.50%; worst month: -9.10%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.50
- Sideways: S=1.35
- Bear: S=0.57

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_short_interest, 5))` S=0.60, F=0.19, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_short_interest)`: S=-0.89, F=-0.34, T=96.7%, INFERIOR (TOP3000)
- `rank(-1 * news_short_interest / close)`: S=-1.13, F=-0.52, T=95.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_short_interest, 5))`: S=0.60, F=0.19, T=119.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_short_interest)` | TOP200 | 0.75 | 0.72 | 24.6% | 40% | mixed |
| `rank(news_short_interest)` | TOP3000 | 0.59 | 0.34 | 17.6% | 60% | mixed |
| `rank(news_short_interest)` | TOP500 | 0.32 | 0.20 | 33.2% | 40% | bear-only |
| `rank(news_short_interest)` | TOP1000 | 0.14 | 0.05 | 39.6% | 20% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_donr: -0.471 (moderately negatively correlated)
- fnd6_newqv1300_cimiiq: -0.212 (weakly negatively correlated)
- fnd6_adesinda_curcd: -0.211 (weakly negatively correlated)
- fnd6_newa1v1300_aul3: 0.187 (weakly positively correlated)
- fnd6_idesindq_curcd: -0.169 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
