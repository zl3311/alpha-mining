---
field: fnd6_mrcta
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.94
best_fitness: 0.73
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 11
max_drawdown: 0.2714
ann_vol: 0.2197
hit_rate: 0.4842
rolling_sharpe_min: -1.142
rolling_sharpe_max: 2.411
top_merge_partner: fn_assets_fair_val_l3_a
negated_best_sharpe: 0.01
negated_best_template: neg_rank_level
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.93
---
# fnd6_mrcta (fundamental6)

*Thereafter Portion of Leases*

## Signal Profile
- `rank(fnd6_mrcta)`: S=0.88, F=0.63, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_mrcta / close)`: S=0.95, F=0.66, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mrcta, 5))`: S=0.94, F=0.73, T=34.2%, INFERIOR (TOP500)
- `-rank(fnd6_mrcta)`: S=-0.40, F=-0.21, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrcta, 5))`: S=-0.90, F=-0.69, T=34.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mrcta, 63)`: S=-0.10, F=-0.03, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mrcta, 10)`: S=0.41, F=0.22, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mrcta, 22))`: S=0.61, F=0.34, T=20.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrcta)`: S=0.01, F=0.00, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrcta / close)`: S=-0.13, F=-0.04, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.94, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.14 (strong), ret=+52.1%
  - 2020: S=0.81 (moderate), ret=+16.2%
  - 2021: S=0.64 (moderate), ret=+12.5%
  - 2022: S=1.34 (moderate), ret=+36.7%
  - 2023: S=-1.11 (negative), ret=-15.8%

## Risk & Drawdown
- Max drawdown: 27.14% over 110 days (recovered)
- Annualized: return +20.8%, volatility 22.0% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew +3.07, excess kurtosis +41.77

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.14, max 2.41, latest -1.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +20.53%; worst month: -12.90%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.36
- Sideways: S=1.04
- Bear: S=0.33

## Negated Direction
Best negated: `rank(-1 * fnd6_mrcta)` S=0.01, F=0.00, INFERIOR
Direction gap: -0.93 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mrcta)`: S=0.01, F=0.00, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrcta / close)`: S=-0.13, F=-0.04, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrcta, 5))`: S=-0.90, F=-0.69, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_mrcta, 5))` | TOP500 | 0.94 | 0.73 | 27.1% | 80% | mixed |
| `rank(fnd6_mrcta / close)` | TOP3000 | 0.94 | 0.66 | 6.8% | 100% | mixed |
| `rank(fnd6_mrcta)` | TOP3000 | 0.87 | 0.63 | 15.1% | 80% | bull-only |
| `rank(ts_delta(fnd6_mrcta, 5))` | TOP1000 | 0.91 | 0.59 | 14.1% | 80% | all-weather |
| `rank(ts_delta(fnd6_mrcta, 5))` | TOP3000 | 0.62 | 0.30 | 27.7% | 60% | all-weather |
| `rank(fnd6_mrcta / close)` | TOP1000 | 0.46 | 0.25 | 9.2% | 80% | bull-only |
| `rank(ts_delta(fnd6_mrcta, 5))` | TOP200 | 0.39 | 0.23 | 35.7% | 60% | weak |
| `rank(fnd6_mrcta)` | TOP1000 | 0.39 | 0.21 | 19.8% | 60% | bull-only |
| `rank(fnd6_mrcta / close)` | TOP200 | 0.35 | 0.19 | 18.1% | 60% | bull-only |
| `rank(fnd6_mrcta)` | TOP200 | 0.21 | 0.10 | 33.0% | 60% | bull-only |
| `rank(fnd6_mrcta / close)` | TOP500 | 0.13 | 0.04 | 15.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mrct: 0.320 (weakly positively correlated)
- fnd6_txpd: 0.284 (weakly positively correlated)
- fnd6_tfvl: 0.247 (weakly positively correlated)
- fnd6_fiao: 0.243 (weakly positively correlated)
- fnd6_mrc1: 0.240 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_assets_fair_val_l3_a | fundamental2 | -0.11 | 1.48 | +0.45 | -0.89 | yes |
| pv13_revere_company_total | pv13 | +0.00 | 1.41 | +0.35 | -0.73 | yes |
| fn_income_taxes_paid_q | fundamental2 | +0.04 | 1.27 | +0.33 | -0.82 | yes |
| fn_comp_options_exercisable_number_a | fundamental2 | -0.02 | 1.30 | +0.36 | -0.40 | yes |
| fnd2_unrgtxbnfinregfprtxps | fundamental2 | +0.01 | 1.30 | +0.36 | -0.20 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
