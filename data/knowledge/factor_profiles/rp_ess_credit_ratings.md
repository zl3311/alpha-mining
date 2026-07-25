---
field: rp_ess_credit_ratings
dataset: news18
best_template: rank_delta
best_sharpe: 0.49
best_fitness: 0.34
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2494
ann_vol: 0.4128
hit_rate: 0.5085
rolling_sharpe_min: -1.61
rolling_sharpe_max: 2.518
negated_best_sharpe: -0.25
negated_best_template: neg_rank_level
negated_best_fitness: -0.05
n_negated_sims: 4
direction_gap: -0.74
---
# rp_ess_credit_ratings (news18)

*Event sentiment score of credit ratings news*

## Signal Profile
- `rank(rp_ess_credit_ratings)`: S=0.42, F=0.11, T=142.6%, INFERIOR (TOP1000)
- `rank(ts_delta(rp_ess_credit_ratings, 5))`: S=0.49, F=0.34, T=42.9%, INFERIOR (TOP500)
- `-rank(rp_ess_credit_ratings)`: S=-0.42, F=-0.11, T=142.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_credit_ratings, 5))`: S=-0.41, F=-0.19, T=58.0%, INFERIOR (TOP3000)
- `ts_zscore(rp_ess_credit_ratings, 22)`: S=0.07, F=0.01, T=92.7%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_credit_ratings, 10)`: S=0.56, F=0.24, T=38.0%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_credit_ratings, 22))`: S=-0.11, F=-0.02, T=115.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_credit_ratings)`: S=-0.25, F=-0.05, T=166.3%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_credit_ratings / close)`: S=-0.47, F=-0.13, T=168.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 11F/9P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.49, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.74 (negative), ret=-8.8%
  - 2020: S=-0.31 (negative), ret=-4.5%
  - 2021: S=0.82 (moderate), ret=+8.7%
  - 2022: S=1.03 (moderate), ret=+15.2%
  - 2023: S=1.01 (moderate), ret=+87.9%

## Risk & Drawdown
- Max drawdown: 24.94% over 1378 days (recovered)
- Annualized: return +20.1%, volatility 41.3% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +29.45, excess kurtosis +976.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.61, max 2.52, latest 1.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +94.88%; worst month: -8.81%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.89
- Sideways: S=0.09
- Bear: S=-0.11

## Negated Direction
Best negated: `rank(-1 * rp_ess_credit_ratings)` S=-0.25, F=-0.05, INFERIOR
Direction gap: -0.74 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_ess_credit_ratings)`: S=-0.25, F=-0.05, T=166.3%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_credit_ratings / close)`: S=-0.47, F=-0.13, T=168.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_credit_ratings, 5))`: S=-0.41, F=-0.19, T=58.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_ess_credit_ratings, 5))` | TOP500 | 0.49 | 0.34 | 24.9% | 60% | mixed |
| `rank(ts_delta(rp_ess_credit_ratings, 5))` | TOP1000 | 0.50 | 0.30 | 34.6% | 80% | mixed |
| `rank(ts_delta(rp_ess_credit_ratings, 5))` | TOP3000 | 0.41 | 0.19 | 29.5% | 60% | mixed |
| `rank(rp_ess_credit_ratings)` | TOP1000 | 0.41 | 0.11 | 48.6% | 80% | bull-only |
| `rank(rp_ess_credit_ratings)` | TOP500 | 0.23 | 0.06 | 41.2% | 80% | bull-only |
| `rank(rp_ess_credit_ratings)` | TOP3000 | 0.23 | 0.05 | 48.4% | 60% | weak |

## Correlation Notes
Top correlates:
- rp_css_credit_ratings: 0.497 (moderately positively correlated)
- est_dividend_ps: 0.302 (weakly positively correlated)
- anl4_qfv4_div_mean: 0.298 (weakly positively correlated)
- anl4_rd_exp_flag: 0.225 (weakly positively correlated)
- earnings_per_share_standard_deviation: -0.198 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
