---
field: fnd6_newqv1300_seqq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.96
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.3156
ann_vol: 0.0962
hit_rate: 0.5085
rolling_sharpe_min: -3.444
rolling_sharpe_max: 2.575
negated_best_sharpe: 0.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.66
---
# fnd6_newqv1300_seqq (fundamental6)

*Stockholders' Equity - Total - Quarterly*

## Signal Profile
- `rank(fnd6_newqv1300_seqq)`: S=0.40, F=0.22, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_seqq / close)`: S=0.27, F=0.10, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_seqq, 5))`: S=0.47, F=0.19, T=37.6%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_seqq)`: S=-0.12, F=-0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_seqq, 5))`: S=0.30, F=0.07, T=37.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_seqq, 22)`: S=0.96, F=0.50, T=39.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_seqq, 10)`: S=-0.02, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_seqq, 22))`: S=0.25, F=0.07, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_seqq)`: S=-0.12, F=-0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_seqq / close)`: S=-0.25, F=-0.10, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.39, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.24 (weak), ret=+1.2%
  - 2020: S=-2.17 (negative), ret=-15.8%
  - 2021: S=0.70 (moderate), ret=+9.5%
  - 2022: S=1.71 (strong), ret=+18.7%
  - 2023: S=0.59 (moderate), ret=+4.7%

## Risk & Drawdown
- Max drawdown: 31.56% over 836 days (recovered)
- Annualized: return +3.8%, volatility 9.6% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.04, excess kurtosis +1.41

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.44, max 2.58, latest 0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.05%; worst month: -6.07%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.87
- Sideways: S=1.21
- Bear: S=-3.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_seqq, 5))` S=0.30, F=0.07, INFERIOR
Direction gap: -0.66 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_seqq)`: S=-0.12, F=-0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_seqq / close)`: S=-0.25, F=-0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_seqq, 5))`: S=0.30, F=0.07, T=37.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_seqq)` | TOP3000 | 0.39 | 0.22 | 31.6% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_seqq, 5))` | TOP200 | 0.48 | 0.19 | 18.8% | 60% | all-weather |
| `rank(ts_delta(fnd6_newqv1300_seqq, 5))` | TOP500 | 0.48 | 0.18 | 17.0% | 60% | all-weather |
| `rank(fnd6_newqv1300_seqq / close)` | TOP3000 | 0.26 | 0.10 | 9.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_seqq / close)` | TOP1000 | 0.24 | 0.10 | 12.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_seqq, 5))` | TOP3000 | 0.26 | 0.05 | 16.8% | 40% | mixed |
| `rank(fnd6_newqv1300_seqq)` | TOP1000 | 0.11 | 0.04 | 33.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_seqq / close)` | TOP500 | 0.09 | 0.03 | 24.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_teqq: 1.000 (strongly positively correlated)
- equity: 1.000 (strongly positively correlated)
- fnd6_cptnewqv1300_ceqq: 1.000 (strongly positively correlated)
- fnd6_cptmfmq_ceqq: 1.000 (strongly positively correlated)
- invested_capital: 0.981 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
