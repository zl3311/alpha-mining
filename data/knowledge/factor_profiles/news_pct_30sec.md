---
field: news_pct_30sec
dataset: news12
best_template: neg_rank_level
best_sharpe: 0.59
best_fitness: 0.12
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.6235
ann_vol: 0.1487
hit_rate: 0.5045
rolling_sharpe_min: -2.674
rolling_sharpe_max: 3.906
negated_best_sharpe: 0.59
negated_best_template: neg_rank_level
negated_best_fitness: 0.12
n_negated_sims: 4
direction_gap: 0.3
---
# news_pct_30sec (news12)

*Percent change in price in the 30 seconds after the news release*

## Signal Profile
- `rank(news_pct_30sec)`: S=0.06, F=0.00, T=116.1%, INFERIOR (TOP200)
- `rank(news_pct_30sec / close)`: S=-0.05, F=0.00, T=136.2%, INFERIOR (TOP3000)
- `rank(ts_delta(news_pct_30sec, 5))`: S=0.26, F=0.04, T=152.0%, INFERIOR (TOP3000)
- `-rank(news_pct_30sec)`: S=0.18, F=0.02, T=134.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_30sec, 5))`: S=-0.26, F=-0.04, T=152.0%, INFERIOR (TOP3000)
- `-ts_zscore(news_pct_30sec, 63)`: S=0.17, F=0.02, T=130.0%, INFERIOR (TOP3000)
- `ts_mean(news_pct_30sec, 10)`: S=0.29, F=0.09, T=29.5%, INFERIOR (TOP3000)
- `rank(ts_rank(news_pct_30sec, 22))`: S=-0.16, F=-0.01, T=139.9%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_30sec)`: S=0.59, F=0.12, T=141.1%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_30sec / close)`: S=0.60, F=0.12, T=143.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/19P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.27, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.01 (moderate), ret=+12.4%
  - 2020: S=-1.75 (negative), ret=-28.0%
  - 2021: S=-1.65 (negative), ret=-26.9%
  - 2022: S=2.63 (strong), ret=+40.2%
  - 2023: S=1.87 (strong), ret=+21.9%

## Risk & Drawdown
- Max drawdown: 62.35% over 1225 days (recovered)
- Annualized: return +4.0%, volatility 14.9% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.04, excess kurtosis +1.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.67, max 3.91, latest 1.99

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +15.03%; worst month: -8.38%
Positive months: 44%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.50
- Sideways: S=2.02
- Bear: S=-0.53

## Negated Direction
Best negated: `rank(-1 * news_pct_30sec)` S=0.59, F=0.12, INFERIOR
Direction gap: +0.30 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_pct_30sec)`: S=0.59, F=0.12, T=141.1%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_30sec / close)`: S=0.60, F=0.12, T=143.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_30sec, 5))`: S=-0.26, F=-0.04, T=152.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_pct_30sec, 5))` | TOP3000 | 0.27 | 0.04 | 62.4% | 60% | mixed |

## Correlation Notes
Top correlates:
- news_pct_1min: 0.420 (moderately positively correlated)
- beta_last_30_days_spy: 0.107 (weakly positively correlated)
- fnd6_newqv1300_cisecglq: 0.100 (weakly positively correlated)
- fnd6_aldo: 0.090 (weakly positively correlated)
- anl4_totassets_std: -0.086 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
