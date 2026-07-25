---
field: fnd6_fato
dataset: fundamental6
best_template: rank_level
best_sharpe: 1.19
best_fitness: 0.67
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 10
max_drawdown: 0.0594
ann_vol: 0.0337
hit_rate: 0.5409
rolling_sharpe_min: -0.636
rolling_sharpe_max: 3.468
top_merge_partner: rank(scl12_sentiment * (-1 * returns))
negated_best_sharpe: 0.5
negated_best_template: rank_neg_delta
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.69
---
# fnd6_fato (fundamental6)

*Plant, Property and Equipment at Cost - Other*

## Signal Profile
- `rank(fnd6_fato)`: S=1.19, F=0.67, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_fato / close)`: S=1.13, F=0.66, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_fato, 5))`: S=0.43, F=0.25, T=23.6%, INFERIOR (TOP500)
- `-rank(fnd6_fato)`: S=-0.64, F=-0.32, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fato, 5))`: S=0.50, F=0.28, T=37.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_fato, 63)`: S=0.29, F=0.24, T=14.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_fato, 10)`: S=-0.05, F=-0.01, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_fato, 22))`: S=0.64, F=0.50, T=21.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fato)`: S=-1.19, F=-0.67, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fato / close)`: S=-1.13, F=-0.66, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.18, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.08 (weak), ret=+0.2%
  - 2020: S=2.21 (strong), ret=+6.8%
  - 2021: S=2.38 (strong), ret=+9.3%
  - 2022: S=-0.32 (negative), ret=-1.1%
  - 2023: S=1.36 (moderate), ret=+4.3%

## Risk & Drawdown
- Max drawdown: 5.94% over 662 days (recovered)
- Annualized: return +4.0%, volatility 3.4% (fraction of booksize)
- Hit rate: 54.1% positive days
- Tail shape: skew +0.02, excess kurtosis +0.68

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.64, max 3.47, latest 1.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +3.76%; worst month: -2.34%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.51
- Sideways: S=1.11
- Bear: S=1.97

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_fato, 5))` S=0.50, F=0.28, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_fato)`: S=-1.19, F=-0.67, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fato / close)`: S=-1.13, F=-0.66, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fato, 5))`: S=0.50, F=0.28, T=37.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_fato)` | TOP3000 | 1.18 | 0.67 | 5.9% | 80% | all-weather |
| `rank(fnd6_fato / close)` | TOP3000 | 1.13 | 0.66 | 6.3% | 60% | mixed |
| `rank(fnd6_fato)` | TOP1000 | 0.65 | 0.32 | 11.6% | 80% | mixed |
| `rank(fnd6_fato / close)` | TOP1000 | 0.62 | 0.32 | 10.2% | 60% | all-weather |
| `rank(fnd6_fato / close)` | TOP200 | 0.47 | 0.29 | 19.6% | 80% | mixed |
| `rank(ts_delta(fnd6_fato, 5))` | TOP500 | 0.42 | 0.25 | 23.6% | 60% | weak |
| `rank(fnd6_fato)` | TOP200 | 0.39 | 0.22 | 19.4% | 80% | mixed |
| `rank(fnd6_fato / close)` | TOP500 | 0.34 | 0.15 | 11.5% | 60% | bull-only |
| `rank(fnd6_fato)` | TOP500 | 0.20 | 0.07 | 14.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_fato, 5))` | TOP200 | 0.14 | 0.06 | 31.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_fcf_flag: 0.476 (moderately positively correlated)
- anl4_fcfps_flag: 0.468 (moderately positively correlated)
- anl4_capex_flag: 0.457 (moderately positively correlated)
- anl4_totassets_flag: 0.453 (moderately positively correlated)
- anl4_cff_flag: 0.451 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.07 | 1.70 | +0.52 | +0.31 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.07 | 1.64 | +0.46 | +0.43 | yes |
| fn_liab_fair_val_l2_a | fundamental2 | +0.15 | 1.56 | +0.38 | -0.82 | yes |
| implied_volatility_mean_60 | option8 | -0.01 | 1.77 | +0.44 | +0.30 | yes |
| anl4_qfd1_az_dts_spe | analyst4 | +0.15 | 1.55 | +0.37 | -0.71 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
