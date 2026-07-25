---
field: est_tbv_ps
dataset: analyst4
best_template: rank_level
best_sharpe: 0.66
best_fitness: 0.36
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0643
ann_vol: 0.056
hit_rate: 0.5287
rolling_sharpe_min: -0.756
rolling_sharpe_max: 2.73
negated_best_sharpe: 0.28
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.38
---
# est_tbv_ps (analyst4)

*Tangible Book Value per Share - mean of estimations*

## Signal Profile
- `rank(est_tbv_ps)`: S=0.66, F=0.36, T=1.5%, INFERIOR (TOP500)
- `rank(est_tbv_ps / close)`: S=0.58, F=0.34, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(est_tbv_ps, 5))`: S=0.29, F=0.08, T=35.4%, INFERIOR (TOP1000)
- `-rank(est_tbv_ps)`: S=-0.35, F=-0.13, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_tbv_ps, 5))`: S=0.28, F=0.08, T=34.1%, INFERIOR (TOP3000)
- `-ts_zscore(est_tbv_ps, 63)`: S=0.42, F=0.18, T=15.9%, INFERIOR (TOP3000)
- `ts_mean(est_tbv_ps, 10)`: S=-0.53, F=-0.48, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(est_tbv_ps, 22))`: S=0.21, F=0.06, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * est_tbv_ps)`: S=-0.66, F=-0.36, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * est_tbv_ps / close)`: S=-0.42, F=-0.21, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.64, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.78 (moderate), ret=+3.1%
  - 2020: S=-0.17 (negative), ret=-1.0%
  - 2021: S=0.43 (weak), ret=+2.6%
  - 2022: S=-0.44 (negative), ret=-2.5%
  - 2023: S=2.74 (strong), ret=+15.6%

## Risk & Drawdown
- Max drawdown: 6.43% over 549 days (recovered)
- Annualized: return +3.6%, volatility 5.6% (fraction of booksize)
- Hit rate: 52.9% positive days
- Tail shape: skew +0.32, excess kurtosis +2.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.76, max 2.73, latest 2.73

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +3.28%; worst month: -3.22%
Positive months: 68%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.00
- Sideways: S=1.00
- Bear: S=-0.02

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_tbv_ps, 5))` S=0.28, F=0.08, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * est_tbv_ps)`: S=-0.66, F=-0.36, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * est_tbv_ps / close)`: S=-0.42, F=-0.21, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_tbv_ps, 5))`: S=0.28, F=0.08, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_tbv_ps)` | TOP500 | 0.64 | 0.36 | 6.4% | 60% | mixed |
| `rank(est_tbv_ps / close)` | TOP3000 | 0.58 | 0.34 | 14.6% | 80% | all-weather |
| `rank(est_tbv_ps / close)` | TOP500 | 0.41 | 0.21 | 10.4% | 40% | mixed |
| `rank(est_tbv_ps / close)` | TOP1000 | 0.41 | 0.21 | 16.7% | 80% | all-weather |
| `rank(est_tbv_ps)` | TOP1000 | 0.34 | 0.13 | 11.3% | 40% | bull-only |
| `rank(ts_delta(est_tbv_ps, 5))` | TOP1000 | 0.29 | 0.08 | 18.7% | 60% | mixed |
| `rank(est_tbv_ps)` | TOP3000 | 0.26 | 0.08 | 9.3% | 60% | bull-only |
| `rank(ts_delta(est_tbv_ps, 5))` | TOP3000 | 0.32 | 0.07 | 12.7% | 60% | weak |
| `rank(ts_delta(est_tbv_ps, 5))` | TOP200 | 0.13 | 0.03 | 32.9% | 60% | weak |

## Correlation Notes
Top correlates:
- max_ebitda_guidance: -0.202 (weakly negatively correlated)
- fnd6_aldo: 0.199 (weakly positively correlated)
- anl4_ebitda_std: 0.195 (weakly positively correlated)
- min_ebitda_guidance: -0.194 (weakly negatively correlated)
- anl4_afv4_dts_spe: 0.193 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
