---
field: income_tax
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.46
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2692
ann_vol: 0.0826
hit_rate: 0.5093
rolling_sharpe_min: -4.263
rolling_sharpe_max: 2.534
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: 0.07
---
# income_tax (fundamental6)

*Income Taxes - Total*

## Signal Profile
- `rank(income_tax)`: S=0.36, F=0.20, T=2.4%, INFERIOR (TOP3000)
- `rank(income_tax / close)`: S=0.46, F=0.25, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_delta(income_tax, 5))`: S=-0.06, F=-0.01, T=36.8%, INFERIOR (TOP200)
- `-rank(income_tax)`: S=-0.11, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(income_tax, 5))`: S=0.53, F=0.17, T=36.9%, INFERIOR (TOP3000)
- `-ts_zscore(income_tax, 63)`: S=0.23, F=0.05, T=17.4%, INFERIOR (TOP3000)
- `ts_mean(income_tax, 10)`: S=0.08, F=0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_rank(income_tax, 22))`: S=-0.60, F=-0.24, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * income_tax)`: S=-0.11, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * income_tax / close)`: S=-0.11, F=-0.03, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.45, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.83 (moderate), ret=+3.3%
  - 2020: S=-3.28 (negative), ret=-17.1%
  - 2021: S=1.12 (moderate), ret=+11.1%
  - 2022: S=1.78 (strong), ret=+20.8%
  - 2023: S=0.01 (weak), ret=+0.1%

## Risk & Drawdown
- Max drawdown: 26.92% over 806 days (recovered)
- Annualized: return +3.7%, volatility 8.3% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew -0.09, excess kurtosis +1.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.26, max 2.53, latest -0.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.11%; worst month: -5.98%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.18
- Sideways: S=1.05
- Bear: S=-3.61

## Negated Direction
Best negated: `rank(-1 * ts_delta(income_tax, 5))` S=0.53, F=0.17, INFERIOR
Direction gap: +0.07 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * income_tax)`: S=-0.11, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * income_tax / close)`: S=-0.11, F=-0.03, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(income_tax, 5))`: S=0.53, F=0.17, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(income_tax / close)` | TOP3000 | 0.45 | 0.25 | 26.9% | 80% | bull-only |
| `rank(income_tax)` | TOP3000 | 0.35 | 0.20 | 33.4% | 60% | bull-only |
| `rank(income_tax / close)` | TOP1000 | 0.10 | 0.03 | 29.4% | 60% | bull-only |
| `rank(income_tax)` | TOP1000 | 0.10 | 0.03 | 36.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_txtq: 1.000 (strongly positively correlated)
- fn_income_tax_expense_q: 0.975 (strongly positively correlated)
- pretax_income_standalone_value: 0.960 (strongly positively correlated)
- anl4_ptp_value: 0.960 (strongly positively correlated)
- pretax_income: 0.960 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
