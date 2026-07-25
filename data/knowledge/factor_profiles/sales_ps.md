---
field: sales_ps
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.07
best_fitness: 1.04
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.178
ann_vol: 0.1119
hit_rate: 0.4915
rolling_sharpe_min: -1.96
rolling_sharpe_max: 3.082
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.77
negated_best_template: rank_neg_delta
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: -0.3
---
# sales_ps (fundamental6)

*Sales per Share (Quarterly)*

## Signal Profile
- `rank(sales_ps)`: S=0.72, F=0.61, T=1.3%, INFERIOR (TOP3000)
- `rank(sales_ps / close)`: S=1.07, F=1.04, T=2.0%, AVERAGE (TOP3000)
- `rank(ts_delta(sales_ps, 5))`: S=-0.13, F=-0.02, T=36.2%, INFERIOR (TOP1000)
- `ts_decay_linear(rank(sales_ps), 5)`: S=0.72, F=0.61, T=1.2%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(sales_ps), ts_std_dev(returns,20)<0.01)`: S=0.73, F=0.62, T=2.0%, INFERIOR (TOP3000)
- `-rank(sales_ps)`: S=-0.47, F=-0.31, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_ps, 5))`: S=0.77, F=0.36, T=36.5%, INFERIOR (TOP3000)
- `ts_zscore(sales_ps, 22)`: S=0.03, F=0.00, T=38.0%, INFERIOR (TOP3000)
- `ts_mean(sales_ps, 10)`: S=0.04, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_ps, 22))`: S=0.20, F=0.05, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_ps)`: S=0.06, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * sales_ps / close)`: S=-0.27, F=-0.15, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/31P
- LOW_FITNESS: 35F/2P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.06, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.53 (negative), ret=-4.0%
  - 2020: S=0.09 (weak), ret=+1.4%
  - 2021: S=2.27 (strong), ret=+29.6%
  - 2022: S=2.23 (strong), ret=+22.6%
  - 2023: S=1.25 (moderate), ret=+8.7%

## Risk & Drawdown
- Max drawdown: 17.80% over 734 days (recovered)
- Annualized: return +11.9%, volatility 11.2% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.45, excess kurtosis +2.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.96, max 3.08, latest 1.35

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +10.13%; worst month: -5.38%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=3.39
- Sideways: S=-0.56
- Bear: S=-0.04

## Negated Direction
Best negated: `rank(-1 * ts_delta(sales_ps, 5))` S=0.77, F=0.36, INFERIOR
Direction gap: -0.30 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sales_ps)`: S=0.06, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * sales_ps / close)`: S=-0.27, F=-0.15, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_ps, 5))`: S=0.77, F=0.36, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_ps / close)` | TOP3000 | 1.06 | 1.04 | 17.8% | 80% | mixed |
| `rank(sales_ps / close)` | TOP1000 | 0.78 | 0.70 | 14.7% | 60% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(sales_ps), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.72 | 0.62 | 37.0% | 60% | bull-only |
| `ts_decay_linear(rank(sales_ps), 5)` | TOP3000 | 0.71 | 0.61 | 35.7% | 80% | bull-only |
| `rank(sales_ps)` | TOP3000 | 0.71 | 0.61 | 35.7% | 80% | bull-only |
| `rank(sales_ps / close)` | TOP500 | 0.61 | 0.48 | 21.7% | 80% | bull-only |
| `rank(sales_ps)` | TOP1000 | 0.46 | 0.31 | 31.6% | 80% | bull-only |
| `rank(sales_ps)` | TOP500 | 0.31 | 0.17 | 32.4% | 80% | bull-only |
| `rank(sales_ps / close)` | TOP200 | 0.27 | 0.15 | 46.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_cogs: 0.892 (strongly positively correlated)
- fnd6_dlto: 0.889 (strongly positively correlated)
- anl4_qf_az_cfps_mean: 0.883 (strongly positively correlated)
- cashflow_per_share_average: 0.883 (strongly positively correlated)
- anl4_qf_az_cfps_median: 0.883 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 1.97 | +0.79 | -0.50 | yes |
| anl4_rd_exp_flag | analyst4 | -0.35 | 1.82 | +0.76 | -0.36 | yes |
| rp_ess_revenue | news18 | -0.38 | 1.75 | +0.69 | -0.67 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.34 | 1.63 | +0.57 | -0.89 | yes |
| max_gross_income_guidance | analyst4 | -0.25 | 1.60 | +0.53 | -0.81 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
