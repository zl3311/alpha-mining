---
field: news_mins_5_chg
dataset: news12
best_template: rank_level
best_sharpe: 0.8
best_fitness: 0.23
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.2226
ann_vol: 0.157
hit_rate: 0.5417
rolling_sharpe_min: -1.255
rolling_sharpe_max: 3.459
top_merge_partner: fnd6_newqv1300_txdbq
redundancy_cluster: 30
negated_best_sharpe: -0.26
negated_best_template: rank_neg_delta
negated_best_fitness: -0.07
n_negated_sims: 4
direction_gap: -1.06
---
# news_mins_5_chg (news12)

*Minimum value among L or S for each minute bucket, indicating the fastest reaction time at the 5th percentile*

## Signal Profile
- `rank(news_mins_5_chg)`: S=0.80, F=0.23, T=155.0%, INFERIOR (TOP3000)
- `rank(news_mins_5_chg / close)`: S=0.28, F=0.06, T=150.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_5_chg, 5))`: S=0.26, F=0.08, T=142.8%, INFERIOR (TOP1000)
- `-rank(news_mins_5_chg)`: S=-0.66, F=-0.21, T=157.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_5_chg, 5))`: S=-0.26, F=-0.07, T=175.9%, INFERIOR (TOP3000)
- `-ts_zscore(news_mins_5_chg, 63)`: S=0.33, F=0.07, T=159.5%, INFERIOR (TOP3000)
- `ts_mean(news_mins_5_chg, 10)`: S=-0.23, F=-0.05, T=33.8%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_5_chg, 22))`: S=-0.19, F=-0.03, T=160.4%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_5_chg)`: S=-0.80, F=-0.23, T=155.0%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_5_chg / close)`: S=-0.47, F=-0.11, T=148.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.83, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.04 (moderate), ret=+20.3%
  - 2020: S=2.57 (strong), ret=+34.0%
  - 2021: S=1.01 (moderate), ret=+15.2%
  - 2022: S=-0.81 (negative), ret=-10.4%
  - 2023: S=0.33 (weak), ret=+5.1%

## Risk & Drawdown
- Max drawdown: 22.26% over 261 days (recovered)
- Annualized: return +13.1%, volatility 15.7% (fraction of booksize)
- Hit rate: 54.2% positive days
- Tail shape: skew -0.35, excess kurtosis +3.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.25, max 3.46, latest 0.22

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +11.59%; worst month: -8.69%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.63
- Sideways: S=1.01
- Bear: S=0.83

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_mins_5_chg, 5))` S=-0.26, F=-0.07, INFERIOR
Direction gap: -1.06 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_mins_5_chg)`: S=-0.80, F=-0.23, T=155.0%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_5_chg / close)`: S=-0.47, F=-0.11, T=148.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_5_chg, 5))`: S=-0.26, F=-0.07, T=175.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_mins_5_chg)` | TOP3000 | 0.83 | 0.23 | 22.3% | 80% | all-weather |
| `rank(news_mins_5_chg)` | TOP1000 | 0.68 | 0.21 | 48.6% | 80% | mixed |
| `rank(ts_delta(news_mins_5_chg, 5))` | TOP1000 | 0.23 | 0.08 | 114.0% | 40% | weak |
| `rank(ts_delta(news_mins_5_chg, 5))` | TOP3000 | 0.26 | 0.07 | 90.8% | 80% | bull-only |

## Correlation Notes
Top correlates:
- news_mins_4_chg: 0.796 (strongly positively correlated)
- news_mins_3_chg: 0.597 (moderately positively correlated)
- news_mins_4_pct_dn: 0.497 (moderately positively correlated)
- news_mins_3_pct_dn: 0.442 (moderately positively correlated)
- news_mins_2_pct_dn: 0.392 (weakly positively correlated)

Redundancy cluster #30: 2 similar fields, mean |rho| 0.796 (representative: news_mins_4_chg). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_newqv1300_txdbq | fundamental6 | -0.00 | 1.19 | +0.34 | -0.86 | yes |
| fnd6_newqv1300_rectaq | fundamental6 | -0.07 | 1.24 | +0.38 | -0.40 | yes |
| fnd2_a_unrgtxbnfitxpenlintacd | fundamental2 | -0.01 | 1.18 | +0.35 | -0.70 | yes |
| fnd6_newqv1300_txwq | fundamental6 | -0.01 | 1.17 | +0.34 | -0.78 | yes |
| rp_ess_mna | news18 | -0.03 | 1.17 | +0.33 | -0.75 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
