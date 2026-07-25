---
field: fnd6_cptnewqv1300_opepsq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.88
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.37
ann_vol: 0.1129
hit_rate: 0.5085
rolling_sharpe_min: -4.575
rolling_sharpe_max: 2.861
negated_best_sharpe: 0.88
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.47
---
# fnd6_cptnewqv1300_opepsq (fundamental6)

*Earnings Per Share from Operations*

## Signal Profile
- `rank(fnd6_cptnewqv1300_opepsq)`: S=0.26, F=0.13, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_opepsq / close)`: S=0.41, F=0.25, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_opepsq, 5))`: S=-0.17, F=-0.03, T=36.8%, INFERIOR (TOP500)
- `-rank(fnd6_cptnewqv1300_opepsq)`: S=-0.22, F=-0.10, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_opepsq, 5))`: S=0.88, F=0.30, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptnewqv1300_opepsq, 22)`: S=0.23, F=0.05, T=37.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_opepsq, 10)`: S=0.27, F=0.13, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_opepsq, 22))`: S=0.29, F=0.08, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_opepsq)`: S=-0.26, F=-0.13, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_opepsq / close)`: S=-0.41, F=-0.25, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.40, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.01 (weak), ret=+0.0%
  - 2020: S=-3.90 (negative), ret=-25.2%
  - 2021: S=1.71 (strong), ret=+21.2%
  - 2022: S=1.68 (strong), ret=+28.1%
  - 2023: S=-0.20 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 37.00% over 792 days (recovered)
- Annualized: return +4.5%, volatility 11.3% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.12, excess kurtosis +1.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.58, max 2.86, latest -0.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.12%; worst month: -9.19%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.00
- Sideways: S=0.50
- Bear: S=-3.22

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_opepsq, 5))` S=0.88, F=0.30, INFERIOR
Direction gap: +0.47 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_opepsq)`: S=-0.26, F=-0.13, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_opepsq / close)`: S=-0.41, F=-0.25, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_opepsq, 5))`: S=0.88, F=0.30, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptnewqv1300_opepsq / close)` | TOP3000 | 0.40 | 0.25 | 37.0% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_opepsq / close)` | TOP1000 | 0.27 | 0.15 | 32.7% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_opepsq)` | TOP3000 | 0.26 | 0.13 | 44.4% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_opepsq)` | TOP1000 | 0.21 | 0.10 | 39.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptmfmq_opepsq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_oepsxq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_epspxq: 0.990 (strongly positively correlated)
- fnd6_cptnewqv1300_epsfxq: 0.990 (strongly positively correlated)
- fnd6_newqv1300_epspiq: 0.989 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
