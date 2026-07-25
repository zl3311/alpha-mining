---
field: anl4_bvps_mean
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.6
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.1931
ann_vol: 0.0899
hit_rate: 0.481
rolling_sharpe_min: -2.349
rolling_sharpe_max: 2.469
redundancy_cluster: 12
negated_best_sharpe: 0.6
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.45
n_negated_sims: 10
direction_gap: -0.01
---
# anl4_bvps_mean (analyst4)

*Book value per share - average of estimations*

## Signal Profile
- `rank(anl4_bvps_mean)`: S=0.25, F=0.10, T=1.6%, INFERIOR (TOP1000)
- `rank(anl4_bvps_mean / close)`: S=0.61, F=0.40, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_bvps_mean, 5))`: S=0.27, F=0.05, T=36.1%, INFERIOR (TOP3000)
- `-rank(anl4_bvps_mean)`: S=-0.25, F=-0.10, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_bvps_mean, 5))`: S=0.22, F=0.06, T=33.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_bvps_mean, 22)`: S=0.45, F=0.16, T=33.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_bvps_mean, 10)`: S=-0.46, F=-0.30, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_bvps_mean, 22))`: S=-0.03, F=0.00, T=14.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_mean)`: S=-0.04, F=-0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_mean / close)`: S=0.60, F=0.45, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.60, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.90 (negative), ret=-6.1%
  - 2020: S=0.35 (weak), ret=+4.8%
  - 2021: S=1.43 (moderate), ret=+11.2%
  - 2022: S=2.35 (strong), ret=+15.4%
  - 2023: S=0.20 (weak), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 19.31% over 747 days (recovered)
- Annualized: return +5.4%, volatility 9.0% (fraction of booksize)
- Hit rate: 48.1% positive days
- Tail shape: skew +0.92, excess kurtosis +4.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.35, max 2.47, latest 0.32

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.52%; worst month: -5.08%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.61
- Sideways: S=-0.79
- Bear: S=-0.03

## Negated Direction
Best negated: `rank(-1 * anl4_bvps_mean / close)` S=0.60, F=0.45, INFERIOR
Direction gap: -0.01 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_bvps_mean)`: S=-0.04, F=-0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_mean / close)`: S=0.60, F=0.45, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_bvps_mean, 5))`: S=0.22, F=0.06, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_bvps_mean / close)` | TOP3000 | 0.60 | 0.40 | 19.3% | 80% | mixed |
| `rank(anl4_bvps_mean / close)` | TOP1000 | 0.30 | 0.15 | 20.0% | 80% | mixed |
| `rank(anl4_bvps_mean)` | TOP1000 | 0.23 | 0.10 | 18.6% | 80% | bull-only |
| `rank(anl4_bvps_mean)` | TOP3000 | 0.16 | 0.05 | 25.5% | 60% | bull-only |
| `rank(ts_delta(anl4_bvps_mean, 5))` | TOP3000 | 0.28 | 0.05 | 8.2% | 60% | weak |
| `rank(ts_delta(anl4_bvps_mean, 5))` | TOP500 | 0.17 | 0.04 | 23.9% | 60% | mixed |
| `rank(ts_delta(anl4_bvps_mean, 5))` | TOP1000 | 0.19 | 0.04 | 14.4% | 60% | all-weather |

## Correlation Notes
Top correlates:
- anl4_bvps_median: 1.000 (strongly positively correlated)
- anl4_bvps_high: 1.000 (strongly positively correlated)
- anl4_bvps_low: 0.999 (strongly positively correlated)
- est_bookvalue_ps: 0.912 (strongly positively correlated)
- book_value_per_share_reported_value: 0.894 (strongly positively correlated)

Redundancy cluster #12: 12 similar fields, mean |rho| 0.749 (representative: fnd6_dlto). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
