---
field: primary_sector_focused_company_count
dataset: pv13
best_template: rank_level
best_sharpe: 1.02
best_fitness: 0.68
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0817
ann_vol: 0.0542
hit_rate: 0.5223
rolling_sharpe_min: -0.766
rolling_sharpe_max: 2.453
top_merge_partner: fnd6_cshtr
redundancy_cluster: 37
negated_best_sharpe: 0.35
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.67
---
# primary_sector_focused_company_count (pv13)

*Number of companies primarily focused in a given sector.*

## Signal Profile
- `rank(primary_sector_focused_company_count)`: S=1.02, F=0.68, T=1.6%, INFERIOR (TOP1000)
- `rank(ts_delta(primary_sector_focused_company_count, 5))`: S=0.78, F=0.55, T=34.7%, INFERIOR (TOP500)
- `-rank(primary_sector_focused_company_count)`: S=-1.02, F=-0.68, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(primary_sector_focused_company_count, 5))`: S=0.35, F=0.12, T=33.3%, INFERIOR (TOP3000)
- `ts_zscore(primary_sector_focused_company_count, 22)`: S=0.15, F=0.09, T=14.8%, INFERIOR (TOP3000)
- `ts_mean(primary_sector_focused_company_count, 10)`: S=0.39, F=0.28, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(primary_sector_focused_company_count, 22))`: S=-0.11, F=-0.04, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * primary_sector_focused_company_count)`: S=-0.29, F=-0.09, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * primary_sector_focused_company_count / close)`: S=-0.36, F=-0.12, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/12P
- LOW_FITNESS: 24F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.01, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.79 (moderate), ret=+3.8%
  - 2020: S=1.79 (strong), ret=+9.9%
  - 2021: S=1.85 (strong), ret=+9.9%
  - 2022: S=0.72 (moderate), ret=+4.1%
  - 2023: S=-0.15 (negative), ret=-0.8%

## Risk & Drawdown
- Max drawdown: 8.17% over 503 days (recovered)
- Annualized: return +5.5%, volatility 5.4% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.31, excess kurtosis +0.73

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.77, max 2.45, latest -0.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +3.34%; worst month: -2.24%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.84
- Sideways: S=-0.22
- Bear: S=0.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(primary_sector_focused_company_count, 5))` S=0.35, F=0.12, INFERIOR
Direction gap: -0.67 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * primary_sector_focused_company_count)`: S=-0.29, F=-0.09, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * primary_sector_focused_company_count / close)`: S=-0.36, F=-0.12, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(primary_sector_focused_company_count, 5))`: S=0.35, F=0.12, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(primary_sector_focused_company_count)` | TOP1000 | 1.01 | 0.68 | 8.2% | 80% | mixed |
| `rank(ts_delta(primary_sector_focused_company_count, 5))` | TOP500 | 0.79 | 0.55 | 40.2% | 60% | mixed |
| `rank(ts_delta(primary_sector_focused_company_count, 5))` | TOP200 | 0.37 | 0.23 | 57.1% | 60% | mixed |
| `rank(primary_sector_focused_company_count)` | TOP3000 | 0.30 | 0.09 | 8.2% | 80% | bull-only |

## Correlation Notes
Top correlates:
- single_sector_pureplay_company_count: 0.844 (strongly positively correlated)
- anl4_qf_az_div_median: 0.254 (weakly positively correlated)
- anl4_qfd1_az_div_median: 0.254 (weakly positively correlated)
- anl4_qf_az_div_mean: 0.252 (weakly positively correlated)
- dividend_estimate_average: 0.252 (weakly positively correlated)

Redundancy cluster #37: 2 similar fields, mean |rho| 0.844 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_cshtr | fundamental6 | -0.12 | 1.52 | +0.51 | +0.83 | yes |
| news_open_vol | news12 | -0.16 | 1.47 | +0.45 | -0.44 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.08 | 1.42 | +0.40 | -0.73 | yes |
| rp_css_mna | news18 | -0.01 | 1.52 | +0.40 | -0.72 | yes |
| fn_assets_fair_val_l2_q | fundamental2 | -0.09 | 1.60 | +0.39 | -0.83 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
