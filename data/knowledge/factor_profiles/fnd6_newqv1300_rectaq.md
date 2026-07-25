---
field: fnd6_newqv1300_rectaq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.86
best_fitness: 0.45
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2513
ann_vol: 0.1879
hit_rate: 0.5166
rolling_sharpe_min: -1.0
rolling_sharpe_max: 2.233
top_merge_partner: fnd2_unrgtxbnfinregfprtxps
negated_best_sharpe: 0.45
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.41
---
# fnd6_newqv1300_rectaq (fundamental6)

*Accum Other Comp Inc - Cumulative Translation Adjustments*

## Signal Profile
- `rank(fnd6_newqv1300_rectaq)`: S=0.20, F=0.09, T=10.2%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_rectaq / close)`: S=0.19, F=0.08, T=10.1%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_rectaq, 5))`: S=0.86, F=0.45, T=58.1%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_rectaq)`: S=0.28, F=0.12, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rectaq, 5))`: S=-0.21, F=-0.04, T=47.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_rectaq, 63)`: S=-0.20, F=-0.05, T=23.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_rectaq, 10)`: S=-0.30, F=-0.15, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_rectaq, 22))`: S=0.56, F=0.25, T=22.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rectaq)`: S=0.40, F=0.18, T=5.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rectaq / close)`: S=0.45, F=0.20, T=5.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.86, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.88 (strong), ret=+23.4%
  - 2020: S=0.72 (moderate), ret=+13.4%
  - 2021: S=-0.58 (negative), ret=-12.1%
  - 2022: S=1.99 (strong), ret=+43.6%
  - 2023: S=0.67 (moderate), ret=+11.2%

## Risk & Drawdown
- Max drawdown: 25.13% over 392 days (recovered)
- Annualized: return +16.2%, volatility 18.8% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.72, excess kurtosis +10.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.00, max 2.23, latest 0.66

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +15.45%; worst month: -12.10%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.37
- Sideways: S=1.49
- Bear: S=0.69

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_rectaq / close)` S=0.45, F=0.20, INFERIOR
Direction gap: -0.41 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_rectaq)`: S=0.40, F=0.18, T=5.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rectaq / close)`: S=0.45, F=0.20, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rectaq, 5))`: S=-0.21, F=-0.04, T=47.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_rectaq, 5))` | TOP500 | 0.86 | 0.45 | 25.1% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_rectaq, 5))` | TOP200 | 0.59 | 0.29 | 34.6% | 80% | mixed |
| `rank(fnd6_newqv1300_rectaq)` | TOP200 | 0.21 | 0.09 | 43.1% | 60% | bear-only |
| `rank(fnd6_newqv1300_rectaq / close)` | TOP200 | 0.20 | 0.08 | 41.4% | 60% | bear-only |
| `rank(ts_delta(fnd6_newqv1300_rectaq, 5))` | TOP1000 | 0.27 | 0.08 | 48.2% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_rectaq, 5))` | TOP3000 | 0.21 | 0.04 | 13.6% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_cicurrq: 0.541 (moderately positively correlated)
- fnd6_newqv1300_acomincq: 0.438 (moderately positively correlated)
- fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q: 0.148 (weakly positively correlated)
- fnd6_newqv1300_ivltq: 0.125 (weakly positively correlated)
- implied_volatility_mean_60: 0.119 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd2_unrgtxbnfinregfprtxps | fundamental2 | -0.03 | 1.28 | +0.36 | -0.85 | yes |
| news_mins_5_chg | news12 | -0.07 | 1.24 | +0.38 | -0.40 | yes |
| fnd2_ebitfr | fundamental2 | -0.01 | 1.24 | +0.36 | -0.60 | yes |
| reporting_currency_code_9 | analyst4 | -0.12 | 1.25 | +0.39 | -0.25 | yes |
| fn_assets_fair_val_l3_a | fundamental2 | -0.07 | 1.39 | +0.37 | -0.19 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
