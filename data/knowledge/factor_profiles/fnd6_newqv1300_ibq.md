---
field: fnd6_newqv1300_ibq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.74
best_fitness: 0.23
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.3834
ann_vol: 0.1114
hit_rate: 0.5077
rolling_sharpe_min: -4.33
rolling_sharpe_max: 2.545
negated_best_sharpe: 0.74
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: 0.52
---
# fnd6_newqv1300_ibq (fundamental6)

*Income Before Extraordinary Items*

## Signal Profile
- `rank(fnd6_newqv1300_ibq)`: S=0.21, F=0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_ibq / close)`: S=0.22, F=0.10, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_ibq, 5))`: S=-0.08, F=-0.01, T=36.8%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_ibq)`: S=-0.05, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ibq, 5))`: S=0.74, F=0.23, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_ibq, 22)`: S=0.33, F=0.10, T=37.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ibq, 10)`: S=0.12, F=0.04, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ibq, 22))`: S=0.16, F=0.03, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ibq)`: S=-0.21, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ibq / close)`: S=-0.22, F=-0.10, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.22, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.17 (weak), ret=+0.9%
  - 2020: S=-3.44 (negative), ret=-25.0%
  - 2021: S=1.13 (moderate), ret=+13.5%
  - 2022: S=1.56 (strong), ret=+24.8%
  - 2023: S=-0.19 (negative), ret=-2.1%

## Risk & Drawdown
- Max drawdown: 38.34% over 893 days (recovered)
- Annualized: return +2.5%, volatility 11.1% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.17, excess kurtosis +1.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.33, max 2.54, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.10%; worst month: -9.22%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.71
- Sideways: S=0.80
- Bear: S=-3.55

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_ibq, 5))` S=0.74, F=0.23, INFERIOR
Direction gap: +0.52 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ibq)`: S=-0.21, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ibq / close)`: S=-0.22, F=-0.10, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ibq, 5))`: S=0.74, F=0.23, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_ibq)` | TOP3000 | 0.21 | 0.10 | 41.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_ibq / close)` | TOP3000 | 0.22 | 0.10 | 38.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- income_beforeextra: 1.000 (strongly positively correlated)
- fnd6_newqv1300_ibcomq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_ibadjq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_dilavq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_ibmiiq: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
