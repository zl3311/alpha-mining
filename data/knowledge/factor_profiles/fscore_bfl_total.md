---
field: fscore_bfl_total
dataset: model16
best_template: neg_rank_level
best_sharpe: 0.46
best_fitness: 0.2
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.1134
ann_vol: 0.0445
hit_rate: 0.4721
rolling_sharpe_min: -2.042
rolling_sharpe_max: 2.193
negated_best_sharpe: 0.46
negated_best_template: neg_rank_level
negated_best_fitness: 0.2
n_negated_sims: 4
direction_gap: -0.03
---
# fscore_bfl_total (model16)

*Blended composite M-Score combining the static pentagon surface score and its acceleration into an overarching rating*

## Signal Profile
- `rank(fscore_bfl_total)`: S=-0.23, F=-0.07, T=5.1%, INFERIOR (TOP1000)
- `rank(ts_delta(fscore_bfl_total, 5))`: S=0.40, F=0.14, T=15.5%, INFERIOR (TOP500)
- `-rank(fscore_bfl_total)`: S=0.23, F=0.07, T=5.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_total, 5))`: S=-0.44, F=-0.17, T=14.8%, INFERIOR (TOP3000)
- `ts_zscore(fscore_bfl_total, 22)`: S=0.49, F=0.15, T=10.4%, INFERIOR (TOP3000)
- `ts_mean(fscore_bfl_total, 10)`: S=-0.27, F=-0.09, T=4.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fscore_bfl_total, 22))`: S=0.46, F=0.14, T=9.1%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_total)`: S=0.46, F=0.20, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_total / close)`: S=-0.39, F=-0.19, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/11P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/4P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.40, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.16 (strong), ret=+7.4%
  - 2020: S=-1.53 (negative), ret=-7.1%
  - 2021: S=0.21 (weak), ret=+1.1%
  - 2022: S=0.76 (moderate), ret=+3.2%
  - 2023: S=1.08 (moderate), ret=+4.0%

## Risk & Drawdown
- Max drawdown: 11.34% over 1243 days (recovered)
- Annualized: return +1.8%, volatility 4.5% (fraction of booksize)
- Hit rate: 47.2% positive days
- Tail shape: skew +0.07, excess kurtosis +2.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.04, max 2.19, latest 1.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +2.78%; worst month: -3.33%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.18
- Sideways: S=0.72
- Bear: S=-0.65

## Negated Direction
Best negated: `rank(-1 * fscore_bfl_total)` S=0.46, F=0.20, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fscore_bfl_total)`: S=0.46, F=0.20, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_total / close)`: S=-0.39, F=-0.19, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_total, 5))`: S=-0.44, F=-0.17, T=14.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fscore_bfl_total, 5))` | TOP500 | 0.40 | 0.14 | 11.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fscore_bfl_surface_accel: 0.968 (strongly positively correlated)
- fscore_bfl_surface: 0.944 (strongly positively correlated)
- fscore_bfl_growth: 0.740 (strongly positively correlated)
- fscore_bfl_momentum: 0.468 (moderately positively correlated)
- min_free_cashflow_per_share_guidance: 0.334 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
