---
field: fnd6_mfmq_cheq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.61
best_fitness: 0.39
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 11
max_drawdown: 0.1238
ann_vol: 0.0835
hit_rate: 0.4899
rolling_sharpe_min: -0.812
rolling_sharpe_max: 2.429
redundancy_cluster: 31
negated_best_sharpe: 0.06
negated_best_template: neg_rank_level
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.55
---
# fnd6_mfmq_cheq (fundamental6)

*Cash and Short-Term Investments*

## Signal Profile
- `rank(fnd6_mfmq_cheq)`: S=0.52, F=0.29, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_mfmq_cheq / close)`: S=0.61, F=0.39, T=3.1%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_mfmq_cheq, 5))`: S=0.50, F=0.20, T=38.0%, INFERIOR (TOP200)
- `-rank(fnd6_mfmq_cheq)`: S=-0.27, F=-0.12, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfmq_cheq, 5))`: S=-0.47, F=-0.19, T=38.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_mfmq_cheq, 22)`: S=0.29, F=0.08, T=37.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfmq_cheq, 10)`: S=0.48, F=0.28, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfmq_cheq, 22))`: S=0.04, F=0.00, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfmq_cheq)`: S=0.06, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfmq_cheq / close)`: S=-0.19, F=-0.08, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.25 (weak), ret=+1.4%
  - 2020: S=-0.03 (negative), ret=-0.3%
  - 2021: S=0.37 (weak), ret=+4.6%
  - 2022: S=2.16 (strong), ret=+13.1%
  - 2023: S=1.51 (strong), ret=+6.5%

## Risk & Drawdown
- Max drawdown: 12.38% over 370 days (recovered)
- Annualized: return +5.2%, volatility 8.3% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.55, excess kurtosis +4.41

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.81, max 2.43, latest 1.61

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.49%; worst month: -7.71%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.75
- Sideways: S=-0.31
- Bear: S=-1.09

## Negated Direction
Best negated: `rank(-1 * fnd6_mfmq_cheq)` S=0.06, F=0.02, INFERIOR
Direction gap: -0.55 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mfmq_cheq)`: S=0.06, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfmq_cheq / close)`: S=-0.19, F=-0.08, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfmq_cheq, 5))`: S=-0.47, F=-0.19, T=38.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfmq_cheq / close)` | TOP500 | 0.62 | 0.39 | 12.4% | 80% | bull-only |
| `rank(fnd6_mfmq_cheq / close)` | TOP1000 | 0.53 | 0.31 | 10.1% | 100% | mixed |
| `rank(fnd6_mfmq_cheq)` | TOP3000 | 0.52 | 0.29 | 24.9% | 80% | bull-only |
| `rank(fnd6_mfmq_cheq / close)` | TOP3000 | 0.44 | 0.23 | 12.6% | 80% | mixed |
| `rank(ts_delta(fnd6_mfmq_cheq, 5))` | TOP200 | 0.50 | 0.20 | 35.8% | 60% | mixed |
| `rank(ts_delta(fnd6_mfmq_cheq, 5))` | TOP500 | 0.51 | 0.19 | 15.9% | 80% | all-weather |
| `rank(ts_delta(fnd6_mfmq_cheq, 5))` | TOP3000 | 0.47 | 0.13 | 9.2% | 60% | mixed |
| `rank(fnd6_mfmq_cheq)` | TOP1000 | 0.27 | 0.12 | 27.4% | 60% | bull-only |
| `rank(fnd6_mfmq_cheq)` | TOP500 | 0.21 | 0.08 | 35.2% | 60% | bull-only |
| `rank(fnd6_mfmq_cheq / close)` | TOP200 | 0.20 | 0.08 | 23.1% | 80% | bull-only |
| `rank(ts_delta(fnd6_mfmq_cheq, 5))` | TOP1000 | 0.23 | 0.05 | 12.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cash_st: 1.000 (strongly positively correlated)
- fnd6_newqv1300_chq: 0.979 (strongly positively correlated)
- fnd6_newa1v1300_che: 0.950 (strongly positively correlated)
- fnd6_ch: 0.927 (strongly positively correlated)
- fnd6_newa2v1300_stkco: 0.819 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
