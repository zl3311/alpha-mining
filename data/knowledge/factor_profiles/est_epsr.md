---
field: est_epsr
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.73
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1671
ann_vol: 0.0935
hit_rate: 0.5053
rolling_sharpe_min: -1.663
rolling_sharpe_max: 2.852
redundancy_cluster: 13
negated_best_sharpe: 0.34
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.39
---
# est_epsr (analyst4)

*GAAP Earnings per share - mean of estimations*

## Signal Profile
- `rank(est_epsr)`: S=0.30, F=0.16, T=1.1%, INFERIOR (TOP3000)
- `rank(est_epsr / close)`: S=0.73, F=0.54, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(est_epsr, 5))`: S=-0.08, F=-0.01, T=36.4%, INFERIOR (TOP1000)
- `-rank(est_epsr)`: S=-0.15, F=-0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_epsr, 5))`: S=0.34, F=0.06, T=36.0%, INFERIOR (TOP3000)
- `ts_zscore(est_epsr, 22)`: S=-0.11, F=-0.02, T=33.6%, INFERIOR (TOP3000)
- `ts_mean(est_epsr, 10)`: S=-0.11, F=-0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(est_epsr, 22))`: S=-0.02, F=0.00, T=14.2%, INFERIOR (TOP3000)
- `rank(-1 * est_epsr)`: S=-0.30, F=-0.16, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * est_epsr / close)`: S=-0.73, F=-0.54, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.72, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.05 (negative), ret=-0.2%
  - 2020: S=-1.28 (negative), ret=-9.4%
  - 2021: S=1.78 (strong), ret=+19.1%
  - 2022: S=1.99 (strong), ret=+25.4%
  - 2023: S=-0.23 (negative), ret=-1.9%

## Risk & Drawdown
- Max drawdown: 16.71% over 550 days (recovered)
- Annualized: return +6.7%, volatility 9.3% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.04, excess kurtosis +1.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.66, max 2.85, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.01%; worst month: -4.68%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.52
- Sideways: S=0.17
- Bear: S=-2.18

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_epsr, 5))` S=0.34, F=0.06, INFERIOR
Direction gap: -0.39 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * est_epsr)`: S=-0.30, F=-0.16, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * est_epsr / close)`: S=-0.73, F=-0.54, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_epsr, 5))`: S=0.34, F=0.06, T=36.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_epsr / close)` | TOP3000 | 0.72 | 0.54 | 16.7% | 40% | bull-only |
| `rank(est_epsr)` | TOP3000 | 0.29 | 0.16 | 39.8% | 60% | bull-only |
| `rank(est_epsr / close)` | TOP1000 | 0.25 | 0.13 | 23.9% | 60% | bull-only |
| `rank(est_epsr)` | TOP1000 | 0.13 | 0.06 | 37.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_epsr_mean: 0.992 (strongly positively correlated)
- anl4_median_epsreported: 0.992 (strongly positively correlated)
- anl4_epsr_high: 0.988 (strongly positively correlated)
- anl4_epsr_low: 0.979 (strongly positively correlated)
- anl4_qfd1_az_wol_spe: 0.976 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
