---
field: fn_def_tax_assets_liab_net_a
dataset: fundamental2
cluster: fundamental2_balance_sheet_assets
coverage: 0.7058
community_alphas: 1141
best_template: rank_level
best_sharpe: 0.92
best_fitness: 0.46
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0561
ann_vol: 0.0346
hit_rate: 0.5126
rolling_sharpe_min: -1.684
rolling_sharpe_max: 2.872
top_merge_partner: rel_num_part
negated_best_sharpe: 0.24
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.68
---
# fn_def_tax_assets_liab_net_a (fundamental2)

*Amount, after allocation of valuation allowances and deferred tax liability, of deferred tax asset attributable to deductible differences and carryforwards, without jurisdictional netting.*

## Signal Profile
- `rank(fn_def_tax_assets_liab_net_a)`: S=0.92, F=0.46, T=1.1%, INFERIOR (TOP1000)
- `rank(fn_def_tax_assets_liab_net_a / close)`: S=0.88, F=0.42, T=1.3%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_def_tax_assets_liab_net_a, 5))`: S=0.39, F=0.15, T=34.2%, INFERIOR (TOP1000)
- `-rank(fn_def_tax_assets_liab_net_a)`: S=-0.92, F=-0.46, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_tax_assets_liab_net_a, 5))`: S=0.24, F=0.09, T=31.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_def_tax_assets_liab_net_a, 63)`: S=0.37, F=0.19, T=17.0%, INFERIOR (TOP3000)
- `ts_mean(fn_def_tax_assets_liab_net_a, 10)`: S=0.28, F=0.10, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_def_tax_assets_liab_net_a, 22))`: S=-0.20, F=-0.07, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_assets_liab_net_a)`: S=-0.36, F=-0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_assets_liab_net_a / close)`: S=-0.24, F=-0.08, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.91, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.15 (negative), ret=-0.4%
  - 2020: S=1.27 (moderate), ret=+4.5%
  - 2021: S=1.70 (strong), ret=+6.3%
  - 2022: S=-0.19 (negative), ret=-0.8%
  - 2023: S=2.36 (strong), ret=+5.9%

## Risk & Drawdown
- Max drawdown: 5.61% over 496 days (recovered)
- Annualized: return +3.2%, volatility 3.5% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.38, excess kurtosis +2.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.68, max 2.87, latest 2.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +2.49%; worst month: -1.25%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.43
- Sideways: S=0.23
- Bear: S=3.15

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_def_tax_assets_liab_net_a, 5))` S=0.24, F=0.09, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_def_tax_assets_liab_net_a)`: S=-0.36, F=-0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_def_tax_assets_liab_net_a / close)`: S=-0.24, F=-0.08, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_def_tax_assets_liab_net_a, 5))`: S=0.24, F=0.09, T=31.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_def_tax_assets_liab_net_a)` | TOP1000 | 0.91 | 0.46 | 5.6% | 60% | mixed |
| `rank(fn_def_tax_assets_liab_net_a)` | TOP500 | 0.88 | 0.45 | 3.8% | 100% | all-weather |
| `rank(fn_def_tax_assets_liab_net_a / close)` | TOP1000 | 0.87 | 0.42 | 4.4% | 100% | mixed |
| `rank(fn_def_tax_assets_liab_net_a / close)` | TOP500 | 0.53 | 0.22 | 5.5% | 80% | all-weather |
| `rank(ts_delta(fn_def_tax_assets_liab_net_a, 5))` | TOP1000 | 0.38 | 0.15 | 14.5% | 80% | mixed |
| `rank(fn_def_tax_assets_liab_net_a)` | TOP200 | 0.35 | 0.15 | 7.8% | 80% | mixed |
| `rank(fn_def_tax_assets_liab_net_a)` | TOP3000 | 0.40 | 0.12 | 4.9% | 80% | bear-only |
| `rank(fn_def_tax_assets_liab_net_a / close)` | TOP3000 | 0.33 | 0.09 | 5.9% | 60% | bear-only |
| `rank(fn_def_tax_assets_liab_net_a / close)` | TOP200 | 0.23 | 0.08 | 6.4% | 80% | mixed |

## Correlation Notes
Top correlates:
- cashflow_dividends: -0.540 (moderately negatively correlated)
- fnd6_newa1v1300_dv: -0.539 (moderately negatively correlated)
- anl4_afv4_div_median: -0.538 (moderately negatively correlated)
- anl4_afv4_div_mean: -0.538 (moderately negatively correlated)
- anl4_afv4_div_high: -0.530 (moderately negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rel_num_part | pv13 | -0.43 | 1.96 | +0.68 | -0.28 | yes |
| fnd6_newqv1300_tstknq | fundamental6 | -0.40 | 1.58 | +0.66 | -0.36 | yes |
| min_capital_expenditure_guidance | analyst4 | -0.37 | 1.57 | +0.65 | -0.28 | yes |
| fnd6_dxd5 | fundamental6 | -0.35 | 1.81 | +0.62 | -0.54 | yes |
| fnd6_dclo | fundamental6 | -0.29 | 1.56 | +0.61 | -0.59 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
