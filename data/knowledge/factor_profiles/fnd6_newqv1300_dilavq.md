---
field: fnd6_newqv1300_dilavq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.6
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.3891
ann_vol: 0.1131
hit_rate: 0.5126
rolling_sharpe_min: -4.372
rolling_sharpe_max: 2.564
negated_best_sharpe: 0.6
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: 0.39
---
# fnd6_newqv1300_dilavq (fundamental6)

*Dilution Available - Excluding Extraordinary Items*

## Signal Profile
- `rank(fnd6_newqv1300_dilavq)`: S=0.21, F=0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_dilavq / close)`: S=0.22, F=0.10, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_dilavq, 5))`: S=-0.07, F=-0.01, T=36.6%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_dilavq)`: S=-0.06, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_dilavq, 5))`: S=0.60, F=0.17, T=37.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_dilavq, 22)`: S=0.21, F=0.05, T=37.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_dilavq, 10)`: S=0.12, F=0.04, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_dilavq, 22))`: S=0.20, F=0.05, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_dilavq)`: S=-0.21, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_dilavq / close)`: S=-0.22, F=-0.10, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.22, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.17 (weak), ret=+0.9%
  - 2020: S=-3.46 (negative), ret=-25.3%
  - 2021: S=1.10 (moderate), ret=+13.2%
  - 2022: S=1.57 (strong), ret=+25.6%
  - 2023: S=-0.21 (negative), ret=-2.4%

## Risk & Drawdown
- Max drawdown: 38.91% over 893 days (recovered)
- Annualized: return +2.5%, volatility 11.3% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.17, excess kurtosis +1.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.37, max 2.56, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.36%; worst month: -9.34%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.68
- Sideways: S=0.80
- Bear: S=-3.53

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_dilavq, 5))` S=0.60, F=0.17, INFERIOR
Direction gap: +0.39 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_dilavq)`: S=-0.21, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_dilavq / close)`: S=-0.22, F=-0.10, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_dilavq, 5))`: S=0.60, F=0.17, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_dilavq)` | TOP3000 | 0.20 | 0.10 | 41.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_dilavq / close)` | TOP3000 | 0.22 | 0.10 | 38.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_dilavq / close)` | TOP1000 | 0.07 | 0.02 | 38.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_ibadjq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_ibcomq: 1.000 (strongly positively correlated)
- income_beforeextra: 1.000 (strongly positively correlated)
- fnd6_newqv1300_ibq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_ibmiiq: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
