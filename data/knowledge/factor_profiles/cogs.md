---
field: cogs
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.22
best_fitness: 1.05
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0778
ann_vol: 0.0762
hit_rate: 0.4947
rolling_sharpe_min: -0.904
rolling_sharpe_max: 2.768
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.86
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: -0.36
---
# cogs (fundamental6)

*Cost of Goods Sold*

## Signal Profile
- `rank(cogs)`: S=0.87, F=0.76, T=1.3%, INFERIOR (TOP3000)
- `rank(cogs / close)`: S=1.22, F=1.05, T=1.7%, AVERAGE (TOP3000)
- `rank(ts_delta(cogs, 5))`: S=-0.04, F=0.00, T=38.0%, INFERIOR (TOP500)
- `ts_decay_linear(rank(cogs), 5)`: S=0.87, F=0.76, T=1.3%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(cogs), ts_std_dev(returns,20)<0.01)`: S=0.85, F=0.72, T=2.1%, INFERIOR (TOP3000)
- `-rank(cogs)`: S=-0.42, F=-0.27, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cogs, 5))`: S=0.86, F=0.30, T=37.6%, INFERIOR (TOP3000)
- `-ts_zscore(cogs, 63)`: S=-0.09, F=-0.01, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(cogs, 10)`: S=0.17, F=0.06, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(cogs, 22))`: S=-0.07, F=-0.01, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * cogs)`: S=-0.87, F=-0.76, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * cogs / close)`: S=-1.22, F=-1.05, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/31P
- LOW_FITNESS: 35F/2P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.21, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.17 (weak), ret=+0.9%
  - 2020: S=0.45 (weak), ret=+4.1%
  - 2021: S=1.93 (strong), ret=+19.1%
  - 2022: S=1.87 (strong), ret=+13.2%
  - 2023: S=1.67 (strong), ret=+7.9%

## Risk & Drawdown
- Max drawdown: 7.78% over 281 days (recovered)
- Annualized: return +9.2%, volatility 7.6% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.52, excess kurtosis +2.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.90, max 2.77, latest 1.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.76%; worst month: -3.47%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.52
- Sideways: S=0.40
- Bear: S=-0.78

## Negated Direction
Best negated: `rank(-1 * ts_delta(cogs, 5))` S=0.86, F=0.30, INFERIOR
Direction gap: -0.36 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cogs)`: S=-0.87, F=-0.76, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * cogs / close)`: S=-1.22, F=-1.05, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cogs, 5))`: S=0.86, F=0.30, T=37.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cogs / close)` | TOP3000 | 1.21 | 1.05 | 7.8% | 100% | bull-only |
| `rank(cogs)` | TOP3000 | 0.86 | 0.76 | 27.3% | 80% | bull-only |
| `ts_decay_linear(rank(cogs), 5)` | TOP3000 | 0.86 | 0.76 | 27.3% | 80% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(cogs), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.83 | 0.72 | 27.7% | 80% | bull-only |
| `rank(cogs / close)` | TOP1000 | 0.73 | 0.55 | 11.4% | 100% | bull-only |
| `rank(cogs / close)` | TOP500 | 0.56 | 0.37 | 16.6% | 60% | bull-only |
| `rank(cogs)` | TOP1000 | 0.41 | 0.27 | 30.5% | 60% | bull-only |
| `rank(cogs)` | TOP500 | 0.24 | 0.12 | 33.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_cogsq: 1.000 (strongly positively correlated)
- fnd6_mfmq_cogsq: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_cogs: 0.985 (strongly positively correlated)
- fnd6_cptnewqv1300_apq: 0.969 (strongly positively correlated)
- liabilities: 0.969 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.34 | 2.04 | +0.83 | -0.40 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.77 | +0.56 | -0.65 | yes |
| anl4_rd_exp_flag | analyst4 | -0.24 | 1.76 | +0.55 | -0.38 | yes |
| anl4_cfo_flag | analyst4 | -0.04 | 1.68 | +0.47 | -0.92 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.26 | 1.77 | +0.56 | +0.32 | yes |

## Actionability
Already in submitted book (alpha: ['ZYrr25Mx']).
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
