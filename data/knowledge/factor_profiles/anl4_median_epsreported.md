---
field: anl4_median_epsreported
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.79
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1756
ann_vol: 0.0993
hit_rate: 0.5069
rolling_sharpe_min: -1.77
rolling_sharpe_max: 2.981
redundancy_cluster: 13
negated_best_sharpe: 0.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.54
---
# anl4_median_epsreported (analyst4)

*GAAP Earnings per share - median of estimations*

## Signal Profile
- `rank(anl4_median_epsreported)`: S=0.36, F=0.21, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_median_epsreported / close)`: S=0.79, F=0.62, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_median_epsreported, 5))`: S=0.06, F=0.01, T=36.7%, INFERIOR (TOP1000)
- `-rank(anl4_median_epsreported)`: S=-0.22, F=-0.10, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_median_epsreported, 5))`: S=0.25, F=0.04, T=36.4%, INFERIOR (TOP3000)
- `ts_zscore(anl4_median_epsreported, 22)`: S=-0.03, F=0.00, T=34.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_median_epsreported, 10)`: S=0.00, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_median_epsreported, 22))`: S=-0.03, F=0.00, T=14.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_median_epsreported)`: S=-0.36, F=-0.21, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_median_epsreported / close)`: S=-0.79, F=-0.62, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.00 (negative), ret=-0.0%
  - 2020: S=-1.33 (negative), ret=-9.6%
  - 2021: S=1.88 (strong), ret=+21.2%
  - 2022: S=2.10 (strong), ret=+29.2%
  - 2023: S=-0.35 (negative), ret=-3.2%

## Risk & Drawdown
- Max drawdown: 17.56% over 546 days (recovered)
- Annualized: return +7.7%, volatility 9.9% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.02, excess kurtosis +1.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.77, max 2.98, latest -0.53

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.56%; worst month: -4.93%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.52
- Sideways: S=0.28
- Bear: S=-2.19

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_median_epsreported, 5))` S=0.25, F=0.04, INFERIOR
Direction gap: -0.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_median_epsreported)`: S=-0.36, F=-0.21, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_median_epsreported / close)`: S=-0.79, F=-0.62, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_median_epsreported, 5))`: S=0.25, F=0.04, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_median_epsreported / close)` | TOP3000 | 0.77 | 0.62 | 17.6% | 40% | bull-only |
| `rank(anl4_median_epsreported)` | TOP3000 | 0.35 | 0.21 | 39.4% | 60% | bull-only |
| `rank(anl4_median_epsreported / close)` | TOP1000 | 0.30 | 0.18 | 23.5% | 60% | bull-only |
| `rank(anl4_median_epsreported)` | TOP1000 | 0.21 | 0.10 | 36.6% | 60% | bull-only |
| `rank(anl4_median_epsreported)` | TOP500 | 0.10 | 0.03 | 35.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_epsr_mean: 1.000 (strongly positively correlated)
- anl4_epsr_high: 0.992 (strongly positively correlated)
- est_epsr: 0.992 (strongly positively correlated)
- anl4_epsr_low: 0.989 (strongly positively correlated)
- anl4_qfd1_az_wol_spe: 0.968 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
