---
field: fnd6_msa
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.74
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 10
max_drawdown: 0.3176
ann_vol: 0.1767
hit_rate: 0.5223
rolling_sharpe_min: -1.946
rolling_sharpe_max: 3.239
top_merge_partner: fn_assets_fair_val_l3_a
negated_best_sharpe: 0.06
negated_best_template: neg_rank_level
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.68
---
# fnd6_msa (fundamental6)

*Marketable Securities Adjustment*

## Signal Profile
- `rank(fnd6_msa)`: S=0.64, F=0.37, T=3.0%, INFERIOR (TOP500)
- `rank(fnd6_msa / close)`: S=0.66, F=0.38, T=3.0%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_msa, 5))`: S=0.86, F=0.60, T=31.2%, INFERIOR (TOP1000)
- `-rank(fnd6_msa)`: S=-0.66, F=-0.34, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_msa, 5))`: S=-0.16, F=-0.06, T=22.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_msa, 22)`: S=0.74, F=0.71, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_msa, 10)`: S=-0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_msa, 22))`: S=0.58, F=0.37, T=20.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_msa)`: S=0.06, F=0.01, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_msa / close)`: S=-0.03, F=0.00, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.86, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=3.19 (strong), ret=+53.5%
  - 2020: S=0.75 (moderate), ret=+11.1%
  - 2021: S=0.55 (moderate), ret=+12.0%
  - 2022: S=0.92 (moderate), ret=+16.6%
  - 2023: S=-1.38 (negative), ret=-19.0%

## Risk & Drawdown
- Max drawdown: 31.76% over 344 days (not yet recovered, ongoing at window end)
- Annualized: return +15.1%, volatility 17.7% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew -0.16, excess kurtosis +7.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.95, max 3.24, latest -1.32

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +27.29%; worst month: -14.08%
Positive months: 61%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.34
- Sideways: S=1.78
- Bear: S=0.44

## Negated Direction
Best negated: `rank(-1 * fnd6_msa)` S=0.06, F=0.01, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_msa)`: S=0.06, F=0.01, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_msa / close)`: S=-0.03, F=0.00, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_msa, 5))`: S=-0.16, F=-0.06, T=22.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_msa, 5))` | TOP1000 | 0.86 | 0.60 | 31.8% | 80% | weak |
| `rank(ts_delta(fnd6_msa, 5))` | TOP3000 | 0.86 | 0.59 | 15.4% | 80% | all-weather |
| `rank(fnd6_msa / close)` | TOP500 | 0.67 | 0.38 | 7.2% | 60% | bull-only |
| `rank(fnd6_msa)` | TOP500 | 0.66 | 0.37 | 7.8% | 60% | bull-only |
| `rank(fnd6_msa / close)` | TOP1000 | 0.71 | 0.37 | 6.9% | 80% | bull-only |
| `rank(fnd6_msa)` | TOP1000 | 0.67 | 0.34 | 7.7% | 80% | bull-only |
| `rank(fnd6_msa / close)` | TOP3000 | 0.44 | 0.17 | 7.2% | 80% | bull-only |
| `rank(fnd6_msa)` | TOP3000 | 0.37 | 0.13 | 7.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_msa, 5))` | TOP200 | 0.23 | 0.10 | 40.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_msa, 5))` | TOP500 | 0.23 | 0.09 | 50.4% | 20% | weak |

## Correlation Notes
Top correlates:
- fnd6_cisecgl: 0.413 (moderately positively correlated)
- fn_comp_options_grants_fair_value_a: 0.129 (weakly positively correlated)
- fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a: 0.128 (weakly positively correlated)
- fnd6_lqpl1: 0.125 (weakly positively correlated)
- news_spy_last: -0.116 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_assets_fair_val_l3_a | fundamental2 | -0.03 | 1.35 | +0.33 | -0.82 | yes |
| fn_comp_options_exercisable_number_a | fundamental2 | -0.07 | 1.27 | +0.39 | -0.18 | yes |
| min_pretax_profit_guidance | analyst4 | -0.09 | 1.17 | +0.32 | -0.77 | yes |
| pretax_income_max_guidance_qtr | analyst4 | -0.09 | 1.17 | +0.32 | -0.77 | yes |
| fnd2_unrgtxbnfinregfprtxps | fundamental2 | -0.05 | 1.28 | +0.36 | -0.29 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
