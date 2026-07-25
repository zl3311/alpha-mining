---
field: fnd2_unrgtxbnfinregfprtxps
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.92
best_fitness: 0.68
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 10
max_drawdown: 0.2398
ann_vol: 0.1614
hit_rate: 0.4947
rolling_sharpe_min: -1.568
rolling_sharpe_max: 3.152
top_merge_partner: fnd6_lcoxdr
negated_best_sharpe: 0.24
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.68
---
# fnd2_unrgtxbnfinregfprtxps (fundamental2)

*Amount of increase in unrecognized tax benefits resulting from tax positions taken in prior period tax returns.*

## Signal Profile
- `rank(fnd2_unrgtxbnfinregfprtxps)`: S=0.29, F=0.11, T=1.4%, INFERIOR (TOP1000)
- `rank(fnd2_unrgtxbnfinregfprtxps / close)`: S=0.59, F=0.27, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_unrgtxbnfinregfprtxps, 5))`: S=0.92, F=0.68, T=27.6%, INFERIOR (TOP200)
- `-rank(fnd2_unrgtxbnfinregfprtxps)`: S=-0.29, F=-0.11, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_unrgtxbnfinregfprtxps, 5))`: S=0.24, F=0.07, T=34.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_unrgtxbnfinregfprtxps, 63)`: S=0.73, F=0.63, T=15.3%, INFERIOR (TOP3000)
- `ts_mean(fnd2_unrgtxbnfinregfprtxps, 10)`: S=0.29, F=0.13, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_unrgtxbnfinregfprtxps, 22))`: S=-0.33, F=-0.14, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfinregfprtxps)`: S=-0.23, F=-0.07, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfinregfprtxps / close)`: S=-0.59, F=-0.27, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.92, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.03 (weak), ret=+0.5%
  - 2020: S=0.75 (moderate), ret=+13.2%
  - 2021: S=2.44 (strong), ret=+42.9%
  - 2022: S=0.67 (moderate), ret=+10.5%
  - 2023: S=0.55 (moderate), ret=+5.9%

## Risk & Drawdown
- Max drawdown: 23.98% over 532 days (recovered)
- Annualized: return +14.9%, volatility 16.1% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +1.66, excess kurtosis +15.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.57, max 3.15, latest 0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +17.00%; worst month: -9.06%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.86
- Sideways: S=-0.44
- Bear: S=1.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_unrgtxbnfinregfprtxps, 5))` S=0.24, F=0.07, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd2_unrgtxbnfinregfprtxps)`: S=-0.23, F=-0.07, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfinregfprtxps / close)`: S=-0.59, F=-0.27, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_unrgtxbnfinregfprtxps, 5))`: S=0.24, F=0.07, T=34.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_unrgtxbnfinregfprtxps, 5))` | TOP200 | 0.92 | 0.68 | 24.0% | 100% | all-weather |
| `rank(fnd2_unrgtxbnfinregfprtxps / close)` | TOP3000 | 0.58 | 0.27 | 6.5% | 60% | bull-only |
| `rank(fnd2_unrgtxbnfinregfprtxps / close)` | TOP1000 | 0.47 | 0.23 | 11.6% | 60% | bull-only |
| `rank(ts_delta(fnd2_unrgtxbnfinregfprtxps, 5))` | TOP500 | 0.49 | 0.22 | 40.2% | 60% | all-weather |
| `rank(fnd2_unrgtxbnfinregfprtxps)` | TOP1000 | 0.28 | 0.11 | 20.2% | 60% | bull-only |
| `rank(fnd2_unrgtxbnfinregfprtxps / close)` | TOP500 | 0.22 | 0.08 | 21.4% | 40% | bull-only |
| `rank(fnd2_unrgtxbnfinregfprtxps)` | TOP3000 | 0.22 | 0.07 | 17.0% | 80% | bull-only |
| `rank(fnd2_unrgtxbnfinregfprtxps / close)` | TOP200 | 0.20 | 0.07 | 28.2% | 60% | bull-only |
| `rank(fnd2_unrgtxbnfinregfprtxps)` | TOP200 | 0.14 | 0.04 | 29.5% | 60% | bull-only |
| `rank(fnd2_unrgtxbnfinregfprtxps)` | TOP500 | 0.12 | 0.03 | 27.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_flintasamt1expyfour: 0.382 (weakly positively correlated)
- fnd2_ebitfr: 0.320 (weakly positively correlated)
- fn_finite_lived_intangible_assets_net_a: 0.282 (weakly positively correlated)
- fn_avg_diluted_sharesout_adj_a: 0.251 (weakly positively correlated)
- fnd2_ebitdm: 0.197 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_lcoxdr | fundamental6 | -0.09 | 1.36 | +0.44 | -0.70 | yes |
| analyst_revision_rank_derivative | model16 | -0.07 | 1.36 | +0.42 | -0.61 | yes |
| relative_valuation_rank_derivative | model16 | -0.07 | 1.36 | +0.42 | -0.61 | yes |
| earnings_certainty_rank_derivative | model16 | -0.07 | 1.36 | +0.42 | -0.61 | yes |
| fnd6_invrm | fundamental6 | -0.04 | 1.35 | +0.40 | -0.58 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
