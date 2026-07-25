---
field: fnd6_cptnewqv1300_epsfxq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.77
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.3715
ann_vol: 0.1104
hit_rate: 0.4947
rolling_sharpe_min: -4.491
rolling_sharpe_max: 2.824
negated_best_sharpe: 0.77
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: 0.45
---
# fnd6_cptnewqv1300_epsfxq (fundamental6)

*Earnings Per Share (Diluted) - Excluding Extraordinary items*

## Signal Profile
- `rank(fnd6_cptnewqv1300_epsfxq)`: S=0.24, F=0.11, T=2.1%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_epsfxq / close)`: S=0.32, F=0.17, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_epsfxq, 5))`: S=0.07, F=0.01, T=36.7%, INFERIOR (TOP200)
- `-rank(fnd6_cptnewqv1300_epsfxq)`: S=-0.16, F=-0.06, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_epsfxq, 5))`: S=0.77, F=0.25, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptnewqv1300_epsfxq, 22)`: S=0.40, F=0.13, T=37.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_epsfxq, 10)`: S=0.13, F=0.04, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_epsfxq, 22))`: S=0.31, F=0.09, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_epsfxq)`: S=-0.24, F=-0.11, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_epsfxq / close)`: S=-0.32, F=-0.17, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.31, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.05 (negative), ret=-0.2%
  - 2020: S=-3.79 (negative), ret=-25.3%
  - 2021: S=1.61 (strong), ret=+18.6%
  - 2022: S=1.59 (strong), ret=+26.3%
  - 2023: S=-0.24 (negative), ret=-2.6%

## Risk & Drawdown
- Max drawdown: 37.15% over 801 days (recovered)
- Annualized: return +3.4%, volatility 11.0% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew -0.18, excess kurtosis +1.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.49, max 2.82, latest -0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.72%; worst month: -9.22%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.82
- Sideways: S=0.51
- Bear: S=-3.26

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_epsfxq, 5))` S=0.77, F=0.25, INFERIOR
Direction gap: +0.45 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_epsfxq)`: S=-0.24, F=-0.11, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_epsfxq / close)`: S=-0.32, F=-0.17, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_epsfxq, 5))`: S=0.77, F=0.25, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptnewqv1300_epsfxq / close)` | TOP3000 | 0.31 | 0.17 | 37.1% | 40% | bull-only |
| `rank(fnd6_cptnewqv1300_epsfxq)` | TOP3000 | 0.23 | 0.11 | 41.6% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_epsfxq)` | TOP1000 | 0.15 | 0.06 | 38.8% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_epsfxq / close)` | TOP1000 | 0.15 | 0.06 | 33.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_epspxq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_epsfiq: 0.999 (strongly positively correlated)
- fnd6_newqv1300_epspiq: 0.999 (strongly positively correlated)
- eps: 0.999 (strongly positively correlated)
- earnings_per_share_reported_value: 0.991 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
