---
field: news_mins_4_pct_dn
dataset: news12
best_template: rank_level
best_sharpe: 1.27
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.2621
ann_vol: 0.1814
hit_rate: 0.5417
rolling_sharpe_min: -1.442
rolling_sharpe_max: 3.442
top_merge_partner: fn_assets_fair_val_a
redundancy_cluster: 11
negated_best_sharpe: -0.35
negated_best_template: rank_neg_delta
negated_best_fitness: -0.12
n_negated_sims: 4
direction_gap: -1.62
---
# news_mins_4_pct_dn (news12)

*Number of minutes before the price decreased by at least 4 percent after the news release*

## Signal Profile
- `rank(news_mins_4_pct_dn)`: S=1.27, F=0.48, T=162.1%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_4_pct_dn, 5))`: S=0.50, F=0.24, T=124.8%, INFERIOR (TOP1000)
- `-rank(news_mins_4_pct_dn)`: S=-0.47, F=-0.13, T=163.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_4_pct_dn, 5))`: S=-0.35, F=-0.12, T=172.8%, INFERIOR (TOP3000)
- `ts_zscore(news_mins_4_pct_dn, 22)`: S=0.61, F=0.20, T=163.5%, INFERIOR (TOP3000)
- `ts_mean(news_mins_4_pct_dn, 10)`: S=-0.66, F=-0.26, T=35.1%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_4_pct_dn, 22))`: S=1.02, F=0.40, T=165.4%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_4_pct_dn)`: S=-1.27, F=-0.48, T=162.1%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_4_pct_dn / close)`: S=-0.53, F=-0.14, T=157.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 19F/1P
- LOW_SUB_UNIVERSE_SHARPE: 11F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.30, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.02 (strong), ret=+46.5%
  - 2020: S=3.55 (strong), ret=+64.5%
  - 2021: S=-0.06 (negative), ret=-0.9%
  - 2022: S=0.20 (weak), ret=+3.3%
  - 2023: S=0.18 (weak), ret=+2.4%

## Risk & Drawdown
- Max drawdown: 26.21% over 725 days (recovered)
- Annualized: return +23.6%, volatility 18.1% (fraction of booksize)
- Hit rate: 54.2% positive days
- Tail shape: skew -0.46, excess kurtosis +8.00

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.44, max 3.44, latest 0.11

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +14.95%; worst month: -9.31%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.55
- Sideways: S=2.93
- Bear: S=0.43

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_mins_4_pct_dn, 5))` S=-0.35, F=-0.12, INFERIOR
Direction gap: -1.62 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_mins_4_pct_dn)`: S=-1.27, F=-0.48, T=162.1%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_4_pct_dn / close)`: S=-0.53, F=-0.14, T=157.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_4_pct_dn, 5))`: S=-0.35, F=-0.12, T=172.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_mins_4_pct_dn)` | TOP3000 | 1.30 | 0.48 | 26.2% | 80% | mixed |
| `rank(news_mins_4_pct_dn)` | TOP200 | 0.65 | 0.25 | 40.8% | 100% | weak |
| `rank(ts_delta(news_mins_4_pct_dn, 5))` | TOP1000 | 0.50 | 0.24 | 101.2% | 80% | mixed |
| `rank(news_mins_4_pct_dn)` | TOP1000 | 0.51 | 0.13 | 45.7% | 40% | weak |
| `rank(ts_delta(news_mins_4_pct_dn, 5))` | TOP3000 | 0.36 | 0.12 | 114.2% | 60% | mixed |
| `rank(news_mins_4_pct_dn)` | TOP500 | 0.41 | 0.11 | 55.6% | 60% | mixed |
| `rank(ts_delta(news_mins_4_pct_dn, 5))` | TOP200 | 0.15 | 0.04 | 67.1% | 60% | weak |

## Correlation Notes
Top correlates:
- news_mins_3_pct_dn: 0.753 (strongly positively correlated)
- news_mins_2_pct_dn: 0.562 (moderately positively correlated)
- news_mins_4_chg: 0.557 (moderately positively correlated)
- news_mins_5_chg: 0.497 (moderately positively correlated)
- news_mins_3_chg: 0.403 (moderately positively correlated)

Redundancy cluster #11: 2 similar fields, mean |rho| 0.753 (representative: news_mins_3_pct_dn). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_assets_fair_val_a | fundamental2 | -0.03 | 1.94 | +0.54 | -0.86 | yes |
| fnd6_mrc1 | fundamental6 | -0.05 | 1.87 | +0.57 | +0.16 | yes |
| fn_line_of_credit_facility_amount_out_a | fundamental2 | +0.07 | 1.77 | +0.47 | -0.96 | yes |
| anl4_ffo_flag | analyst_revision_momentum | +0.00 | 1.84 | +0.50 | -0.52 | yes |
| fnd6_nopio | fundamental6 | -0.03 | 1.85 | +0.55 | +0.14 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
