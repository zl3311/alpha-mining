---
field: news_max_dn_ret
dataset: news12
best_template: rank_delta
best_sharpe: 1.14
best_fitness: 0.3
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0937
ann_vol: 0.0801
hit_rate: 0.519
rolling_sharpe_min: -0.667
rolling_sharpe_max: 2.862
top_merge_partner: implied_volatility_mean_skew_360
negated_best_sharpe: 0.28
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.06
n_negated_sims: 4
direction_gap: -0.86
---
# news_max_dn_ret (news12)

*Percent change from price at time of news to lowest price after news*

## Signal Profile
- `rank(news_max_dn_ret)`: S=0.43, F=0.10, T=101.7%, INFERIOR (TOP500)
- `rank(news_max_dn_ret / close)`: S=0.11, F=0.01, T=90.7%, INFERIOR (TOP3000)
- `rank(ts_delta(news_max_dn_ret, 5))`: S=1.14, F=0.30, T=134.2%, INFERIOR (TOP1000)
- `-rank(news_max_dn_ret)`: S=-0.24, F=-0.04, T=110.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_max_dn_ret, 5))`: S=-0.48, F=-0.08, T=147.5%, INFERIOR (TOP3000)
- `ts_zscore(news_max_dn_ret, 22)`: S=0.88, F=0.18, T=114.8%, INFERIOR (TOP3000)
- `ts_mean(news_max_dn_ret, 10)`: S=-0.24, F=-0.11, T=21.1%, INFERIOR (TOP3000)
- `rank(ts_rank(news_max_dn_ret, 22))`: S=1.07, F=0.23, T=118.9%, INFERIOR (TOP3000)
- `rank(-1 * news_max_dn_ret)`: S=0.35, F=0.06, T=125.0%, INFERIOR (TOP3000)
- `rank(-1 * news_max_dn_ret / close)`: S=0.28, F=0.06, T=105.7%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.13, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.54 (strong), ret=+10.1%
  - 2020: S=0.19 (weak), ret=+1.4%
  - 2021: S=1.01 (moderate), ret=+10.4%
  - 2022: S=2.05 (strong), ret=+19.2%
  - 2023: S=0.81 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 9.37% over 202 days (recovered)
- Annualized: return +9.1%, volatility 8.0% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +1.62, excess kurtosis +16.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.67, max 2.86, latest 0.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.99%; worst month: -3.70%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.57
- Sideways: S=1.09
- Bear: S=0.74

## Negated Direction
Best negated: `rank(-1 * news_max_dn_ret / close)` S=0.28, F=0.06, INFERIOR
Direction gap: -0.86 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_max_dn_ret)`: S=0.35, F=0.06, T=125.0%, INFERIOR (TOP3000)
- `rank(-1 * news_max_dn_ret / close)`: S=0.28, F=0.06, T=105.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_max_dn_ret, 5))`: S=-0.48, F=-0.08, T=147.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_max_dn_ret, 5))` | TOP1000 | 1.13 | 0.30 | 9.4% | 100% | all-weather |
| `rank(ts_delta(news_max_dn_ret, 5))` | TOP500 | 1.07 | 0.29 | 11.8% | 80% | mixed |
| `rank(ts_delta(news_max_dn_ret, 5))` | TOP200 | 0.82 | 0.24 | 14.2% | 60% | bull-only |
| `rank(news_max_dn_ret)` | TOP500 | 0.43 | 0.10 | 34.3% | 80% | bear-only |
| `rank(ts_delta(news_max_dn_ret, 5))` | TOP3000 | 0.48 | 0.08 | 16.2% | 60% | all-weather |
| `rank(news_max_dn_ret)` | TOP1000 | 0.24 | 0.04 | 31.3% | 60% | bear-only |
| `rank(news_max_dn_ret)` | TOP200 | 0.22 | 0.04 | 33.9% | 60% | bear-only |

## Correlation Notes
Top correlates:
- news_max_dn_amt: 0.579 (moderately positively correlated)
- news_low_exc_stddev: 0.517 (moderately positively correlated)
- news_tot_ticks: 0.264 (weakly positively correlated)
- news_session_range: 0.250 (weakly positively correlated)
- rank(scl12_buzz * (-1 * returns)): 0.242 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_mean_skew_360 | option8 | -0.15 | 1.71 | +0.57 | +0.83 | yes |
| fnd6_newqv1300_msaq | fundamental6 | -0.07 | 1.75 | +0.49 | -0.86 | yes |
| implied_volatility_mean_skew_180 | option8 | -0.16 | 1.69 | +0.56 | +0.96 | yes |
| rel_num_comp | pv13 | -0.12 | 1.68 | +0.55 | +0.81 | yes |
| rel_num_all | pv13 | -0.12 | 1.77 | +0.55 | +0.88 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
