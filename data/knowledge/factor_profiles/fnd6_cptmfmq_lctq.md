---
field: fnd6_cptmfmq_lctq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.95
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0912
ann_vol: 0.0807
hit_rate: 0.4826
rolling_sharpe_min: -0.898
rolling_sharpe_max: 2.61
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.27
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.68
---
# fnd6_cptmfmq_lctq (fundamental6)

*Current Liabilities - Total*

## Signal Profile
- `rank(fnd6_cptmfmq_lctq)`: S=0.74, F=0.62, T=1.6%, INFERIOR (TOP3000)
- `rank(fnd6_cptmfmq_lctq / close)`: S=0.95, F=0.74, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptmfmq_lctq, 5))`: S=0.17, F=0.04, T=37.6%, INFERIOR (TOP200)
- `-rank(fnd6_cptmfmq_lctq)`: S=-0.35, F=-0.21, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_lctq, 5))`: S=0.27, F=0.07, T=37.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptmfmq_lctq, 22)`: S=0.24, F=0.06, T=38.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptmfmq_lctq, 10)`: S=0.08, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptmfmq_lctq, 22))`: S=0.17, F=0.04, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_lctq)`: S=-0.35, F=-0.21, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_lctq / close)`: S=-0.53, F=-0.35, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.94, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.01 (negative), ret=-0.0%
  - 2020: S=0.34 (weak), ret=+3.0%
  - 2021: S=1.74 (strong), ret=+18.5%
  - 2022: S=1.50 (moderate), ret=+11.8%
  - 2023: S=0.76 (moderate), ret=+4.0%

## Risk & Drawdown
- Max drawdown: 9.12% over 491 days (recovered)
- Annualized: return +7.6%, volatility 8.1% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.47, excess kurtosis +2.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.90, max 2.61, latest 0.85

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.34%; worst month: -4.15%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.09
- Sideways: S=0.14
- Bear: S=-0.98

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptmfmq_lctq, 5))` S=0.27, F=0.07, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cptmfmq_lctq)`: S=-0.35, F=-0.21, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_lctq / close)`: S=-0.53, F=-0.35, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_lctq, 5))`: S=0.27, F=0.07, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptmfmq_lctq / close)` | TOP3000 | 0.94 | 0.74 | 9.1% | 80% | bull-only |
| `rank(fnd6_cptmfmq_lctq)` | TOP3000 | 0.73 | 0.62 | 29.9% | 80% | bull-only |
| `rank(fnd6_cptmfmq_lctq / close)` | TOP1000 | 0.53 | 0.35 | 13.8% | 60% | bull-only |
| `rank(fnd6_cptmfmq_lctq)` | TOP1000 | 0.34 | 0.21 | 35.5% | 60% | bull-only |
| `rank(fnd6_cptmfmq_lctq / close)` | TOP500 | 0.29 | 0.15 | 22.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_cptmfmq_lctq, 5))` | TOP200 | 0.17 | 0.04 | 35.9% | 80% | mixed |
| `rank(fnd6_cptmfmq_lctq)` | TOP500 | 0.09 | 0.03 | 50.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- liabilities_curr: 1.000 (strongly positively correlated)
- fnd6_cptnewqv1300_lctq: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_lct: 0.989 (strongly positively correlated)
- fnd6_newqv1300_ltmibq: 0.975 (strongly positively correlated)
- liabilities: 0.975 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.33 | 1.83 | +0.65 | -0.64 | yes |
| rp_ess_revenue | news18 | -0.33 | 1.57 | +0.62 | -0.73 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.17 | 1.46 | +0.52 | -0.67 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.27 | 1.42 | +0.48 | -0.91 | yes |
| anl4_rd_exp_flag | analyst4 | -0.20 | 1.55 | +0.53 | -0.34 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
