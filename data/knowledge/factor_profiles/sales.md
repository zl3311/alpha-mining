---
field: sales
dataset: fundamental6
cluster: fundamental6_income_revenue
coverage: 0.5
community_alphas: 36130
best_template: rank_value_norm
best_sharpe: 1.05
best_fitness: 0.88
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0873
ann_vol: 0.0846
hit_rate: 0.502
rolling_sharpe_min: -1.11
rolling_sharpe_max: 2.735
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.82
negated_best_template: rank_neg_delta
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.23
---
# sales (fundamental6)

*Sales/Turnover (Net)*

## Signal Profile
- `rank(sales)`: S=0.74, F=0.63, T=1.1%, INFERIOR (TOP3000)
- `rank(sales / close)`: S=1.05, F=0.88, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(sales, 5))`: S=-0.01, F=0.00, T=36.9%, INFERIOR (TOP500)
- `ts_decay_linear(rank(sales), 5)`: S=0.74, F=0.63, T=1.1%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(sales), ts_std_dev(returns,20)<0.01)`: S=0.72, F=0.60, T=2.0%, INFERIOR (TOP3000)
- `-rank(sales)`: S=-0.36, F=-0.23, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales, 5))`: S=0.82, F=0.28, T=37.0%, INFERIOR (TOP3000)
- `-ts_zscore(sales, 63)`: S=-0.03, F=0.00, T=19.5%, INFERIOR (TOP3000)
- `ts_mean(sales, 10)`: S=0.17, F=0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(sales, 22))`: S=-0.07, F=-0.01, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * sales)`: S=-0.74, F=-0.63, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * sales / close)`: S=-1.05, F=-0.88, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/26P
- LOW_FITNESS: 37F/0P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/21P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.04, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.07 (negative), ret=-0.4%
  - 2020: S=-0.11 (negative), ret=-1.0%
  - 2021: S=1.69 (strong), ret=+19.8%
  - 2022: S=1.95 (strong), ret=+17.0%
  - 2023: S=1.72 (strong), ret=+7.8%

## Risk & Drawdown
- Max drawdown: 8.73% over 217 days (recovered)
- Annualized: return +8.8%, volatility 8.5% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.32, excess kurtosis +2.64

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.11, max 2.73, latest 1.73

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.07%; worst month: -3.68%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.61
- Sideways: S=0.36
- Bear: S=-1.52

## Negated Direction
Best negated: `rank(-1 * ts_delta(sales, 5))` S=0.82, F=0.28, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sales)`: S=-0.74, F=-0.63, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * sales / close)`: S=-1.05, F=-0.88, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales, 5))`: S=0.82, F=0.28, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales / close)` | TOP3000 | 1.04 | 0.88 | 8.7% | 60% | bull-only |
| `ts_decay_linear(rank(sales), 5)` | TOP3000 | 0.73 | 0.63 | 32.9% | 80% | bull-only |
| `rank(sales)` | TOP3000 | 0.73 | 0.63 | 32.9% | 80% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(sales), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.71 | 0.60 | 33.4% | 80% | bull-only |
| `rank(sales / close)` | TOP1000 | 0.63 | 0.46 | 14.7% | 60% | bull-only |
| `rank(sales / close)` | TOP500 | 0.44 | 0.28 | 25.3% | 60% | bull-only |
| `rank(sales)` | TOP1000 | 0.35 | 0.23 | 38.1% | 60% | bull-only |
| `rank(sales)` | TOP500 | 0.18 | 0.09 | 49.0% | 60% | bull-only |
| `rank(sales / close)` | TOP200 | 0.12 | 0.04 | 38.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_saleq: 1.000 (strongly positively correlated)
- fnd6_cptmfmq_saleq: 1.000 (strongly positively correlated)
- revenue: 0.998 (strongly positively correlated)
- fnd6_newqv1300_revtq: 0.998 (strongly positively correlated)
- fnd6_mfma2_revt: 0.989 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.33 | 1.76 | +0.72 | -0.51 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.89 | +0.71 | -0.33 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.68 | +0.63 | -0.63 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.23 | 1.60 | +0.56 | -0.62 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.30 | 1.53 | +0.49 | -0.71 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
