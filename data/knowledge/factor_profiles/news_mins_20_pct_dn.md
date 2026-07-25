---
field: news_mins_20_pct_dn
dataset: news12
best_template: neg_rank_value_norm
best_sharpe: 0.58
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.0753
ann_vol: 0.0874
hit_rate: 0.0024
rolling_sharpe_min: -1.0
rolling_sharpe_max: 1.094
negated_best_sharpe: 0.58
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.53
n_negated_sims: 4
direction_gap: 0.0
---
# news_mins_20_pct_dn (news12)

*Number of minutes that elapsed before price went down 20 percentage points*

## Signal Profile
- `rank(news_mins_20_pct_dn)`: S=0.06, F=0.02, T=80.5%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_20_pct_dn, 5))`: S=0.58, F=0.41, T=0.6%, INFERIOR (TOP3000)
- `-rank(news_mins_20_pct_dn)`: S=0.28, F=0.24, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_20_pct_dn, 5))`: S=-0.58, F=-0.41, T=0.6%, INFERIOR (TOP3000)
- `ts_zscore(news_mins_20_pct_dn, 22)`: S=0.34, F=0.32, T=2.4%, INFERIOR (TOP3000)
- `ts_mean(news_mins_20_pct_dn, 10)`: S=-0.41, F=-0.59, T=30.8%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_20_pct_dn, 22))`: S=0.13, F=0.08, T=9.1%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_20_pct_dn)`: S=-0.06, F=-0.02, T=80.5%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_20_pct_dn / close)`: S=0.58, F=0.53, T=79.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 7F/13P
- LOW_FITNESS: 19F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/10P
- LOW_TURNOVER: 3F/17P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.48, Consistency 20% positive years (1/5)
Yearly breakdown:
  - 2019: S=0.00 (negative), ret=+0.0%
  - 2020: S=-1.04 (negative), ret=-0.4%
  - 2021: S=0.00 (negative), ret=+0.0%
  - 2022: S=0.00 (negative), ret=+0.0%
  - 2023: S=1.10 (moderate), ret=+21.2%

## Risk & Drawdown
- Max drawdown: 7.53% over 1685 days (recovered)
- Annualized: return +4.2%, volatility 8.7% (fraction of booksize)
- Hit rate: 0.2% positive days
- Tail shape: skew +18.59, excess kurtosis +535.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.00, max 1.09, latest 1.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +23.73%; worst month: -2.57%
Positive months: 33%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.08
- Sideways: S=-0.23
- Bear: S=-0.79

## Negated Direction
Best negated: `rank(-1 * news_mins_20_pct_dn / close)` S=0.58, F=0.53, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_mins_20_pct_dn)`: S=-0.06, F=-0.02, T=80.5%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_20_pct_dn / close)`: S=0.58, F=0.53, T=79.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_20_pct_dn, 5))`: S=-0.58, F=-0.41, T=0.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_mins_20_pct_dn, 5))` | TOP3000 | 0.48 | 0.41 | 7.5% | 20% | bull-only |
| `rank(news_mins_20_pct_dn)` | TOP3000 | 0.06 | 0.02 | 276.7% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_bvps_number: 0.134 (weakly positively correlated)
- rp_css_credit_ratings: -0.128 (weakly negatively correlated)
- news_mins_10_chg: 0.126 (weakly positively correlated)
- fnd6_txdbclq: 0.098 (weakly positively correlated)
- fnd2_itxreclstatelocalitxes: 0.091 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
