---
field: fnd6_newqv1300_lltq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.9
best_fitness: 0.7
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0925
ann_vol: 0.0852
hit_rate: 0.4931
rolling_sharpe_min: -0.974
rolling_sharpe_max: 2.578
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.11
negated_best_template: neg_rank_level
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.79
---
# fnd6_newqv1300_lltq (fundamental6)

*Long-Term Liabilities (Total)*

## Signal Profile
- `rank(fnd6_newqv1300_lltq)`: S=0.72, F=0.59, T=1.6%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_lltq / close)`: S=0.90, F=0.70, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_lltq, 5))`: S=0.65, F=0.25, T=37.1%, INFERIOR (TOP1000)
- `-rank(fnd6_newqv1300_lltq)`: S=-0.23, F=-0.12, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lltq, 5))`: S=0.05, F=0.01, T=37.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_lltq, 63)`: S=0.34, F=0.11, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_lltq, 10)`: S=0.14, F=0.05, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_lltq, 22))`: S=0.56, F=0.23, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lltq)`: S=0.11, F=0.04, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lltq / close)`: S=0.03, F=0.01, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.90, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.48 (weak), ret=+2.4%
  - 2020: S=0.51 (moderate), ret=+4.9%
  - 2021: S=1.43 (moderate), ret=+17.1%
  - 2022: S=1.31 (moderate), ret=+10.2%
  - 2023: S=0.56 (moderate), ret=+2.9%

## Risk & Drawdown
- Max drawdown: 9.25% over 90 days (recovered)
- Annualized: return +7.6%, volatility 8.5% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +0.47, excess kurtosis +3.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.97, max 2.58, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.01%; worst month: -3.48%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.87
- Sideways: S=0.20
- Bear: S=-0.94

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_lltq)` S=0.11, F=0.04, INFERIOR
Direction gap: -0.79 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_lltq)`: S=0.11, F=0.04, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lltq / close)`: S=0.03, F=0.01, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lltq, 5))`: S=0.05, F=0.01, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_lltq / close)` | TOP3000 | 0.90 | 0.70 | 9.2% | 100% | bull-only |
| `rank(fnd6_newqv1300_lltq)` | TOP3000 | 0.71 | 0.59 | 28.2% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_lltq, 5))` | TOP1000 | 0.64 | 0.25 | 19.2% | 80% | all-weather |
| `rank(fnd6_newqv1300_lltq / close)` | TOP1000 | 0.39 | 0.23 | 14.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_lltq, 5))` | TOP500 | 0.39 | 0.13 | 26.1% | 60% | mixed |
| `rank(fnd6_newqv1300_lltq / close)` | TOP500 | 0.24 | 0.12 | 27.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_lltq)` | TOP1000 | 0.23 | 0.12 | 36.4% | 60% | bull-only |
| `rank(fnd6_newqv1300_lltq)` | TOP500 | 0.06 | 0.02 | 52.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- debt: 0.983 (strongly positively correlated)
- debt_lt: 0.980 (strongly positively correlated)
- fnd6_cptnewqv1300_dlttq: 0.980 (strongly positively correlated)
- fnd6_cptmfmq_dlttq: 0.979 (strongly positively correlated)
- liabilities: 0.971 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.35 | 1.55 | +0.66 | -0.78 | yes |
| anl4_epsr_flag | analyst4 | -0.35 | 1.83 | +0.65 | -0.78 | yes |
| anl4_rd_exp_flag | analyst4 | -0.32 | 1.65 | +0.62 | -0.44 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.24 | 1.50 | +0.55 | -0.76 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.29 | 1.41 | +0.52 | -0.80 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
