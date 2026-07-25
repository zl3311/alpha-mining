---
field: news_mins_7_5_pct_dn
dataset: news12
best_template: rank_delta
best_sharpe: 0.58
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.9583
ann_vol: 0.7275
hit_rate: 0.2745
rolling_sharpe_min: -0.542
rolling_sharpe_max: 1.989
negated_best_sharpe: 0.19
negated_best_template: neg_rank
negated_best_fitness: 0.05
n_negated_sims: 4
direction_gap: -0.39
---
# news_mins_7_5_pct_dn (news12)

*Number of minutes elapsed before price decreases by 7.5 percentage points after the event*

## Signal Profile
- `rank(news_mins_7_5_pct_dn)`: S=0.53, F=0.21, T=170.5%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_7_5_pct_dn, 5))`: S=0.58, F=0.45, T=70.0%, INFERIOR (TOP3000)
- `-rank(news_mins_7_5_pct_dn)`: S=0.19, F=0.05, T=140.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_7_5_pct_dn, 5))`: S=-0.58, F=-0.45, T=70.0%, INFERIOR (TOP3000)
- `ts_zscore(news_mins_7_5_pct_dn, 22)`: S=0.50, F=0.27, T=105.2%, INFERIOR (TOP3000)
- `ts_mean(news_mins_7_5_pct_dn, 10)`: S=-0.01, F=0.00, T=40.9%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_7_5_pct_dn, 22))`: S=-0.17, F=-0.05, T=134.5%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_7_5_pct_dn)`: S=-0.53, F=-0.21, T=170.5%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_7_5_pct_dn / close)`: S=-0.27, F=-0.08, T=168.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 11F/9P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/5P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.24 (negative), ret=-11.0%
  - 2020: S=0.58 (moderate), ret=+52.8%
  - 2021: S=0.19 (weak), ret=+14.5%
  - 2022: S=0.76 (moderate), ret=+44.5%
  - 2023: S=1.42 (moderate), ret=+106.6%

## Risk & Drawdown
- Max drawdown: 95.83% over 851 days (recovered)
- Annualized: return +42.3%, volatility 72.8% (fraction of booksize)
- Hit rate: 27.5% positive days
- Tail shape: skew -0.68, excess kurtosis +21.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.54, max 1.99, latest 1.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +49.12%; worst month: -36.29%
Positive months: 62%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.94
- Sideways: S=0.97
- Bear: S=-0.81

## Negated Direction
Best negated: `-rank(news_mins_7_5_pct_dn)` S=0.19, F=0.05, INFERIOR
Direction gap: -0.39 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_mins_7_5_pct_dn)`: S=-0.53, F=-0.21, T=170.5%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_7_5_pct_dn / close)`: S=-0.27, F=-0.08, T=168.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_7_5_pct_dn, 5))`: S=-0.58, F=-0.45, T=70.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_mins_7_5_pct_dn, 5))` | TOP3000 | 0.58 | 0.45 | 95.8% | 80% | bull-only |
| `rank(ts_delta(news_mins_7_5_pct_dn, 5))` | TOP1000 | 0.42 | 0.35 | 82.2% | 40% | mixed |
| `rank(news_mins_7_5_pct_dn)` | TOP3000 | 0.53 | 0.21 | 97.7% | 80% | mixed |
| `rank(news_mins_7_5_pct_dn)` | TOP500 | 0.45 | 0.20 | 92.6% | 60% | weak |

## Correlation Notes
Top correlates:
- news_mins_4_pct_dn: 0.121 (weakly positively correlated)
- news_mins_3_pct_dn: 0.107 (weakly positively correlated)
- fnd2_a_gwllimrml: 0.099 (weakly positively correlated)
- news_mins_20_pct_dn: 0.091 (weakly positively correlated)
- earnings_per_share_guidance_value: 0.091 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
