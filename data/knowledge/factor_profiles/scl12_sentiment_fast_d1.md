---
field: scl12_sentiment_fast_d1
dataset: socialmedia12
best_template: neg_rank_value_norm
best_sharpe: 1.16
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.1529
ann_vol: 0.0697
hit_rate: 0.5134
rolling_sharpe_min: -1.092
rolling_sharpe_max: 2.972
negated_best_sharpe: 1.16
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: 0.55
---
# scl12_sentiment_fast_d1 (socialmedia12)

*sentiment*

## Signal Profile
- `rank(scl12_sentiment_fast_d1)`: S=0.32, F=0.07, T=58.3%, INFERIOR (TOP200)
- `rank(ts_delta(scl12_sentiment_fast_d1, 5))`: S=0.61, F=0.15, T=69.7%, INFERIOR (TOP200)
- `-rank(scl12_sentiment_fast_d1)`: S=0.84, F=0.20, T=61.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(scl12_sentiment_fast_d1, 5))`: S=0.36, F=0.05, T=76.6%, INFERIOR (TOP3000)
- `-ts_zscore(scl12_sentiment_fast_d1, 63)`: S=-0.04, F=0.00, T=61.4%, INFERIOR (TOP3000)
- `ts_mean(scl12_sentiment_fast_d1, 10)`: S=-0.35, F=-0.16, T=19.9%, INFERIOR (TOP3000)
- `rank(ts_rank(scl12_sentiment_fast_d1, 22))`: S=-0.51, F=-0.08, T=70.1%, INFERIOR (TOP3000)
- `rank(-1 * scl12_sentiment_fast_d1)`: S=0.84, F=0.20, T=61.2%, INFERIOR (TOP3000)
- `rank(-1 * scl12_sentiment_fast_d1 / close)`: S=1.16, F=0.34, T=60.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/25P
- HIGH_TURNOVER: 10F/16P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.59, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.10 (moderate), ret=+5.7%
  - 2020: S=1.88 (strong), ret=+11.9%
  - 2021: S=-0.54 (negative), ret=-5.1%
  - 2022: S=1.26 (moderate), ret=+8.5%
  - 2023: S=-0.11 (negative), ret=-0.6%

## Risk & Drawdown
- Max drawdown: 15.29% over 742 days (recovered)
- Annualized: return +4.2%, volatility 7.0% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.21, excess kurtosis +2.99

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 2.97, latest -0.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +8.12%; worst month: -11.32%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.35
- Sideways: S=-0.02
- Bear: S=2.20

## Negated Direction
Best negated: `rank(-1 * scl12_sentiment_fast_d1 / close)` S=1.16, F=0.34, INFERIOR
Direction gap: +0.55 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * scl12_sentiment_fast_d1)`: S=0.84, F=0.20, T=61.2%, INFERIOR (TOP3000)
- `rank(-1 * scl12_sentiment_fast_d1 / close)`: S=1.16, F=0.34, T=60.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(scl12_sentiment_fast_d1, 5))`: S=0.36, F=0.05, T=76.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(scl12_sentiment_fast_d1, 5))` | TOP200 | 0.59 | 0.15 | 15.3% | 60% | mixed |
| `rank(scl12_sentiment_fast_d1)` | TOP200 | 0.31 | 0.07 | 13.4% | 80% | mixed |

## Correlation Notes
Top correlates:
- snt_value_fast_d1: -0.231 (weakly negatively correlated)
- scl12_sentiment: 0.224 (weakly positively correlated)
- rp_ess_business: 0.212 (weakly positively correlated)
- rp_css_business: 0.191 (weakly positively correlated)
- rp_ess_price: 0.182 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
