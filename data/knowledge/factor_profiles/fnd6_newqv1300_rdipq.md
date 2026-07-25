---
field: fnd6_newqv1300_rdipq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.78
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.4265
ann_vol: 0.1925
hit_rate: 0.4615
rolling_sharpe_min: -2.245
rolling_sharpe_max: 2.392
negated_best_sharpe: 0.78
negated_best_template: rank_neg_delta
negated_best_fitness: 0.62
n_negated_sims: 10
direction_gap: 0.66
---
# fnd6_newqv1300_rdipq (fundamental6)

*In Process R&D*

## Signal Profile
- `rank(fnd6_newqv1300_rdipq)`: S=-0.14, F=-0.06, T=3.9%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_rdipq / close)`: S=-0.13, F=-0.06, T=3.9%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_rdipq, 5))`: S=0.12, F=0.04, T=19.6%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_rdipq)`: S=0.31, F=0.19, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rdipq, 5))`: S=0.78, F=0.62, T=24.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_rdipq, 63)`: S=-0.01, F=0.00, T=12.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_rdipq, 10)`: S=-0.57, F=-0.52, T=3.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_rdipq, 22))`: S=-0.69, F=-0.63, T=17.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rdipq)`: S=0.31, F=0.19, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rdipq / close)`: S=0.31, F=0.19, T=4.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/15P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.11, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.16 (negative), ret=-1.8%
  - 2020: S=0.59 (moderate), ret=+15.9%
  - 2021: S=1.04 (moderate), ret=+24.1%
  - 2022: S=-0.28 (negative), ret=-4.5%
  - 2023: S=-2.07 (negative), ret=-23.0%

## Risk & Drawdown
- Max drawdown: 42.65% over 665 days (not yet recovered, ongoing at window end)
- Annualized: return +2.2%, volatility 19.2% (fraction of booksize)
- Hit rate: 46.2% positive days
- Tail shape: skew +1.73, excess kurtosis +30.00

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.25, max 2.39, latest -2.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +23.70%; worst month: -10.68%
Positive months: 42%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.99
- Sideways: S=-0.98
- Bear: S=-0.44

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_rdipq, 5))` S=0.78, F=0.62, INFERIOR
Direction gap: +0.66 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_rdipq)`: S=0.31, F=0.19, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rdipq / close)`: S=0.31, F=0.19, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rdipq, 5))`: S=0.78, F=0.62, T=24.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_rdipq, 5))` | TOP200 | 0.11 | 0.04 | 42.6% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_rdipaq: 0.555 (moderately positively correlated)
- fnd6_newqv1300_rdipepsq: 0.495 (moderately positively correlated)
- fnd6_itcb: 0.318 (weakly positively correlated)
- fnd6_newqv1300_rdipdq: 0.296 (weakly positively correlated)
- min_stock_option_expense_guidance: 0.278 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
