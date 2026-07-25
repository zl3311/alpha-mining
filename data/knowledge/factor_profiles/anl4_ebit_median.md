---
field: anl4_ebit_median
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.65
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2253
ann_vol: 0.093
hit_rate: 0.5045
rolling_sharpe_min: -2.524
rolling_sharpe_max: 2.667
redundancy_cluster: 13
negated_best_sharpe: 0.52
negated_best_template: rank_neg_delta
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.13
---
# anl4_ebit_median (analyst4)

*Earnings before interest and taxes - median of estimations*

## Signal Profile
- `rank(anl4_ebit_median)`: S=0.40, F=0.25, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_ebit_median / close)`: S=0.65, F=0.45, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ebit_median, 5))`: S=0.72, F=0.22, T=36.7%, INFERIOR (TOP1000)
- `-rank(anl4_ebit_median)`: S=-0.16, F=-0.07, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebit_median, 5))`: S=0.52, F=0.19, T=36.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ebit_median, 22)`: S=0.22, F=0.04, T=34.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebit_median, 10)`: S=0.02, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebit_median, 22))`: S=0.11, F=0.02, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_median)`: S=-0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_median / close)`: S=-0.04, F=-0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.65, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.07 (negative), ret=-0.3%
  - 2020: S=-1.80 (negative), ret=-12.3%
  - 2021: S=1.42 (moderate), ret=+16.8%
  - 2022: S=1.91 (strong), ret=+23.9%
  - 2023: S=0.20 (weak), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 22.53% over 782 days (recovered)
- Annualized: return +6.0%, volatility 9.3% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.05, excess kurtosis +1.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.52, max 2.67, latest -0.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.15%; worst month: -4.08%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.50
- Sideways: S=0.75
- Bear: S=-3.09

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ebit_median, 5))` S=0.52, F=0.19, INFERIOR
Direction gap: -0.13 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_ebit_median)`: S=-0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_median / close)`: S=-0.04, F=-0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebit_median, 5))`: S=0.52, F=0.19, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ebit_median / close)` | TOP3000 | 0.65 | 0.45 | 22.5% | 60% | bull-only |
| `rank(anl4_ebit_median)` | TOP3000 | 0.39 | 0.25 | 39.4% | 60% | bull-only |
| `rank(ts_delta(anl4_ebit_median, 5))` | TOP1000 | 0.74 | 0.22 | 8.4% | 80% | mixed |
| `rank(anl4_ebit_median / close)` | TOP1000 | 0.34 | 0.19 | 24.9% | 60% | bull-only |
| `rank(anl4_ebit_median / close)` | TOP500 | 0.23 | 0.11 | 36.0% | 60% | bull-only |
| `rank(ts_delta(anl4_ebit_median, 5))` | TOP3000 | 0.51 | 0.11 | 5.6% | 60% | mixed |
| `rank(anl4_ebit_median)` | TOP1000 | 0.15 | 0.07 | 42.6% | 60% | bull-only |
| `rank(anl4_ebit_median)` | TOP500 | 0.12 | 0.05 | 51.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ebit_mean: 1.000 (strongly positively correlated)
- est_ebit: 0.996 (strongly positively correlated)
- anl4_ebit_low: 0.995 (strongly positively correlated)
- anl4_ebit_high: 0.994 (strongly positively correlated)
- anl4_ptp_high: 0.985 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
