---
field: fnd6_newqv1300_rdipepsq
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.5
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.2541
ann_vol: 0.1999
hit_rate: 0.4891
rolling_sharpe_min: -0.795
rolling_sharpe_max: 2.467
negated_best_sharpe: 0.5
negated_best_template: neg_rank_level
negated_best_fitness: 0.43
n_negated_sims: 10
direction_gap: 0.03
---
# fnd6_newqv1300_rdipepsq (fundamental6)

*In-Process R&D Expense Basic EPS Effect*

## Signal Profile
- `rank(fnd6_newqv1300_rdipepsq)`: S=-0.15, F=-0.07, T=4.4%, INFERIOR (TOP1000)
- `rank(fnd6_newqv1300_rdipepsq / close)`: S=-0.15, F=-0.07, T=4.4%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_rdipepsq, 5))`: S=0.47, F=0.32, T=19.9%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_rdipepsq)`: S=0.15, F=0.07, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rdipepsq, 5))`: S=-0.45, F=-0.28, T=22.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_rdipepsq, 63)`: S=-0.10, F=-0.05, T=11.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_rdipepsq, 10)`: S=-0.28, F=-0.20, T=3.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_rdipepsq, 22))`: S=0.15, F=0.08, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rdipepsq)`: S=0.50, F=0.43, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rdipepsq / close)`: S=0.49, F=0.42, T=4.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.47, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.06 (negative), ret=-1.1%
  - 2020: S=0.41 (weak), ret=+9.0%
  - 2021: S=1.24 (moderate), ret=+27.4%
  - 2022: S=0.44 (weak), ret=+9.9%
  - 2023: S=0.06 (weak), ret=+0.6%

## Risk & Drawdown
- Max drawdown: 25.41% over 319 days (recovered)
- Annualized: return +9.3%, volatility 20.0% (fraction of booksize)
- Hit rate: 48.9% positive days
- Tail shape: skew +1.82, excess kurtosis +27.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.80, max 2.47, latest 0.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +24.12%; worst month: -20.44%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.46
- Sideways: S=0.67
- Bear: S=-0.62

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_rdipepsq)` S=0.50, F=0.43, INFERIOR
Direction gap: +0.03 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_rdipepsq)`: S=0.50, F=0.43, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rdipepsq / close)`: S=0.49, F=0.42, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rdipepsq, 5))`: S=-0.45, F=-0.28, T=22.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_rdipepsq, 5))` | TOP500 | 0.47 | 0.32 | 25.4% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_rdipepsq, 5))` | TOP3000 | 0.46 | 0.30 | 24.2% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_rdipepsq, 5))` | TOP200 | 0.26 | 0.13 | 32.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_rdipaq: 0.856 (strongly positively correlated)
- fnd6_newqv1300_rdipdq: 0.531 (moderately positively correlated)
- fnd6_newqv1300_rdipq: 0.495 (moderately positively correlated)
- fnd6_txdbcl: 0.173 (weakly positively correlated)
- fnd6_optvol: -0.135 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
