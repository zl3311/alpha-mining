---
field: fnd6_newqv1300_ciderglq
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.6
best_fitness: 0.36
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 11
max_drawdown: 0.1248
ann_vol: 0.0767
hit_rate: 0.5198
rolling_sharpe_min: -1.169
rolling_sharpe_max: 2.713
negated_best_sharpe: 0.18
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.42
---
# fnd6_newqv1300_ciderglq (fundamental6)

*Comp Inc - Derivative Gains/Losses*

## Signal Profile
- `rank(fnd6_newqv1300_ciderglq)`: S=0.60, F=0.36, T=10.3%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_ciderglq / close)`: S=0.57, F=0.34, T=10.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_ciderglq, 5))`: S=0.69, F=0.34, T=59.3%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_ciderglq)`: S=-0.39, F=-0.14, T=8.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ciderglq, 5))`: S=0.18, F=0.04, T=58.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_ciderglq, 22)`: S=-0.10, F=-0.02, T=39.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ciderglq, 10)`: S=0.09, F=0.02, T=5.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ciderglq, 22))`: S=0.25, F=0.06, T=22.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ciderglq)`: S=-0.30, F=-0.10, T=9.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ciderglq / close)`: S=-0.29, F=-0.10, T=9.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.58, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.83 (negative), ret=-4.6%
  - 2020: S=0.80 (moderate), ret=+4.7%
  - 2021: S=-0.14 (negative), ret=-1.3%
  - 2022: S=2.40 (strong), ret=+24.4%
  - 2023: S=-0.24 (negative), ret=-1.4%

## Risk & Drawdown
- Max drawdown: 12.48% over 349 days (recovered)
- Annualized: return +4.5%, volatility 7.7% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew -0.18, excess kurtosis +2.93

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.17, max 2.71, latest -0.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.68%; worst month: -7.85%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.73
- Sideways: S=0.06
- Bear: S=-0.34

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_ciderglq, 5))` S=0.18, F=0.04, INFERIOR
Direction gap: -0.42 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ciderglq)`: S=-0.30, F=-0.10, T=9.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ciderglq / close)`: S=-0.29, F=-0.10, T=9.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ciderglq, 5))`: S=0.18, F=0.04, T=58.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_ciderglq)` | TOP200 | 0.58 | 0.36 | 12.5% | 40% | mixed |
| `rank(fnd6_newqv1300_ciderglq / close)` | TOP200 | 0.55 | 0.34 | 13.3% | 40% | mixed |
| `rank(ts_delta(fnd6_newqv1300_ciderglq, 5))` | TOP200 | 0.69 | 0.34 | 22.5% | 100% | mixed |
| `rank(fnd6_newqv1300_ciderglq / close)` | TOP1000 | 0.40 | 0.15 | 5.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_ciderglq)` | TOP1000 | 0.39 | 0.14 | 5.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_ciderglq, 5))` | TOP1000 | 0.37 | 0.11 | 22.1% | 80% | all-weather |
| `rank(fnd6_newqv1300_ciderglq / close)` | TOP3000 | 0.33 | 0.11 | 6.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_ciderglq)` | TOP3000 | 0.33 | 0.11 | 7.1% | 60% | bull-only |
| `rank(fnd6_newqv1300_ciderglq / close)` | TOP500 | 0.28 | 0.10 | 9.1% | 40% | bull-only |
| `rank(fnd6_newqv1300_ciderglq)` | TOP500 | 0.28 | 0.10 | 8.6% | 40% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_ciderglq, 5))` | TOP3000 | 0.25 | 0.06 | 17.3% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_prchq: -0.345 (weakly negatively correlated)
- parkinson_volatility_150: -0.338 (weakly negatively correlated)
- parkinson_volatility_180: -0.337 (weakly negatively correlated)
- historical_volatility_180: -0.331 (weakly negatively correlated)
- historical_volatility_150: -0.330 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
