---
field: fnd6_cptmfmq_opepsq
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
max_drawdown: 0.3697
ann_vol: 0.1129
hit_rate: 0.5077
rolling_sharpe_min: -4.571
rolling_sharpe_max: 2.86
negated_best_sharpe: 0.88
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.48
---
# fnd6_cptmfmq_opepsq (fundamental6)

*Earnings Per Share from Operations*

## Signal Profile
- `rank(fnd6_cptmfmq_opepsq)`: S=0.26, F=0.13, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_cptmfmq_opepsq / close)`: S=0.40, F=0.24, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptmfmq_opepsq, 5))`: S=-0.17, F=-0.03, T=36.8%, INFERIOR (TOP500)
- `-rank(fnd6_cptmfmq_opepsq)`: S=-0.21, F=-0.09, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_opepsq, 5))`: S=0.88, F=0.30, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptmfmq_opepsq, 22)`: S=0.18, F=0.04, T=37.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptmfmq_opepsq, 10)`: S=0.27, F=0.13, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptmfmq_opepsq, 22))`: S=0.26, F=0.07, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_opepsq)`: S=-0.26, F=-0.13, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_opepsq / close)`: S=-0.40, F=-0.24, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.39, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.02 (weak), ret=+0.1%
  - 2020: S=-3.90 (negative), ret=-25.1%
  - 2021: S=1.71 (strong), ret=+21.2%
  - 2022: S=1.65 (strong), ret=+27.7%
  - 2023: S=-0.23 (negative), ret=-2.5%

## Risk & Drawdown
- Max drawdown: 36.97% over 792 days (recovered)
- Annualized: return +4.4%, volatility 11.3% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.13, excess kurtosis +1.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.57, max 2.86, latest -0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.09%; worst month: -9.16%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.98
- Sideways: S=0.48
- Bear: S=-3.22

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptmfmq_opepsq, 5))` S=0.88, F=0.30, INFERIOR
Direction gap: +0.48 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptmfmq_opepsq)`: S=-0.26, F=-0.13, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_opepsq / close)`: S=-0.40, F=-0.24, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_opepsq, 5))`: S=0.88, F=0.30, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptmfmq_opepsq / close)` | TOP3000 | 0.39 | 0.24 | 37.0% | 60% | bull-only |
| `rank(fnd6_cptmfmq_opepsq / close)` | TOP1000 | 0.26 | 0.14 | 33.0% | 60% | bull-only |
| `rank(fnd6_cptmfmq_opepsq)` | TOP3000 | 0.25 | 0.13 | 44.2% | 60% | bull-only |
| `rank(fnd6_cptmfmq_opepsq)` | TOP1000 | 0.20 | 0.09 | 40.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_opepsq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_oepsxq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_epspxq: 0.990 (strongly positively correlated)
- fnd6_cptnewqv1300_epsfxq: 0.990 (strongly positively correlated)
- fnd6_newqv1300_epspiq: 0.989 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
