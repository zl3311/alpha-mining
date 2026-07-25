---
field: news_mins_1_pct_dn
dataset: news12
best_template: ts_zscore
best_sharpe: 1.02
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.0999
ann_vol: 0.0716
hit_rate: 0.5296
rolling_sharpe_min: -0.524
rolling_sharpe_max: 2.16
redundancy_cluster: 64
negated_best_sharpe: 0.39
negated_best_template: neg_rank
negated_best_fitness: 0.06
n_negated_sims: 4
direction_gap: -0.63
---
# news_mins_1_pct_dn (news12)

*Number of minutes before the price decreased by at least 1 percent after the news release*

## Signal Profile
- `rank(news_mins_1_pct_dn)`: S=0.60, F=0.10, T=141.4%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_1_pct_dn, 5))`: S=0.19, F=0.02, T=150.9%, INFERIOR (TOP500)
- `-rank(news_mins_1_pct_dn)`: S=0.39, F=0.06, T=134.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_1_pct_dn, 5))`: S=0.25, F=0.03, T=162.0%, INFERIOR (TOP3000)
- `-ts_zscore(news_mins_1_pct_dn, 63)`: S=1.02, F=0.22, T=134.8%, INFERIOR (TOP3000)
- `ts_mean(news_mins_1_pct_dn, 10)`: S=-0.29, F=-0.06, T=25.7%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_1_pct_dn, 22))`: S=-0.73, F=-0.13, T=137.5%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_1_pct_dn)`: S=-0.60, F=-0.10, T=141.4%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_1_pct_dn / close)`: S=-0.02, F=0.00, T=133.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/11P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.13 (weak), ret=+0.8%
  - 2020: S=2.00 (strong), ret=+11.8%
  - 2021: S=0.57 (moderate), ret=+4.8%
  - 2022: S=0.73 (moderate), ret=+6.1%
  - 2023: S=-0.30 (negative), ret=-1.7%

## Risk & Drawdown
- Max drawdown: 9.99% over 259 days (recovered)
- Annualized: return +4.4%, volatility 7.2% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.27, excess kurtosis +2.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.52, max 2.16, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +6.85%; worst month: -5.83%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.34
- Sideways: S=0.93
- Bear: S=-0.51

## Negated Direction
Best negated: `-rank(news_mins_1_pct_dn)` S=0.39, F=0.06, INFERIOR
Direction gap: -0.63 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_mins_1_pct_dn)`: S=-0.60, F=-0.10, T=141.4%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_1_pct_dn / close)`: S=-0.02, F=0.00, T=133.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_1_pct_dn, 5))`: S=0.25, F=0.03, T=162.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_mins_1_pct_dn)` | TOP3000 | 0.62 | 0.10 | 10.0% | 80% | bull-only |
| `rank(ts_delta(news_mins_1_pct_dn, 5))` | TOP500 | 0.20 | 0.02 | 22.6% | 80% | mixed |

## Correlation Notes
Top correlates:
- news_mins_2_chg: 0.746 (strongly positively correlated)
- news_mins_2_pct_dn: 0.735 (strongly positively correlated)
- news_mins_3_chg: 0.560 (moderately positively correlated)
- est_eps: 0.552 (moderately positively correlated)
- fnd6_ci: 0.551 (moderately positively correlated)

Redundancy cluster #64: 2 similar fields, mean |rho| 0.735 (representative: news_mins_2_pct_dn). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
