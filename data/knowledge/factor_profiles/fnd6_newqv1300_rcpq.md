---
field: fnd6_newqv1300_rcpq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 1.03
best_fitness: 0.66
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1414
ann_vol: 0.1234
hit_rate: 0.5036
rolling_sharpe_min: -1.556
rolling_sharpe_max: 2.348
negated_best_sharpe: 0.47
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.56
---
# fnd6_newqv1300_rcpq (fundamental6)

*Restructuring Cost Pretax*

## Signal Profile
- `rank(fnd6_newqv1300_rcpq)`: S=-0.23, F=-0.07, T=4.0%, INFERIOR (TOP1000)
- `rank(fnd6_newqv1300_rcpq / close)`: S=-0.11, F=-0.03, T=5.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_rcpq, 5))`: S=0.65, F=0.31, T=35.8%, INFERIOR (TOP1000)
- `-rank(fnd6_newqv1300_rcpq)`: S=0.23, F=0.07, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rcpq, 5))`: S=0.44, F=0.13, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_rcpq, 22)`: S=1.03, F=0.66, T=36.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_rcpq, 10)`: S=-0.85, F=-0.65, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_rcpq, 22))`: S=0.89, F=0.50, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rcpq)`: S=0.44, F=0.19, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rcpq / close)`: S=0.47, F=0.22, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.65, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.41 (weak), ret=+3.4%
  - 2020: S=0.77 (moderate), ret=+14.5%
  - 2021: S=0.15 (weak), ret=+1.1%
  - 2022: S=2.29 (strong), ret=+26.9%
  - 2023: S=-0.71 (negative), ret=-6.7%

## Risk & Drawdown
- Max drawdown: 14.14% over 302 days (not yet recovered, ongoing at window end)
- Annualized: return +8.0%, volatility 12.3% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +5.32, excess kurtosis +76.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.56, max 2.35, latest -0.72

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +23.87%; worst month: -9.17%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.38
- Sideways: S=0.17
- Bear: S=0.21

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_rcpq / close)` S=0.47, F=0.22, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_rcpq)`: S=0.44, F=0.19, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rcpq / close)`: S=0.47, F=0.22, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rcpq, 5))`: S=0.44, F=0.13, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_rcpq, 5))` | TOP1000 | 0.65 | 0.31 | 14.1% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_aocipenq: 0.217 (weakly positively correlated)
- fnd2_a_ltrmdmrepoplinyfour: 0.202 (weakly positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_a: 0.194 (weakly positively correlated)
- fnd6_esopct: 0.192 (weakly positively correlated)
- fnd2_a_ltrmdmrepoplinythree: 0.185 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
