---
field: fnd6_optprcgr
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.51
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.2286
ann_vol: 0.1379
hit_rate: 0.4704
rolling_sharpe_min: -1.0
rolling_sharpe_max: 2.377
redundancy_cluster: 33
negated_best_sharpe: 0.41
negated_best_template: neg_rank_level
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.1
---
# fnd6_optprcgr (fundamental6)

*Options Granted - Price*

## Signal Profile
- `rank(fnd6_optprcgr)`: S=0.51, F=0.36, T=2.1%, INFERIOR (TOP3000)
- `rank(fnd6_optprcgr / close)`: S=0.51, F=0.38, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_optprcgr, 5))`: S=0.25, F=0.06, T=37.1%, INFERIOR (TOP3000)
- `-rank(fnd6_optprcgr)`: S=0.03, F=0.00, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optprcgr, 5))`: S=0.35, F=0.14, T=33.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optprcgr, 22)`: S=-0.01, F=0.00, T=40.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optprcgr, 10)`: S=0.04, F=0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optprcgr, 22))`: S=0.39, F=0.16, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcgr)`: S=0.41, F=0.28, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcgr / close)`: S=0.31, F=0.21, T=5.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 7F/25P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.50, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.36 (weak), ret=+3.1%
  - 2020: S=0.69 (moderate), ret=+10.5%
  - 2021: S=1.93 (strong), ret=+21.6%
  - 2022: S=-0.26 (negative), ret=-4.4%
  - 2023: S=0.21 (weak), ret=+3.0%

## Risk & Drawdown
- Max drawdown: 22.86% over 504 days (not yet recovered, ongoing at window end)
- Annualized: return +6.9%, volatility 13.8% (fraction of booksize)
- Hit rate: 47.0% positive days
- Tail shape: skew +0.87, excess kurtosis +3.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.00, max 2.38, latest 0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +9.96%; worst month: -8.18%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.88
- Sideways: S=-0.89
- Bear: S=1.25

## Negated Direction
Best negated: `rank(-1 * fnd6_optprcgr)` S=0.41, F=0.28, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_optprcgr)`: S=0.41, F=0.28, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcgr / close)`: S=0.31, F=0.21, T=5.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optprcgr, 5))`: S=0.35, F=0.14, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optprcgr / close)` | TOP3000 | 0.50 | 0.38 | 22.9% | 80% | all-weather |
| `rank(fnd6_optprcgr)` | TOP3000 | 0.51 | 0.36 | 46.6% | 80% | bull-only |
| `rank(fnd6_optprcgr / close)` | TOP500 | 0.27 | 0.15 | 33.9% | 80% | bull-only |
| `rank(ts_delta(fnd6_optprcgr, 5))` | TOP3000 | 0.23 | 0.06 | 29.4% | 80% | bull-only |
| `rank(ts_delta(fnd6_optprcgr, 5))` | TOP500 | 0.13 | 0.02 | 23.1% | 60% | mixed |
| `rank(ts_delta(fnd6_optprcgr, 5))` | TOP1000 | 0.13 | 0.02 | 15.5% | 60% | bull-only |
| `rank(fnd6_optprcgr / close)` | TOP1000 | 0.06 | 0.02 | 28.8% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_oth_comp_fair_value_a: 0.922 (strongly positively correlated)
- fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a: 0.913 (strongly positively correlated)
- fn_oth_comp_forfeitures_fair_value_a: 0.895 (strongly positively correlated)
- fnd6_optprcey: 0.858 (strongly positively correlated)
- fn_comp_options_out_weighted_avg_a: 0.851 (strongly positively correlated)

Redundancy cluster #33: 12 similar fields, mean |rho| 0.787 (representative: anl4_afv4_eps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
