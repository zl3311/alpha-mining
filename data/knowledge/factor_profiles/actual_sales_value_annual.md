---
field: actual_sales_value_annual
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.85
best_fitness: 0.64
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1107
ann_vol: 0.0851
hit_rate: 0.5036
rolling_sharpe_min: -1.09
rolling_sharpe_max: 2.387
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.38
---
# actual_sales_value_annual (analyst4)

*Sales - Actual Value*

## Signal Profile
- `rank(actual_sales_value_annual)`: S=0.58, F=0.43, T=0.9%, INFERIOR (TOP3000)
- `rank(actual_sales_value_annual / close)`: S=0.85, F=0.64, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(actual_sales_value_annual, 5))`: S=0.05, F=0.00, T=36.6%, INFERIOR (TOP500)
- `-rank(actual_sales_value_annual)`: S=-0.26, F=-0.14, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(actual_sales_value_annual, 5))`: S=0.47, F=0.16, T=34.4%, INFERIOR (TOP3000)
- `ts_zscore(actual_sales_value_annual, 22)`: S=0.52, F=0.18, T=42.5%, INFERIOR (TOP3000)
- `ts_mean(actual_sales_value_annual, 10)`: S=-0.04, F=-0.01, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(actual_sales_value_annual, 22))`: S=0.20, F=0.05, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * actual_sales_value_annual)`: S=0.13, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * actual_sales_value_annual / close)`: S=0.09, F=0.03, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.84, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.31 (negative), ret=-1.6%
  - 2020: S=-0.00 (negative), ret=-0.0%
  - 2021: S=1.21 (moderate), ret=+13.1%
  - 2022: S=1.94 (strong), ret=+17.8%
  - 2023: S=1.17 (moderate), ret=+5.8%

## Risk & Drawdown
- Max drawdown: 11.07% over 237 days (recovered)
- Annualized: return +7.2%, volatility 8.5% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.43, excess kurtosis +2.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 2.39, latest 1.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +10.04%; worst month: -4.02%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.39
- Sideways: S=0.11
- Bear: S=-1.67

## Negated Direction
Best negated: `rank(-1 * ts_delta(actual_sales_value_annual, 5))` S=0.47, F=0.16, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * actual_sales_value_annual)`: S=0.13, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * actual_sales_value_annual / close)`: S=0.09, F=0.03, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(actual_sales_value_annual, 5))`: S=0.47, F=0.16, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(actual_sales_value_annual / close)` | TOP3000 | 0.84 | 0.64 | 11.1% | 60% | bull-only |
| `rank(actual_sales_value_annual)` | TOP3000 | 0.57 | 0.43 | 33.4% | 80% | bull-only |
| `rank(actual_sales_value_annual / close)` | TOP1000 | 0.48 | 0.31 | 16.8% | 60% | bull-only |
| `rank(actual_sales_value_annual)` | TOP1000 | 0.26 | 0.14 | 39.6% | 60% | bull-only |
| `rank(actual_sales_value_annual / close)` | TOP500 | 0.22 | 0.10 | 32.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- actual_sales_value_quarterly: 0.989 (strongly positively correlated)
- fnd6_mfma2_revt: 0.984 (strongly positively correlated)
- fnd6_newa2v1300_sale: 0.984 (strongly positively correlated)
- fnd6_newa2v1300_revt: 0.984 (strongly positively correlated)
- fnd6_cptmfmq_saleq: 0.978 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.36 | 1.53 | +0.64 | -0.51 | yes |
| fnd6_txtubadjust | fundamental6 | -0.23 | 1.36 | +0.52 | -0.94 | yes |
| news_pct_10min | news12 | -0.14 | 1.30 | +0.43 | -0.48 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.31 | 1.39 | +0.55 | -0.73 | no |
| systematic_risk_last_60_days | model51 | -0.13 | 1.29 | +0.42 | -0.42 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
