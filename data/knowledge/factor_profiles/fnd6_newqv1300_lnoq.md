---
field: fnd6_newqv1300_lnoq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.77
best_fitness: 0.4
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1792
ann_vol: 0.1378
hit_rate: 0.4866
rolling_sharpe_min: -1.314
rolling_sharpe_max: 2.13
negated_best_sharpe: 0.61
negated_best_template: neg_rank_level
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: -0.16
---
# fnd6_newqv1300_lnoq (fundamental6)

*Liabilities Netting & Other Adjustments*

## Signal Profile
- `rank(fnd6_newqv1300_lnoq)`: S=-0.43, F=-0.21, T=10.3%, INFERIOR (TOP500)
- `rank(fnd6_newqv1300_lnoq / close)`: S=-0.43, F=-0.22, T=10.3%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_lnoq, 5))`: S=0.77, F=0.40, T=39.0%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_lnoq)`: S=0.59, F=0.32, T=9.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lnoq, 5))`: S=-0.41, F=-0.15, T=39.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_lnoq, 63)`: S=0.31, F=0.16, T=17.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_lnoq, 10)`: S=0.11, F=0.04, T=9.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_lnoq, 22))`: S=0.24, F=0.08, T=25.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lnoq)`: S=0.61, F=0.33, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lnoq / close)`: S=0.61, F=0.33, T=8.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/15P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.77, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.26 (moderate), ret=+24.7%
  - 2020: S=0.17 (weak), ret=+1.9%
  - 2021: S=0.47 (weak), ret=+5.0%
  - 2022: S=-0.21 (negative), ret=-2.8%
  - 2023: S=2.14 (strong), ret=+23.1%

## Risk & Drawdown
- Max drawdown: 17.92% over 656 days (recovered)
- Annualized: return +10.6%, volatility 13.8% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +5.48, excess kurtosis +103.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.31, max 2.13, latest 2.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +17.69%; worst month: -10.77%
Positive months: 55%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.67
- Sideways: S=1.15
- Bear: S=0.33

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_lnoq)` S=0.61, F=0.33, INFERIOR
Direction gap: -0.16 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_lnoq)`: S=0.61, F=0.33, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lnoq / close)`: S=0.61, F=0.33, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lnoq, 5))`: S=-0.41, F=-0.15, T=39.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_lnoq, 5))` | TOP500 | 0.77 | 0.40 | 17.9% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_lnoq, 5))` | TOP3000 | 0.47 | 0.18 | 22.3% | 60% | weak |
| `rank(ts_delta(fnd6_newqv1300_lnoq, 5))` | TOP1000 | 0.32 | 0.11 | 28.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_lnoq, 5))` | TOP200 | 0.18 | 0.06 | 29.5% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fn_eff_income_tax_rate_continuing_operations_q: -0.132 (weakly negatively correlated)
- fscore_bfl_value: -0.121 (weakly negatively correlated)
- est_bookvalue_ps: -0.121 (weakly negatively correlated)
- anl4_afv4_cfps_mean: -0.118 (weakly negatively correlated)
- anl4_afv4_cfps_high: -0.117 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
