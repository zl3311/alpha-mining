---
field: fnd6_newqv1300_invoq
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 0.85
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 2
max_drawdown: 0.3632
ann_vol: 0.2403
hit_rate: 0.4826
rolling_sharpe_min: -1.534
rolling_sharpe_max: 2.035
negated_best_sharpe: 0.85
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.8
n_negated_sims: 10
direction_gap: 0.16
---
# fnd6_newqv1300_invoq (fundamental6)

*Inventory - Other*

## Signal Profile
- `rank(fnd6_newqv1300_invoq)`: S=-0.08, F=-0.03, T=10.2%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_invoq / close)`: S=-0.08, F=-0.03, T=10.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_invoq, 5))`: S=0.40, F=0.22, T=33.1%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_invoq)`: S=0.41, F=0.22, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_invoq, 5))`: S=-0.35, F=-0.15, T=44.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_invoq, 22)`: S=0.17, F=0.10, T=14.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_invoq, 10)`: S=0.69, F=0.49, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_invoq, 22))`: S=-0.09, F=-0.03, T=20.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invoq)`: S=0.84, F=0.79, T=9.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invoq / close)`: S=0.85, F=0.80, T=9.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 22F/10P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.41, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.33 (negative), ret=-4.8%
  - 2020: S=0.89 (moderate), ret=+34.5%
  - 2021: S=0.03 (weak), ret=+0.5%
  - 2022: S=1.41 (moderate), ret=+30.6%
  - 2023: S=-1.14 (negative), ret=-13.1%

## Risk & Drawdown
- Max drawdown: 36.32% over 328 days (recovered)
- Annualized: return +9.8%, volatility 24.0% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew -0.43, excess kurtosis +69.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.53, max 2.04, latest -1.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +28.31%; worst month: -14.24%
Positive months: 50%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.82
- Sideways: S=-1.26
- Bear: S=1.11

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_invoq / close)` S=0.85, F=0.80, INFERIOR
Direction gap: +0.16 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_invoq)`: S=0.84, F=0.79, T=9.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invoq / close)`: S=0.85, F=0.80, T=9.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_invoq, 5))`: S=-0.35, F=-0.15, T=44.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_invoq, 5))` | TOP200 | 0.41 | 0.22 | 36.3% | 60% | all-weather |
| `rank(ts_delta(fnd6_newqv1300_invoq, 5))` | TOP500 | 0.14 | 0.04 | 47.7% | 40% | weak |

## Correlation Notes
Top correlates:
- snt_buzz: 0.166 (weakly positively correlated)
- min_stock_option_expense_guidance: 0.153 (weakly positively correlated)
- stock_option_expense_max_guidance_qtr: 0.153 (weakly positively correlated)
- scl12_buzz: -0.148 (weakly negatively correlated)
- fnd6_itcb: 0.147 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
