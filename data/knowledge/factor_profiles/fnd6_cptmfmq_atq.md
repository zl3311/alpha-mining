---
field: fnd6_cptmfmq_atq
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.66
best_fitness: 0.51
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.095
ann_vol: 0.081
hit_rate: 0.4858
rolling_sharpe_min: -0.938
rolling_sharpe_max: 2.33
redundancy_cluster: 1
negated_best_sharpe: 0.09
negated_best_template: rank_neg_delta
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.57
---
# fnd6_cptmfmq_atq (fundamental6)

*Assets - Total*

## Signal Profile
- `rank(fnd6_cptmfmq_atq)`: S=0.66, F=0.51, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_cptmfmq_atq / close)`: S=0.74, F=0.51, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptmfmq_atq, 5))`: S=0.21, F=0.05, T=37.4%, INFERIOR (TOP500)
- `-rank(fnd6_cptmfmq_atq)`: S=-0.32, F=-0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_atq, 5))`: S=0.09, F=0.01, T=37.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cptmfmq_atq, 63)`: S=0.20, F=0.05, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptmfmq_atq, 10)`: S=0.20, F=0.07, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptmfmq_atq, 22))`: S=-0.10, F=-0.02, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_atq)`: S=-0.32, F=-0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_atq / close)`: S=-0.54, F=-0.36, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.07 (negative), ret=-0.4%
  - 2020: S=0.32 (weak), ret=+3.1%
  - 2021: S=1.34 (moderate), ret=+13.6%
  - 2022: S=1.07 (moderate), ret=+7.6%
  - 2023: S=0.86 (moderate), ret=+5.3%

## Risk & Drawdown
- Max drawdown: 9.50% over 239 days (recovered)
- Annualized: return +6.0%, volatility 8.1% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew +0.68, excess kurtosis +3.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.94, max 2.33, latest 0.96

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.96%; worst month: -3.54%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.52
- Sideways: S=0.13
- Bear: S=-0.86

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptmfmq_atq, 5))` S=0.09, F=0.01, INFERIOR
Direction gap: -0.57 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cptmfmq_atq)`: S=-0.32, F=-0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_atq / close)`: S=-0.54, F=-0.36, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_atq, 5))`: S=0.09, F=0.01, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptmfmq_atq / close)` | TOP3000 | 0.74 | 0.51 | 9.5% | 80% | bull-only |
| `rank(fnd6_cptmfmq_atq)` | TOP3000 | 0.65 | 0.51 | 30.6% | 80% | bull-only |
| `rank(fnd6_cptmfmq_atq / close)` | TOP1000 | 0.54 | 0.36 | 14.2% | 80% | bull-only |
| `rank(fnd6_cptmfmq_atq / close)` | TOP500 | 0.41 | 0.26 | 23.0% | 80% | bull-only |
| `rank(fnd6_cptmfmq_atq)` | TOP1000 | 0.32 | 0.19 | 35.1% | 60% | bull-only |
| `rank(fnd6_cptmfmq_atq)` | TOP500 | 0.15 | 0.07 | 48.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_cptmfmq_atq, 5))` | TOP500 | 0.23 | 0.05 | 13.6% | 60% | mixed |
| `rank(fnd6_cptmfmq_atq / close)` | TOP200 | 0.10 | 0.03 | 32.5% | 80% | bull-only |
| `rank(ts_delta(fnd6_cptmfmq_atq, 5))` | TOP200 | 0.12 | 0.02 | 35.3% | 40% | bear-only |

## Correlation Notes
Top correlates:
- assets: 1.000 (strongly positively correlated)
- fnd6_cptnewqv1300_atq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_lseq: 1.000 (strongly positively correlated)
- fnd6_mfma1_at: 0.990 (strongly positively correlated)
- fnd6_newa1v1300_at: 0.990 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
