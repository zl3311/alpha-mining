---
field: fnd6_newqv1300_cimiiq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.56
best_fitness: 0.34
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.1495
ann_vol: 0.0815
hit_rate: 0.5004
rolling_sharpe_min: -0.727
rolling_sharpe_max: 2.527
redundancy_cluster: 51
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.09
---
# fnd6_newqv1300_cimiiq (fundamental6)

*Comprehensive Income - Noncontrolling Interest*

## Signal Profile
- `rank(fnd6_newqv1300_cimiiq)`: S=0.53, F=0.31, T=9.8%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_cimiiq / close)`: S=0.56, F=0.34, T=9.8%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_cimiiq, 5))`: S=0.33, F=0.12, T=59.0%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_cimiiq)`: S=-0.23, F=-0.07, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cimiiq, 5))`: S=0.47, F=0.16, T=46.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_cimiiq, 63)`: S=0.29, F=0.08, T=20.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_cimiiq, 10)`: S=-0.50, F=-0.28, T=5.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_cimiiq, 22))`: S=-0.11, F=-0.02, T=21.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cimiiq)`: S=-0.48, F=-0.20, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cimiiq / close)`: S=-0.50, F=-0.21, T=6.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.49 (moderate), ret=+8.6%
  - 2020: S=1.31 (moderate), ret=+9.7%
  - 2021: S=-0.56 (negative), ret=-5.8%
  - 2022: S=1.30 (moderate), ret=+12.1%
  - 2023: S=-0.39 (negative), ret=-2.3%

## Risk & Drawdown
- Max drawdown: 14.95% over 497 days (recovered)
- Annualized: return +4.5%, volatility 8.2% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew -0.23, excess kurtosis +2.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.73, max 2.53, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +6.75%; worst month: -6.01%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.24
- Sideways: S=1.41
- Bear: S=-0.76

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_cimiiq, 5))` S=0.47, F=0.16, INFERIOR
Direction gap: -0.09 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_cimiiq)`: S=-0.48, F=-0.20, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cimiiq / close)`: S=-0.50, F=-0.21, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cimiiq, 5))`: S=0.47, F=0.16, T=46.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_cimiiq / close)` | TOP200 | 0.56 | 0.34 | 14.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_cimiiq)` | TOP200 | 0.52 | 0.31 | 15.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_cimiiq / close)` | TOP3000 | 0.49 | 0.21 | 12.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_cimiiq)` | TOP3000 | 0.47 | 0.20 | 13.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_cimiiq, 5))` | TOP200 | 0.33 | 0.12 | 58.5% | 60% | mixed |
| `rank(fnd6_newqv1300_cimiiq)` | TOP1000 | 0.22 | 0.07 | 12.9% | 40% | bull-only |
| `rank(fnd6_newqv1300_cimiiq / close)` | TOP1000 | 0.24 | 0.07 | 11.9% | 40% | bull-only |
| `rank(fnd6_newqv1300_cimiiq / close)` | TOP500 | 0.22 | 0.07 | 12.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_cimiiq)` | TOP500 | 0.20 | 0.06 | 13.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_cimiiq, 5))` | TOP1000 | 0.21 | 0.05 | 43.3% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_miiq: 0.802 (strongly positively correlated)
- fnd6_newa2v1300_mii: 0.574 (moderately positively correlated)
- fnd6_newa1v1300_fincf: -0.345 (weakly negatively correlated)
- cashflow_fin: -0.344 (weakly negatively correlated)
- cash_flow_from_financing: -0.329 (weakly negatively correlated)

Redundancy cluster #51: 2 similar fields, mean |rho| 0.802 (representative: fnd6_newqv1300_miiq). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
