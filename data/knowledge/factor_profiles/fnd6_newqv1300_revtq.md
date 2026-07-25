---
field: fnd6_newqv1300_revtq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.03
best_fitness: 0.87
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0894
ann_vol: 0.0865
hit_rate: 0.4988
rolling_sharpe_min: -1.129
rolling_sharpe_max: 2.755
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.92
negated_best_template: rank_neg_delta
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: -0.11
---
# fnd6_newqv1300_revtq (fundamental6)

*Revenue - Total*

## Signal Profile
- `rank(fnd6_newqv1300_revtq)`: S=0.71, F=0.60, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_revtq / close)`: S=1.03, F=0.87, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_revtq, 5))`: S=0.11, F=0.02, T=36.6%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_revtq)`: S=-0.36, F=-0.23, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_revtq, 5))`: S=0.92, F=0.34, T=36.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_revtq, 63)`: S=-0.17, F=-0.04, T=19.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_revtq, 10)`: S=0.18, F=0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_revtq, 22))`: S=0.04, F=0.00, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_revtq)`: S=-0.71, F=-0.60, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_revtq / close)`: S=-1.03, F=-0.87, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.02, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.13 (negative), ret=-0.7%
  - 2020: S=-0.17 (negative), ret=-1.5%
  - 2021: S=1.72 (strong), ret=+20.8%
  - 2022: S=1.93 (strong), ret=+17.4%
  - 2023: S=1.64 (strong), ret=+7.4%

## Risk & Drawdown
- Max drawdown: 8.94% over 238 days (recovered)
- Annualized: return +8.8%, volatility 8.6% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.32, excess kurtosis +2.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.13, max 2.75, latest 1.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.22%; worst month: -3.80%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.62
- Sideways: S=0.27
- Bear: S=-1.55

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_revtq, 5))` S=0.92, F=0.34, INFERIOR
Direction gap: -0.11 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_revtq)`: S=-0.71, F=-0.60, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_revtq / close)`: S=-1.03, F=-0.87, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_revtq, 5))`: S=0.92, F=0.34, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_revtq / close)` | TOP3000 | 1.02 | 0.87 | 8.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_revtq)` | TOP3000 | 0.71 | 0.60 | 34.8% | 80% | bull-only |
| `rank(fnd6_newqv1300_revtq / close)` | TOP1000 | 0.64 | 0.48 | 14.6% | 80% | bull-only |
| `rank(fnd6_newqv1300_revtq / close)` | TOP500 | 0.47 | 0.32 | 25.5% | 80% | bull-only |
| `rank(fnd6_newqv1300_revtq)` | TOP1000 | 0.36 | 0.23 | 38.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_revtq)` | TOP500 | 0.19 | 0.10 | 49.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_revtq / close)` | TOP200 | 0.13 | 0.05 | 38.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_revtq, 5))` | TOP500 | 0.13 | 0.02 | 12.7% | 40% | mixed |

## Correlation Notes
Top correlates:
- revenue: 1.000 (strongly positively correlated)
- fnd6_cptnewqv1300_saleq: 0.998 (strongly positively correlated)
- sales: 0.998 (strongly positively correlated)
- fnd6_cptmfmq_saleq: 0.998 (strongly positively correlated)
- fnd6_mfma2_revt: 0.987 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.33 | 1.76 | +0.73 | -0.51 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.88 | +0.70 | -0.36 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.67 | +0.64 | -0.65 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.23 | 1.59 | +0.57 | -0.64 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.30 | 1.52 | +0.50 | -0.73 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
