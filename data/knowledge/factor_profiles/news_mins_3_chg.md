---
field: news_mins_3_chg
dataset: news12
best_template: rank_level
best_sharpe: 0.76
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1021
ann_vol: 0.0854
hit_rate: 0.5247
rolling_sharpe_min: -0.717
rolling_sharpe_max: 3.313
top_merge_partner: parkinson_volatility_120
negated_best_sharpe: 0.09
negated_best_template: rank_neg_delta
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -0.67
---
# news_mins_3_chg (news12)

*Minimum number of minutes taken for price to move (up or down) 3 percentage points after the event*

## Signal Profile
- `rank(news_mins_3_chg)`: S=0.76, F=0.16, T=145.0%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_3_chg, 5))`: S=-0.09, F=-0.01, T=168.0%, INFERIOR (TOP3000)
- `-rank(news_mins_3_chg)`: S=-0.18, F=-0.02, T=146.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_3_chg, 5))`: S=0.09, F=0.01, T=168.0%, INFERIOR (TOP3000)
- `-ts_zscore(news_mins_3_chg, 63)`: S=0.42, F=0.08, T=147.5%, INFERIOR (TOP3000)
- `ts_mean(news_mins_3_chg, 10)`: S=-0.72, F=-0.25, T=29.7%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_3_chg, 22))`: S=0.39, F=0.07, T=149.8%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_3_chg)`: S=-0.76, F=-0.16, T=145.0%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_3_chg / close)`: S=-0.27, F=-0.04, T=136.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/4P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.80, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.96 (moderate), ret=+9.3%
  - 2020: S=4.13 (strong), ret=+28.8%
  - 2021: S=-0.40 (negative), ret=-4.0%
  - 2022: S=0.12 (weak), ret=+0.9%
  - 2023: S=-0.23 (negative), ret=-1.6%

## Risk & Drawdown
- Max drawdown: 10.21% over 1026 days (not yet recovered, ongoing at window end)
- Annualized: return +6.9%, volatility 8.5% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew -0.15, excess kurtosis +1.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.72, max 3.31, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +7.11%; worst month: -5.85%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.56
- Sideways: S=1.45
- Bear: S=0.35

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_mins_3_chg, 5))` S=0.09, F=0.01, INFERIOR
Direction gap: -0.67 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_mins_3_chg)`: S=-0.76, F=-0.16, T=145.0%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_3_chg / close)`: S=-0.27, F=-0.04, T=136.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_3_chg, 5))`: S=0.09, F=0.01, T=168.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_mins_3_chg)` | TOP3000 | 0.80 | 0.16 | 10.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- news_mins_4_chg: 0.801 (strongly positively correlated)
- news_mins_2_chg: 0.764 (strongly positively correlated)
- news_mins_5_chg: 0.597 (moderately positively correlated)
- news_mins_2_pct_dn: 0.590 (moderately positively correlated)
- news_mins_3_pct_dn: 0.569 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| parkinson_volatility_120 | option8 | -0.24 | 1.37 | +0.48 | -0.26 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.23 | 1.46 | +0.46 | +0.20 | yes |
| rank(fnd6_acdo) * rank(volume/adv20) | unknown | -0.12 | 1.17 | +0.35 | -0.87 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.15 | 1.24 | +0.43 | +0.95 | yes |
| parkinson_volatility_90 | option8 | -0.17 | 1.30 | +0.41 | +0.19 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
