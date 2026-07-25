---
field: snt_buzz
dataset: socialmedia12
best_template: neg_rank_level
best_sharpe: 0.57
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 29
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.2297
ann_vol: 0.0845
hit_rate: 0.5077
rolling_sharpe_min: -2.554
rolling_sharpe_max: 2.459
negated_best_sharpe: 0.57
negated_best_template: neg_rank_level
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: 0.19
---
# snt_buzz (socialmedia12)

*Negative relative sentiment volume measure for current day, with missing values filled as 0*

## Signal Profile
- `rank(snt_buzz)`: S=0.21, F=0.03, T=37.0%, INFERIOR (TOP3000)
- `rank(ts_delta(snt_buzz, 5))`: S=0.25, F=0.05, T=63.5%, INFERIOR (TOP200)
- `ts_decay_linear(rank(snt_buzz), 5)`: S=0.18, F=0.04, T=20.9%, INFERIOR (TOP3000)
- `-rank(snt_buzz)`: S=-0.03, F=0.00, T=37.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_buzz, 5))`: S=-0.25, F=-0.05, T=63.5%, INFERIOR (TOP3000)
- `-ts_zscore(snt_buzz, 63)`: S=0.38, F=0.08, T=53.0%, INFERIOR (TOP3000)
- `ts_mean(snt_buzz, 10)`: S=0.11, F=0.03, T=17.6%, INFERIOR (TOP3000)
- `rank(ts_rank(snt_buzz, 22))`: S=0.10, F=0.01, T=60.2%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz)`: S=0.57, F=0.17, T=52.0%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz / close)`: S=0.40, F=0.16, T=25.7%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 29F/0P
- LOW_SHARPE: 29F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.28, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.55 (moderate), ret=+3.8%
  - 2020: S=1.20 (moderate), ret=+10.2%
  - 2021: S=1.95 (strong), ret=+18.1%
  - 2022: S=-1.14 (negative), ret=-11.2%
  - 2023: S=-1.53 (negative), ret=-9.3%

## Risk & Drawdown
- Max drawdown: 22.97% over 694 days (not yet recovered, ongoing at window end)
- Annualized: return +2.4%, volatility 8.5% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.11, excess kurtosis +8.68

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.55, max 2.46, latest -1.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +10.67%; worst month: -6.77%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.14
- Sideways: S=0.45
- Bear: S=0.60

## Negated Direction
Best negated: `rank(-1 * snt_buzz)` S=0.57, F=0.17, INFERIOR
Direction gap: +0.19 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * snt_buzz)`: S=0.57, F=0.17, T=52.0%, INFERIOR (TOP3000)
- `rank(-1 * snt_buzz / close)`: S=0.40, F=0.16, T=25.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_buzz, 5))`: S=-0.25, F=-0.05, T=63.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(snt_buzz, 5))` | TOP200 | 0.28 | 0.05 | 23.0% | 60% | mixed |
| `ts_decay_linear(rank(snt_buzz), 5)` | TOP3000 | 0.16 | 0.04 | 7.6% | 60% | mixed |
| `rank(snt_buzz)` | TOP3000 | 0.19 | 0.03 | 6.5% | 80% | mixed |

## Correlation Notes
Top correlates:
- scl12_buzz: -0.644 (moderately negatively correlated)
- scl12_buzz_fast_d1: -0.590 (moderately negatively correlated)
- news_atr_ratio: -0.358 (weakly negatively correlated)
- news_range_stddev: -0.357 (weakly negatively correlated)
- implied_volatility_mean_10: -0.329 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: rank_value_norm, trade_when
