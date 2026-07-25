---
field: actual_sales_value_quarterly
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.93
best_fitness: 0.72
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1004
ann_vol: 0.0819
hit_rate: 0.4972
rolling_sharpe_min: -0.986
rolling_sharpe_max: 2.492
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.26
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.67
---
# actual_sales_value_quarterly (analyst4)

*Sales - Value in financial services income statement (in millions)*

## Signal Profile
- `rank(actual_sales_value_quarterly)`: S=0.65, F=0.51, T=1.2%, INFERIOR (TOP3000)
- `rank(actual_sales_value_quarterly / close)`: S=0.93, F=0.72, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(actual_sales_value_quarterly, 5))`: S=0.01, F=0.00, T=35.1%, INFERIOR (TOP3000)
- `-rank(actual_sales_value_quarterly)`: S=-0.28, F=-0.15, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(actual_sales_value_quarterly, 5))`: S=0.26, F=0.05, T=36.6%, INFERIOR (TOP3000)
- `-ts_zscore(actual_sales_value_quarterly, 63)`: S=0.29, F=0.08, T=17.9%, INFERIOR (TOP3000)
- `ts_mean(actual_sales_value_quarterly, 10)`: S=-0.08, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(actual_sales_value_quarterly, 22))`: S=-0.15, F=-0.03, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * actual_sales_value_quarterly)`: S=-0.28, F=-0.15, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * actual_sales_value_quarterly / close)`: S=-0.51, F=-0.33, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.93, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.05 (negative), ret=-0.2%
  - 2020: S=-0.12 (negative), ret=-1.1%
  - 2021: S=1.35 (moderate), ret=+14.5%
  - 2022: S=2.00 (strong), ret=+17.6%
  - 2023: S=1.35 (moderate), ret=+6.4%

## Risk & Drawdown
- Max drawdown: 10.04% over 237 days (recovered)
- Annualized: return +7.6%, volatility 8.2% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew +0.34, excess kurtosis +2.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 2.49, latest 1.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.30%; worst month: -3.87%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.51
- Sideways: S=0.25
- Bear: S=-1.62

## Negated Direction
Best negated: `rank(-1 * ts_delta(actual_sales_value_quarterly, 5))` S=0.26, F=0.05, INFERIOR
Direction gap: -0.67 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * actual_sales_value_quarterly)`: S=-0.28, F=-0.15, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * actual_sales_value_quarterly / close)`: S=-0.51, F=-0.33, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(actual_sales_value_quarterly, 5))`: S=0.26, F=0.05, T=36.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(actual_sales_value_quarterly / close)` | TOP3000 | 0.93 | 0.72 | 10.0% | 60% | bull-only |
| `rank(actual_sales_value_quarterly)` | TOP3000 | 0.65 | 0.51 | 32.6% | 80% | bull-only |
| `rank(actual_sales_value_quarterly / close)` | TOP1000 | 0.51 | 0.33 | 16.2% | 60% | bull-only |
| `rank(actual_sales_value_quarterly)` | TOP1000 | 0.28 | 0.15 | 37.5% | 60% | bull-only |
| `rank(actual_sales_value_quarterly / close)` | TOP500 | 0.25 | 0.12 | 25.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- actual_sales_value_annual: 0.989 (strongly positively correlated)
- fnd6_cptnewqv1300_saleq: 0.985 (strongly positively correlated)
- sales: 0.985 (strongly positively correlated)
- fnd6_cptmfmq_saleq: 0.985 (strongly positively correlated)
- fnd6_newqv1300_revtq: 0.983 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.35 | 1.57 | +0.65 | -0.58 | yes |
| fnd6_txtubadjust | fundamental6 | -0.22 | 1.42 | +0.49 | -0.96 | yes |
| anl4_rd_exp_flag | analyst4 | -0.28 | 1.61 | +0.59 | -0.57 | no |
| anl4_epsr_flag | analyst4 | -0.30 | 1.79 | +0.61 | -0.31 | no |
| sharesout | pv1 | -0.11 | 1.46 | +0.42 | -0.67 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
