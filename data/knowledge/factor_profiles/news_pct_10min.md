---
field: news_pct_10min
dataset: news12
best_template: rank_level
best_sharpe: 0.87
best_fitness: 0.24
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1099
ann_vol: 0.0911
hit_rate: 0.5247
rolling_sharpe_min: -0.762
rolling_sharpe_max: 2.012
top_merge_partner: fnd6_newqv1300_lltq
negated_best_sharpe: 0.55
negated_best_template: neg_rank
negated_best_fitness: 0.09
n_negated_sims: 4
direction_gap: -0.32
---
# news_pct_10min (news12)

*Percent change in price during the first 10 minutes following the news release*

## Signal Profile
- `rank(news_pct_10min)`: S=0.87, F=0.24, T=101.7%, INFERIOR (TOP200)
- `rank(news_pct_10min / close)`: S=-0.52, F=-0.09, T=119.9%, INFERIOR (TOP3000)
- `rank(ts_delta(news_pct_10min, 5))`: S=0.41, F=0.08, T=118.8%, INFERIOR (TOP200)
- `-rank(news_pct_10min)`: S=0.55, F=0.09, T=119.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_10min, 5))`: S=0.25, F=0.03, T=146.6%, INFERIOR (TOP3000)
- `-ts_zscore(news_pct_10min, 63)`: S=0.36, F=0.05, T=115.5%, INFERIOR (TOP3000)
- `ts_mean(news_pct_10min, 10)`: S=-0.39, F=-0.12, T=27.2%, INFERIOR (TOP3000)
- `rank(ts_rank(news_pct_10min, 22))`: S=-0.53, F=-0.08, T=122.0%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_10min)`: S=-0.71, F=-0.13, T=127.5%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_10min / close)`: S=-0.64, F=-0.11, T=129.1%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.87, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.85 (moderate), ret=+6.3%
  - 2020: S=1.76 (strong), ret=+17.5%
  - 2021: S=0.20 (weak), ret=+2.2%
  - 2022: S=0.89 (moderate), ret=+7.9%
  - 2023: S=0.73 (moderate), ret=+5.1%

## Risk & Drawdown
- Max drawdown: 10.99% over 503 days (recovered)
- Annualized: return +7.9%, volatility 9.1% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew -0.23, excess kurtosis +2.99

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.76, max 2.01, latest 0.73

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +6.79%; worst month: -4.19%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.24
- Sideways: S=1.28
- Bear: S=1.72

## Negated Direction
Best negated: `-rank(news_pct_10min)` S=0.55, F=0.09, INFERIOR
Direction gap: -0.32 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_pct_10min)`: S=-0.71, F=-0.13, T=127.5%, INFERIOR (TOP3000)
- `rank(-1 * news_pct_10min / close)`: S=-0.64, F=-0.11, T=129.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pct_10min, 5))`: S=0.25, F=0.03, T=146.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_pct_10min)` | TOP200 | 0.87 | 0.24 | 11.0% | 100% | mixed |
| `rank(news_pct_10min)` | TOP3000 | 0.75 | 0.13 | 8.6% | 100% | bear-only |
| `rank(ts_delta(news_pct_10min, 5))` | TOP200 | 0.43 | 0.08 | 15.1% | 80% | bear-only |
| `rank(ts_delta(news_pct_10min, 5))` | TOP500 | 0.28 | 0.04 | 18.2% | 60% | bear-only |

## Correlation Notes
Top correlates:
- news_pct_5_min: 0.658 (moderately positively correlated)
- news_pct_30min: 0.588 (moderately positively correlated)
- fnd6_prcl: -0.194 (weakly negatively correlated)
- fnd6_prcc: -0.171 (weakly negatively correlated)
- fnd2_a_ptoacqbnsesg: -0.160 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_newqv1300_lltq | fundamental6 | -0.14 | 1.35 | +0.45 | -0.60 | yes |
| fnd6_newqv1300_ppentq | fundamental6 | -0.14 | 1.39 | +0.43 | -0.71 | yes |
| ppent | fundamental6 | -0.14 | 1.39 | +0.43 | -0.71 | yes |
| fnd6_mfma1_dp | fundamental6 | -0.13 | 1.31 | +0.44 | -0.61 | yes |
| fnd6_newqv1300_rectrq | fundamental6 | -0.13 | 1.40 | +0.42 | -0.77 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
