---
field: fscore_bfl_momentum
dataset: model16
best_template: neg_rank_level
best_sharpe: 0.47
best_fitness: 0.2
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.0951
ann_vol: 0.0692
hit_rate: 0.4704
rolling_sharpe_min: -0.99
rolling_sharpe_max: 1.992
negated_best_sharpe: 0.47
negated_best_template: neg_rank_level
negated_best_fitness: 0.2
n_negated_sims: 4
direction_gap: 0.12
---
# fscore_bfl_momentum (model16)

*Composite momentum measure reflecting recent price dynamics and analyst estimate revisions to identify improving or deteriorating names*

## Signal Profile
- `rank(fscore_bfl_momentum)`: S=0.20, F=0.07, T=5.9%, INFERIOR (TOP200)
- `rank(ts_delta(fscore_bfl_momentum, 5))`: S=0.35, F=0.14, T=15.6%, INFERIOR (TOP200)
- `-rank(fscore_bfl_momentum)`: S=0.19, F=0.06, T=5.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_momentum, 5))`: S=-0.50, F=-0.22, T=15.1%, INFERIOR (TOP3000)
- `ts_zscore(fscore_bfl_momentum, 22)`: S=0.21, F=0.05, T=10.7%, INFERIOR (TOP3000)
- `ts_mean(fscore_bfl_momentum, 10)`: S=-0.21, F=-0.07, T=4.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fscore_bfl_momentum, 22))`: S=0.30, F=0.08, T=9.7%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_momentum)`: S=0.47, F=0.20, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_momentum / close)`: S=-0.39, F=-0.18, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/11P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.36, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=2.00 (strong), ret=+11.4%
  - 2020: S=-0.02 (negative), ret=-0.1%
  - 2021: S=-0.03 (negative), ret=-0.2%
  - 2022: S=-0.37 (negative), ret=-2.5%
  - 2023: S=0.72 (moderate), ret=+3.6%

## Risk & Drawdown
- Max drawdown: 9.51% over 989 days (not yet recovered, ongoing at window end)
- Annualized: return +2.5%, volatility 6.9% (fraction of booksize)
- Hit rate: 47.0% positive days
- Tail shape: skew +0.31, excess kurtosis +3.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 1.99, latest 0.77

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +4.87%; worst month: -3.43%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.40
- Sideways: S=-0.04
- Bear: S=-0.41

## Negated Direction
Best negated: `rank(-1 * fscore_bfl_momentum)` S=0.47, F=0.20, INFERIOR
Direction gap: +0.12 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fscore_bfl_momentum)`: S=0.47, F=0.20, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_momentum / close)`: S=-0.39, F=-0.18, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_momentum, 5))`: S=-0.50, F=-0.22, T=15.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fscore_bfl_momentum, 5))` | TOP200 | 0.36 | 0.14 | 9.5% | 40% | mixed |
| `rank(fscore_bfl_momentum)` | TOP200 | 0.23 | 0.07 | 19.4% | 80% | mixed |
| `rank(ts_delta(fscore_bfl_momentum, 5))` | TOP500 | 0.17 | 0.04 | 13.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fscore_bfl_total: 0.468 (moderately positively correlated)
- fscore_bfl_surface: 0.461 (moderately positively correlated)
- fscore_bfl_surface_accel: 0.438 (moderately positively correlated)
- fnd6_itcb: 0.394 (weakly positively correlated)
- anl4_cfi_low: -0.360 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
