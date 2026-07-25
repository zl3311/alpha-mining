---
field: anl4_netprofit_std
dataset: analyst4
best_template: rank_level
best_sharpe: 0.77
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.108
ann_vol: 0.0541
hit_rate: 0.5377
rolling_sharpe_min: -1.254
rolling_sharpe_max: 2.687
redundancy_cluster: 32
negated_best_sharpe: 0.37
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.4
---
# anl4_netprofit_std (analyst4)

*Net profit - standard deviation of estimations*

## Signal Profile
- `rank(anl4_netprofit_std)`: S=0.77, F=0.44, T=4.5%, INFERIOR (TOP3000)
- `rank(anl4_netprofit_std / close)`: S=0.36, F=0.17, T=5.9%, INFERIOR (TOP500)
- `rank(ts_delta(anl4_netprofit_std, 5))`: S=0.57, F=0.15, T=39.1%, INFERIOR (TOP1000)
- `-rank(anl4_netprofit_std)`: S=-0.50, F=-0.26, T=5.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofit_std, 5))`: S=0.37, F=0.09, T=39.0%, INFERIOR (TOP3000)
- `ts_zscore(anl4_netprofit_std, 22)`: S=0.52, F=0.15, T=33.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_netprofit_std, 10)`: S=0.58, F=0.43, T=4.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netprofit_std, 22))`: S=0.58, F=0.21, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_std)`: S=-0.55, F=-0.32, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_std / close)`: S=-0.36, F=-0.17, T=5.9%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.76, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.81 (moderate), ret=+3.2%
  - 2020: S=-0.35 (negative), ret=-1.9%
  - 2021: S=1.10 (moderate), ret=+7.5%
  - 2022: S=1.50 (strong), ret=+7.9%
  - 2023: S=0.79 (moderate), ret=+3.6%

## Risk & Drawdown
- Max drawdown: 10.80% over 388 days (recovered)
- Annualized: return +4.1%, volatility 5.4% (fraction of booksize)
- Hit rate: 53.8% positive days
- Tail shape: skew -0.12, excess kurtosis +0.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.25, max 2.69, latest 0.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.81%; worst month: -2.93%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.51
- Sideways: S=1.21
- Bear: S=-1.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netprofit_std, 5))` S=0.37, F=0.09, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_netprofit_std)`: S=-0.55, F=-0.32, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_std / close)`: S=-0.36, F=-0.17, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofit_std, 5))`: S=0.37, F=0.09, T=39.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netprofit_std)` | TOP3000 | 0.76 | 0.44 | 10.8% | 80% | bull-only |
| `rank(anl4_netprofit_std)` | TOP500 | 0.54 | 0.32 | 13.3% | 60% | bull-only |
| `rank(anl4_netprofit_std)` | TOP1000 | 0.50 | 0.26 | 11.9% | 80% | bull-only |
| `rank(anl4_netprofit_std / close)` | TOP500 | 0.36 | 0.17 | 11.1% | 100% | bull-only |
| `rank(ts_delta(anl4_netprofit_std, 5))` | TOP1000 | 0.55 | 0.15 | 7.6% | 60% | mixed |
| `rank(anl4_netprofit_std / close)` | TOP3000 | 0.33 | 0.14 | 12.1% | 60% | mixed |
| `rank(anl4_netprofit_std / close)` | TOP1000 | 0.24 | 0.10 | 12.7% | 80% | mixed |
| `rank(anl4_netprofit_std)` | TOP200 | 0.10 | 0.03 | 31.1% | 80% | bull-only |

## Correlation Notes
Top correlates:
- anl4_dts_ptp: 0.949 (strongly positively correlated)
- anl4_ebit_std: 0.933 (strongly positively correlated)
- sales_estimate_stddev_quarterly: 0.827 (strongly positively correlated)
- sales_estimate_standard_deviation: 0.827 (strongly positively correlated)
- sales_estimate_dispersion: 0.795 (strongly positively correlated)

Redundancy cluster #32: 9 similar fields, mean |rho| 0.765 (representative: fnd6_fopox). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
