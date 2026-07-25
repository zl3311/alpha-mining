---
field: fnd6_newa2v1300_mib
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.95
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.041
ann_vol: 0.0357
hit_rate: 0.515
rolling_sharpe_min: -0.791
rolling_sharpe_max: 3.198
top_merge_partner: fn_def_tax_assets_liab_net_a
negated_best_sharpe: 0.67
negated_best_template: rank_neg_delta
negated_best_fitness: 0.46
n_negated_sims: 10
direction_gap: -0.28
---
# fnd6_newa2v1300_mib (fundamental6)

*Minority Interest (Balance Sheet)*

## Signal Profile
- `rank(fnd6_newa2v1300_mib)`: S=0.92, F=0.47, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_mib / close)`: S=0.95, F=0.49, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_mib, 5))`: S=-0.17, F=-0.06, T=28.5%, INFERIOR (TOP3000)
- `-rank(fnd6_newa2v1300_mib)`: S=-0.18, F=-0.04, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_mib, 5))`: S=0.67, F=0.46, T=26.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_mib, 22)`: S=-0.01, F=0.00, T=8.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_mib, 10)`: S=0.48, F=0.24, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_mib, 22))`: S=-0.38, F=-0.26, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_mib)`: S=-0.18, F=-0.04, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_mib / close)`: S=-0.22, F=-0.06, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.94, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.48 (weak), ret=+1.3%
  - 2020: S=1.31 (moderate), ret=+4.7%
  - 2021: S=1.11 (moderate), ret=+4.3%
  - 2022: S=1.79 (strong), ret=+6.9%
  - 2023: S=-0.26 (negative), ret=-0.8%

## Risk & Drawdown
- Max drawdown: 4.10% over 359 days (not yet recovered, ongoing at window end)
- Annualized: return +3.4%, volatility 3.6% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.15, excess kurtosis +1.25

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.79, max 3.20, latest -0.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +2.57%; worst month: -2.41%
Positive months: 68%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.20
- Sideways: S=0.88
- Bear: S=-0.24

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_mib, 5))` S=0.67, F=0.46, INFERIOR
Direction gap: -0.28 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_mib)`: S=-0.18, F=-0.04, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_mib / close)`: S=-0.22, F=-0.06, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_mib, 5))`: S=0.67, F=0.46, T=26.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_mib / close)` | TOP3000 | 0.94 | 0.49 | 4.1% | 80% | mixed |
| `rank(fnd6_newa2v1300_mib)` | TOP3000 | 0.92 | 0.47 | 4.1% | 80% | mixed |
| `rank(fnd6_newa2v1300_mib)` | TOP200 | 0.24 | 0.10 | 20.3% | 60% | bull-only |
| `rank(fnd6_newa2v1300_mib / close)` | TOP200 | 0.24 | 0.10 | 20.6% | 60% | bull-only |
| `rank(fnd6_newa2v1300_mib / close)` | TOP1000 | 0.20 | 0.06 | 7.2% | 40% | bull-only |
| `rank(fnd6_newa2v1300_mib)` | TOP1000 | 0.17 | 0.04 | 7.5% | 40% | bull-only |
| `rank(fnd6_newa2v1300_mib / close)` | TOP500 | 0.13 | 0.03 | 10.0% | 20% | bull-only |
| `rank(fnd6_newa2v1300_mib)` | TOP500 | 0.11 | 0.02 | 10.3% | 20% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_ivaeq: 0.450 (moderately positively correlated)
- fnd6_newa1v1300_caps: 0.443 (moderately positively correlated)
- actual_sales_value_quarterly: 0.440 (moderately positively correlated)
- actual_sales_value_annual: 0.439 (moderately positively correlated)
- fn_prepaid_expense_a: 0.439 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.10 | 1.38 | +0.44 | -0.53 | yes |
| operating_profit_before_depr_amort_max_guidance_qtr | analyst4 | -0.17 | 1.43 | +0.48 | +0.07 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.18 | 1.64 | +0.48 | +0.07 | yes |
| operating_profit_before_depr_amort_min_guidance_qtr | analyst4 | -0.16 | 1.45 | +0.48 | +0.07 | yes |
| anl4_capex_flag | analyst4 | -0.04 | 1.46 | +0.37 | -0.86 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
