---
field: fnd6_mkvaltq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 1.04
best_fitness: 0.61
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.1398
ann_vol: 0.119
hit_rate: 0.404
rolling_sharpe_min: -0.726
rolling_sharpe_max: 3.152
top_merge_partner: sales_ps
negated_best_sharpe: 0.1
negated_best_template: neg_rank_level
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.94
---
# fnd6_mkvaltq (fundamental6)

*Market Value - Total*

## Signal Profile
- `rank(fnd6_mkvaltq)`: S=0.42, F=0.19, T=22.3%, INFERIOR (TOP3000)
- `rank(fnd6_mkvaltq / close)`: S=0.47, F=0.20, T=22.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mkvaltq, 5))`: S=1.04, F=0.61, T=36.1%, INFERIOR (TOP200)
- `-rank(fnd6_mkvaltq)`: S=0.06, F=0.01, T=20.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mkvaltq, 5))`: S=-1.04, F=-0.61, T=36.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mkvaltq, 63)`: S=0.22, F=0.05, T=31.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mkvaltq, 10)`: S=0.01, F=0.00, T=17.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mkvaltq, 22))`: S=0.08, F=0.01, T=27.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mkvaltq)`: S=0.10, F=0.03, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mkvaltq / close)`: S=-0.23, F=-0.08, T=16.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.03, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.45 (weak), ret=+4.1%
  - 2020: S=1.86 (strong), ret=+29.1%
  - 2021: S=0.18 (weak), ret=+2.2%
  - 2022: S=1.28 (moderate), ret=+13.6%
  - 2023: S=1.20 (moderate), ret=+11.3%

## Risk & Drawdown
- Max drawdown: 13.98% over 410 days (recovered)
- Annualized: return +12.3%, volatility 11.9% (fraction of booksize)
- Hit rate: 40.4% positive days
- Tail shape: skew +0.34, excess kurtosis +11.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.73, max 3.15, latest 1.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +14.22%; worst month: -5.87%
Positive months: 70%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.53
- Sideways: S=0.89
- Bear: S=0.84

## Negated Direction
Best negated: `rank(-1 * fnd6_mkvaltq)` S=0.10, F=0.03, INFERIOR
Direction gap: -0.94 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mkvaltq)`: S=0.10, F=0.03, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mkvaltq / close)`: S=-0.23, F=-0.08, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mkvaltq, 5))`: S=-1.04, F=-0.61, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_mkvaltq, 5))` | TOP200 | 1.03 | 0.61 | 14.0% | 100% | all-weather |
| `rank(fnd6_mkvaltq / close)` | TOP3000 | 0.47 | 0.20 | 18.9% | 60% | bull-only |
| `rank(fnd6_mkvaltq)` | TOP3000 | 0.42 | 0.19 | 21.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_mkvaltq, 5))` | TOP500 | 0.53 | 0.17 | 11.1% | 80% | mixed |
| `rank(ts_delta(fnd6_mkvaltq, 5))` | TOP1000 | 0.45 | 0.12 | 7.2% | 100% | bear-only |
| `rank(fnd6_mkvaltq / close)` | TOP500 | 0.25 | 0.09 | 13.2% | 60% | bull-only |
| `rank(fnd6_mkvaltq / close)` | TOP200 | 0.23 | 0.08 | 13.5% | 40% | bull-only |
| `rank(fnd6_mkvaltq / close)` | TOP1000 | 0.20 | 0.06 | 13.5% | 40% | bull-only |
| `rank(ts_delta(fnd6_mkvaltq, 5))` | TOP3000 | 0.19 | 0.03 | 9.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- anl4_af_cfps_value: -0.215 (weakly negatively correlated)
- anl4_qf_az_cfps_mean: -0.208 (weakly negatively correlated)
- cashflow_per_share_average: -0.208 (weakly negatively correlated)
- anl4_qf_az_cfps_median: -0.208 (weakly negatively correlated)
- anl4_qfd1_az_cfps_median: -0.208 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| sales_ps | fundamental_value | -0.19 | 1.65 | +0.58 | -0.17 | yes |
| anl4_fcf_high | analyst4 | -0.16 | 1.55 | +0.52 | -0.67 | yes |
| anl4_qfd1_az_hgih_spe | analyst4 | -0.18 | 1.57 | +0.54 | -0.43 | yes |
| anl4_qf_az_hgih_spe | analyst4 | -0.18 | 1.57 | +0.54 | -0.43 | yes |
| fn_accum_depr_depletion_and_amortization_ppne_q | fundamental2 | -0.18 | 1.56 | +0.53 | -0.37 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
