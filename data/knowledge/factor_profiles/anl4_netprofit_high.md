---
field: anl4_netprofit_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.67
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.2192
ann_vol: 0.0872
hit_rate: 0.4939
rolling_sharpe_min: -2.797
rolling_sharpe_max: 2.8
redundancy_cluster: 13
negated_best_sharpe: 0.54
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.13
---
# anl4_netprofit_high (analyst4)

*Net Profit - The highest estimation*

## Signal Profile
- `rank(anl4_netprofit_high)`: S=0.42, F=0.27, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_netprofit_high / close)`: S=0.67, F=0.46, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netprofit_high, 5))`: S=0.15, F=0.02, T=36.9%, INFERIOR (TOP1000)
- `-rank(anl4_netprofit_high)`: S=-0.17, F=-0.07, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofit_high, 5))`: S=0.54, F=0.21, T=35.6%, INFERIOR (TOP3000)
- `ts_zscore(anl4_netprofit_high, 22)`: S=-0.06, F=-0.01, T=35.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_netprofit_high, 10)`: S=0.14, F=0.05, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netprofit_high, 22))`: S=0.06, F=0.01, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_high)`: S=0.03, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_high / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/2P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.66, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.06 (negative), ret=-0.2%
  - 2020: S=-2.03 (negative), ret=-12.2%
  - 2021: S=1.49 (moderate), ret=+16.6%
  - 2022: S=2.06 (strong), ret=+23.9%
  - 2023: S=0.02 (weak), ret=+0.1%

## Risk & Drawdown
- Max drawdown: 21.92% over 782 days (recovered)
- Annualized: return +5.8%, volatility 8.7% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.06, excess kurtosis +1.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.80, max 2.80, latest -0.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.72%; worst month: -4.59%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.44
- Sideways: S=0.86
- Bear: S=-3.09

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netprofit_high, 5))` S=0.54, F=0.21, INFERIOR
Direction gap: -0.13 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_netprofit_high)`: S=0.03, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_high / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofit_high, 5))`: S=0.54, F=0.21, T=35.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netprofit_high / close)` | TOP3000 | 0.66 | 0.46 | 21.9% | 60% | bull-only |
| `rank(anl4_netprofit_high)` | TOP3000 | 0.42 | 0.27 | 37.4% | 60% | bull-only |
| `rank(anl4_netprofit_high / close)` | TOP1000 | 0.24 | 0.11 | 28.8% | 60% | bull-only |
| `rank(anl4_netprofit_high / close)` | TOP500 | 0.19 | 0.09 | 37.9% | 60% | bull-only |
| `rank(anl4_netprofit_high)` | TOP1000 | 0.17 | 0.07 | 43.1% | 60% | bull-only |
| `rank(anl4_netprofit_high)` | TOP500 | 0.16 | 0.07 | 49.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ptp_high: 0.994 (strongly positively correlated)
- anl4_netprofit_median: 0.993 (strongly positively correlated)
- anl4_netprofit_mean: 0.992 (strongly positively correlated)
- est_netprofit: 0.992 (strongly positively correlated)
- est_ptp: 0.989 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
