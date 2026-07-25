---
field: fnd6_cptnewqv1300_ceqq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 1.02
best_fitness: 0.55
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.3205
ann_vol: 0.0963
hit_rate: 0.5117
rolling_sharpe_min: -3.489
rolling_sharpe_max: 2.593
negated_best_sharpe: 0.34
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.68
---
# fnd6_cptnewqv1300_ceqq (fundamental6)

*Common/Ordinary Equity - Total*

## Signal Profile
- `rank(fnd6_cptnewqv1300_ceqq)`: S=0.39, F=0.21, T=1.5%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_ceqq / close)`: S=0.25, F=0.09, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_ceqq, 5))`: S=0.46, F=0.16, T=37.8%, INFERIOR (TOP500)
- `-rank(fnd6_cptnewqv1300_ceqq)`: S=-0.12, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_ceqq, 5))`: S=0.34, F=0.09, T=37.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptnewqv1300_ceqq, 22)`: S=1.02, F=0.55, T=39.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_ceqq, 10)`: S=0.04, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_ceqq, 22))`: S=0.36, F=0.12, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_ceqq)`: S=-0.12, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_ceqq / close)`: S=-0.24, F=-0.09, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.39, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.24 (weak), ret=+1.2%
  - 2020: S=-2.24 (negative), ret=-16.3%
  - 2021: S=0.73 (moderate), ret=+9.9%
  - 2022: S=1.70 (strong), ret=+18.7%
  - 2023: S=0.59 (moderate), ret=+4.7%

## Risk & Drawdown
- Max drawdown: 32.05% over 836 days (recovered)
- Annualized: return +3.7%, volatility 9.6% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.04, excess kurtosis +1.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.49, max 2.59, latest 0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.09%; worst month: -6.06%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.88
- Sideways: S=1.20
- Bear: S=-3.49

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_ceqq, 5))` S=0.34, F=0.09, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_ceqq)`: S=-0.12, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_ceqq / close)`: S=-0.24, F=-0.09, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_ceqq, 5))`: S=0.34, F=0.09, T=37.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptnewqv1300_ceqq)` | TOP3000 | 0.39 | 0.21 | 32.0% | 80% | bull-only |
| `rank(ts_delta(fnd6_cptnewqv1300_ceqq, 5))` | TOP500 | 0.46 | 0.16 | 17.8% | 60% | all-weather |
| `rank(ts_delta(fnd6_cptnewqv1300_ceqq, 5))` | TOP200 | 0.37 | 0.13 | 24.9% | 60% | all-weather |
| `rank(fnd6_cptnewqv1300_ceqq / close)` | TOP3000 | 0.23 | 0.09 | 9.2% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_ceqq / close)` | TOP1000 | 0.23 | 0.09 | 12.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_cptnewqv1300_ceqq, 5))` | TOP3000 | 0.34 | 0.07 | 15.6% | 60% | mixed |
| `rank(fnd6_cptnewqv1300_ceqq)` | TOP1000 | 0.11 | 0.04 | 33.9% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_ceqq / close)` | TOP500 | 0.08 | 0.02 | 26.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- equity: 1.000 (strongly positively correlated)
- fnd6_cptmfmq_ceqq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_seqq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_teqq: 0.999 (strongly positively correlated)
- invested_capital: 0.981 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
