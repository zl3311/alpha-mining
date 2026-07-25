---
field: fn_def_tax_assets_net_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.21
best_fitness: 0.93
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0756
ann_vol: 0.0616
hit_rate: 0.5036
rolling_sharpe_min: -1.137
rolling_sharpe_max: 2.952
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.71
negated_best_template: rank_neg_delta
negated_best_fitness: 0.47
n_negated_sims: 10
direction_gap: -0.5
---
# fn_def_tax_assets_net_a (fundamental2)

*Deferred Tax Assets Net Of Valuation Allowance*

## Signal Profile
- `rank(fn_def_tax_assets_net_a)`: S=0.89, F=0.68, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_def_tax_assets_net_a / close)`: S=1.21, F=0.93, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_def_tax_assets_net_a, 5))`: S=-0.40, F=-0.16, T=34.2%, INFERIOR (TOP1000)
- `-rank(fn_def_tax_assets_net_a)`: S=-0.57, F=-0.39, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_tax_assets_net_a, 5))`: S=0.71, F=0.47, T=30.8%, INFERIOR (TOP3000)
- `-ts_zscore(fn_def_tax_assets_net_a, 63)`: S=0.64, F=0.45, T=17.7%, INFERIOR (TOP3000)
- `ts_mean(fn_def_tax_assets_net_a, 10)`: S=0.25, F=0.11, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_def_tax_assets_net_a, 22))`: S=-0.40, F=-0.19, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_assets_net_a)`: S=0.03, F=0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_assets_net_a / close)`: S=-0.11, F=-0.03, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.20, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.43 (weak), ret=+1.7%
  - 2020: S=1.25 (moderate), ret=+9.4%
  - 2021: S=2.01 (strong), ret=+14.9%
  - 2022: S=1.30 (moderate), ret=+7.4%
  - 2023: S=0.59 (moderate), ret=+2.7%

## Risk & Drawdown
- Max drawdown: 7.56% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +7.4%, volatility 6.2% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.57, excess kurtosis +2.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.14, max 2.95, latest 0.66

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.35%; worst month: -2.96%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.78
- Sideways: S=0.38
- Bear: S=0.15

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_def_tax_assets_net_a, 5))` S=0.71, F=0.47, INFERIOR
Direction gap: -0.50 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_def_tax_assets_net_a)`: S=0.03, F=0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_assets_net_a / close)`: S=-0.11, F=-0.03, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_tax_assets_net_a, 5))`: S=0.71, F=0.47, T=30.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_def_tax_assets_net_a / close)` | TOP3000 | 1.20 | 0.93 | 7.6% | 100% | mixed |
| `rank(fn_def_tax_assets_net_a)` | TOP3000 | 0.88 | 0.68 | 15.8% | 80% | bull-only |
| `rank(fn_def_tax_assets_net_a / close)` | TOP1000 | 0.80 | 0.60 | 8.6% | 100% | bull-only |
| `rank(fn_def_tax_assets_net_a)` | TOP1000 | 0.56 | 0.39 | 22.2% | 80% | bull-only |
| `rank(fn_def_tax_assets_net_a / close)` | TOP500 | 0.44 | 0.25 | 19.6% | 80% | bull-only |
| `rank(fn_def_tax_assets_net_a)` | TOP500 | 0.27 | 0.13 | 35.0% | 80% | bull-only |
| `rank(fn_def_tax_assets_net_a / close)` | TOP200 | 0.12 | 0.03 | 27.9% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_lt: 0.912 (strongly positively correlated)
- fnd6_cptnewqv1300_ltq: 0.909 (strongly positively correlated)
- liabilities: 0.909 (strongly positively correlated)
- fnd6_xopr: 0.909 (strongly positively correlated)
- fnd6_newa1v1300_dpc: 0.908 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.37 | 1.99 | +0.80 | -0.68 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.17 | 1.75 | +0.56 | +0.61 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.12 | 2.13 | +0.51 | -0.24 | yes |
| est_rd_expense | analyst4 | -0.11 | 1.73 | +0.53 | +0.61 | yes |
| rp_ess_revenue | news18 | -0.34 | 1.66 | +0.46 | -0.51 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
