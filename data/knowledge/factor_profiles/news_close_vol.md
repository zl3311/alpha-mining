---
field: news_close_vol
dataset: news12
best_template: rank_delta
best_sharpe: 1.2
best_fitness: 0.27
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.1689
ann_vol: 0.0673
hit_rate: 0.5069
rolling_sharpe_min: -2.355
rolling_sharpe_max: 3.76
top_merge_partner: anl4_tbve_ft
negated_best_sharpe: 0.24
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.04
n_negated_sims: 4
direction_gap: -0.96
---
# news_close_vol (news12)

*Main session close volume*

## Signal Profile
- `rank(news_close_vol)`: S=0.53, F=0.12, T=114.3%, INFERIOR (TOP500)
- `rank(news_close_vol / close)`: S=0.04, F=0.00, T=106.1%, INFERIOR (TOP3000)
- `rank(ts_delta(news_close_vol, 5))`: S=1.20, F=0.27, T=161.0%, INFERIOR (TOP3000)
- `-rank(news_close_vol)`: S=-0.25, F=-0.04, T=126.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_close_vol, 5))`: S=-1.20, F=-0.27, T=161.0%, INFERIOR (TOP3000)
- `ts_zscore(news_close_vol, 22)`: S=0.44, F=0.06, T=141.2%, INFERIOR (TOP3000)
- `ts_mean(news_close_vol, 10)`: S=-0.32, F=-0.14, T=20.3%, INFERIOR (TOP3000)
- `rank(ts_rank(news_close_vol, 22))`: S=0.59, F=0.08, T=141.9%, INFERIOR (TOP3000)
- `rank(-1 * news_close_vol)`: S=0.07, F=0.00, T=142.2%, INFERIOR (TOP3000)
- `rank(-1 * news_close_vol / close)`: S=0.24, F=0.04, T=121.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.19, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.69 (negative), ret=-3.4%
  - 2020: S=-0.33 (negative), ret=-2.2%
  - 2021: S=2.65 (strong), ret=+25.2%
  - 2022: S=2.63 (strong), ret=+16.0%
  - 2023: S=0.78 (moderate), ret=+3.6%

## Risk & Drawdown
- Max drawdown: 16.89% over 746 days (recovered)
- Annualized: return +8.0%, volatility 6.7% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +2.76, excess kurtosis +37.76

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.35, max 3.76, latest 0.82

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +5.67%; worst month: -2.54%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.43
- Sideways: S=0.16
- Bear: S=0.96

## Negated Direction
Best negated: `rank(-1 * news_close_vol / close)` S=0.24, F=0.04, INFERIOR
Direction gap: -0.96 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_close_vol)`: S=0.07, F=0.00, T=142.2%, INFERIOR (TOP3000)
- `rank(-1 * news_close_vol / close)`: S=0.24, F=0.04, T=121.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_close_vol, 5))`: S=-1.20, F=-0.27, T=161.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_close_vol, 5))` | TOP3000 | 1.19 | 0.27 | 16.9% | 60% | all-weather |
| `rank(news_close_vol)` | TOP500 | 0.52 | 0.12 | 22.9% | 80% | bear-only |
| `rank(ts_delta(news_close_vol, 5))` | TOP1000 | 0.48 | 0.08 | 11.7% | 60% | mixed |
| `rank(news_close_vol)` | TOP200 | 0.33 | 0.07 | 17.9% | 60% | mixed |
| `rank(ts_delta(news_close_vol, 5))` | TOP500 | 0.40 | 0.06 | 10.4% | 60% | mixed |
| `rank(news_close_vol)` | TOP1000 | 0.24 | 0.04 | 25.6% | 60% | bear-only |
| `rank(ts_delta(news_close_vol, 5))` | TOP200 | 0.29 | 0.04 | 20.1% | 40% | all-weather |

## Correlation Notes
Top correlates:
- snt_buzz_bfl_fast_d1: -0.173 (weakly negatively correlated)
- news_max_dn_ret: 0.172 (weakly positively correlated)
- fnd6_optlife: 0.169 (weakly positively correlated)
- fnd6_newqv1300_stkcpaq: 0.150 (weakly positively correlated)
- fn_debt_instrument_interest_rate_stated_percentage_q: 0.145 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_tbve_ft | analyst_estimate | -0.08 | 1.80 | +0.55 | -0.47 | yes |
| fnd6_newqv1300_msaq | fundamental6 | -0.12 | 1.85 | +0.58 | +0.02 | yes |
| pcr_vol_20 | option9 | -0.14 | 1.74 | +0.55 | -0.12 | yes |
| anl4_netdebt_flag | analyst_revision | -0.08 | 1.82 | +0.55 | +0.75 | yes |
| pcr_vol_10 | option9 | -0.09 | 1.80 | +0.54 | +0.73 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
