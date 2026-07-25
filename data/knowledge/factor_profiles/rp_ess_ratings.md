---
field: rp_ess_ratings
dataset: news18
best_template: rank_delta
best_sharpe: 0.98
best_fitness: 0.18
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: all-weather
n_variations_with_pnl: 1
max_drawdown: 0.0846
ann_vol: 0.0605
hit_rate: 0.5215
rolling_sharpe_min: -0.732
rolling_sharpe_max: 3.309
top_merge_partner: fnd2_a_flintasacmamtzcsrld
negated_best_sharpe: 0.3
negated_best_template: neg_rank
negated_best_fitness: 0.03
n_negated_sims: 4
direction_gap: -0.68
---
# rp_ess_ratings (news18)

*Event sentiment score of analyst ratings-related news*

## Signal Profile
- `rank(rp_ess_ratings)`: S=0.11, F=0.01, T=138.1%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_ess_ratings, 5))`: S=0.98, F=0.18, T=167.8%, INFERIOR (TOP3000)
- `-rank(rp_ess_ratings)`: S=0.30, F=0.03, T=126.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_ratings, 5))`: S=-0.98, F=-0.18, T=167.8%, INFERIOR (TOP3000)
- `ts_zscore(rp_ess_ratings, 22)`: S=0.31, F=0.03, T=133.3%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_ratings, 10)`: S=-0.16, F=-0.04, T=13.7%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_ratings, 22))`: S=0.31, F=0.03, T=135.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_ratings)`: S=-0.11, F=-0.01, T=138.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_ratings / close)`: S=-0.03, F=0.00, T=141.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/14P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/5P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.96, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.48 (moderate), ret=+11.8%
  - 2020: S=-0.21 (negative), ret=-1.0%
  - 2021: S=1.90 (strong), ret=+12.7%
  - 2022: S=-0.24 (negative), ret=-1.4%
  - 2023: S=1.66 (strong), ret=+6.3%

## Risk & Drawdown
- Max drawdown: 8.46% over 552 days (recovered)
- Annualized: return +5.8%, volatility 6.0% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.19, excess kurtosis +4.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.73, max 3.31, latest 1.49

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +4.79%; worst month: -3.48%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.91
- Sideways: S=1.22
- Bear: S=0.70

## Negated Direction
Best negated: `-rank(rp_ess_ratings)` S=0.30, F=0.03, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_ess_ratings)`: S=-0.11, F=-0.01, T=138.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_ratings / close)`: S=-0.03, F=0.00, T=141.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_ratings, 5))`: S=-0.98, F=-0.18, T=167.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_ess_ratings, 5))` | TOP3000 | 0.96 | 0.18 | 8.5% | 60% | all-weather |

## Correlation Notes
Top correlates:
- rp_css_ratings: 0.359 (weakly positively correlated)
- rp_css_price: 0.118 (weakly positively correlated)
- est_tbv_ps: 0.096 (weakly positively correlated)
- pv13_reveremap: -0.094 (weakly negatively correlated)
- fnd6_optlifeq: -0.087 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd2_a_flintasacmamtzcsrld | fundamental2 | +0.03 | 1.34 | +0.38 | -0.47 | yes |
| fnd6_dltp | fundamental6 | -0.01 | 1.40 | +0.39 | -0.32 | yes |
| fn_treasury_stock_shares_a | fundamental2 | -0.02 | 1.31 | +0.35 | -0.69 | yes |
| unsystematic_risk_last_60_days | model51 | -0.01 | 1.40 | +0.39 | -0.28 | yes |
| operating_profit_before_depr_amort_min_guidance_qtr | analyst4 | -0.02 | 1.37 | +0.41 | -0.11 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
