---
field: fnd6_mfmq_ibcomq
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
max_drawdown: 0.4149
ann_vol: 0.1228
hit_rate: 0.5117
rolling_sharpe_min: -4.042
rolling_sharpe_max: 2.52
negated_best_sharpe: 0.62
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: 0.42
---
# fnd6_mfmq_ibcomq (fundamental6)

*Income Before Extraordinary Items - Available for Common*

## Signal Profile
- `rank(fnd6_mfmq_ibcomq)`: S=0.20, F=0.09, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_mfmq_ibcomq / close)`: S=0.20, F=0.08, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mfmq_ibcomq, 5))`: S=-0.07, F=-0.01, T=36.9%, INFERIOR (TOP200)
- `-rank(fnd6_mfmq_ibcomq)`: S=-0.04, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfmq_ibcomq, 5))`: S=0.62, F=0.18, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_mfmq_ibcomq, 22)`: S=0.27, F=0.07, T=37.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfmq_ibcomq, 10)`: S=0.11, F=0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfmq_ibcomq, 22))`: S=0.14, F=0.03, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfmq_ibcomq)`: S=-0.20, F=-0.09, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfmq_ibcomq / close)`: S=-0.20, F=-0.08, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.19, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.36 (weak), ret=+2.3%
  - 2020: S=-3.25 (negative), ret=-27.5%
  - 2021: S=1.24 (moderate), ret=+16.0%
  - 2022: S=1.37 (moderate), ret=+23.9%
  - 2023: S=-0.27 (negative), ret=-3.2%

## Risk & Drawdown
- Max drawdown: 41.49% over 942 days (recovered)
- Annualized: return +2.4%, volatility 12.3% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew -0.18, excess kurtosis +1.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.04, max 2.52, latest -0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.23%; worst month: -10.13%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.51
- Sideways: S=0.85
- Bear: S=-3.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mfmq_ibcomq, 5))` S=0.62, F=0.18, INFERIOR
Direction gap: +0.42 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_mfmq_ibcomq)`: S=-0.20, F=-0.09, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfmq_ibcomq / close)`: S=-0.20, F=-0.08, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfmq_ibcomq, 5))`: S=0.62, F=0.18, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfmq_ibcomq)` | TOP3000 | 0.19 | 0.09 | 41.5% | 60% | bull-only |
| `rank(fnd6_mfmq_ibcomq / close)` | TOP3000 | 0.20 | 0.08 | 38.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- income: 1.000 (strongly positively correlated)
- fnd6_newqv1300_cibegniq: 0.996 (strongly positively correlated)
- fnd6_newqv1300_dilavq: 0.990 (strongly positively correlated)
- fnd6_newqv1300_ibadjq: 0.990 (strongly positively correlated)
- fnd6_newqv1300_ibcomq: 0.990 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
