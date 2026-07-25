---
field: fnd6_newqv1300_dlcq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.96
best_fitness: 0.67
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0909
ann_vol: 0.0644
hit_rate: 0.4988
rolling_sharpe_min: -0.914
rolling_sharpe_max: 2.488
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.98
negated_best_template: rank_neg_delta
negated_best_fitness: 0.56
n_negated_sims: 10
direction_gap: 0.02
---
# fnd6_newqv1300_dlcq (fundamental6)

*Debt in Current Liabilities*

## Signal Profile
- `rank(fnd6_newqv1300_dlcq)`: S=0.72, F=0.52, T=2.7%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_dlcq / close)`: S=0.96, F=0.67, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_dlcq, 5))`: S=-0.33, F=-0.08, T=38.7%, INFERIOR (TOP1000)
- `-rank(fnd6_newqv1300_dlcq)`: S=-0.38, F=-0.22, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_dlcq, 5))`: S=0.98, F=0.56, T=38.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_dlcq, 63)`: S=-0.16, F=-0.03, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_dlcq, 10)`: S=0.15, F=0.06, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_dlcq, 22))`: S=0.42, F=0.14, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_dlcq)`: S=-0.10, F=-0.03, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_dlcq / close)`: S=-0.24, F=-0.10, T=4.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.95, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.63 (strong), ret=+6.0%
  - 2020: S=-0.06 (negative), ret=-0.4%
  - 2021: S=1.62 (strong), ret=+14.0%
  - 2022: S=1.53 (strong), ret=+10.4%
  - 2023: S=0.02 (weak), ret=+0.1%

## Risk & Drawdown
- Max drawdown: 9.09% over 237 days (recovered)
- Annualized: return +6.2%, volatility 6.4% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.41, excess kurtosis +2.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.91, max 2.49, latest 0.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +7.60%; worst month: -3.06%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.89
- Sideways: S=0.79
- Bear: S=-1.25

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_dlcq, 5))` S=0.98, F=0.56, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_dlcq)`: S=-0.10, F=-0.03, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_dlcq / close)`: S=-0.24, F=-0.10, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_dlcq, 5))`: S=0.98, F=0.56, T=38.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_dlcq / close)` | TOP3000 | 0.95 | 0.67 | 9.1% | 80% | bull-only |
| `rank(fnd6_newqv1300_dlcq)` | TOP3000 | 0.71 | 0.52 | 22.6% | 80% | bull-only |
| `rank(fnd6_newqv1300_dlcq / close)` | TOP1000 | 0.58 | 0.38 | 14.1% | 60% | bull-only |
| `rank(fnd6_newqv1300_dlcq)` | TOP1000 | 0.37 | 0.22 | 28.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_dlcq / close)` | TOP500 | 0.24 | 0.10 | 19.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_dlcq)` | TOP500 | 0.10 | 0.03 | 38.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- debt_st: 1.000 (strongly positively correlated)
- fnd6_mfmq_dlcq: 1.000 (strongly positively correlated)
- fnd6_dd1q: 0.965 (strongly positively correlated)
- fnd6_newa1v1300_dlc: 0.957 (strongly positively correlated)
- fnd6_cptmfmq_lctq: 0.952 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.33 | 1.80 | +0.62 | -0.80 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.53 | +0.57 | -0.72 | yes |
| anl4_rd_exp_flag | analyst4 | -0.26 | 1.57 | +0.55 | -0.77 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.20 | 1.48 | +0.52 | -0.84 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.26 | 1.44 | +0.48 | -0.63 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
