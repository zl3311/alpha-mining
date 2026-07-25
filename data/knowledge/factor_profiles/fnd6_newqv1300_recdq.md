---
field: fnd6_newqv1300_recdq
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.68
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1168
ann_vol: 0.0846
hit_rate: 0.5053
rolling_sharpe_min: -1.205
rolling_sharpe_max: 2.593
redundancy_cluster: 1
negated_best_sharpe: 0.43
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.25
---
# fnd6_newqv1300_recdq (fundamental6)

*Receivables - Estimated Doubtful*

## Signal Profile
- `rank(fnd6_newqv1300_recdq)`: S=0.66, F=0.48, T=5.6%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_recdq / close)`: S=0.75, F=0.53, T=5.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_recdq, 5))`: S=0.36, F=0.15, T=48.8%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_recdq)`: S=-0.26, F=-0.13, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_recdq, 5))`: S=0.43, F=0.16, T=46.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_recdq, 22)`: S=0.60, F=0.33, T=38.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_recdq, 10)`: S=0.68, F=0.54, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_recdq, 22))`: S=-0.72, F=-0.38, T=22.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_recdq)`: S=-0.26, F=-0.13, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_recdq / close)`: S=-0.32, F=-0.17, T=7.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 14F/18P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.18 (weak), ret=+0.9%
  - 2020: S=-0.11 (negative), ret=-1.1%
  - 2021: S=1.54 (strong), ret=+17.1%
  - 2022: S=1.19 (moderate), ret=+9.9%
  - 2023: S=0.89 (moderate), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 11.68% over 406 days (recovered)
- Annualized: return +6.3%, volatility 8.5% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.76, excess kurtosis +6.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.21, max 2.59, latest 0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.50%; worst month: -3.94%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.05
- Sideways: S=0.06
- Bear: S=-1.54

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_recdq, 5))` S=0.43, F=0.16, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_recdq)`: S=-0.26, F=-0.13, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_recdq / close)`: S=-0.32, F=-0.17, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_recdq, 5))`: S=0.43, F=0.16, T=46.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_recdq / close)` | TOP3000 | 0.74 | 0.53 | 11.7% | 80% | bull-only |
| `rank(fnd6_newqv1300_recdq)` | TOP3000 | 0.66 | 0.48 | 28.3% | 80% | bull-only |
| `rank(fnd6_newqv1300_recdq / close)` | TOP200 | 0.58 | 0.47 | 26.6% | 60% | mixed |
| `rank(fnd6_newqv1300_recdq)` | TOP200 | 0.39 | 0.29 | 36.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_recdq / close)` | TOP1000 | 0.32 | 0.17 | 26.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_recdq / close)` | TOP500 | 0.30 | 0.17 | 30.1% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_recdq, 5))` | TOP200 | 0.35 | 0.15 | 31.5% | 60% | mixed |
| `rank(fnd6_newqv1300_recdq)` | TOP1000 | 0.26 | 0.13 | 38.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_recdq)` | TOP500 | 0.10 | 0.03 | 45.9% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_recd: 0.931 (strongly positively correlated)
- receivable: 0.913 (strongly positively correlated)
- fnd6_cptnewqv1300_rectq: 0.913 (strongly positively correlated)
- fnd6_newqv1300_rectrq: 0.905 (strongly positively correlated)
- fnd6_newa2v1300_rect: 0.902 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
