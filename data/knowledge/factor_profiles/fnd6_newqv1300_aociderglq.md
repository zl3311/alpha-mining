---
field: fnd6_newqv1300_aociderglq
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 1.34
best_fitness: 0.82
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.403
ann_vol: 0.205
hit_rate: 0.4988
rolling_sharpe_min: -1.435
rolling_sharpe_max: 2.714
negated_best_sharpe: 0.42
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.92
---
# fnd6_newqv1300_aociderglq (fundamental6)

*Accum Other Comp Inc - Derivatives Unrealized Gain/Loss*

## Signal Profile
- `rank(fnd6_newqv1300_aociderglq)`: S=-0.11, F=-0.03, T=10.3%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_aociderglq / close)`: S=-0.09, F=-0.02, T=10.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_aociderglq, 5))`: S=0.52, F=0.22, T=60.4%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_aociderglq)`: S=0.35, F=0.11, T=8.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aociderglq, 5))`: S=-0.31, F=-0.10, T=63.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_aociderglq, 22)`: S=0.03, F=0.00, T=41.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_aociderglq, 10)`: S=-0.25, F=-0.13, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_aociderglq, 22))`: S=1.34, F=0.82, T=22.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aociderglq)`: S=0.39, F=0.15, T=9.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aociderglq / close)`: S=0.42, F=0.17, T=9.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.52, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.86 (moderate), ret=+12.2%
  - 2020: S=2.32 (strong), ret=+44.7%
  - 2021: S=-1.11 (negative), ret=-24.4%
  - 2022: S=0.76 (moderate), ret=+20.0%
  - 2023: S=-0.03 (negative), ret=-0.6%

## Risk & Drawdown
- Max drawdown: 40.30% over 813 days (recovered)
- Annualized: return +10.6%, volatility 20.5% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.84, excess kurtosis +8.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.44, max 2.71, latest -0.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +14.74%; worst month: -20.36%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.87
- Sideways: S=0.49
- Bear: S=0.17

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_aociderglq / close)` S=0.42, F=0.17, INFERIOR
Direction gap: -0.92 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_aociderglq)`: S=0.39, F=0.15, T=9.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aociderglq / close)`: S=0.42, F=0.17, T=9.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aociderglq, 5))`: S=-0.31, F=-0.10, T=63.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_aociderglq, 5))` | TOP200 | 0.52 | 0.22 | 40.3% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_aociderglq, 5))` | TOP1000 | 0.39 | 0.12 | 23.9% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_aociderglq, 5))` | TOP500 | 0.22 | 0.06 | 57.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_aociderglq, 5))` | TOP3000 | 0.26 | 0.06 | 16.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_prcc: 0.141 (weakly positively correlated)
- fnd6_newqv1300_ciderglq: 0.138 (weakly positively correlated)
- fnd6_prcl: 0.133 (weakly positively correlated)
- fnd2_a_sbcpnargmsptawervl: 0.133 (weakly positively correlated)
- snt_value: 0.131 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
