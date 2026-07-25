---
field: fnd6_newqv1300_spiq
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 0.78
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.1574
ann_vol: 0.0985
hit_rate: 0.4988
rolling_sharpe_min: -1.195
rolling_sharpe_max: 2.151
negated_best_sharpe: 0.78
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.44
n_negated_sims: 10
direction_gap: 0.47
---
# fnd6_newqv1300_spiq (fundamental6)

*Special Items*

## Signal Profile
- `rank(fnd6_newqv1300_spiq)`: S=-0.32, F=-0.11, T=3.5%, INFERIOR (TOP1000)
- `rank(fnd6_newqv1300_spiq / close)`: S=-0.32, F=-0.11, T=3.5%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_spiq, 5))`: S=0.31, F=0.09, T=36.7%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_spiq)`: S=0.32, F=0.11, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_spiq, 5))`: S=-0.28, F=-0.08, T=36.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_spiq, 22)`: S=-0.57, F=-0.21, T=34.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_spiq, 10)`: S=-0.82, F=-0.60, T=3.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_spiq, 22))`: S=-0.21, F=-0.05, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_spiq)`: S=0.68, F=0.37, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_spiq / close)`: S=0.78, F=0.44, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.32, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.08 (moderate), ret=+7.4%
  - 2020: S=-1.01 (negative), ret=-8.7%
  - 2021: S=1.27 (moderate), ret=+10.5%
  - 2022: S=0.30 (weak), ret=+4.1%
  - 2023: S=0.23 (weak), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 15.74% over 714 days (not yet recovered, ongoing at window end)
- Annualized: return +3.2%, volatility 9.8% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +2.14, excess kurtosis +28.75

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.20, max 2.15, latest -0.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +15.15%; worst month: -7.26%
Positive months: 52%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.40
- Sideways: S=0.53
- Bear: S=0.03

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_spiq / close)` S=0.78, F=0.44, INFERIOR
Direction gap: +0.47 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_spiq)`: S=0.68, F=0.37, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_spiq / close)`: S=0.78, F=0.44, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_spiq, 5))`: S=-0.28, F=-0.08, T=36.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_spiq, 5))` | TOP500 | 0.32 | 0.09 | 15.7% | 80% | weak |
| `rank(ts_delta(fnd6_newqv1300_spiq, 5))` | TOP1000 | 0.18 | 0.03 | 14.1% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_acomincq: -0.168 (weakly negatively correlated)
- fn_derivative_fair_value_of_derivative_liability_q: -0.132 (weakly negatively correlated)
- fnd6_newa2v1300_oiadp: -0.125 (weakly negatively correlated)
- fnd6_newa1v1300_ebit: -0.125 (weakly negatively correlated)
- ebit: -0.124 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
