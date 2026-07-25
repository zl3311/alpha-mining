---
field: fnd6_newqv1300_ibadj12
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.77
best_fitness: 0.4
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 1
max_drawdown: 0.2441
ann_vol: 0.1331
hit_rate: 0.5231
rolling_sharpe_min: -0.492
rolling_sharpe_max: 2.85
negated_best_sharpe: 0.95
negated_best_template: rank_neg_delta
negated_best_fitness: 0.35
n_negated_sims: 10
direction_gap: 0.18
---
# fnd6_newqv1300_ibadj12 (fundamental6)

*Income Before Extra Items - Adj for Common Stock Equivalents - 12MM*

## Signal Profile
- `rank(fnd6_newqv1300_ibadj12)`: S=-0.21, F=-0.08, T=2.2%, INFERIOR (TOP500)
- `rank(fnd6_newqv1300_ibadj12 / close)`: S=-0.18, F=-0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_ibadj12, 5))`: S=0.77, F=0.40, T=37.4%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_ibadj12)`: S=0.55, F=0.32, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ibadj12, 5))`: S=0.95, F=0.35, T=38.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_ibadj12, 63)`: S=0.82, F=0.36, T=18.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ibadj12, 10)`: S=-0.63, F=-0.38, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ibadj12, 22))`: S=-1.12, F=-0.63, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ibadj12)`: S=0.25, F=0.11, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ibadj12 / close)`: S=0.18, F=0.06, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.77, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.12 (weak), ret=+1.1%
  - 2020: S=0.44 (weak), ret=+4.3%
  - 2021: S=0.51 (moderate), ret=+9.6%
  - 2022: S=1.98 (strong), ret=+25.0%
  - 2023: S=0.84 (moderate), ret=+10.4%

## Risk & Drawdown
- Max drawdown: 24.41% over 210 days (recovered)
- Annualized: return +10.3%, volatility 13.3% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew -0.17, excess kurtosis +5.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.49, max 2.85, latest 0.91

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +13.18%; worst month: -7.70%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.05
- Sideways: S=0.23
- Bear: S=0.95

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_ibadj12, 5))` S=0.95, F=0.35, INFERIOR
Direction gap: +0.18 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ibadj12)`: S=0.25, F=0.11, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ibadj12 / close)`: S=0.18, F=0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ibadj12, 5))`: S=0.95, F=0.35, T=38.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_ibadj12, 5))` | TOP200 | 0.77 | 0.40 | 24.4% | 100% | all-weather |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_epsx12: 0.490 (moderately positively correlated)
- fnd6_cptnewqv1300_epsf12: 0.476 (moderately positively correlated)
- fnd6_newqv1300_reunaq: 0.242 (weakly positively correlated)
- retained_earnings: 0.151 (weakly positively correlated)
- fnd6_cptnewqv1300_req: 0.151 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
