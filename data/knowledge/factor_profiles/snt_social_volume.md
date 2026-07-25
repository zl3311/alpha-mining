---
field: snt_social_volume
dataset: socialmedia8
cluster: socialmedia8_other
coverage: 1.0
community_alphas: 4888
best_template: ts_mean
best_sharpe: 0.47
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 25
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1267
ann_vol: 0.0419
hit_rate: 0.4939
rolling_sharpe_min: -3.299
rolling_sharpe_max: 3.022
negated_best_sharpe: 0.4
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.07
---
# snt_social_volume (socialmedia8)

*Normalized tweet volume*

## Signal Profile
- `rank(snt_social_volume)`: S=0.44, F=0.13, T=21.8%, INFERIOR (TOP3000)
- `rank(snt_social_volume / close)`: S=0.15, F=0.03, T=20.3%, INFERIOR (TOP3000)
- `rank(ts_delta(snt_social_volume, 5))`: S=0.07, F=0.01, T=31.4%, INFERIOR (TOP1000)
- `-rank(snt_social_volume)`: S=-0.42, F=-0.13, T=23.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_social_volume, 5))`: S=0.40, F=0.10, T=31.6%, INFERIOR (TOP3000)
- `ts_zscore(snt_social_volume, 22)`: S=-0.04, F=0.00, T=25.7%, INFERIOR (TOP3000)
- `ts_mean(snt_social_volume, 10)`: S=0.47, F=0.16, T=19.7%, INFERIOR (TOP3000)
- `rank(ts_rank(snt_social_volume, 22))`: S=-0.01, F=0.00, T=26.1%, INFERIOR (TOP3000)
- `rank(-1 * snt_social_volume)`: S=-0.14, F=-0.03, T=24.2%, INFERIOR (TOP3000)
- `rank(-1 * snt_social_volume / close)`: S=-0.05, F=-0.01, T=22.1%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 25F/0P
- LOW_SHARPE: 25F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.44, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.76 (negative), ret=-1.8%
  - 2020: S=-1.36 (negative), ret=-4.7%
  - 2021: S=0.74 (moderate), ret=+4.5%
  - 2022: S=2.31 (strong), ret=+10.8%
  - 2023: S=0.11 (weak), ret=+0.3%

## Risk & Drawdown
- Max drawdown: 12.67% over 1168 days (recovered)
- Annualized: return +1.8%, volatility 4.2% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.33, excess kurtosis +3.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.30, max 3.02, latest 0.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.07%; worst month: -2.50%
Positive months: 41%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.07
- Sideways: S=-0.89
- Bear: S=-0.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(snt_social_volume, 5))` S=0.40, F=0.10, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * snt_social_volume)`: S=-0.14, F=-0.03, T=24.2%, INFERIOR (TOP3000)
- `rank(-1 * snt_social_volume / close)`: S=-0.05, F=-0.01, T=22.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(snt_social_volume, 5))`: S=0.40, F=0.10, T=31.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(snt_social_volume)` | TOP1000 | 0.42 | 0.13 | 8.5% | 60% | mixed |
| `rank(snt_social_volume)` | TOP3000 | 0.44 | 0.13 | 12.7% | 60% | bull-only |
| `rank(snt_social_volume)` | TOP500 | 0.14 | 0.03 | 12.0% | 60% | bull-only |
| `rank(snt_social_volume)` | TOP200 | 0.11 | 0.02 | 15.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- rank(fnd6_acdo) * rank(volume/adv20): 0.515 (moderately positively correlated)
- fnd6_newqv1300_rectrq: 0.462 (moderately positively correlated)
- fnd6_dpvieb: 0.458 (moderately positively correlated)
- fnd6_newa1v1300_dpact: 0.456 (moderately positively correlated)
- fnd6_rectr: 0.453 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
