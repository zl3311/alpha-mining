---
field: news_open_vol
dataset: news12
best_template: rank_level
best_sharpe: 0.93
best_fitness: 0.21
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.1165
ann_vol: 0.0712
hit_rate: 0.5109
rolling_sharpe_min: -1.477
rolling_sharpe_max: 2.837
top_merge_partner: implied_volatility_mean_skew_1080
negated_best_sharpe: 0.4
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 4
direction_gap: -0.53
---
# news_open_vol (news12)

*Main session open volume*

## Signal Profile
- `rank(news_open_vol)`: S=0.93, F=0.21, T=124.1%, INFERIOR (TOP3000)
- `rank(news_open_vol / close)`: S=0.17, F=0.02, T=104.7%, INFERIOR (TOP3000)
- `rank(ts_delta(news_open_vol, 5))`: S=-0.32, F=-0.05, T=141.0%, INFERIOR (TOP1000)
- `-rank(news_open_vol)`: S=-0.41, F=-0.07, T=105.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_open_vol, 5))`: S=0.40, F=0.06, T=152.3%, INFERIOR (TOP3000)
- `ts_zscore(news_open_vol, 22)`: S=0.19, F=0.02, T=132.8%, INFERIOR (TOP3000)
- `ts_mean(news_open_vol, 10)`: S=0.25, F=0.12, T=9.6%, INFERIOR (TOP3000)
- `rank(ts_rank(news_open_vol, 22))`: S=0.39, F=0.05, T=134.3%, INFERIOR (TOP3000)
- `rank(-1 * news_open_vol)`: S=-0.93, F=-0.21, T=124.1%, INFERIOR (TOP3000)
- `rank(-1 * news_open_vol / close)`: S=-0.15, F=-0.02, T=123.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.93, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.97 (strong), ret=+9.1%
  - 2020: S=1.21 (moderate), ret=+8.0%
  - 2021: S=-0.09 (negative), ret=-0.7%
  - 2022: S=0.98 (moderate), ret=+8.8%
  - 2023: S=1.10 (moderate), ret=+7.2%

## Risk & Drawdown
- Max drawdown: 11.65% over 435 days (recovered)
- Annualized: return +6.6%, volatility 7.1% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.76, excess kurtosis +3.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.48, max 2.84, latest 1.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +6.98%; worst month: -4.46%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.90
- Sideways: S=1.07
- Bear: S=0.83

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_open_vol, 5))` S=0.40, F=0.06, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_open_vol)`: S=-0.93, F=-0.21, T=124.1%, INFERIOR (TOP3000)
- `rank(-1 * news_open_vol / close)`: S=-0.15, F=-0.02, T=123.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_open_vol, 5))`: S=0.40, F=0.06, T=152.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_open_vol)` | TOP3000 | 0.93 | 0.21 | 11.7% | 80% | all-weather |
| `rank(news_open_vol)` | TOP500 | 0.41 | 0.08 | 17.8% | 80% | mixed |
| `rank(news_open_vol)` | TOP200 | 0.34 | 0.07 | 16.6% | 60% | mixed |
| `rank(news_open_vol)` | TOP1000 | 0.39 | 0.07 | 15.9% | 80% | mixed |

## Correlation Notes
Top correlates:
- adv20: 0.806 (strongly positively correlated)
- fnd6_cshtr: 0.707 (strongly positively correlated)
- implied_volatility_mean_skew_1080: -0.603 (moderately negatively correlated)
- implied_volatility_mean_skew_720: -0.602 (moderately negatively correlated)
- implied_volatility_mean_skew_360: -0.584 (moderately negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_mean_skew_1080 | option8 | -0.60 | 2.08 | +1.07 | -0.35 | yes |
| implied_volatility_mean_skew_720 | option8 | -0.60 | 2.09 | +1.07 | -0.28 | yes |
| implied_volatility_mean_skew_360 | option8 | -0.58 | 2.20 | +1.10 | +0.12 | yes |
| implied_volatility_mean_skew_270 | option8 | -0.56 | 2.09 | +1.06 | +0.17 | yes |
| implied_volatility_mean_skew_180 | option8 | -0.53 | 2.06 | +0.99 | +0.15 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
