---
field: single_sector_pureplay_company_count
dataset: pv13
best_template: ts_zscore
best_sharpe: 0.91
best_fitness: 1.45
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.0642
ann_vol: 0.0554
hit_rate: 0.5077
rolling_sharpe_min: -0.353
rolling_sharpe_max: 2.495
top_merge_partner: pcr_vol_60
redundancy_cluster: 37
negated_best_sharpe: 0.87
negated_best_template: rank_neg_delta
negated_best_fitness: 0.66
n_negated_sims: 10
direction_gap: -0.04
---
# single_sector_pureplay_company_count (pv13)

*Number of companies exclusively operating in a single sector.*

## Signal Profile
- `rank(single_sector_pureplay_company_count)`: S=0.87, F=0.54, T=1.6%, INFERIOR (TOP1000)
- `rank(ts_delta(single_sector_pureplay_company_count, 5))`: S=0.48, F=0.35, T=19.8%, INFERIOR (TOP200)
- `-rank(single_sector_pureplay_company_count)`: S=-0.87, F=-0.54, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(single_sector_pureplay_company_count, 5))`: S=0.87, F=0.66, T=30.0%, INFERIOR (TOP3000)
- `-ts_zscore(single_sector_pureplay_company_count, 63)`: S=0.91, F=1.45, T=6.3%, AVERAGE (TOP3000)
- `ts_mean(single_sector_pureplay_company_count, 10)`: S=0.31, F=0.22, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(single_sector_pureplay_company_count, 22))`: S=-0.14, F=-0.07, T=12.0%, INFERIOR (TOP3000)
- `rank(-1 * single_sector_pureplay_company_count)`: S=-0.17, F=-0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * single_sector_pureplay_company_count / close)`: S=-0.13, F=-0.03, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/11P
- LOW_FITNESS: 23F/1P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.86, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.20 (weak), ret=+1.0%
  - 2020: S=1.68 (strong), ret=+10.0%
  - 2021: S=1.41 (moderate), ret=+7.7%
  - 2022: S=1.08 (moderate), ret=+5.9%
  - 2023: S=-0.21 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 6.42% over 157 days (recovered)
- Annualized: return +4.8%, volatility 5.5% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.25, excess kurtosis +0.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.35, max 2.50, latest -0.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +3.84%; worst month: -2.86%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.90
- Sideways: S=-0.93
- Bear: S=1.61

## Negated Direction
Best negated: `rank(-1 * ts_delta(single_sector_pureplay_company_count, 5))` S=0.87, F=0.66, INFERIOR
Direction gap: -0.04 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * single_sector_pureplay_company_count)`: S=-0.17, F=-0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * single_sector_pureplay_company_count / close)`: S=-0.13, F=-0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(single_sector_pureplay_company_count, 5))`: S=0.87, F=0.66, T=30.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(single_sector_pureplay_company_count)` | TOP1000 | 0.86 | 0.54 | 6.4% | 80% | all-weather |
| `rank(ts_delta(single_sector_pureplay_company_count, 5))` | TOP200 | 0.47 | 0.35 | 23.3% | 60% | weak |
| `rank(ts_delta(single_sector_pureplay_company_count, 5))` | TOP500 | 0.49 | 0.31 | 39.0% | 80% | bull-only |
| `rank(single_sector_pureplay_company_count)` | TOP3000 | 0.18 | 0.04 | 10.8% | 80% | mixed |
| `rank(single_sector_pureplay_company_count)` | TOP500 | 0.08 | 0.02 | 16.4% | 40% | mixed |

## Correlation Notes
Top correlates:
- primary_sector_focused_company_count: 0.844 (strongly positively correlated)
- fnd6_newqv1300_tfvaq: -0.124 (weakly negatively correlated)
- fn_proceeds_from_issuance_of_debt_q: -0.107 (weakly negatively correlated)
- fnd2_a_sbcpnargmsptawervl: -0.103 (weakly negatively correlated)
- fn_derivative_fair_value_of_derivative_asset_q: -0.103 (weakly negatively correlated)

Redundancy cluster #37: 2 similar fields, mean |rho| 0.844 (representative: primary_sector_focused_company_count). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pcr_vol_60 | option9 | -0.01 | 1.24 | +0.36 | -0.70 | yes |
| anl4_qfv4_cfps_high | analyst4 | -0.05 | 1.22 | +0.36 | -0.70 | yes |
| news_open_vol | news12 | -0.05 | 1.30 | +0.37 | -0.49 | yes |
| cashflow_per_share_minimum | analyst4 | -0.04 | 1.24 | +0.37 | -0.43 | yes |
| fnd6_fopox | fundamental6 | -0.04 | 1.38 | +0.32 | -0.88 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
