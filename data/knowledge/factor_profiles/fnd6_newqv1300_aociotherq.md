---
field: fnd6_newqv1300_aociotherq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.5
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.0815
ann_vol: 0.0423
hit_rate: 0.5061
rolling_sharpe_min: -1.497
rolling_sharpe_max: 1.816
negated_best_sharpe: 0.27
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.23
---
# fnd6_newqv1300_aociotherq (fundamental6)

*Accumulated Other Comprehensive Income - Other Adjustments*

## Signal Profile
- `rank(fnd6_newqv1300_aociotherq)`: S=0.53, F=0.22, T=7.5%, INFERIOR (TOP1000)
- `rank(fnd6_newqv1300_aociotherq / close)`: S=0.54, F=0.23, T=7.5%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_aociotherq, 5))`: S=0.43, F=0.15, T=43.6%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_aociotherq)`: S=-0.53, F=-0.22, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aociotherq, 5))`: S=-0.15, F=-0.03, T=51.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_aociotherq, 63)`: S=0.50, F=0.25, T=18.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_aociotherq, 10)`: S=-0.15, F=-0.05, T=5.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_aociotherq, 22))`: S=-0.30, F=-0.10, T=21.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aociotherq)`: S=0.26, F=0.08, T=8.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aociotherq / close)`: S=0.27, F=0.09, T=8.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.55, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.07 (moderate), ret=+3.2%
  - 2020: S=0.95 (moderate), ret=+3.9%
  - 2021: S=0.08 (weak), ret=+0.4%
  - 2022: S=0.16 (weak), ret=+0.8%
  - 2023: S=1.03 (moderate), ret=+3.1%

## Risk & Drawdown
- Max drawdown: 8.15% over 1043 days (not yet recovered, ongoing at window end)
- Annualized: return +2.3%, volatility 4.2% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.24, excess kurtosis +3.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.50, max 1.82, latest 1.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +3.15%; worst month: -1.66%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.40
- Sideways: S=-0.47
- Bear: S=2.47

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_aociotherq / close)` S=0.27, F=0.09, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_aociotherq)`: S=0.26, F=0.08, T=8.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aociotherq / close)`: S=0.27, F=0.09, T=8.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aociotherq, 5))`: S=-0.15, F=-0.03, T=51.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_aociotherq / close)` | TOP1000 | 0.55 | 0.23 | 8.2% | 100% | mixed |
| `rank(fnd6_newqv1300_aociotherq)` | TOP1000 | 0.54 | 0.22 | 8.6% | 100% | mixed |
| `rank(ts_delta(fnd6_newqv1300_aociotherq, 5))` | TOP3000 | 0.43 | 0.15 | 17.8% | 40% | mixed |
| `rank(ts_delta(fnd6_newqv1300_aociotherq, 5))` | TOP200 | 0.33 | 0.11 | 28.3% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_aociotherq, 5))` | TOP500 | 0.12 | 0.02 | 39.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_aociotherq, 5))` | TOP1000 | 0.11 | 0.02 | 29.6% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_txfo: -0.438 (moderately negatively correlated)
- ebitda: -0.437 (moderately negatively correlated)
- operating_profit_before_depr_amort: -0.437 (moderately negatively correlated)
- fnd6_newa1v1300_ebitda: -0.437 (moderately negatively correlated)
- fnd6_newa2v1300_oibdp: -0.436 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
