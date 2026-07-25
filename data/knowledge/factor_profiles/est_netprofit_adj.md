---
field: est_netprofit_adj
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.45
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.2449
ann_vol: 0.0875
hit_rate: 0.498
rolling_sharpe_min: -3.157
rolling_sharpe_max: 2.483
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: 0.08
---
# est_netprofit_adj (analyst4)

*Adjusted net income - Mean of estimations*

## Signal Profile
- `rank(est_netprofit_adj)`: S=0.26, F=0.13, T=1.1%, INFERIOR (TOP3000)
- `rank(est_netprofit_adj / close)`: S=0.45, F=0.25, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(est_netprofit_adj, 5))`: S=-0.08, F=-0.01, T=35.9%, INFERIOR (TOP3000)
- `-rank(est_netprofit_adj)`: S=-0.01, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_netprofit_adj, 5))`: S=0.53, F=0.18, T=36.4%, INFERIOR (TOP3000)
- `ts_zscore(est_netprofit_adj, 22)`: S=0.14, F=0.02, T=33.9%, INFERIOR (TOP3000)
- `ts_mean(est_netprofit_adj, 10)`: S=0.04, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(est_netprofit_adj, 22))`: S=-0.06, F=-0.01, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * est_netprofit_adj)`: S=0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * est_netprofit_adj / close)`: S=0.00, F=0.00, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.45, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.23 (weak), ret=+1.0%
  - 2020: S=-2.28 (negative), ret=-14.2%
  - 2021: S=0.92 (moderate), ret=+10.4%
  - 2022: S=1.89 (strong), ret=+21.8%
  - 2023: S=0.02 (weak), ret=+0.1%

## Risk & Drawdown
- Max drawdown: 24.49% over 813 days (recovered)
- Annualized: return +3.9%, volatility 8.8% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.11, excess kurtosis +1.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.16, max 2.48, latest -0.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.62%; worst month: -3.98%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.22
- Sideways: S=0.86
- Bear: S=-3.52

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_netprofit_adj, 5))` S=0.53, F=0.18, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * est_netprofit_adj)`: S=0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * est_netprofit_adj / close)`: S=0.00, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_netprofit_adj, 5))`: S=0.53, F=0.18, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_netprofit_adj / close)` | TOP3000 | 0.45 | 0.25 | 24.5% | 80% | bull-only |
| `rank(est_netprofit_adj)` | TOP3000 | 0.25 | 0.13 | 39.9% | 60% | bull-only |
| `rank(est_netprofit_adj / close)` | TOP1000 | 0.15 | 0.06 | 29.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_netprofita_median: 0.993 (strongly positively correlated)
- anl4_netprofita_mean: 0.993 (strongly positively correlated)
- anl4_netprofita_high: 0.990 (strongly positively correlated)
- anl4_netprofita_low: 0.988 (strongly positively correlated)
- est_netprofit: 0.985 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
