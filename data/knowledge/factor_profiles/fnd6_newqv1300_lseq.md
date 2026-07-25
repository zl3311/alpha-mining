---
field: fnd6_newqv1300_lseq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.76
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0938
ann_vol: 0.0809
hit_rate: 0.4883
rolling_sharpe_min: -0.913
rolling_sharpe_max: 2.352
redundancy_cluster: 1
negated_best_sharpe: 0.08
negated_best_template: rank_neg_delta
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.68
---
# fnd6_newqv1300_lseq (fundamental6)

*Liabilities and Stockholders' Equity - Total*

## Signal Profile
- `rank(fnd6_newqv1300_lseq)`: S=0.67, F=0.52, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_lseq / close)`: S=0.76, F=0.53, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_lseq, 5))`: S=0.23, F=0.06, T=37.4%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_lseq)`: S=-0.32, F=-0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lseq, 5))`: S=0.08, F=0.01, T=37.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_lseq, 63)`: S=0.20, F=0.05, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_lseq, 10)`: S=0.20, F=0.07, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_lseq, 22))`: S=-0.08, F=-0.01, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lseq)`: S=-0.32, F=-0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lseq / close)`: S=-0.54, F=-0.36, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.75, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.04 (negative), ret=-0.2%
  - 2020: S=0.31 (weak), ret=+3.1%
  - 2021: S=1.37 (moderate), ret=+13.8%
  - 2022: S=1.05 (moderate), ret=+7.5%
  - 2023: S=0.91 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 9.38% over 239 days (recovered)
- Annualized: return +6.1%, volatility 8.1% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +0.69, excess kurtosis +3.73

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.91, max 2.35, latest 1.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.94%; worst month: -3.56%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.54
- Sideways: S=0.16
- Bear: S=-0.86

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_lseq, 5))` S=0.08, F=0.01, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_lseq)`: S=-0.32, F=-0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lseq / close)`: S=-0.54, F=-0.36, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lseq, 5))`: S=0.08, F=0.01, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_lseq / close)` | TOP3000 | 0.75 | 0.53 | 9.4% | 80% | bull-only |
| `rank(fnd6_newqv1300_lseq)` | TOP3000 | 0.67 | 0.52 | 30.7% | 80% | bull-only |
| `rank(fnd6_newqv1300_lseq / close)` | TOP1000 | 0.54 | 0.36 | 14.3% | 80% | bull-only |
| `rank(fnd6_newqv1300_lseq / close)` | TOP500 | 0.41 | 0.26 | 23.2% | 80% | bull-only |
| `rank(fnd6_newqv1300_lseq)` | TOP1000 | 0.32 | 0.19 | 35.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_lseq)` | TOP500 | 0.15 | 0.07 | 48.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_lseq, 5))` | TOP500 | 0.26 | 0.06 | 13.7% | 60% | mixed |
| `rank(fnd6_newqv1300_lseq / close)` | TOP200 | 0.10 | 0.03 | 32.5% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_lseq, 5))` | TOP200 | 0.10 | 0.02 | 35.6% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_atq: 1.000 (strongly positively correlated)
- assets: 1.000 (strongly positively correlated)
- fnd6_cptmfmq_atq: 1.000 (strongly positively correlated)
- fnd6_mfma1_at: 0.989 (strongly positively correlated)
- fnd6_newa1v1300_at: 0.989 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
