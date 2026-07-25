---
field: fnd6_cptnewqv1300_oiadpq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.45
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.3484
ann_vol: 0.1175
hit_rate: 0.5077
rolling_sharpe_min: -4.353
rolling_sharpe_max: 2.783
negated_best_sharpe: 0.62
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: 0.17
---
# fnd6_cptnewqv1300_oiadpq (fundamental6)

*Operating Income After Depreciation - Quarterly*

## Signal Profile
- `rank(fnd6_cptnewqv1300_oiadpq)`: S=0.31, F=0.18, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_oiadpq / close)`: S=0.45, F=0.29, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_oiadpq, 5))`: S=-0.22, F=-0.06, T=38.3%, INFERIOR (TOP200)
- `-rank(fnd6_cptnewqv1300_oiadpq)`: S=-0.10, F=-0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_oiadpq, 5))`: S=0.62, F=0.18, T=37.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptnewqv1300_oiadpq, 22)`: S=0.49, F=0.17, T=37.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_oiadpq, 10)`: S=0.16, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_oiadpq, 22))`: S=0.30, F=0.08, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_oiadpq)`: S=-0.31, F=-0.18, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_oiadpq / close)`: S=-0.45, F=-0.29, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.44, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.34 (weak), ret=+1.6%
  - 2020: S=-3.22 (negative), ret=-20.8%
  - 2021: S=1.33 (moderate), ret=+18.6%
  - 2022: S=1.57 (strong), ret=+27.3%
  - 2023: S=-0.11 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 34.84% over 810 days (recovered)
- Annualized: return +5.2%, volatility 11.8% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.09, excess kurtosis +1.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.35, max 2.78, latest -0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.55%; worst month: -7.20%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.08
- Sideways: S=0.92
- Bear: S=-3.53

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_oiadpq, 5))` S=0.62, F=0.18, INFERIOR
Direction gap: +0.17 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_oiadpq)`: S=-0.31, F=-0.18, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_oiadpq / close)`: S=-0.45, F=-0.29, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_oiadpq, 5))`: S=0.62, F=0.18, T=37.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptnewqv1300_oiadpq / close)` | TOP3000 | 0.44 | 0.29 | 34.8% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_oiadpq)` | TOP3000 | 0.30 | 0.18 | 44.0% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_oiadpq / close)` | TOP1000 | 0.13 | 0.05 | 39.1% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_oiadpq)` | TOP1000 | 0.09 | 0.03 | 48.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- operating_income: 1.000 (strongly positively correlated)
- anl4_ebit_value: 0.990 (strongly positively correlated)
- ebit_reported_value: 0.990 (strongly positively correlated)
- anl4_ptp_value: 0.981 (strongly positively correlated)
- pretax_income_standalone_value: 0.981 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
