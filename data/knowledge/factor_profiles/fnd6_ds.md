---
field: fnd6_ds
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.59
best_fitness: 0.48
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: mixed
n_variations_with_pnl: 12
max_drawdown: 0.2507
ann_vol: 0.1462
hit_rate: 0.4729
rolling_sharpe_min: -1.768
rolling_sharpe_max: 2.407
negated_best_sharpe: 0.14
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 4
direction_gap: -0.45
---
# fnd6_ds (fundamental6)

*Debt - Subordinated*

## Signal Profile
- `rank(fnd6_ds)`: S=0.61, F=0.44, T=2.7%, INFERIOR (TOP500)
- `rank(fnd6_ds / close)`: S=0.60, F=0.44, T=2.7%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_ds, 5))`: S=0.59, F=0.48, T=13.2%, INFERIOR (TOP500)
- `-rank(fnd6_ds)`: S=-0.51, F=-0.29, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ds, 5))`: S=0.14, F=0.05, T=16.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_ds, 22)`: S=0.33, F=0.13, T=4.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ds, 10)`: S=0.26, F=0.11, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ds, 22))`: S=-0.22, F=-0.12, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ds)`: S=-0.75, F=-0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ds / close)`: S=-0.75, F=-0.42, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/14P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.58, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.85 (strong), ret=+13.7%
  - 2020: S=-0.67 (negative), ret=-7.5%
  - 2021: S=0.64 (moderate), ret=+14.3%
  - 2022: S=2.23 (strong), ret=+23.8%
  - 2023: S=-0.17 (negative), ret=-2.6%

## Risk & Drawdown
- Max drawdown: 25.07% over 484 days (recovered)
- Annualized: return +8.5%, volatility 14.6% (fraction of booksize)
- Hit rate: 47.3% positive days
- Tail shape: skew +0.47, excess kurtosis +51.64

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.77, max 2.41, latest -0.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.93%; worst month: -7.51%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.40
- Sideways: S=0.10
- Bear: S=-0.12

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_ds, 5))` S=0.14, F=0.05, INFERIOR
Direction gap: -0.45 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_ds)`: S=-0.75, F=-0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ds / close)`: S=-0.75, F=-0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ds, 5))`: S=0.14, F=0.05, T=16.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_ds, 5))` | TOP500 | 0.58 | 0.48 | 25.1% | 60% | mixed |
| `rank(fnd6_ds / close)` | TOP500 | 0.61 | 0.44 | 19.2% | 80% | mixed |
| `rank(fnd6_ds)` | TOP500 | 0.61 | 0.44 | 19.0% | 80% | mixed |
| `rank(fnd6_ds)` | TOP3000 | 0.75 | 0.42 | 8.6% | 60% | all-weather |
| `rank(fnd6_ds / close)` | TOP3000 | 0.75 | 0.42 | 8.6% | 60% | all-weather |
| `rank(ts_delta(fnd6_ds, 5))` | TOP1000 | 0.49 | 0.37 | 19.6% | 80% | all-weather |
| `rank(fnd6_ds / close)` | TOP200 | 0.45 | 0.31 | 17.1% | 80% | bear-only |
| `rank(fnd6_ds)` | TOP200 | 0.45 | 0.31 | 17.1% | 80% | bear-only |
| `rank(fnd6_ds / close)` | TOP1000 | 0.51 | 0.30 | 13.4% | 60% | all-weather |
| `rank(fnd6_ds)` | TOP1000 | 0.51 | 0.29 | 13.2% | 60% | all-weather |
| `rank(ts_delta(fnd6_ds, 5))` | TOP200 | 0.39 | 0.23 | 39.3% | 60% | mixed |
| `rank(ts_delta(fnd6_ds, 5))` | TOP3000 | 0.29 | 0.14 | 16.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_aocipen: 0.299 (weakly positively correlated)
- fnd6_dvpa: 0.276 (weakly positively correlated)
- fnd6_lifr: 0.267 (weakly positively correlated)
- fnd6_esopnr: 0.247 (weakly positively correlated)
- fnd6_newa1v1300_dcom: 0.244 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
