---
field: fnd6_cptmfmq_dlttq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.19
best_fitness: 1.05
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0779
ann_vol: 0.0819
hit_rate: 0.5028
rolling_sharpe_min: -0.696
rolling_sharpe_max: 2.839
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.43
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.76
---
# fnd6_cptmfmq_dlttq (fundamental6)

*Long-Term Debt - Total*

## Signal Profile
- `rank(fnd6_cptmfmq_dlttq)`: S=0.87, F=0.73, T=1.6%, INFERIOR (TOP3000)
- `rank(fnd6_cptmfmq_dlttq / close)`: S=1.19, F=1.05, T=1.9%, AVERAGE (TOP3000)
- `rank(ts_delta(fnd6_cptmfmq_dlttq, 5))`: S=-0.30, F=-0.07, T=37.8%, INFERIOR (TOP1000)
- `-rank(fnd6_cptmfmq_dlttq)`: S=-0.34, F=-0.20, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_dlttq, 5))`: S=0.43, F=0.10, T=37.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cptmfmq_dlttq, 63)`: S=0.62, F=0.23, T=18.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptmfmq_dlttq, 10)`: S=0.29, F=0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptmfmq_dlttq, 22))`: S=0.06, F=0.01, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_dlttq)`: S=-0.87, F=-0.73, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_dlttq / close)`: S=-1.19, F=-1.05, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.19, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.94 (moderate), ret=+4.2%
  - 2020: S=0.81 (moderate), ret=+7.9%
  - 2021: S=1.72 (strong), ret=+19.0%
  - 2022: S=1.61 (strong), ret=+12.3%
  - 2023: S=0.83 (moderate), ret=+4.1%

## Risk & Drawdown
- Max drawdown: 7.79% over 90 days (recovered)
- Annualized: return +9.7%, volatility 8.2% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.50, excess kurtosis +3.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.70, max 2.84, latest 0.90

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.99%; worst month: -2.87%
Positive months: 66%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.01
- Sideways: S=0.69
- Bear: S=-0.57

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptmfmq_dlttq, 5))` S=0.43, F=0.10, INFERIOR
Direction gap: -0.76 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cptmfmq_dlttq)`: S=-0.87, F=-0.73, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_dlttq / close)`: S=-1.19, F=-1.05, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_dlttq, 5))`: S=0.43, F=0.10, T=37.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptmfmq_dlttq / close)` | TOP3000 | 1.19 | 1.05 | 7.8% | 100% | bull-only |
| `rank(fnd6_cptmfmq_dlttq)` | TOP3000 | 0.86 | 0.73 | 20.6% | 80% | bull-only |
| `rank(fnd6_cptmfmq_dlttq / close)` | TOP1000 | 0.62 | 0.44 | 12.8% | 80% | bull-only |
| `rank(fnd6_cptmfmq_dlttq / close)` | TOP500 | 0.47 | 0.31 | 18.9% | 60% | bull-only |
| `rank(fnd6_cptmfmq_dlttq)` | TOP1000 | 0.34 | 0.20 | 28.2% | 60% | bull-only |
| `rank(fnd6_cptmfmq_dlttq)` | TOP500 | 0.20 | 0.10 | 41.6% | 60% | bull-only |
| `rank(fnd6_cptmfmq_dlttq / close)` | TOP200 | 0.11 | 0.04 | 29.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- debt_lt: 1.000 (strongly positively correlated)
- fnd6_cptnewqv1300_dlttq: 1.000 (strongly positively correlated)
- debt: 0.991 (strongly positively correlated)
- fnd6_newa1v1300_dltt: 0.990 (strongly positively correlated)
- fnd6_newqv1300_lltq: 0.979 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 2.07 | +0.89 | -0.84 | yes |
| anl4_rd_exp_flag | analyst4 | -0.32 | 1.85 | +0.67 | -0.52 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.77 | +0.59 | -0.81 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.24 | 1.72 | +0.54 | -0.82 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.13 | 2.15 | +0.52 | -0.61 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
