---
field: fnd6_cptmfmq_ceqq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 1.0
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.3191
ann_vol: 0.0964
hit_rate: 0.5134
rolling_sharpe_min: -3.483
rolling_sharpe_max: 2.562
negated_best_sharpe: 0.33
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.67
---
# fnd6_cptmfmq_ceqq (fundamental6)

*Common/Ordinary Equity - Total*

## Signal Profile
- `rank(fnd6_cptmfmq_ceqq)`: S=0.38, F=0.20, T=1.5%, INFERIOR (TOP3000)
- `rank(fnd6_cptmfmq_ceqq / close)`: S=0.24, F=0.09, T=2.3%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_cptmfmq_ceqq, 5))`: S=0.44, F=0.15, T=37.8%, INFERIOR (TOP500)
- `-rank(fnd6_cptmfmq_ceqq)`: S=-0.12, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_ceqq, 5))`: S=0.33, F=0.09, T=37.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptmfmq_ceqq, 22)`: S=1.00, F=0.53, T=39.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptmfmq_ceqq, 10)`: S=0.04, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptmfmq_ceqq, 22))`: S=0.35, F=0.11, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_ceqq)`: S=-0.12, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_ceqq / close)`: S=-0.24, F=-0.09, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.37, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.23 (weak), ret=+1.2%
  - 2020: S=-2.23 (negative), ret=-16.2%
  - 2021: S=0.72 (moderate), ret=+9.8%
  - 2022: S=1.69 (strong), ret=+18.6%
  - 2023: S=0.53 (moderate), ret=+4.2%

## Risk & Drawdown
- Max drawdown: 31.91% over 836 days (recovered)
- Annualized: return +3.6%, volatility 9.6% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.04, excess kurtosis +1.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.48, max 2.56, latest 0.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.07%; worst month: -6.03%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.86
- Sideways: S=1.16
- Bear: S=-3.49

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptmfmq_ceqq, 5))` S=0.33, F=0.09, INFERIOR
Direction gap: -0.67 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cptmfmq_ceqq)`: S=-0.12, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_ceqq / close)`: S=-0.24, F=-0.09, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_ceqq, 5))`: S=0.33, F=0.09, T=37.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptmfmq_ceqq)` | TOP3000 | 0.37 | 0.20 | 31.9% | 80% | bull-only |
| `rank(ts_delta(fnd6_cptmfmq_ceqq, 5))` | TOP500 | 0.44 | 0.15 | 17.9% | 60% | all-weather |
| `rank(ts_delta(fnd6_cptmfmq_ceqq, 5))` | TOP200 | 0.38 | 0.14 | 25.7% | 60% | all-weather |
| `rank(fnd6_cptmfmq_ceqq / close)` | TOP1000 | 0.23 | 0.09 | 13.0% | 60% | bull-only |
| `rank(fnd6_cptmfmq_ceqq / close)` | TOP3000 | 0.22 | 0.08 | 9.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_cptmfmq_ceqq, 5))` | TOP3000 | 0.34 | 0.07 | 15.8% | 60% | mixed |
| `rank(fnd6_cptmfmq_ceqq)` | TOP1000 | 0.11 | 0.04 | 34.0% | 60% | bull-only |
| `rank(fnd6_cptmfmq_ceqq / close)` | TOP500 | 0.07 | 0.02 | 25.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_ceqq: 1.000 (strongly positively correlated)
- equity: 1.000 (strongly positively correlated)
- fnd6_newqv1300_seqq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_teqq: 0.999 (strongly positively correlated)
- invested_capital: 0.981 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
