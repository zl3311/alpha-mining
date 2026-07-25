---
field: fscore_bfl_surface
dataset: model16
best_template: ts_zscore
best_sharpe: 0.73
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.1172
ann_vol: 0.044
hit_rate: 0.4729
rolling_sharpe_min: -2.085
rolling_sharpe_max: 2.339
negated_best_sharpe: 0.49
negated_best_template: neg_rank_level
negated_best_fitness: 0.24
n_negated_sims: 4
direction_gap: -0.24
---
# fscore_bfl_surface (model16)

*Static composite “style surface” score aggregating the five primary style scores; larger surface implies higher rank*

## Signal Profile
- `rank(fscore_bfl_surface)`: S=-0.34, F=-0.14, T=3.2%, INFERIOR (TOP1000)
- `rank(ts_delta(fscore_bfl_surface, 5))`: S=0.27, F=0.07, T=15.4%, INFERIOR (TOP500)
- `-rank(fscore_bfl_surface)`: S=0.34, F=0.14, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_surface, 5))`: S=-0.39, F=-0.14, T=14.8%, INFERIOR (TOP3000)
- `ts_zscore(fscore_bfl_surface, 22)`: S=0.73, F=0.29, T=11.7%, INFERIOR (TOP3000)
- `ts_mean(fscore_bfl_surface, 10)`: S=-0.30, F=-0.12, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fscore_bfl_surface, 22))`: S=0.59, F=0.21, T=9.5%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_surface)`: S=0.49, F=0.24, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_surface / close)`: S=-0.35, F=-0.16, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/11P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.27, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.49 (moderate), ret=+4.9%
  - 2020: S=-1.65 (negative), ret=-7.2%
  - 2021: S=0.19 (weak), ret=+1.0%
  - 2022: S=-0.01 (negative), ret=-0.0%
  - 2023: S=1.92 (strong), ret=+7.1%

## Risk & Drawdown
- Max drawdown: 11.72% over 1513 days (not yet recovered, ongoing at window end)
- Annualized: return +1.2%, volatility 4.4% (fraction of booksize)
- Hit rate: 47.3% positive days
- Tail shape: skew -0.02, excess kurtosis +2.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.08, max 2.34, latest 2.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +3.00%; worst month: -3.03%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=0.60
- Sideways: S=0.84
- Bear: S=-0.58

## Negated Direction
Best negated: `rank(-1 * fscore_bfl_surface)` S=0.49, F=0.24, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fscore_bfl_surface)`: S=0.49, F=0.24, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_surface / close)`: S=-0.35, F=-0.16, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_surface, 5))`: S=-0.39, F=-0.14, T=14.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fscore_bfl_surface, 5))` | TOP500 | 0.27 | 0.07 | 11.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fscore_bfl_total: 0.944 (strongly positively correlated)
- fscore_bfl_surface_accel: 0.888 (strongly positively correlated)
- fscore_bfl_growth: 0.769 (strongly positively correlated)
- fscore_bfl_momentum: 0.461 (moderately positively correlated)
- min_free_cashflow_per_share_guidance: 0.336 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
