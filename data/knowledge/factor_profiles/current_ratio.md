---
field: current_ratio
dataset: fundamental6
cluster: fundamental6_ratio
coverage: 0.5
community_alphas: 6905
best_template: rank_delta
best_sharpe: 1.67
best_fitness: 1.15
best_universe: TOP500
grade: AVERAGE
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.1035
ann_vol: 0.1053
hit_rate: 0.5522
rolling_sharpe_min: -0.719
rolling_sharpe_max: 4.444
top_merge_partner: fnd6_city
negated_best_sharpe: 0.7
negated_best_template: neg_rank_level
negated_best_fitness: 0.45
n_negated_sims: 10
direction_gap: -0.97
---
# current_ratio (fundamental6)

*Current Ratio*

## Signal Profile
- `rank(current_ratio)`: S=0.39, F=0.20, T=2.9%, INFERIOR (TOP500)
- `rank(current_ratio / close)`: S=0.20, F=0.08, T=3.0%, INFERIOR (TOP500)
- `rank(ts_delta(current_ratio, 5))`: S=1.67, F=1.15, T=37.0%, AVERAGE (TOP500)
- `-rank(current_ratio)`: S=0.22, F=0.09, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(current_ratio, 5))`: S=-0.08, F=-0.01, T=37.8%, INFERIOR (TOP3000)
- `ts_zscore(current_ratio, 22)`: S=0.49, F=0.18, T=38.2%, INFERIOR (TOP3000)
- `ts_mean(current_ratio, 10)`: S=-0.04, F=-0.01, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_rank(current_ratio, 22))`: S=0.35, F=0.11, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * current_ratio)`: S=0.70, F=0.45, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * current_ratio / close)`: S=0.14, F=0.06, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.66, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.41 (weak), ret=+3.1%
  - 2020: S=0.78 (moderate), ret=+9.9%
  - 2021: S=1.85 (strong), ret=+19.7%
  - 2022: S=3.27 (strong), ret=+35.9%
  - 2023: S=1.99 (strong), ret=+17.2%

## Risk & Drawdown
- Max drawdown: 10.35% over 365 days (recovered)
- Annualized: return +17.5%, volatility 10.5% (fraction of booksize)
- Hit rate: 55.2% positive days
- Tail shape: skew +0.91, excess kurtosis +9.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.72, max 4.44, latest 2.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +9.42%; worst month: -4.66%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.46
- Sideways: S=1.03
- Bear: S=1.55

## Negated Direction
Best negated: `rank(-1 * current_ratio)` S=0.70, F=0.45, INFERIOR
Direction gap: -0.97 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * current_ratio)`: S=0.70, F=0.45, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * current_ratio / close)`: S=0.14, F=0.06, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(current_ratio, 5))`: S=-0.08, F=-0.01, T=37.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(current_ratio, 5))` | TOP500 | 1.66 | 1.15 | 10.3% | 100% | all-weather |
| `rank(ts_delta(current_ratio, 5))` | TOP1000 | 0.97 | 0.45 | 8.6% | 80% | all-weather |
| `rank(ts_delta(current_ratio, 5))` | TOP200 | 0.69 | 0.35 | 27.8% | 100% | all-weather |
| `rank(current_ratio)` | TOP500 | 0.40 | 0.20 | 20.3% | 60% | bear-only |
| `rank(current_ratio / close)` | TOP500 | 0.20 | 0.08 | 32.3% | 40% | bear-only |
| `rank(current_ratio / close)` | TOP200 | 0.18 | 0.07 | 27.6% | 60% | bear-only |
| `rank(current_ratio)` | TOP200 | 0.15 | 0.04 | 22.1% | 60% | bear-only |

## Correlation Notes
Top correlates:
- retained_earnings: -0.145 (weakly negatively correlated)
- fnd6_cptnewqv1300_req: -0.145 (weakly negatively correlated)
- fnd6_newqv1300_acomincq: 0.133 (weakly positively correlated)
- fnd6_newqv1300_ibadj12: 0.125 (weakly positively correlated)
- fnd6_ivst: -0.122 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_city | fundamental_rare_event | -0.07 | 2.31 | +0.64 | +0.84 | yes |
| implied_volatility_mean_150 | option8 | -0.07 | 2.29 | +0.63 | +0.22 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | +0.03 | 2.29 | +0.63 | +0.04 | yes |
| implied_volatility_put_120 | option8 | -0.05 | 2.27 | +0.61 | +0.25 | yes |
| implied_volatility_mean_120 | option8 | -0.05 | 2.26 | +0.60 | +0.28 | yes |

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
