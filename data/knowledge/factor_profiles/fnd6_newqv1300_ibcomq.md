---
field: fnd6_newqv1300_ibcomq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.62
best_fitness: 0.18
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.3856
ann_vol: 0.1115
hit_rate: 0.5093
rolling_sharpe_min: -4.33
rolling_sharpe_max: 2.537
negated_best_sharpe: 0.62
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: 0.41
---
# fnd6_newqv1300_ibcomq (fundamental6)

*Income Before Extraordinary Items - Available for Common*

## Signal Profile
- `rank(fnd6_newqv1300_ibcomq)`: S=0.21, F=0.09, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_ibcomq / close)`: S=0.21, F=0.09, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_ibcomq, 5))`: S=-0.07, F=-0.01, T=37.0%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_ibcomq)`: S=-0.05, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ibcomq, 5))`: S=0.62, F=0.18, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_ibcomq, 22)`: S=0.30, F=0.08, T=37.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ibcomq, 10)`: S=0.11, F=0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ibcomq, 22))`: S=0.18, F=0.04, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ibcomq)`: S=-0.21, F=-0.09, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ibcomq / close)`: S=-0.21, F=-0.09, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.21, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.17 (weak), ret=+0.9%
  - 2020: S=-3.43 (negative), ret=-25.2%
  - 2021: S=1.11 (moderate), ret=+13.3%
  - 2022: S=1.56 (strong), ret=+24.8%
  - 2023: S=-0.22 (negative), ret=-2.5%

## Risk & Drawdown
- Max drawdown: 38.56% over 900 days (recovered)
- Annualized: return +2.3%, volatility 11.2% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew -0.17, excess kurtosis +1.10

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.33, max 2.54, latest -0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.09%; worst month: -9.30%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.70
- Sideways: S=0.78
- Bear: S=-3.55

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_ibcomq, 5))` S=0.62, F=0.18, INFERIOR
Direction gap: +0.41 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ibcomq)`: S=-0.21, F=-0.09, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ibcomq / close)`: S=-0.21, F=-0.09, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ibcomq, 5))`: S=0.62, F=0.18, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_ibcomq)` | TOP3000 | 0.20 | 0.09 | 41.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_ibcomq / close)` | TOP3000 | 0.21 | 0.09 | 38.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_ibadjq: 1.000 (strongly positively correlated)
- income_beforeextra: 1.000 (strongly positively correlated)
- fnd6_newqv1300_ibq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_dilavq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_ibmiiq: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
