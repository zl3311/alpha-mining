---
field: fnd6_exre
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.99
best_fitness: 0.51
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.0523
ann_vol: 0.0342
hit_rate: 0.532
rolling_sharpe_min: -1.247
rolling_sharpe_max: 3.649
top_merge_partner: rank(scl12_sentiment * (-1 * returns))
negated_best_sharpe: 0.39
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.6
---
# fnd6_exre (fundamental6)

*Exchange Rate Effect*

## Signal Profile
- `rank(fnd6_exre)`: S=0.87, F=0.44, T=1.6%, INFERIOR (TOP3000)
- `rank(fnd6_exre / close)`: S=0.99, F=0.51, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_exre, 5))`: S=0.73, F=0.39, T=34.3%, INFERIOR (TOP1000)
- `-rank(fnd6_exre)`: S=-0.52, F=-0.23, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_exre, 5))`: S=0.39, F=0.20, T=30.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_exre, 22)`: S=-0.35, F=-0.20, T=25.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_exre, 10)`: S=-0.59, F=-0.35, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_exre, 22))`: S=0.48, F=0.25, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_exre)`: S=-0.49, F=-0.28, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_exre / close)`: S=-0.53, F=-0.31, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.02, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.05 (negative), ret=-0.1%
  - 2020: S=0.72 (moderate), ret=+1.9%
  - 2021: S=3.39 (strong), ret=+14.8%
  - 2022: S=-0.21 (negative), ret=-0.8%
  - 2023: S=0.45 (weak), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 5.23% over 500 days (not yet recovered, ongoing at window end)
- Annualized: return +3.5%, volatility 3.4% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.13, excess kurtosis +2.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.25, max 3.65, latest 0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +3.59%; worst month: -3.06%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.33
- Sideways: S=1.01
- Bear: S=2.04

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_exre, 5))` S=0.39, F=0.20, INFERIOR
Direction gap: -0.60 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_exre)`: S=-0.49, F=-0.28, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_exre / close)`: S=-0.53, F=-0.31, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_exre, 5))`: S=0.39, F=0.20, T=30.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_exre / close)` | TOP3000 | 1.02 | 0.51 | 5.2% | 60% | mixed |
| `rank(fnd6_exre)` | TOP3000 | 0.90 | 0.44 | 6.7% | 60% | mixed |
| `rank(ts_delta(fnd6_exre, 5))` | TOP1000 | 0.74 | 0.39 | 20.6% | 80% | mixed |
| `rank(fnd6_exre / close)` | TOP200 | 0.53 | 0.31 | 11.5% | 60% | mixed |
| `rank(fnd6_exre / close)` | TOP1000 | 0.66 | 0.31 | 7.4% | 60% | bear-only |
| `rank(fnd6_exre)` | TOP200 | 0.49 | 0.28 | 11.0% | 60% | mixed |
| `rank(fnd6_exre)` | TOP1000 | 0.53 | 0.23 | 7.8% | 60% | bear-only |
| `rank(fnd6_exre / close)` | TOP500 | 0.46 | 0.20 | 11.1% | 60% | bear-only |
| `rank(fnd6_exre)` | TOP500 | 0.41 | 0.18 | 11.0% | 60% | bear-only |
| `rank(ts_delta(fnd6_exre, 5))` | TOP3000 | 0.33 | 0.12 | 23.8% | 80% | weak |

## Correlation Notes
Top correlates:
- fnd6_cicurr: 0.589 (moderately positively correlated)
- fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a: 0.393 (weakly positively correlated)
- sales_min_guidance_value: 0.347 (weakly positively correlated)
- reporting_currency_code_9: 0.343 (weakly positively correlated)
- anl4_capex_flag: 0.340 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.10 | 1.61 | +0.47 | -0.28 | yes |
| rp_nip_credit_ratings | news18 | -0.04 | 1.42 | +0.40 | -0.60 | yes |
| fn_repayments_of_lt_debt_q | fundamental2 | -0.05 | 1.52 | +0.44 | +0.94 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.21 | 1.38 | +0.36 | -0.82 | yes |
| fn_derivative_fair_value_of_derivative_asset_a | fundamental2 | -0.01 | 1.44 | +0.43 | +0.66 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
