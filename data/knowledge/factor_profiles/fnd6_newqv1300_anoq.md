---
field: fnd6_newqv1300_anoq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.7
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.1753
ann_vol: 0.0721
hit_rate: 0.5053
rolling_sharpe_min: -1.496
rolling_sharpe_max: 4.279
negated_best_sharpe: 0.02
negated_best_template: neg_rank_level
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.68
---
# fnd6_newqv1300_anoq (fundamental6)

*Assets Netting & Other Adjustments*

## Signal Profile
- `rank(fnd6_newqv1300_anoq)`: S=0.54, F=0.30, T=9.7%, INFERIOR (TOP500)
- `rank(fnd6_newqv1300_anoq / close)`: S=0.54, F=0.30, T=9.7%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_anoq, 5))`: S=0.46, F=0.19, T=40.5%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_anoq)`: S=-0.30, F=-0.12, T=9.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_anoq, 5))`: S=-0.19, F=-0.06, T=33.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_anoq, 22)`: S=0.70, F=0.49, T=20.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_anoq, 10)`: S=0.58, F=0.40, T=8.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_anoq, 22))`: S=0.24, F=0.09, T=27.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_anoq)`: S=0.02, F=0.00, T=11.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_anoq / close)`: S=0.03, F=0.00, T=11.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/11P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.55, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.18 (weak), ret=+1.4%
  - 2020: S=-0.72 (negative), ret=-5.6%
  - 2021: S=2.23 (strong), ret=+15.6%
  - 2022: S=2.17 (strong), ret=+13.8%
  - 2023: S=-1.01 (negative), ret=-5.7%

## Risk & Drawdown
- Max drawdown: 17.53% over 572 days (recovered)
- Annualized: return +4.0%, volatility 7.2% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.52, excess kurtosis +12.52

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.50, max 4.28, latest -1.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +4.33%; worst month: -5.41%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.82
- Sideways: S=-0.11
- Bear: S=0.07

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_anoq)` S=0.02, F=0.00, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_anoq)`: S=0.02, F=0.00, T=11.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_anoq / close)`: S=0.03, F=0.00, T=11.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_anoq, 5))`: S=-0.19, F=-0.06, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_anoq / close)` | TOP500 | 0.55 | 0.30 | 17.5% | 60% | mixed |
| `rank(fnd6_newqv1300_anoq)` | TOP500 | 0.55 | 0.30 | 17.5% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_anoq, 5))` | TOP3000 | 0.47 | 0.19 | 35.4% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_anoq, 5))` | TOP200 | 0.38 | 0.17 | 35.6% | 60% | bear-only |
| `rank(fnd6_newqv1300_anoq / close)` | TOP3000 | 0.43 | 0.16 | 9.0% | 80% | mixed |
| `rank(fnd6_newqv1300_anoq)` | TOP3000 | 0.43 | 0.16 | 9.0% | 80% | mixed |
| `rank(fnd6_newqv1300_anoq / close)` | TOP1000 | 0.32 | 0.13 | 12.5% | 40% | mixed |
| `rank(fnd6_newqv1300_anoq)` | TOP1000 | 0.31 | 0.12 | 12.5% | 40% | mixed |
| `rank(ts_delta(fnd6_newqv1300_anoq, 5))` | TOP500 | 0.27 | 0.08 | 40.9% | 60% | weak |
| `rank(ts_delta(fnd6_newqv1300_anoq, 5))` | TOP1000 | 0.25 | 0.08 | 35.9% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ano: 0.421 (moderately positively correlated)
- fnd6_newa2v1300_prsho: 0.289 (weakly positively correlated)
- anl4_qf_az_div_number: -0.283 (weakly negatively correlated)
- anl4_qfd1_az_div_number: -0.283 (weakly negatively correlated)
- fnd2_propplteqmuflmblgland: -0.280 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
