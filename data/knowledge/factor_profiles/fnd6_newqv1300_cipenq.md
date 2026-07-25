---
field: fnd6_newqv1300_cipenq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.92
best_fitness: 0.48
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.402
ann_vol: 0.1861
hit_rate: 0.5304
rolling_sharpe_min: -1.298
rolling_sharpe_max: 3.729
top_merge_partner: reporting_currency_code_9
negated_best_sharpe: 0.04
negated_best_template: neg_rank
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.88
---
# fnd6_newqv1300_cipenq (fundamental6)

*Comp Inc - Minimum Pension Adj*

## Signal Profile
- `rank(fnd6_newqv1300_cipenq)`: S=0.60, F=0.28, T=6.9%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_cipenq / close)`: S=0.66, F=0.32, T=6.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_cipenq, 5))`: S=0.92, F=0.48, T=62.5%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_cipenq)`: S=0.04, F=0.01, T=8.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cipenq, 5))`: S=-0.63, F=-0.27, T=62.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_cipenq, 63)`: S=0.51, F=0.17, T=20.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_cipenq, 10)`: S=-0.57, F=-0.33, T=5.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_cipenq, 22))`: S=-0.64, F=-0.27, T=22.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cipenq)`: S=0.04, F=0.01, T=10.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cipenq / close)`: S=0.01, F=0.00, T=10.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.92, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.53 (negative), ret=-6.5%
  - 2020: S=1.31 (moderate), ret=+21.7%
  - 2021: S=0.24 (weak), ret=+5.9%
  - 2022: S=1.43 (moderate), ret=+32.1%
  - 2023: S=2.46 (strong), ret=+30.7%

## Risk & Drawdown
- Max drawdown: 40.20% over 365 days (recovered)
- Annualized: return +17.1%, volatility 18.6% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +0.39, excess kurtosis +10.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.30, max 3.73, latest 2.47

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +17.26%; worst month: -16.26%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.15
- Sideways: S=0.36
- Bear: S=1.18

## Negated Direction
Best negated: `-rank(fnd6_newqv1300_cipenq)` S=0.04, F=0.01, INFERIOR
Direction gap: -0.88 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_cipenq)`: S=0.04, F=0.01, T=10.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cipenq / close)`: S=0.01, F=0.00, T=10.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cipenq, 5))`: S=-0.63, F=-0.27, T=62.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_cipenq, 5))` | TOP200 | 0.92 | 0.48 | 40.2% | 80% | all-weather |
| `rank(fnd6_newqv1300_cipenq / close)` | TOP3000 | 0.66 | 0.32 | 8.2% | 80% | bull-only |
| `rank(fnd6_newqv1300_cipenq)` | TOP3000 | 0.60 | 0.28 | 9.2% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_cipenq, 5))` | TOP3000 | 0.58 | 0.19 | 29.1% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_cipenq, 5))` | TOP1000 | 0.36 | 0.12 | 26.2% | 40% | mixed |
| `rank(ts_delta(fnd6_newqv1300_cipenq, 5))` | TOP500 | 0.10 | 0.02 | 52.2% | 60% | mixed |
| `rank(fnd6_newqv1300_cipenq / close)` | TOP500 | 0.08 | 0.02 | 9.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- reporting_currency_code_9: -0.183 (weakly negatively correlated)
- anl4_tot_gw_ft: -0.151 (weakly negatively correlated)
- sales_max_guidance_value: -0.149 (weakly negatively correlated)
- volume: 0.148 (weakly positively correlated)
- anl4_totassets_flag: -0.147 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| reporting_currency_code_9 | analyst4 | -0.18 | 1.35 | +0.43 | -0.60 | yes |
| pv13_revere_key_sector_total | pv13 | -0.02 | 1.27 | +0.35 | -0.74 | yes |
| fnd2_ebitfr | fundamental2 | +0.02 | 1.26 | +0.34 | -0.57 | yes |
| fnd2_unrgtxbnfinregfprtxps | fundamental2 | -0.00 | 1.30 | +0.38 | -0.12 | yes |
| anl4_qfd1_azeps | analyst4 | -0.09 | 1.27 | +0.35 | -0.31 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
