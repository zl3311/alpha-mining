---
field: fnd6_aqc
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 0.85
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.1912
ann_vol: 0.1351
hit_rate: 0.5158
rolling_sharpe_min: -1.244
rolling_sharpe_max: 3.583
top_merge_partner: anl4_tbvps_number
negated_best_sharpe: 0.64
negated_best_template: neg_rank_level
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: -0.21
---
# fnd6_aqc (fundamental6)

*Acquisitions*

## Signal Profile
- `rank(fnd6_aqc)`: S=0.11, F=0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_aqc / close)`: S=0.09, F=0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_aqc, 5))`: S=0.82, F=0.47, T=34.2%, INFERIOR (TOP1000)
- `-rank(fnd6_aqc)`: S=0.03, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_aqc, 5))`: S=0.32, F=0.15, T=27.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_aqc, 63)`: S=0.24, F=0.11, T=16.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_aqc, 10)`: S=-0.24, F=-0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_aqc, 22))`: S=0.85, F=0.59, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aqc)`: S=0.64, F=0.41, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aqc / close)`: S=0.59, F=0.36, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.81, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.44 (negative), ret=-5.4%
  - 2020: S=1.46 (moderate), ret=+21.1%
  - 2021: S=2.11 (strong), ret=+28.7%
  - 2022: S=0.69 (moderate), ret=+10.3%
  - 2023: S=-0.07 (negative), ret=-0.8%

## Risk & Drawdown
- Max drawdown: 19.12% over 547 days (not yet recovered, ongoing at window end)
- Annualized: return +11.0%, volatility 13.5% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.31, excess kurtosis +2.52

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.24, max 3.58, latest -0.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +15.78%; worst month: -7.19%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.69
- Sideways: S=0.52
- Bear: S=1.22

## Negated Direction
Best negated: `rank(-1 * fnd6_aqc)` S=0.64, F=0.41, INFERIOR
Direction gap: -0.21 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_aqc)`: S=0.64, F=0.41, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aqc / close)`: S=0.59, F=0.36, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_aqc, 5))`: S=0.32, F=0.15, T=27.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_aqc, 5))` | TOP1000 | 0.81 | 0.47 | 19.1% | 60% | all-weather |
| `rank(ts_delta(fnd6_aqc, 5))` | TOP500 | 0.40 | 0.19 | 33.7% | 60% | mixed |
| `rank(ts_delta(fnd6_aqc, 5))` | TOP3000 | 0.41 | 0.16 | 15.9% | 60% | bear-only |
| `rank(fnd6_aqc / close)` | TOP3000 | 0.09 | 0.02 | 13.6% | 60% | bull-only |
| `rank(fnd6_aqc)` | TOP3000 | 0.10 | 0.02 | 16.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_gdwl: 0.180 (weakly positively correlated)
- fnd6_mrc1: 0.123 (weakly positively correlated)
- fnd6_mrct: 0.121 (weakly positively correlated)
- anl4_bvps_value: 0.117 (weakly positively correlated)
- implied_volatility_call_360: -0.116 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_tbvps_number | analyst4 | -0.04 | 1.19 | +0.33 | -0.99 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.05 | 1.16 | +0.34 | -0.81 | yes |
| fnd2_a_unrgtxbnfitxpenlintacd | fundamental2 | -0.03 | 1.18 | +0.35 | -0.70 | yes |
| fnd2_propplteqflublgland | fundamental2 | +0.00 | 1.14 | +0.33 | -0.84 | yes |
| fn_comp_options_exercisable_number_a | fundamental2 | -0.01 | 1.20 | +0.32 | -0.85 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
