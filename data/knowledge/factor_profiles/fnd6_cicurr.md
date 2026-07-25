---
field: fnd6_cicurr
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 0.79
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.064
ann_vol: 0.0425
hit_rate: 0.5117
rolling_sharpe_min: -1.225
rolling_sharpe_max: 2.558
top_merge_partner: snt_value_fast_d1
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.2
---
# fnd6_cicurr (fundamental6)

*Comp Inc - Currency Trans Adj*

## Signal Profile
- `rank(fnd6_cicurr)`: S=0.71, F=0.33, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_cicurr / close)`: S=0.87, F=0.47, T=2.7%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_cicurr, 5))`: S=0.30, F=0.15, T=26.9%, INFERIOR (TOP200)
- `-rank(fnd6_cicurr)`: S=-0.63, F=-0.31, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cicurr, 5))`: S=0.59, F=0.29, T=39.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cicurr, 63)`: S=-0.42, F=-0.27, T=19.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cicurr, 10)`: S=0.04, F=0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cicurr, 22))`: S=0.79, F=0.53, T=18.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cicurr)`: S=-0.71, F=-0.33, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cicurr / close)`: S=-0.83, F=-0.40, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.90, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.14 (weak), ret=+0.4%
  - 2020: S=-0.03 (negative), ret=-0.1%
  - 2021: S=1.39 (moderate), ret=+7.7%
  - 2022: S=1.33 (moderate), ret=+6.2%
  - 2023: S=1.13 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 6.40% over 404 days (recovered)
- Annualized: return +3.8%, volatility 4.2% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew -0.04, excess kurtosis +1.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.23, max 2.56, latest 1.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +3.61%; worst month: -2.36%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.37
- Sideways: S=2.42
- Bear: S=1.11

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cicurr, 5))` S=0.59, F=0.29, INFERIOR
Direction gap: -0.20 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_cicurr)`: S=-0.71, F=-0.33, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cicurr / close)`: S=-0.83, F=-0.40, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cicurr, 5))`: S=0.59, F=0.29, T=39.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cicurr / close)` | TOP1000 | 0.90 | 0.47 | 6.4% | 80% | mixed |
| `rank(fnd6_cicurr / close)` | TOP3000 | 0.86 | 0.40 | 5.4% | 100% | all-weather |
| `rank(fnd6_cicurr)` | TOP3000 | 0.74 | 0.33 | 6.0% | 80% | mixed |
| `rank(fnd6_cicurr / close)` | TOP500 | 0.65 | 0.32 | 8.1% | 60% | mixed |
| `rank(fnd6_cicurr)` | TOP1000 | 0.65 | 0.31 | 5.9% | 60% | bear-only |
| `rank(fnd6_cicurr)` | TOP500 | 0.55 | 0.26 | 7.6% | 60% | mixed |
| `rank(ts_delta(fnd6_cicurr, 5))` | TOP200 | 0.30 | 0.15 | 28.4% | 80% | mixed |
| `rank(fnd6_cicurr / close)` | TOP200 | 0.33 | 0.13 | 18.9% | 60% | weak |
| `rank(fnd6_cicurr)` | TOP200 | 0.29 | 0.11 | 17.9% | 60% | weak |
| `rank(ts_delta(fnd6_cicurr, 5))` | TOP1000 | 0.29 | 0.10 | 29.5% | 40% | mixed |

## Correlation Notes
Top correlates:
- fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a: 0.614 (moderately positively correlated)
- fnd6_exre: 0.589 (moderately positively correlated)
- fn_oth_income_loss_net_of_tax_a: 0.432 (moderately positively correlated)
- fn_comp_options_grants_weighted_avg_a: 0.364 (weakly positively correlated)
- correlation_last_360_days_spy: 0.353 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| snt_value_fast_d1 | socialmedia12 | -0.13 | 1.35 | +0.46 | -0.12 | yes |
| news_open_vol | news12 | -0.05 | 1.28 | +0.36 | -0.71 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.10 | 1.30 | +0.35 | -0.73 | yes |
| cashflow_per_share_minimum | analyst4 | -0.01 | 1.25 | +0.35 | -0.74 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.16 | 1.55 | +0.40 | -0.12 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
