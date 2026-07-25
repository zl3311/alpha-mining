---
field: fnd6_newqv1300_teqq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.98
best_fitness: 0.51
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.3205
ann_vol: 0.097
hit_rate: 0.5077
rolling_sharpe_min: -3.477
rolling_sharpe_max: 2.575
negated_best_sharpe: 0.42
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.56
---
# fnd6_newqv1300_teqq (fundamental6)

*Stockholders' Equity - Total - Quarterly*

## Signal Profile
- `rank(fnd6_newqv1300_teqq)`: S=0.40, F=0.22, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_teqq / close)`: S=0.29, F=0.11, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_teqq, 5))`: S=0.39, F=0.15, T=37.3%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_teqq)`: S=-0.13, F=-0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_teqq, 5))`: S=0.42, F=0.12, T=37.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_teqq, 22)`: S=0.98, F=0.51, T=39.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_teqq, 10)`: S=-0.03, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_teqq, 22))`: S=0.43, F=0.15, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_teqq)`: S=-0.13, F=-0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_teqq / close)`: S=-0.27, F=-0.11, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.39, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.25 (weak), ret=+1.3%
  - 2020: S=-2.19 (negative), ret=-16.0%
  - 2021: S=0.71 (moderate), ret=+9.8%
  - 2022: S=1.69 (strong), ret=+18.6%
  - 2023: S=0.62 (moderate), ret=+4.9%

## Risk & Drawdown
- Max drawdown: 32.05% over 836 days (recovered)
- Annualized: return +3.8%, volatility 9.7% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.04, excess kurtosis +1.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.48, max 2.58, latest 0.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.16%; worst month: -6.17%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.87
- Sideways: S=1.22
- Bear: S=-3.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_teqq, 5))` S=0.42, F=0.12, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_teqq)`: S=-0.13, F=-0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_teqq / close)`: S=-0.27, F=-0.11, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_teqq, 5))`: S=0.42, F=0.12, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_teqq)` | TOP3000 | 0.39 | 0.22 | 32.0% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_teqq, 5))` | TOP200 | 0.40 | 0.15 | 15.5% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_teqq, 5))` | TOP500 | 0.37 | 0.12 | 17.5% | 40% | all-weather |
| `rank(fnd6_newqv1300_teqq / close)` | TOP1000 | 0.27 | 0.11 | 12.3% | 40% | bull-only |
| `rank(fnd6_newqv1300_teqq / close)` | TOP3000 | 0.28 | 0.11 | 9.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_teqq, 5))` | TOP3000 | 0.29 | 0.06 | 16.5% | 40% | mixed |
| `rank(fnd6_newqv1300_teqq)` | TOP1000 | 0.12 | 0.04 | 33.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_teqq / close)` | TOP500 | 0.10 | 0.03 | 25.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_seqq: 1.000 (strongly positively correlated)
- fnd6_cptnewqv1300_ceqq: 0.999 (strongly positively correlated)
- equity: 0.999 (strongly positively correlated)
- fnd6_cptmfmq_ceqq: 0.999 (strongly positively correlated)
- invested_capital: 0.982 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
