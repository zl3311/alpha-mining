---
field: fnd6_prclq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.66
best_fitness: 0.51
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2176
ann_vol: 0.1131
hit_rate: 0.5045
rolling_sharpe_min: -1.761
rolling_sharpe_max: 2.103
negated_best_sharpe: 0.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.36
---
# fnd6_prclq (fundamental6)

*Price Low - Quarter*

## Signal Profile
- `rank(fnd6_prclq)`: S=0.19, F=0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_prclq / close)`: S=0.66, F=0.51, T=7.8%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_prclq, 5))`: S=0.57, F=0.18, T=36.1%, INFERIOR (TOP500)
- `-rank(fnd6_prclq)`: S=-0.05, F=-0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prclq, 5))`: S=0.30, F=0.08, T=34.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_prclq, 22)`: S=0.40, F=0.14, T=33.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_prclq, 10)`: S=0.27, F=0.13, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_prclq, 22))`: S=0.28, F=0.10, T=13.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prclq)`: S=0.15, F=0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prclq / close)`: S=-0.19, F=-0.09, T=8.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.64, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.59 (moderate), ret=+3.6%
  - 2020: S=-0.70 (negative), ret=-6.8%
  - 2021: S=0.80 (moderate), ret=+12.0%
  - 2022: S=1.43 (moderate), ret=+20.5%
  - 2023: S=0.83 (moderate), ret=+6.1%

## Risk & Drawdown
- Max drawdown: 21.76% over 666 days (recovered)
- Annualized: return +7.2%, volatility 11.3% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.47, excess kurtosis +3.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.76, max 2.10, latest 1.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.32%; worst month: -4.48%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.72
- Sideways: S=-0.12
- Bear: S=-1.17

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_prclq, 5))` S=0.30, F=0.08, INFERIOR
Direction gap: -0.36 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_prclq)`: S=0.15, F=0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prclq / close)`: S=-0.19, F=-0.09, T=8.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prclq, 5))`: S=0.30, F=0.08, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_prclq / close)` | TOP1000 | 0.64 | 0.51 | 21.8% | 80% | bull-only |
| `rank(fnd6_prclq / close)` | TOP3000 | 0.44 | 0.28 | 23.7% | 80% | bull-only |
| `rank(fnd6_prclq / close)` | TOP500 | 0.32 | 0.20 | 35.6% | 80% | bull-only |
| `rank(ts_delta(fnd6_prclq, 5))` | TOP500 | 0.57 | 0.18 | 14.7% | 80% | bull-only |
| `rank(ts_delta(fnd6_prclq, 5))` | TOP1000 | 0.38 | 0.09 | 11.5% | 40% | bull-only |
| `rank(fnd6_prclq / close)` | TOP200 | 0.17 | 0.09 | 45.2% | 60% | bull-only |
| `rank(fnd6_prclq)` | TOP3000 | 0.18 | 0.08 | 52.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_prclq, 5))` | TOP3000 | 0.12 | 0.02 | 17.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_prccq: 0.682 (moderately positively correlated)
- fnd6_prcl: 0.628 (moderately positively correlated)
- fnd6_prcc: 0.594 (moderately positively correlated)
- fnd6_prch: 0.450 (moderately positively correlated)
- fnd6_newqv1300_chq: 0.415 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
