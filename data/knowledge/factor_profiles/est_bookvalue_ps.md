---
field: est_bookvalue_ps
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.66
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.1315
ann_vol: 0.0851
hit_rate: 0.4818
rolling_sharpe_min: -1.745
rolling_sharpe_max: 2.725
redundancy_cluster: 29
negated_best_sharpe: 0.17
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.49
---
# est_bookvalue_ps (analyst4)

*Book value per share - average of estimations*

## Signal Profile
- `rank(est_bookvalue_ps)`: S=0.14, F=0.04, T=1.2%, INFERIOR (TOP1000)
- `rank(est_bookvalue_ps / close)`: S=0.66, F=0.44, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(est_bookvalue_ps, 5))`: S=0.18, F=0.03, T=36.8%, INFERIOR (TOP1000)
- `-rank(est_bookvalue_ps)`: S=-0.14, F=-0.04, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_bookvalue_ps, 5))`: S=0.04, F=0.00, T=33.5%, INFERIOR (TOP3000)
- `ts_zscore(est_bookvalue_ps, 22)`: S=0.49, F=0.18, T=34.0%, INFERIOR (TOP3000)
- `ts_mean(est_bookvalue_ps, 10)`: S=-0.37, F=-0.21, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(est_bookvalue_ps, 22))`: S=0.00, F=0.00, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * est_bookvalue_ps)`: S=0.09, F=0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * est_bookvalue_ps / close)`: S=0.17, F=0.06, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.65, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.40 (negative), ret=-2.5%
  - 2020: S=0.90 (moderate), ret=+11.4%
  - 2021: S=1.54 (strong), ret=+11.4%
  - 2022: S=1.17 (moderate), ret=+7.3%
  - 2023: S=-0.08 (negative), ret=-0.6%

## Risk & Drawdown
- Max drawdown: 13.15% over 512 days (recovered)
- Annualized: return +5.5%, volatility 8.5% (fraction of booksize)
- Hit rate: 48.2% positive days
- Tail shape: skew +0.90, excess kurtosis +4.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.75, max 2.73, latest 0.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.74%; worst month: -4.53%
Positive months: 52%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.73
- Sideways: S=-0.83
- Bear: S=0.92

## Negated Direction
Best negated: `rank(-1 * est_bookvalue_ps / close)` S=0.17, F=0.06, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * est_bookvalue_ps)`: S=0.09, F=0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * est_bookvalue_ps / close)`: S=0.17, F=0.06, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_bookvalue_ps, 5))`: S=0.04, F=0.00, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_bookvalue_ps / close)` | TOP3000 | 0.65 | 0.44 | 13.2% | 60% | all-weather |
| `rank(est_bookvalue_ps / close)` | TOP1000 | 0.47 | 0.27 | 16.4% | 80% | mixed |
| `rank(est_bookvalue_ps / close)` | TOP500 | 0.23 | 0.10 | 13.2% | 40% | mixed |
| `rank(est_bookvalue_ps)` | TOP1000 | 0.12 | 0.04 | 17.9% | 60% | bull-only |
| `rank(ts_delta(est_bookvalue_ps, 5))` | TOP1000 | 0.19 | 0.03 | 14.9% | 60% | all-weather |
| `rank(est_bookvalue_ps)` | TOP3000 | 0.10 | 0.03 | 24.1% | 60% | bull-only |
| `rank(ts_delta(est_bookvalue_ps, 5))` | TOP500 | 0.13 | 0.02 | 26.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_bvps_high: 0.914 (strongly positively correlated)
- anl4_bvps_median: 0.912 (strongly positively correlated)
- anl4_bvps_mean: 0.912 (strongly positively correlated)
- anl4_bvps_low: 0.910 (strongly positively correlated)
- fnd6_newa1v1300_bkvlps: 0.908 (strongly positively correlated)

Redundancy cluster #29: 5 similar fields, mean |rho| 0.883 (representative: anl4_tbvps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
