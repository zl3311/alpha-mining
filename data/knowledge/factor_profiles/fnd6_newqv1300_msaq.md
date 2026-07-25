---
field: fnd6_newqv1300_msaq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.26
best_fitness: 1.1
best_universe: TOP500
grade: AVERAGE
submittability: needs_upgrade
n_sims: 31
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.0994
ann_vol: 0.0756
hit_rate: 0.5279
rolling_sharpe_min: -0.998
rolling_sharpe_max: 2.747
top_merge_partner: rank(scl12_buzz * (-1 * returns))
negated_best_sharpe: 0.26
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 9
direction_gap: -1.0
---
# fnd6_newqv1300_msaq (fundamental6)

*Accumulated Other Comprehensive Income - Marketable Security Adjustments*

## Signal Profile
- `rank(fnd6_newqv1300_msaq)`: S=1.25, F=1.08, T=9.0%, AVERAGE (TOP500)
- `rank(fnd6_newqv1300_msaq / close)`: S=1.26, F=1.10, T=9.0%, AVERAGE (TOP500)
- `rank(ts_delta(fnd6_newqv1300_msaq, 5))`: S=1.12, F=0.66, T=45.2%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_msaq)`: S=-0.81, F=-0.50, T=7.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_msaq, 5))`: S=0.26, F=0.08, T=60.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_msaq, 63)`: S=0.43, F=0.17, T=23.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_msaq, 10)`: S=0.24, F=0.09, T=5.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_msaq, 22))`: S=-0.86, F=-0.49, T=23.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_msaq)`: S=-1.25, F=-1.08, T=9.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_msaq / close)`: S=-1.26, F=-1.10, T=9.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/20P
- LOW_FITNESS: 29F/2P
- LOW_SHARPE: 29F/2P
- LOW_SUB_UNIVERSE_SHARPE: 10F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.26, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.52 (moderate), ret=+2.2%
  - 2020: S=2.01 (strong), ret=+12.7%
  - 2021: S=1.51 (strong), ret=+17.2%
  - 2022: S=0.93 (moderate), ret=+7.2%
  - 2023: S=1.42 (moderate), ret=+7.5%

## Risk & Drawdown
- Max drawdown: 9.94% over 492 days (recovered)
- Annualized: return +9.6%, volatility 7.6% (fraction of booksize)
- Hit rate: 52.8% positive days
- Tail shape: skew -0.22, excess kurtosis +3.96

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.00, max 2.75, latest 1.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +4.47%; worst month: -3.60%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.84
- Sideways: S=1.39
- Bear: S=0.54

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_msaq, 5))` S=0.26, F=0.08, INFERIOR
Direction gap: -1.00 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_msaq)`: S=-1.25, F=-1.08, T=9.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_msaq / close)`: S=-1.26, F=-1.10, T=9.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_msaq, 5))`: S=0.26, F=0.08, T=60.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_msaq / close)` | TOP500 | 1.26 | 1.10 | 9.9% | 100% | all-weather |
| `rank(fnd6_newqv1300_msaq)` | TOP500 | 1.26 | 1.08 | 9.5% | 100% | all-weather |
| `rank(fnd6_newqv1300_msaq / close)` | TOP200 | 0.97 | 0.80 | 13.5% | 100% | all-weather |
| `rank(fnd6_newqv1300_msaq)` | TOP200 | 0.93 | 0.76 | 16.4% | 100% | all-weather |
| `rank(ts_delta(fnd6_newqv1300_msaq, 5))` | TOP3000 | 1.12 | 0.66 | 15.4% | 100% | all-weather |
| `rank(fnd6_newqv1300_msaq / close)` | TOP1000 | 0.83 | 0.52 | 9.6% | 100% | bull-only |
| `rank(fnd6_newqv1300_msaq)` | TOP1000 | 0.81 | 0.50 | 10.5% | 100% | bull-only |
| `rank(fnd6_newqv1300_msaq / close)` | TOP3000 | 0.36 | 0.13 | 12.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_msaq)` | TOP3000 | 0.28 | 0.09 | 12.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_free_cashflow_per_share_guidance: 0.568 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.568 (moderately positively correlated)
- min_total_assets_guidance: 0.568 (moderately positively correlated)
- max_free_cashflow_per_share_guidance: 0.568 (moderately positively correlated)
- shareholders_equity_max_guidance: 0.568 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.19 | 2.29 | +0.66 | +0.66 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.22 | 2.67 | +0.65 | +0.81 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.20 | 2.50 | +0.63 | +0.81 | yes |
| news_open_vol | news12 | -0.28 | 1.83 | +0.56 | -0.48 | yes |
| news_close_vol | news12 | -0.12 | 1.85 | +0.58 | +0.02 | yes |

## Actionability
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, trade_when
