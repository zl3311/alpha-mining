---
field: rp_css_ratings
dataset: news18
best_template: rank_delta
best_sharpe: 0.45
best_fitness: 0.06
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1022
ann_vol: 0.0609
hit_rate: 0.5085
rolling_sharpe_min: -1.278
rolling_sharpe_max: 2.415
negated_best_sharpe: 0.23
negated_best_template: neg_rank
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.22
---
# rp_css_ratings (news18)

*Composite sentiment score of analyst ratings-related news*

## Signal Profile
- `rank(rp_css_ratings)`: S=0.29, F=0.04, T=120.8%, INFERIOR (TOP200)
- `rank(ts_delta(rp_css_ratings, 5))`: S=0.45, F=0.06, T=167.9%, INFERIOR (TOP3000)
- `-rank(rp_css_ratings)`: S=0.23, F=0.02, T=131.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_ratings, 5))`: S=-0.45, F=-0.06, T=167.9%, INFERIOR (TOP3000)
- `-ts_zscore(rp_css_ratings, 63)`: S=0.21, F=0.02, T=136.4%, INFERIOR (TOP3000)
- `ts_mean(rp_css_ratings, 10)`: S=-0.37, F=-0.12, T=19.3%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_ratings, 22))`: S=0.20, F=0.02, T=140.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_ratings)`: S=-0.13, F=-0.01, T=144.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_ratings / close)`: S=-0.31, F=-0.03, T=145.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/14P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.46, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.55 (moderate), ret=+4.1%
  - 2020: S=0.01 (weak), ret=+0.0%
  - 2021: S=1.15 (moderate), ret=+8.8%
  - 2022: S=0.29 (weak), ret=+1.6%
  - 2023: S=-0.18 (negative), ret=-0.7%

## Risk & Drawdown
- Max drawdown: 10.22% over 799 days (not yet recovered, ongoing at window end)
- Annualized: return +2.8%, volatility 6.1% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.62, excess kurtosis +4.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.28, max 2.42, latest -0.22

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.02%; worst month: -3.37%
Positive months: 48%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.57
- Sideways: S=0.68
- Bear: S=0.12

## Negated Direction
Best negated: `-rank(rp_css_ratings)` S=0.23, F=0.02, INFERIOR
Direction gap: -0.22 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_css_ratings)`: S=-0.13, F=-0.01, T=144.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_ratings / close)`: S=-0.31, F=-0.03, T=145.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_ratings, 5))`: S=-0.45, F=-0.06, T=167.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_css_ratings, 5))` | TOP3000 | 0.46 | 0.06 | 10.2% | 80% | mixed |
| `rank(rp_css_ratings)` | TOP200 | 0.31 | 0.04 | 25.8% | 40% | mixed |
| `rank(rp_css_ratings)` | TOP500 | 0.27 | 0.03 | 10.1% | 40% | mixed |

## Correlation Notes
Top correlates:
- rp_ess_ratings: 0.359 (weakly positively correlated)
- snt_social_volume: 0.108 (weakly positively correlated)
- fnd6_newa2v1300_txach: -0.097 (weakly negatively correlated)
- fnd6_mfma2_txach: -0.097 (weakly negatively correlated)
- fnd6_txndbr: 0.093 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
