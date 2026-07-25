---
field: fnd6_newqv1300_oepsxq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.84
best_fitness: 0.28
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.3751
ann_vol: 0.1149
hit_rate: 0.5045
rolling_sharpe_min: -4.626
rolling_sharpe_max: 2.877
negated_best_sharpe: 0.84
negated_best_template: rank_neg_delta
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: 0.44
---
# fnd6_newqv1300_oepsxq (fundamental6)

*Earnings Per Share - Diluted - from Operations*

## Signal Profile
- `rank(fnd6_newqv1300_oepsxq)`: S=0.26, F=0.13, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_oepsxq / close)`: S=0.40, F=0.24, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_oepsxq, 5))`: S=-0.10, F=-0.02, T=36.8%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_oepsxq)`: S=-0.22, F=-0.10, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_oepsxq, 5))`: S=0.84, F=0.28, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_oepsxq, 22)`: S=0.02, F=0.00, T=37.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_oepsxq, 10)`: S=0.28, F=0.14, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_oepsxq, 22))`: S=0.35, F=0.11, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_oepsxq)`: S=-0.26, F=-0.13, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_oepsxq / close)`: S=-0.40, F=-0.24, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.40, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.01 (weak), ret=+0.1%
  - 2020: S=-3.94 (negative), ret=-25.5%
  - 2021: S=1.69 (strong), ret=+21.2%
  - 2022: S=1.66 (strong), ret=+28.7%
  - 2023: S=-0.21 (negative), ret=-2.3%

## Risk & Drawdown
- Max drawdown: 37.51% over 793 days (recovered)
- Annualized: return +4.5%, volatility 11.5% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.13, excess kurtosis +1.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.63, max 2.88, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.43%; worst month: -9.19%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.96
- Sideways: S=0.53
- Bear: S=-3.22

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_oepsxq, 5))` S=0.84, F=0.28, INFERIOR
Direction gap: +0.44 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_oepsxq)`: S=-0.26, F=-0.13, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_oepsxq / close)`: S=-0.40, F=-0.24, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_oepsxq, 5))`: S=0.84, F=0.28, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_oepsxq / close)` | TOP3000 | 0.40 | 0.24 | 37.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_oepsxq / close)` | TOP1000 | 0.30 | 0.18 | 32.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_oepsxq)` | TOP3000 | 0.26 | 0.13 | 44.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_oepsxq)` | TOP1000 | 0.21 | 0.10 | 39.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_opepsq: 1.000 (strongly positively correlated)
- fnd6_cptmfmq_opepsq: 1.000 (strongly positively correlated)
- fnd6_cptnewqv1300_epsfxq: 0.990 (strongly positively correlated)
- fnd6_newqv1300_epspxq: 0.990 (strongly positively correlated)
- fnd6_newqv1300_epsfiq: 0.990 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
