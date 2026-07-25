---
field: fn_incremental_shares_attributable_to_share_based_payment_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 1.12
best_fitness: 0.81
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.123
ann_vol: 0.175
hit_rate: 0.5101
rolling_sharpe_min: 0.243
rolling_sharpe_max: 2.551
top_merge_partner: news_open_gap
redundancy_cluster: 25
negated_best_sharpe: 0.81
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.47
n_negated_sims: 10
direction_gap: -0.31
---
# fn_incremental_shares_attributable_to_share_based_payment_q (fundamental2)

*Additional shares included in the calculation of diluted EPS as a result of the potentially dilutive effect of share-based payment arrangements using the treasury stock method.*

## Signal Profile
- `rank(fn_incremental_shares_attributable_to_share_based_payment_q)`: S=0.02, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(fn_incremental_shares_attributable_to_share_based_payment_q / close)`: S=0.38, F=0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_incremental_shares_attributable_to_share_based_payment_q, 5))`: S=1.12, F=0.81, T=37.2%, INFERIOR (TOP500)
- `-rank(fn_incremental_shares_attributable_to_share_based_payment_q)`: S=0.38, F=0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_incremental_shares_attributable_to_share_based_payment_q, 5))`: S=-1.12, F=-0.81, T=37.1%, INFERIOR (TOP3000)
- `-ts_zscore(fn_incremental_shares_attributable_to_share_based_payment_q, 63)`: S=0.24, F=0.07, T=17.2%, INFERIOR (TOP3000)
- `ts_mean(fn_incremental_shares_attributable_to_share_based_payment_q, 10)`: S=0.38, F=0.20, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_incremental_shares_attributable_to_share_based_payment_q, 22))`: S=-0.05, F=-0.01, T=16.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_incremental_shares_attributable_to_share_based_payment_q)`: S=0.79, F=0.46, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_incremental_shares_attributable_to_share_based_payment_q / close)`: S=0.81, F=0.47, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.12, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.66 (strong), ret=+17.3%
  - 2020: S=0.84 (moderate), ret=+11.9%
  - 2021: S=2.42 (strong), ret=+30.6%
  - 2022: S=0.63 (moderate), ret=+13.4%
  - 2023: S=0.97 (moderate), ret=+23.1%

## Risk & Drawdown
- Max drawdown: 12.30% over 85 days (not yet recovered, ongoing at window end)
- Annualized: return +19.6%, volatility 17.5% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +3.28, excess kurtosis +34.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.24, max 2.55, latest 0.94

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +17.49%; worst month: -5.15%
Positive months: 73%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.76
- Sideways: S=1.34
- Bear: S=1.20

## Negated Direction
Best negated: `rank(-1 * fn_incremental_shares_attributable_to_share_based_payment_q / close)` S=0.81, F=0.47, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_incremental_shares_attributable_to_share_based_payment_q)`: S=0.79, F=0.46, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_incremental_shares_attributable_to_share_based_payment_q / close)`: S=0.81, F=0.47, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_incremental_shares_attributable_to_share_based_payment_q, 5))`: S=-1.12, F=-0.81, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_incremental_shares_attributable_to_share_based_payment_q, 5))` | TOP500 | 1.12 | 0.81 | 12.3% | 100% | all-weather |
| `rank(ts_delta(fn_incremental_shares_attributable_to_share_based_payment_q, 5))` | TOP1000 | 0.69 | 0.30 | 14.7% | 80% | mixed |
| `rank(ts_delta(fn_incremental_shares_attributable_to_share_based_payment_q, 5))` | TOP200 | 0.58 | 0.30 | 16.4% | 80% | weak |
| `rank(fn_incremental_shares_attributable_to_share_based_payment_q / close)` | TOP3000 | 0.35 | 0.12 | 5.2% | 60% | bull-only |
| `rank(ts_delta(fn_incremental_shares_attributable_to_share_based_payment_q, 5))` | TOP3000 | 0.20 | 0.04 | 24.3% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fn_avg_diluted_sharesout_adj_q: 0.743 (strongly positively correlated)
- fn_oth_income_loss_net_of_tax_q: 0.321 (weakly positively correlated)
- snt_buzz_ret: 0.110 (weakly positively correlated)
- max_selling_general_admin_guidance: -0.109 (weakly negatively correlated)
- sg_and_admin_min_guidance_value: -0.109 (weakly negatively correlated)

Redundancy cluster #25: 2 similar fields, mean |rho| 0.743 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_gap | news12 | +0.02 | 1.61 | +0.43 | -0.97 | yes |
| anl4_netprofit_flag | analyst4 | -0.04 | 1.68 | +0.40 | -0.85 | yes |
| implied_volatility_put_20 | option8 | -0.04 | 1.56 | +0.44 | -0.51 | yes |
| implied_volatility_mean_10 | option8 | -0.01 | 1.62 | +0.40 | -0.88 | yes |
| fnd6_mkvaltq | fundamental6 | -0.00 | 1.51 | +0.39 | -0.89 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
