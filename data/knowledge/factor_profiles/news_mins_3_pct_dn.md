---
field: news_mins_3_pct_dn
dataset: news12
best_template: rank_level
best_sharpe: 1.33
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 20
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.2484
ann_vol: 0.1281
hit_rate: 0.549
rolling_sharpe_min: -1.455
rolling_sharpe_max: 4.129
top_merge_partner: fn_assets_fair_val_a
redundancy_cluster: 11
negated_best_sharpe: 0.02
negated_best_template: rank_neg_delta
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.31
---
# news_mins_3_pct_dn (news12)

*Number of minutes before the price decreased by at least 3 percent after the news release*

## Signal Profile
- `rank(news_mins_3_pct_dn)`: S=1.33, F=0.44, T=157.9%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_3_pct_dn, 5))`: S=0.59, F=0.27, T=111.8%, INFERIOR (TOP200)
- `-rank(news_mins_3_pct_dn)`: S=-0.20, F=-0.03, T=158.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_3_pct_dn, 5))`: S=0.02, F=0.00, T=176.7%, INFERIOR (TOP3000)
- `ts_zscore(news_mins_3_pct_dn, 22)`: S=0.76, F=0.23, T=160.2%, INFERIOR (TOP3000)
- `ts_mean(news_mins_3_pct_dn, 10)`: S=-1.01, F=-0.44, T=33.0%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_3_pct_dn, 22))`: S=0.56, F=0.14, T=161.5%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_3_pct_dn)`: S=-1.33, F=-0.44, T=157.9%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_3_pct_dn / close)`: S=-0.42, F=-0.09, T=151.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/4P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 19F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.37, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.77 (strong), ret=+44.2%
  - 2020: S=4.24 (strong), ret=+49.5%
  - 2021: S=0.02 (weak), ret=+0.2%
  - 2022: S=-0.32 (negative), ret=-3.6%
  - 2023: S=-0.47 (negative), ret=-4.1%

## Risk & Drawdown
- Max drawdown: 24.84% over 1029 days (not yet recovered, ongoing at window end)
- Annualized: return +17.6%, volatility 12.8% (fraction of booksize)
- Hit rate: 54.9% positive days
- Tail shape: skew +0.09, excess kurtosis +5.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.46, max 4.13, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +11.73%; worst month: -6.67%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.73
- Sideways: S=2.32
- Bear: S=0.94

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_mins_3_pct_dn, 5))` S=0.02, F=0.00, INFERIOR
Direction gap: -1.31 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_mins_3_pct_dn)`: S=-1.33, F=-0.44, T=157.9%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_3_pct_dn / close)`: S=-0.42, F=-0.09, T=151.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_3_pct_dn, 5))`: S=0.02, F=0.00, T=176.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_mins_3_pct_dn)` | TOP3000 | 1.37 | 0.44 | 24.8% | 60% | all-weather |
| `rank(ts_delta(news_mins_3_pct_dn, 5))` | TOP200 | 0.59 | 0.27 | 51.4% | 80% | mixed |
| `rank(news_mins_3_pct_dn)` | TOP200 | 0.37 | 0.09 | 50.9% | 80% | weak |
| `rank(news_mins_3_pct_dn)` | TOP500 | 0.41 | 0.09 | 38.6% | 60% | weak |
| `rank(ts_delta(news_mins_3_pct_dn, 5))` | TOP1000 | 0.26 | 0.08 | 67.2% | 80% | weak |
| `rank(news_mins_3_pct_dn)` | TOP1000 | 0.23 | 0.03 | 45.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- news_mins_2_pct_dn: 0.769 (strongly positively correlated)
- news_mins_4_pct_dn: 0.753 (strongly positively correlated)
- news_mins_3_chg: 0.569 (moderately positively correlated)
- news_mins_4_chg: 0.532 (moderately positively correlated)
- news_mins_1_pct_dn: 0.496 (moderately positively correlated)

Redundancy cluster #11: 2 similar fields, mean |rho| 0.753 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_assets_fair_val_a | fundamental2 | -0.02 | 1.95 | +0.55 | -0.92 | yes |
| anl4_ffo_flag | analyst_revision_momentum | +0.02 | 1.89 | +0.52 | -0.58 | yes |
| fnd6_city | fundamental_rare_event | +0.05 | 2.03 | +0.47 | -0.95 | yes |
| implied_volatility_put_10 | option8 | -0.05 | 1.93 | +0.56 | +0.51 | yes |
| anl4_netprofit_flag | analyst4 | -0.02 | 1.89 | +0.52 | -0.33 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
