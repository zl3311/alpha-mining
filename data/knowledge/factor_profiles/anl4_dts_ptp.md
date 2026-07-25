---
field: anl4_dts_ptp
dataset: analyst4
best_template: rank_level
best_sharpe: 0.77
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1432
ann_vol: 0.0602
hit_rate: 0.5296
rolling_sharpe_min: -1.638
rolling_sharpe_max: 2.621
redundancy_cluster: 32
negated_best_sharpe: 0.6
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.17
---
# anl4_dts_ptp (analyst4)

*Pretax income - std of estimations*

## Signal Profile
- `rank(anl4_dts_ptp)`: S=0.77, F=0.47, T=4.5%, INFERIOR (TOP3000)
- `rank(anl4_dts_ptp / close)`: S=0.28, F=0.11, T=4.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_dts_ptp, 5))`: S=0.39, F=0.09, T=39.0%, INFERIOR (TOP1000)
- `-rank(anl4_dts_ptp)`: S=-0.38, F=-0.18, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_dts_ptp, 5))`: S=0.60, F=0.20, T=38.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_dts_ptp, 22)`: S=0.20, F=0.04, T=33.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_dts_ptp, 10)`: S=0.46, F=0.31, T=4.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_dts_ptp, 22))`: S=0.43, F=0.14, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_dts_ptp)`: S=-0.42, F=-0.22, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_dts_ptp / close)`: S=-0.27, F=-0.11, T=5.9%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.77, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.07 (moderate), ret=+4.5%
  - 2020: S=-0.33 (negative), ret=-1.9%
  - 2021: S=0.70 (moderate), ret=+5.7%
  - 2022: S=1.68 (strong), ret=+9.5%
  - 2023: S=1.04 (moderate), ret=+5.0%

## Risk & Drawdown
- Max drawdown: 14.32% over 405 days (recovered)
- Annualized: return +4.6%, volatility 6.0% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.06, excess kurtosis +0.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.64, max 2.62, latest 0.89

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.90%; worst month: -3.24%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.52
- Sideways: S=1.30
- Bear: S=-1.62

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_dts_ptp, 5))` S=0.60, F=0.20, INFERIOR
Direction gap: -0.17 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_dts_ptp)`: S=-0.42, F=-0.22, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_dts_ptp / close)`: S=-0.27, F=-0.11, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_dts_ptp, 5))`: S=0.60, F=0.20, T=38.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_dts_ptp)` | TOP3000 | 0.77 | 0.47 | 14.3% | 80% | bull-only |
| `rank(anl4_dts_ptp)` | TOP500 | 0.41 | 0.22 | 18.4% | 60% | bull-only |
| `rank(anl4_dts_ptp)` | TOP1000 | 0.37 | 0.18 | 14.2% | 80% | bull-only |
| `rank(anl4_dts_ptp / close)` | TOP3000 | 0.27 | 0.11 | 13.1% | 60% | mixed |
| `rank(anl4_dts_ptp / close)` | TOP500 | 0.25 | 0.11 | 10.0% | 80% | bull-only |
| `rank(ts_delta(anl4_dts_ptp, 5))` | TOP1000 | 0.39 | 0.09 | 9.2% | 40% | bull-only |
| `rank(anl4_dts_ptp / close)` | TOP1000 | 0.18 | 0.06 | 12.8% | 80% | mixed |
| `rank(anl4_dts_ptp / close)` | TOP200 | 0.12 | 0.03 | 21.9% | 60% | bull-only |
| `rank(ts_delta(anl4_dts_ptp, 5))` | TOP3000 | 0.21 | 0.03 | 9.8% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_ebit_std: 0.953 (strongly positively correlated)
- anl4_netprofit_std: 0.949 (strongly positively correlated)
- sales_estimate_stddev_quarterly: 0.864 (strongly positively correlated)
- sales_estimate_standard_deviation: 0.864 (strongly positively correlated)
- cash: 0.828 (strongly positively correlated)

Redundancy cluster #32: 9 similar fields, mean |rho| 0.765 (representative: fnd6_fopox). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
