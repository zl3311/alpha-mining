---
field: anl4_netprofita_median
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.51
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.231
ann_vol: 0.0877
hit_rate: 0.4923
rolling_sharpe_min: -2.996
rolling_sharpe_max: 2.48
redundancy_cluster: 13
negated_best_sharpe: 0.33
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.18
---
# anl4_netprofita_median (analyst4)

*Adjusted net income - median of estimations*

## Signal Profile
- `rank(anl4_netprofita_median)`: S=0.28, F=0.14, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_netprofita_median / close)`: S=0.51, F=0.31, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netprofita_median, 5))`: S=0.12, F=0.01, T=36.3%, INFERIOR (TOP3000)
- `-rank(anl4_netprofita_median)`: S=-0.05, F=-0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofita_median, 5))`: S=0.33, F=0.07, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_netprofita_median, 22)`: S=0.23, F=0.05, T=34.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_netprofita_median, 10)`: S=0.07, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netprofita_median, 22))`: S=0.15, F=0.03, T=14.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_median)`: S=0.08, F=0.02, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_median / close)`: S=-0.02, F=0.00, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.51, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.27 (weak), ret=+1.2%
  - 2020: S=-2.23 (negative), ret=-13.6%
  - 2021: S=1.03 (moderate), ret=+11.3%
  - 2022: S=1.95 (strong), ret=+23.2%
  - 2023: S=-0.06 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 23.10% over 807 days (recovered)
- Annualized: return +4.4%, volatility 8.8% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew +0.08, excess kurtosis +1.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.00, max 2.48, latest -0.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.05%; worst month: -4.09%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.22
- Sideways: S=0.91
- Bear: S=-3.31

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netprofita_median, 5))` S=0.33, F=0.07, INFERIOR
Direction gap: -0.18 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_netprofita_median)`: S=0.08, F=0.02, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_median / close)`: S=-0.02, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofita_median, 5))`: S=0.33, F=0.07, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netprofita_median / close)` | TOP3000 | 0.51 | 0.31 | 23.1% | 60% | bull-only |
| `rank(anl4_netprofita_median)` | TOP3000 | 0.27 | 0.14 | 39.7% | 60% | bull-only |
| `rank(anl4_netprofita_median / close)` | TOP1000 | 0.18 | 0.07 | 29.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_netprofita_mean: 1.000 (strongly positively correlated)
- anl4_netprofita_high: 0.996 (strongly positively correlated)
- anl4_netprofita_low: 0.995 (strongly positively correlated)
- est_netprofit_adj: 0.993 (strongly positively correlated)
- anl4_netprofit_median: 0.982 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
