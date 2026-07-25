---
field: fnd6_newqv1300_ibmiiq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.75
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.387
ann_vol: 0.1143
hit_rate: 0.5101
rolling_sharpe_min: -4.312
rolling_sharpe_max: 2.574
negated_best_sharpe: 0.75
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.52
---
# fnd6_newqv1300_ibmiiq (fundamental6)

*Income before Extraordinary Items and Noncontrolling Interests*

## Signal Profile
- `rank(fnd6_newqv1300_ibmiiq)`: S=0.22, F=0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_ibmiiq / close)`: S=0.23, F=0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_ibmiiq, 5))`: S=-0.02, F=0.00, T=36.9%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_ibmiiq)`: S=-0.07, F=-0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ibmiiq, 5))`: S=0.75, F=0.24, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_ibmiiq, 22)`: S=0.32, F=0.09, T=37.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ibmiiq, 10)`: S=0.12, F=0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ibmiiq, 22))`: S=0.24, F=0.06, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ibmiiq)`: S=-0.22, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ibmiiq / close)`: S=-0.23, F=-0.11, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.23, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.28 (weak), ret=+1.5%
  - 2020: S=-3.40 (negative), ret=-25.3%
  - 2021: S=1.12 (moderate), ret=+13.7%
  - 2022: S=1.55 (strong), ret=+25.4%
  - 2023: S=-0.23 (negative), ret=-2.6%

## Risk & Drawdown
- Max drawdown: 38.70% over 891 days (recovered)
- Annualized: return +2.6%, volatility 11.4% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew -0.17, excess kurtosis +1.13

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.31, max 2.57, latest -0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.20%; worst month: -9.34%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.72
- Sideways: S=0.79
- Bear: S=-3.56

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_ibmiiq, 5))` S=0.75, F=0.24, INFERIOR
Direction gap: +0.52 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ibmiiq)`: S=-0.22, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ibmiiq / close)`: S=-0.23, F=-0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ibmiiq, 5))`: S=0.75, F=0.24, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_ibmiiq / close)` | TOP3000 | 0.23 | 0.11 | 38.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_ibmiiq)` | TOP3000 | 0.21 | 0.10 | 42.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_ibmiiq)` | TOP1000 | 0.06 | 0.02 | 44.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- income_beforeextra: 0.999 (strongly positively correlated)
- fnd6_newqv1300_ibq: 0.999 (strongly positively correlated)
- fnd6_newqv1300_ibcomq: 0.999 (strongly positively correlated)
- fnd6_newqv1300_ibadjq: 0.999 (strongly positively correlated)
- fnd6_newqv1300_dilavq: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
