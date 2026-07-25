---
field: fnd6_newqv1300_cibegniq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.56
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.4137
ann_vol: 0.1255
hit_rate: 0.5093
rolling_sharpe_min: -4.138
rolling_sharpe_max: 2.593
negated_best_sharpe: 0.56
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: 0.15
---
# fnd6_newqv1300_cibegniq (fundamental6)

*Comp Inc - Beginning Net Income*

## Signal Profile
- `rank(fnd6_newqv1300_cibegniq)`: S=0.22, F=0.10, T=5.9%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_cibegniq / close)`: S=0.18, F=0.07, T=6.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_cibegniq, 5))`: S=-0.04, F=0.00, T=51.7%, INFERIOR (TOP1000)
- `-rank(fnd6_newqv1300_cibegniq)`: S=-0.09, F=-0.03, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cibegniq, 5))`: S=0.56, F=0.17, T=46.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_cibegniq, 22)`: S=0.07, F=0.01, T=42.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_cibegniq, 10)`: S=0.17, F=0.07, T=4.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_cibegniq, 22))`: S=0.41, F=0.13, T=21.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cibegniq)`: S=-0.22, F=-0.10, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cibegniq / close)`: S=-0.18, F=-0.07, T=6.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.21, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.34 (weak), ret=+2.2%
  - 2020: S=-3.42 (negative), ret=-28.6%
  - 2021: S=1.42 (moderate), ret=+18.6%
  - 2022: S=1.36 (moderate), ret=+24.6%
  - 2023: S=-0.32 (negative), ret=-3.9%

## Risk & Drawdown
- Max drawdown: 41.37% over 924 days (recovered)
- Annualized: return +2.6%, volatility 12.6% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew -0.18, excess kurtosis +1.38

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.14, max 2.59, latest -0.50

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.62%; worst month: -10.73%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.48
- Sideways: S=0.87
- Bear: S=-3.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_cibegniq, 5))` S=0.56, F=0.17, INFERIOR
Direction gap: +0.15 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_cibegniq)`: S=-0.22, F=-0.10, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cibegniq / close)`: S=-0.18, F=-0.07, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cibegniq, 5))`: S=0.56, F=0.17, T=46.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_cibegniq)` | TOP3000 | 0.21 | 0.10 | 41.4% | 60% | bull-only |
| `rank(fnd6_newqv1300_cibegniq / close)` | TOP3000 | 0.17 | 0.07 | 39.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_cibegniq)` | TOP1000 | 0.08 | 0.03 | 43.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- income: 0.996 (strongly positively correlated)
- fnd6_mfmq_ibcomq: 0.996 (strongly positively correlated)
- fnd6_newqv1300_dilavq: 0.986 (strongly positively correlated)
- fnd6_newqv1300_ibadjq: 0.986 (strongly positively correlated)
- fnd6_newqv1300_ibcomq: 0.986 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
