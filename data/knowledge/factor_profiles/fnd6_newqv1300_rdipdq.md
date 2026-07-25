---
field: fnd6_newqv1300_rdipdq
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.57
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.2188
ann_vol: 0.1933
hit_rate: 0.4761
rolling_sharpe_min: -0.089
rolling_sharpe_max: 2.12
negated_best_sharpe: 0.57
negated_best_template: neg_rank_level
negated_best_fitness: 0.5
n_negated_sims: 10
direction_gap: 0.0
---
# fnd6_newqv1300_rdipdq (fundamental6)

*In Process R&D Expense Diluted EPS Effect*

## Signal Profile
- `rank(fnd6_newqv1300_rdipdq)`: S=-0.20, F=-0.11, T=4.1%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_rdipdq / close)`: S=-0.17, F=-0.08, T=4.1%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_rdipdq, 5))`: S=0.57, F=0.40, T=22.4%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_rdipdq)`: S=0.24, F=0.13, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rdipdq, 5))`: S=-0.40, F=-0.25, T=19.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_rdipdq, 22)`: S=0.19, F=0.13, T=12.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_rdipdq, 10)`: S=-0.32, F=-0.24, T=3.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_rdipdq, 22))`: S=0.19, F=0.11, T=16.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rdipdq)`: S=0.57, F=0.50, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rdipdq / close)`: S=0.57, F=0.50, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.57, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.32 (weak), ret=+5.9%
  - 2020: S=0.82 (moderate), ret=+14.0%
  - 2021: S=0.28 (weak), ret=+6.9%
  - 2022: S=0.86 (moderate), ret=+17.8%
  - 2023: S=0.81 (moderate), ret=+9.7%

## Risk & Drawdown
- Max drawdown: 21.88% over 235 days (recovered)
- Annualized: return +11.1%, volatility 19.3% (fraction of booksize)
- Hit rate: 47.6% positive days
- Tail shape: skew -0.03, excess kurtosis +23.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.09, max 2.12, latest 0.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +22.04%; worst month: -17.00%
Positive months: 48%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.64
- Sideways: S=0.62
- Bear: S=0.46

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_rdipdq)` S=0.57, F=0.50, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_rdipdq)`: S=0.57, F=0.50, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rdipdq / close)`: S=0.57, F=0.50, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rdipdq, 5))`: S=-0.40, F=-0.25, T=19.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_rdipdq, 5))` | TOP3000 | 0.57 | 0.40 | 21.9% | 100% | mixed |
| `rank(ts_delta(fnd6_newqv1300_rdipdq, 5))` | TOP500 | 0.54 | 0.39 | 21.4% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_rdipdq, 5))` | TOP200 | 0.34 | 0.20 | 29.6% | 40% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_rdipdq, 5))` | TOP1000 | 0.17 | 0.07 | 33.4% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_rdipepsq: 0.531 (moderately positively correlated)
- fnd6_newqv1300_rdipaq: 0.481 (moderately positively correlated)
- fnd6_newqv1300_rdipq: 0.296 (weakly positively correlated)
- min_capital_expenditure_guidance: 0.111 (weakly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: -0.109 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
