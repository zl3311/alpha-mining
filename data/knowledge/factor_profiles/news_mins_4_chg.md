---
field: news_mins_4_chg
dataset: news12
best_template: rank_level
best_sharpe: 1.03
best_fitness: 0.28
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1435
ann_vol: 0.1108
hit_rate: 0.532
rolling_sharpe_min: -1.417
rolling_sharpe_max: 3.852
top_merge_partner: implied_volatility_put_20
redundancy_cluster: 30
negated_best_sharpe: 0.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 4
direction_gap: -0.78
---
# news_mins_4_chg (news12)

*Minimum value among L or S (minutes to reach positive/negative return thresholds) for each minute bucket, representing the fastest reaction time at the 4th percentile*

## Signal Profile
- `rank(news_mins_4_chg)`: S=1.03, F=0.28, T=150.2%, INFERIOR (TOP3000)
- `rank(news_mins_4_chg / close)`: S=0.19, F=0.03, T=144.1%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_4_chg, 5))`: S=0.02, F=0.00, T=118.1%, INFERIOR (TOP200)
- `-rank(news_mins_4_chg)`: S=-0.29, F=-0.05, T=152.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_4_chg, 5))`: S=0.25, F=0.05, T=172.3%, INFERIOR (TOP3000)
- `-ts_zscore(news_mins_4_chg, 63)`: S=0.21, F=0.03, T=154.9%, INFERIOR (TOP3000)
- `ts_mean(news_mins_4_chg, 10)`: S=-0.33, F=-0.08, T=32.0%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_4_chg, 22))`: S=0.13, F=0.02, T=156.7%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_4_chg)`: S=-1.03, F=-0.28, T=150.2%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_4_chg / close)`: S=-0.37, F=-0.07, T=142.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.09, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.65 (strong), ret=+22.5%
  - 2020: S=3.94 (strong), ret=+38.0%
  - 2021: S=0.36 (weak), ret=+4.3%
  - 2022: S=-0.98 (negative), ret=-8.7%
  - 2023: S=0.31 (weak), ret=+3.0%

## Risk & Drawdown
- Max drawdown: 14.35% over 604 days (recovered)
- Annualized: return +12.0%, volatility 11.1% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.18, excess kurtosis +1.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.42, max 3.85, latest 0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +8.10%; worst month: -6.70%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.41
- Sideways: S=2.17
- Bear: S=0.55

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_mins_4_chg, 5))` S=0.25, F=0.05, INFERIOR
Direction gap: -0.78 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_mins_4_chg)`: S=-1.03, F=-0.28, T=150.2%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_4_chg / close)`: S=-0.37, F=-0.07, T=142.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_4_chg, 5))`: S=0.25, F=0.05, T=172.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_mins_4_chg)` | TOP3000 | 1.09 | 0.28 | 14.3% | 80% | mixed |
| `rank(news_mins_4_chg)` | TOP1000 | 0.31 | 0.05 | 35.4% | 60% | mixed |
| `rank(news_mins_4_chg)` | TOP500 | 0.21 | 0.03 | 33.4% | 60% | mixed |

## Correlation Notes
Top correlates:
- news_mins_3_chg: 0.801 (strongly positively correlated)
- news_mins_5_chg: 0.796 (strongly positively correlated)
- news_mins_4_pct_dn: 0.557 (moderately positively correlated)
- news_mins_2_chg: 0.552 (moderately positively correlated)
- news_mins_3_pct_dn: 0.532 (moderately positively correlated)

Redundancy cluster #30: 2 similar fields, mean |rho| 0.796 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_put_20 | option8 | -0.05 | 1.59 | +0.48 | -0.36 | yes |
| implied_volatility_mean_20 | option8 | -0.04 | 1.55 | +0.47 | -0.51 | yes |
| anl4_afv4_eps_high | analyst4 | -0.04 | 1.51 | +0.43 | -0.87 | yes |
| rp_ess_technical | news18 | -0.04 | 1.51 | +0.43 | -0.83 | yes |
| sales_ps | fundamental_value | +0.02 | 1.50 | +0.42 | -0.76 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
