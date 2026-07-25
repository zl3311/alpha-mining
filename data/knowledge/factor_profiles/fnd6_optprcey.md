---
field: fnd6_optprcey
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.78
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.1565
ann_vol: 0.1058
hit_rate: 0.4713
rolling_sharpe_min: -1.404
rolling_sharpe_max: 2.548
redundancy_cluster: 33
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.19
---
# fnd6_optprcey (fundamental6)

*Options Outstanding End of Year - Price*

## Signal Profile
- `rank(fnd6_optprcey)`: S=0.46, F=0.30, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_optprcey / close)`: S=0.78, F=0.63, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_optprcey, 5))`: S=0.06, F=0.01, T=36.6%, INFERIOR (TOP500)
- `-rank(fnd6_optprcey)`: S=-0.04, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optprcey, 5))`: S=0.59, F=0.29, T=33.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optprcey, 22)`: S=0.41, F=0.15, T=43.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optprcey, 10)`: S=0.23, F=0.10, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optprcey, 22))`: S=0.34, F=0.13, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcey)`: S=0.12, F=0.05, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcey / close)`: S=-0.35, F=-0.22, T=4.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.15 (negative), ret=-1.1%
  - 2020: S=0.91 (moderate), ret=+13.0%
  - 2021: S=1.78 (strong), ret=+17.6%
  - 2022: S=1.02 (moderate), ret=+8.9%
  - 2023: S=0.13 (weak), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 15.65% over 330 days (not yet recovered, ongoing at window end)
- Annualized: return +8.1%, volatility 10.6% (fraction of booksize)
- Hit rate: 47.1% positive days
- Tail shape: skew +0.96, excess kurtosis +4.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.40, max 2.55, latest 0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.00%; worst month: -4.57%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.62
- Sideways: S=-0.93
- Bear: S=1.33

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_optprcey, 5))` S=0.59, F=0.29, INFERIOR
Direction gap: -0.19 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_optprcey)`: S=0.12, F=0.05, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcey / close)`: S=-0.35, F=-0.22, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optprcey, 5))`: S=0.59, F=0.29, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optprcey / close)` | TOP3000 | 0.77 | 0.63 | 15.7% | 80% | all-weather |
| `rank(fnd6_optprcey / close)` | TOP500 | 0.59 | 0.45 | 19.3% | 80% | bull-only |
| `rank(fnd6_optprcey)` | TOP3000 | 0.45 | 0.30 | 37.9% | 60% | bull-only |
| `rank(fnd6_optprcey / close)` | TOP1000 | 0.41 | 0.26 | 19.1% | 80% | bull-only |
| `rank(fnd6_optprcey / close)` | TOP200 | 0.34 | 0.22 | 26.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_optprcca: 0.974 (strongly positively correlated)
- fnd6_optprcby: 0.967 (strongly positively correlated)
- fn_comp_options_out_weighted_avg_a: 0.966 (strongly positively correlated)
- fnd6_optprcwa: 0.965 (strongly positively correlated)
- fn_comp_options_exercisable_weighted_avg_a: 0.954 (strongly positively correlated)

Redundancy cluster #33: 12 similar fields, mean |rho| 0.787 (representative: anl4_afv4_eps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
