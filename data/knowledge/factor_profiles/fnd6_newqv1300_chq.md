---
field: fnd6_newqv1300_chq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.62
best_fitness: 0.39
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.1254
ann_vol: 0.0818
hit_rate: 0.4955
rolling_sharpe_min: -0.958
rolling_sharpe_max: 2.43
redundancy_cluster: 31
negated_best_sharpe: 0.07
negated_best_template: neg_rank_level
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.55
---
# fnd6_newqv1300_chq (fundamental6)

*Cash*

## Signal Profile
- `rank(fnd6_newqv1300_chq)`: S=0.46, F=0.24, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_chq / close)`: S=0.62, F=0.39, T=3.1%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_chq, 5))`: S=0.75, F=0.33, T=37.1%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_chq)`: S=-0.28, F=-0.13, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_chq, 5))`: S=-0.22, F=-0.06, T=37.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_chq, 22)`: S=0.53, F=0.20, T=37.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_chq, 10)`: S=0.51, F=0.30, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_chq, 22))`: S=-0.24, F=-0.06, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_chq)`: S=0.07, F=0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_chq / close)`: S=-0.13, F=-0.04, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.38 (weak), ret=+2.0%
  - 2020: S=-0.24 (negative), ret=-2.2%
  - 2021: S=0.41 (weak), ret=+5.1%
  - 2022: S=1.97 (strong), ret=+11.8%
  - 2023: S=1.94 (strong), ret=+8.2%

## Risk & Drawdown
- Max drawdown: 12.54% over 370 days (recovered)
- Annualized: return +5.1%, volatility 8.2% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.52, excess kurtosis +4.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.96, max 2.43, latest 2.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.31%; worst month: -8.04%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.72
- Sideways: S=-0.25
- Bear: S=-1.19

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_chq)` S=0.07, F=0.02, INFERIOR
Direction gap: -0.55 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_chq)`: S=0.07, F=0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_chq / close)`: S=-0.13, F=-0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_chq, 5))`: S=-0.22, F=-0.06, T=37.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_chq / close)` | TOP500 | 0.62 | 0.39 | 12.5% | 80% | bull-only |
| `rank(fnd6_newqv1300_chq / close)` | TOP1000 | 0.57 | 0.34 | 10.1% | 100% | mixed |
| `rank(ts_delta(fnd6_newqv1300_chq, 5))` | TOP500 | 0.74 | 0.33 | 13.9% | 100% | all-weather |
| `rank(fnd6_newqv1300_chq)` | TOP3000 | 0.46 | 0.24 | 26.1% | 80% | bull-only |
| `rank(fnd6_newqv1300_chq / close)` | TOP3000 | 0.40 | 0.19 | 13.1% | 80% | mixed |
| `rank(fnd6_newqv1300_chq)` | TOP1000 | 0.28 | 0.13 | 26.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_chq)` | TOP500 | 0.18 | 0.07 | 34.2% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_chq, 5))` | TOP200 | 0.24 | 0.07 | 35.4% | 80% | mixed |
| `rank(fnd6_newqv1300_chq / close)` | TOP200 | 0.14 | 0.04 | 22.6% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_chq, 5))` | TOP3000 | 0.19 | 0.03 | 10.7% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_mfmq_cheq: 0.979 (strongly positively correlated)
- cash_st: 0.979 (strongly positively correlated)
- fnd6_ch: 0.942 (strongly positively correlated)
- fnd6_newa1v1300_che: 0.933 (strongly positively correlated)
- fnd6_newa2v1300_stkco: 0.824 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
