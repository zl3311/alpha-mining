---
field: fnd6_newqv1300_aocipenq
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 0.75
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1536
ann_vol: 0.1117
hit_rate: 0.4996
rolling_sharpe_min: -0.667
rolling_sharpe_max: 2.076
negated_best_sharpe: 0.75
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.46
n_negated_sims: 10
direction_gap: 0.24
---
# fnd6_newqv1300_aocipenq (fundamental6)

*Accum Other Comp Inc - Min Pension Liab Adj*

## Signal Profile
- `rank(fnd6_newqv1300_aocipenq)`: S=0.21, F=0.10, T=10.2%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_aocipenq / close)`: S=0.19, F=0.09, T=10.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_aocipenq, 5))`: S=0.51, F=0.17, T=51.6%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_aocipenq)`: S=0.42, F=0.21, T=7.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aocipenq, 5))`: S=-0.51, F=-0.17, T=51.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_aocipenq, 63)`: S=0.43, F=0.14, T=21.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_aocipenq, 10)`: S=0.06, F=0.01, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_aocipenq, 22))`: S=-0.06, F=-0.01, T=22.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aocipenq)`: S=0.64, F=0.37, T=6.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aocipenq / close)`: S=0.75, F=0.46, T=6.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.51, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.35 (weak), ret=+2.9%
  - 2020: S=1.05 (moderate), ret=+14.3%
  - 2021: S=0.08 (weak), ret=+0.8%
  - 2022: S=0.77 (moderate), ret=+8.7%
  - 2023: S=0.12 (weak), ret=+1.2%

## Risk & Drawdown
- Max drawdown: 15.36% over 375 days (not yet recovered, ongoing at window end)
- Annualized: return +5.7%, volatility 11.2% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +1.20, excess kurtosis +10.81

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.67, max 2.08, latest 0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +7.20%; worst month: -5.84%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.90
- Sideways: S=-0.30
- Bear: S=-0.34

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_aocipenq / close)` S=0.75, F=0.46, INFERIOR
Direction gap: +0.24 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_aocipenq)`: S=0.64, F=0.37, T=6.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aocipenq / close)`: S=0.75, F=0.46, T=6.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aocipenq, 5))`: S=-0.51, F=-0.17, T=51.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_aocipenq, 5))` | TOP3000 | 0.51 | 0.17 | 15.4% | 100% | mixed |
| `rank(ts_delta(fnd6_newqv1300_aocipenq, 5))` | TOP1000 | 0.33 | 0.11 | 39.7% | 60% | mixed |
| `rank(fnd6_newqv1300_aocipenq)` | TOP200 | 0.22 | 0.10 | 40.7% | 60% | bear-only |
| `rank(fnd6_newqv1300_aocipenq / close)` | TOP200 | 0.20 | 0.09 | 40.2% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_dxd2: 0.223 (weakly positively correlated)
- fnd6_dd2: 0.218 (weakly positively correlated)
- fnd6_newqv1300_rcpq: 0.217 (weakly positively correlated)
- fnd6_dd3: 0.211 (weakly positively correlated)
- fnd6_dxd3: 0.210 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
