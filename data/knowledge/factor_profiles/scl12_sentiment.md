---
field: scl12_sentiment
dataset: socialmedia12
best_template: neg_rank_value_norm
best_sharpe: 0.77
best_fitness: 0.15
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 30
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0665
ann_vol: 0.0481
hit_rate: 0.5117
rolling_sharpe_min: -0.931
rolling_sharpe_max: 2.627
negated_best_sharpe: 0.77
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: 0.12
---
# scl12_sentiment (socialmedia12)

*sentiment*

## Signal Profile
- `rank(scl12_sentiment)`: S=0.47, F=0.12, T=56.8%, INFERIOR (TOP200)
- `rank(ts_delta(scl12_sentiment, 5))`: S=0.65, F=0.13, T=72.6%, INFERIOR (TOP500)
- `ts_decay_linear(rank(scl12_sentiment), 5)`: S=-0.79, F=-0.17, T=57.7%, INFERIOR (TOP3000)
- `-rank(scl12_sentiment)`: S=0.21, F=0.02, T=61.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(scl12_sentiment, 5))`: S=0.39, F=0.04, T=96.1%, INFERIOR (TOP3000)
- `-ts_zscore(scl12_sentiment, 63)`: S=0.08, F=0.01, T=62.4%, INFERIOR (TOP3000)
- `ts_mean(scl12_sentiment, 10)`: S=-0.45, F=-0.23, T=19.2%, INFERIOR (TOP3000)
- `rank(ts_rank(scl12_sentiment, 22))`: S=0.05, F=0.00, T=71.2%, INFERIOR (TOP3000)
- `rank(-1 * scl12_sentiment)`: S=0.64, F=0.10, T=77.8%, INFERIOR (TOP3000)
- `rank(-1 * scl12_sentiment / close)`: S=0.77, F=0.15, T=79.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/29P
- HIGH_TURNOVER: 20F/10P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 30F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/19P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.65, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.47 (strong), ret=+8.2%
  - 2020: S=-0.66 (negative), ret=-3.2%
  - 2021: S=1.39 (moderate), ret=+8.3%
  - 2022: S=-0.44 (negative), ret=-2.0%
  - 2023: S=0.87 (moderate), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 6.65% over 498 days (recovered)
- Annualized: return +3.1%, volatility 4.8% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.35, excess kurtosis +2.99

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.93, max 2.63, latest 0.82

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +5.32%; worst month: -3.54%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.27
- Sideways: S=0.77
- Bear: S=1.49

## Negated Direction
Best negated: `rank(-1 * scl12_sentiment / close)` S=0.77, F=0.15, INFERIOR
Direction gap: +0.12 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * scl12_sentiment)`: S=0.64, F=0.10, T=77.8%, INFERIOR (TOP3000)
- `rank(-1 * scl12_sentiment / close)`: S=0.77, F=0.15, T=79.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(scl12_sentiment, 5))`: S=0.39, F=0.04, T=96.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(scl12_sentiment, 5))` | TOP500 | 0.65 | 0.13 | 6.7% | 60% | mixed |
| `rank(scl12_sentiment)` | TOP200 | 0.46 | 0.12 | 13.3% | 40% | mixed |
| `rank(ts_delta(scl12_sentiment, 5))` | TOP200 | 0.52 | 0.12 | 10.2% | 80% | all-weather |
| `rank(ts_delta(scl12_sentiment, 5))` | TOP1000 | 0.30 | 0.04 | 6.7% | 60% | weak |

## Correlation Notes
Top correlates:
- scl12_sentiment_fast_d1: 0.224 (weakly positively correlated)
- snt_value_fast_d1: -0.191 (weakly negatively correlated)
- rp_ess_credit_ratings: 0.182 (weakly positively correlated)
- news_range_stddev: 0.157 (weakly positively correlated)
- snt_buzz_bfl_fast_d1: -0.154 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: rank_value_norm, trade_when
