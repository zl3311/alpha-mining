---
field: fnd6_cptmfmq_saleq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.04
best_fitness: 0.87
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0868
ann_vol: 0.0848
hit_rate: 0.502
rolling_sharpe_min: -1.124
rolling_sharpe_max: 2.738
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.83
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.21
---
# fnd6_cptmfmq_saleq (fundamental6)

*Sales/Turnover (Net)*

## Signal Profile
- `rank(fnd6_cptmfmq_saleq)`: S=0.73, F=0.62, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_cptmfmq_saleq / close)`: S=1.04, F=0.87, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptmfmq_saleq, 5))`: S=0.00, F=0.00, T=36.9%, INFERIOR (TOP500)
- `-rank(fnd6_cptmfmq_saleq)`: S=-0.36, F=-0.23, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_saleq, 5))`: S=0.83, F=0.29, T=37.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cptmfmq_saleq, 63)`: S=0.04, F=0.00, T=19.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptmfmq_saleq, 10)`: S=0.17, F=0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptmfmq_saleq, 22))`: S=-0.10, F=-0.02, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_saleq)`: S=-0.73, F=-0.62, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_saleq / close)`: S=-1.04, F=-0.87, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.04, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.09 (negative), ret=-0.4%
  - 2020: S=-0.11 (negative), ret=-1.0%
  - 2021: S=1.68 (strong), ret=+19.8%
  - 2022: S=1.95 (strong), ret=+17.1%
  - 2023: S=1.67 (strong), ret=+7.6%

## Risk & Drawdown
- Max drawdown: 8.68% over 238 days (recovered)
- Annualized: return +8.8%, volatility 8.5% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.32, excess kurtosis +2.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.12, max 2.74, latest 1.68

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.10%; worst month: -3.66%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.62
- Sideways: S=0.32
- Bear: S=-1.53

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptmfmq_saleq, 5))` S=0.83, F=0.29, INFERIOR
Direction gap: -0.21 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptmfmq_saleq)`: S=-0.73, F=-0.62, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_saleq / close)`: S=-1.04, F=-0.87, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_saleq, 5))`: S=0.83, F=0.29, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptmfmq_saleq / close)` | TOP3000 | 1.04 | 0.87 | 8.7% | 60% | bull-only |
| `rank(fnd6_cptmfmq_saleq)` | TOP3000 | 0.72 | 0.62 | 32.7% | 80% | bull-only |
| `rank(fnd6_cptmfmq_saleq / close)` | TOP1000 | 0.63 | 0.46 | 14.7% | 60% | bull-only |
| `rank(fnd6_cptmfmq_saleq / close)` | TOP500 | 0.44 | 0.29 | 25.1% | 60% | bull-only |
| `rank(fnd6_cptmfmq_saleq)` | TOP1000 | 0.35 | 0.23 | 38.1% | 60% | bull-only |
| `rank(fnd6_cptmfmq_saleq)` | TOP500 | 0.18 | 0.09 | 48.8% | 60% | bull-only |
| `rank(fnd6_cptmfmq_saleq / close)` | TOP200 | 0.12 | 0.04 | 38.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- sales: 1.000 (strongly positively correlated)
- fnd6_cptnewqv1300_saleq: 1.000 (strongly positively correlated)
- revenue: 0.998 (strongly positively correlated)
- fnd6_newqv1300_revtq: 0.998 (strongly positively correlated)
- fnd6_mfma2_revt: 0.989 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.33 | 1.76 | +0.72 | -0.51 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.89 | +0.71 | -0.34 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.67 | +0.63 | -0.64 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.23 | 1.60 | +0.56 | -0.63 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.30 | 1.53 | +0.49 | -0.72 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
