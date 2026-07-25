---
field: fnd6_newqv1300_acomincq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.94
best_fitness: 0.5
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.1985
ann_vol: 0.1239
hit_rate: 0.5255
rolling_sharpe_min: -0.91
rolling_sharpe_max: 2.443
top_merge_partner: news_low_exc_stddev
negated_best_sharpe: 0.59
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.35
---
# fnd6_newqv1300_acomincq (fundamental6)

*Accumulated Other Comprehensive Income (Loss)*

## Signal Profile
- `rank(fnd6_newqv1300_acomincq)`: S=0.17, F=0.07, T=5.1%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_acomincq / close)`: S=0.19, F=0.08, T=5.2%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_acomincq, 5))`: S=0.94, F=0.50, T=41.4%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_acomincq)`: S=0.20, F=0.07, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_acomincq, 5))`: S=-0.60, F=-0.19, T=39.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_acomincq, 63)`: S=-0.09, F=-0.01, T=20.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_acomincq, 10)`: S=-0.17, F=-0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_acomincq, 22))`: S=0.25, F=0.07, T=18.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_acomincq)`: S=0.47, F=0.22, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_acomincq / close)`: S=0.59, F=0.29, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.96, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.03 (negative), ret=-0.3%
  - 2020: S=1.38 (moderate), ret=+20.7%
  - 2021: S=0.79 (moderate), ret=+9.1%
  - 2022: S=1.63 (strong), ret=+21.6%
  - 2023: S=0.64 (moderate), ret=+6.8%

## Risk & Drawdown
- Max drawdown: 19.85% over 455 days (recovered)
- Annualized: return +11.8%, volatility 12.4% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +1.49, excess kurtosis +21.64

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.91, max 2.44, latest 0.51

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +11.31%; worst month: -5.95%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.08
- Sideways: S=0.89
- Bear: S=0.91

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_acomincq / close)` S=0.59, F=0.29, INFERIOR
Direction gap: -0.35 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_acomincq)`: S=0.47, F=0.22, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_acomincq / close)`: S=0.59, F=0.29, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_acomincq, 5))`: S=-0.60, F=-0.19, T=39.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_acomincq, 5))` | TOP500 | 0.96 | 0.50 | 19.9% | 80% | all-weather |
| `rank(ts_delta(fnd6_newqv1300_acomincq, 5))` | TOP3000 | 0.62 | 0.19 | 8.9% | 80% | all-weather |
| `rank(ts_delta(fnd6_newqv1300_acomincq, 5))` | TOP1000 | 0.42 | 0.13 | 13.6% | 80% | mixed |
| `rank(fnd6_newqv1300_acomincq / close)` | TOP200 | 0.21 | 0.08 | 32.7% | 60% | bear-only |
| `rank(fnd6_newqv1300_acomincq)` | TOP200 | 0.18 | 0.07 | 34.7% | 60% | bear-only |
| `rank(ts_delta(fnd6_newqv1300_acomincq, 5))` | TOP200 | 0.23 | 0.07 | 20.4% | 80% | mixed |
| `rank(fnd6_newqv1300_acomincq)` | TOP500 | 0.09 | 0.02 | 29.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_rectaq: 0.438 (moderately positively correlated)
- fnd6_newqv1300_cicurrq: 0.356 (weakly positively correlated)
- fnd6_newqv1300_spiq: -0.168 (weakly negatively correlated)
- fnd6_ivst: -0.164 (weakly negatively correlated)
- fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q: 0.141 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_low_exc_stddev | news12 | -0.09 | 1.34 | +0.39 | -0.48 | yes |
| fn_incremental_shares_attributable_to_share_based_payment_q | fundamental2 | -0.03 | 1.49 | +0.37 | -0.56 | yes |
| max_gross_income_guidance | analyst4 | +0.01 | 1.29 | +0.34 | -0.80 | yes |
| parkinson_volatility_120 | option8 | +0.01 | 1.28 | +0.33 | -0.82 | yes |
| min_gross_income_guidance | analyst4 | +0.01 | 1.28 | +0.33 | -0.80 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
