---
field: fnd6_mfmq_cogsq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.22
best_fitness: 1.05
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0785
ann_vol: 0.0763
hit_rate: 0.4931
rolling_sharpe_min: -0.915
rolling_sharpe_max: 2.764
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.84
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.38
---
# fnd6_mfmq_cogsq (fundamental6)

*Cost of Goods Sold*

## Signal Profile
- `rank(fnd6_mfmq_cogsq)`: S=0.86, F=0.75, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_mfmq_cogsq / close)`: S=1.22, F=1.05, T=1.7%, AVERAGE (TOP3000)
- `rank(ts_delta(fnd6_mfmq_cogsq, 5))`: S=-0.03, F=0.00, T=38.6%, INFERIOR (TOP200)
- `-rank(fnd6_mfmq_cogsq)`: S=-0.42, F=-0.27, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfmq_cogsq, 5))`: S=0.84, F=0.29, T=37.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mfmq_cogsq, 63)`: S=-0.05, F=-0.01, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfmq_cogsq, 10)`: S=0.16, F=0.06, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfmq_cogsq, 22))`: S=-0.07, F=-0.01, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfmq_cogsq)`: S=-0.86, F=-0.75, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfmq_cogsq / close)`: S=-1.22, F=-1.05, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.21, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.16 (weak), ret=+0.8%
  - 2020: S=0.46 (weak), ret=+4.1%
  - 2021: S=1.92 (strong), ret=+19.1%
  - 2022: S=1.88 (strong), ret=+13.2%
  - 2023: S=1.65 (strong), ret=+7.8%

## Risk & Drawdown
- Max drawdown: 7.85% over 281 days (recovered)
- Annualized: return +9.2%, volatility 7.6% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +0.52, excess kurtosis +2.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.92, max 2.76, latest 1.75

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.78%; worst month: -3.46%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.54
- Sideways: S=0.38
- Bear: S=-0.79

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mfmq_cogsq, 5))` S=0.84, F=0.29, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_mfmq_cogsq)`: S=-0.86, F=-0.75, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfmq_cogsq / close)`: S=-1.22, F=-1.05, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfmq_cogsq, 5))`: S=0.84, F=0.29, T=37.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfmq_cogsq / close)` | TOP3000 | 1.21 | 1.05 | 7.8% | 100% | bull-only |
| `rank(fnd6_mfmq_cogsq)` | TOP3000 | 0.85 | 0.75 | 27.1% | 80% | bull-only |
| `rank(fnd6_mfmq_cogsq / close)` | TOP1000 | 0.73 | 0.55 | 11.5% | 100% | bull-only |
| `rank(fnd6_mfmq_cogsq / close)` | TOP500 | 0.56 | 0.37 | 16.6% | 60% | bull-only |
| `rank(fnd6_mfmq_cogsq)` | TOP1000 | 0.41 | 0.27 | 30.6% | 60% | bull-only |
| `rank(fnd6_mfmq_cogsq)` | TOP500 | 0.24 | 0.12 | 33.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cogs: 1.000 (strongly positively correlated)
- fnd6_newqv1300_cogsq: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_cogs: 0.985 (strongly positively correlated)
- fnd6_cptnewqv1300_apq: 0.969 (strongly positively correlated)
- liabilities: 0.969 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.34 | 2.04 | +0.83 | -0.39 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.77 | +0.56 | -0.64 | yes |
| anl4_rd_exp_flag | analyst4 | -0.24 | 1.76 | +0.55 | -0.38 | yes |
| anl4_cfo_flag | analyst4 | -0.04 | 1.68 | +0.47 | -0.92 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.26 | 1.77 | +0.56 | +0.33 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
