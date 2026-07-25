---
field: fscore_bfl_surface_accel
dataset: model16
best_template: rank_delta
best_sharpe: 0.39
best_fitness: 0.13
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1229
ann_vol: 0.0442
hit_rate: 0.4753
rolling_sharpe_min: -2.273
rolling_sharpe_max: 2.621
negated_best_sharpe: 0.11
negated_best_template: neg_rank_level
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.28
---
# fscore_bfl_surface_accel (model16)

*Acceleration (derivative) of the pentagon surface score relative to the previous month*

## Signal Profile
- `rank(fscore_bfl_surface_accel)`: S=0.23, F=0.05, T=6.8%, INFERIOR (TOP1000)
- `rank(ts_delta(fscore_bfl_surface_accel, 5))`: S=0.39, F=0.13, T=15.4%, INFERIOR (TOP500)
- `-rank(fscore_bfl_surface_accel)`: S=-0.23, F=-0.05, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_surface_accel, 5))`: S=-0.45, F=-0.17, T=14.8%, INFERIOR (TOP3000)
- `-ts_zscore(fscore_bfl_surface_accel, 63)`: S=0.07, F=0.01, T=8.8%, INFERIOR (TOP3000)
- `ts_mean(fscore_bfl_surface_accel, 10)`: S=0.03, F=0.00, T=6.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fscore_bfl_surface_accel, 22))`: S=0.17, F=0.03, T=9.0%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_surface_accel)`: S=0.11, F=0.02, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_surface_accel / close)`: S=-0.52, F=-0.30, T=3.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/11P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/4P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.39, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.59 (strong), ret=+8.8%
  - 2020: S=-1.70 (negative), ret=-7.8%
  - 2021: S=0.13 (weak), ret=+0.7%
  - 2022: S=0.90 (moderate), ret=+3.7%
  - 2023: S=0.84 (moderate), ret=+3.1%

## Risk & Drawdown
- Max drawdown: 12.29% over 1300 days (recovered)
- Annualized: return +1.7%, volatility 4.4% (fraction of booksize)
- Hit rate: 47.5% positive days
- Tail shape: skew +0.12, excess kurtosis +2.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.27, max 2.62, latest 0.93

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +2.74%; worst month: -3.43%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.24
- Sideways: S=1.09
- Bear: S=-1.04

## Negated Direction
Best negated: `rank(-1 * fscore_bfl_surface_accel)` S=0.11, F=0.02, INFERIOR
Direction gap: -0.28 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fscore_bfl_surface_accel)`: S=0.11, F=0.02, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_surface_accel / close)`: S=-0.52, F=-0.30, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_surface_accel, 5))`: S=-0.45, F=-0.17, T=14.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fscore_bfl_surface_accel, 5))` | TOP500 | 0.39 | 0.13 | 12.3% | 80% | bull-only |
| `rank(fscore_bfl_surface_accel)` | TOP1000 | 0.23 | 0.05 | 5.4% | 60% | mixed |

## Correlation Notes
Top correlates:
- fscore_bfl_total: 0.968 (strongly positively correlated)
- fscore_bfl_surface: 0.888 (strongly positively correlated)
- fscore_bfl_growth: 0.711 (strongly positively correlated)
- fscore_bfl_momentum: 0.438 (moderately positively correlated)
- min_free_cashflow_per_share_guidance: 0.341 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
