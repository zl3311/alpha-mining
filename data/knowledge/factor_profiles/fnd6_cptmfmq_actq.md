---
field: fnd6_cptmfmq_actq
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.63
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.3502
ann_vol: 0.1103
hit_rate: 0.5231
rolling_sharpe_min: -3.326
rolling_sharpe_max: 2.629
redundancy_cluster: 13
negated_best_sharpe: 0.17
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.46
---
# fnd6_cptmfmq_actq (fundamental6)

*Current Assets - Total*

## Signal Profile
- `rank(fnd6_cptmfmq_actq)`: S=0.63, F=0.47, T=1.7%, INFERIOR (TOP3000)
- `rank(fnd6_cptmfmq_actq / close)`: S=0.63, F=0.40, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptmfmq_actq, 5))`: S=0.45, F=0.16, T=37.0%, INFERIOR (TOP500)
- `-rank(fnd6_cptmfmq_actq)`: S=-0.30, F=-0.16, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_actq, 5))`: S=0.17, F=0.03, T=37.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptmfmq_actq, 22)`: S=0.42, F=0.15, T=38.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptmfmq_actq, 10)`: S=0.17, F=0.07, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptmfmq_actq, 22))`: S=-0.01, F=0.00, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_actq)`: S=-0.63, F=-0.47, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_actq / close)`: S=-0.63, F=-0.40, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.87 (moderate), ret=+4.8%
  - 2020: S=-1.88 (negative), ret=-15.5%
  - 2021: S=0.90 (moderate), ret=+14.6%
  - 2022: S=1.87 (strong), ret=+22.5%
  - 2023: S=0.84 (moderate), ret=+7.6%

## Risk & Drawdown
- Max drawdown: 35.02% over 787 days (recovered)
- Annualized: return +7.0%, volatility 11.0% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew +0.03, excess kurtosis +1.83

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.33, max 2.63, latest 0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.01%; worst month: -6.82%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.18
- Sideways: S=1.24
- Bear: S=-3.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptmfmq_actq, 5))` S=0.17, F=0.03, INFERIOR
Direction gap: -0.46 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptmfmq_actq)`: S=-0.63, F=-0.47, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_actq / close)`: S=-0.63, F=-0.40, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_actq, 5))`: S=0.17, F=0.03, T=37.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptmfmq_actq)` | TOP3000 | 0.63 | 0.47 | 35.0% | 80% | bull-only |
| `rank(fnd6_cptmfmq_actq / close)` | TOP3000 | 0.62 | 0.40 | 9.2% | 100% | mixed |
| `rank(fnd6_cptmfmq_actq / close)` | TOP1000 | 0.45 | 0.27 | 13.0% | 60% | bull-only |
| `rank(fnd6_cptmfmq_actq / close)` | TOP500 | 0.39 | 0.22 | 17.6% | 80% | bull-only |
| `rank(ts_delta(fnd6_cptmfmq_actq, 5))` | TOP500 | 0.46 | 0.16 | 11.8% | 80% | mixed |
| `rank(fnd6_cptmfmq_actq)` | TOP1000 | 0.29 | 0.16 | 34.5% | 60% | bull-only |
| `rank(fnd6_cptmfmq_actq)` | TOP500 | 0.14 | 0.05 | 46.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- assets_curr: 1.000 (strongly positively correlated)
- fnd6_cptnewqv1300_actq: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_act: 0.993 (strongly positively correlated)
- fnd6_newqv1300_acoq: 0.978 (strongly positively correlated)
- fnd6_newqv1300_teqq: 0.978 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
