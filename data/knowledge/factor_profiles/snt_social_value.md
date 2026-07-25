---
field: snt_social_value
dataset: socialmedia12
cluster: socialmedia8_analyst_rating
coverage: 1.0
community_alphas: 4976
best_template: rank_neg_delta
best_sharpe: 0.94
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.053
ann_vol: 0.0337
hit_rate: 0.5255
rolling_sharpe_min: -1.837
rolling_sharpe_max: 2.468
negated_best_sharpe: 0.94
negated_best_template: rank_neg_delta
negated_best_fitness: 0.43
n_negated_sims: 10
direction_gap: 0.45
---
# snt_social_value (socialmedia12)

*Z-score of sentiment*

## Signal Profile
- `rank(snt_social_value)`: S=0.49, F=0.13, T=23.4%, INFERIOR (TOP3000)
- `rank(ts_delta(snt_social_value, 5))`: S=0.55, F=0.11, T=32.7%, INFERIOR (TOP3000)
- `-rank(snt_social_value)`: S=-0.22, F=-0.04, T=24.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_social_value, 5))`: S=0.94, F=0.43, T=33.6%, INFERIOR (TOP3000)
- `-ts_zscore(snt_social_value, 63)`: S=-0.07, F=-0.01, T=25.8%, INFERIOR (TOP3000)
- `ts_mean(snt_social_value, 10)`: S=0.23, F=0.05, T=19.7%, INFERIOR (TOP3000)
- `rank(ts_rank(snt_social_value, 22))`: S=-0.15, F=-0.02, T=27.2%, INFERIOR (TOP3000)
- `rank(-1 * snt_social_value)`: S=0.19, F=0.05, T=25.9%, INFERIOR (TOP3000)
- `rank(-1 * snt_social_value / close)`: S=-0.10, F=-0.02, T=26.0%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 24F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.50, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.01 (strong), ret=+3.7%
  - 2020: S=0.74 (moderate), ret=+2.3%
  - 2021: S=0.86 (moderate), ret=+3.2%
  - 2022: S=0.72 (moderate), ret=+3.2%
  - 2023: S=-1.63 (negative), ret=-4.3%

## Risk & Drawdown
- Max drawdown: 5.30% over 367 days (not yet recovered, ongoing at window end)
- Annualized: return +1.7%, volatility 3.4% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew -0.71, excess kurtosis +5.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.84, max 2.47, latest -1.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +1.86%; worst month: -1.42%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.01
- Sideways: S=0.83
- Bear: S=0.89

## Negated Direction
Best negated: `rank(-1 * ts_delta(snt_social_value, 5))` S=0.94, F=0.43, INFERIOR
Direction gap: +0.45 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * snt_social_value)`: S=0.19, F=0.05, T=25.9%, INFERIOR (TOP3000)
- `rank(-1 * snt_social_value / close)`: S=-0.10, F=-0.02, T=26.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_social_value, 5))`: S=0.94, F=0.43, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(snt_social_value)` | TOP3000 | 0.50 | 0.13 | 5.3% | 80% | mixed |
| `rank(ts_delta(snt_social_value, 5))` | TOP3000 | 0.56 | 0.11 | 3.0% | 60% | all-weather |
| `rank(snt_social_value)` | TOP1000 | 0.21 | 0.04 | 7.7% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_prchq: -0.472 (moderately negatively correlated)
- rank(scl12_buzz * (-1 * returns)): -0.459 (moderately negatively correlated)
- fnd6_prccq: -0.457 (moderately negatively correlated)
- rank(fnd6_acdo) * rank(-1 * returns): -0.455 (moderately negatively correlated)
- max_reported_eps_guidance: 0.443 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
