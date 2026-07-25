---
field: anl4_ebit_mean
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.64
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.2269
ann_vol: 0.0935
hit_rate: 0.5085
rolling_sharpe_min: -2.542
rolling_sharpe_max: 2.654
redundancy_cluster: 13
negated_best_sharpe: 0.72
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: 0.08
---
# anl4_ebit_mean (analyst4)

*Earnings before interest and taxes - mean of estimations*

## Signal Profile
- `rank(anl4_ebit_mean)`: S=0.39, F=0.24, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_ebit_mean / close)`: S=0.64, F=0.44, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ebit_mean, 5))`: S=0.43, F=0.10, T=36.2%, INFERIOR (TOP1000)
- `-rank(anl4_ebit_mean)`: S=-0.16, F=-0.07, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebit_mean, 5))`: S=0.72, F=0.29, T=36.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ebit_mean, 22)`: S=0.36, F=0.09, T=33.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebit_mean, 10)`: S=0.02, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebit_mean, 22))`: S=0.02, F=0.00, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_mean)`: S=-0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_mean / close)`: S=-0.04, F=-0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.63, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.05 (negative), ret=-0.2%
  - 2020: S=-1.82 (negative), ret=-12.5%
  - 2021: S=1.43 (moderate), ret=+17.0%
  - 2022: S=1.85 (strong), ret=+23.3%
  - 2023: S=0.18 (weak), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 22.69% over 782 days (recovered)
- Annualized: return +5.9%, volatility 9.3% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.05, excess kurtosis +1.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.54, max 2.65, latest -0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.17%; worst month: -4.04%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.47
- Sideways: S=0.76
- Bear: S=-3.12

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ebit_mean, 5))` S=0.72, F=0.29, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_ebit_mean)`: S=-0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_mean / close)`: S=-0.04, F=-0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebit_mean, 5))`: S=0.72, F=0.29, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ebit_mean / close)` | TOP3000 | 0.63 | 0.44 | 22.7% | 60% | bull-only |
| `rank(anl4_ebit_mean)` | TOP3000 | 0.39 | 0.24 | 39.5% | 60% | bull-only |
| `rank(anl4_ebit_mean / close)` | TOP1000 | 0.33 | 0.18 | 25.1% | 60% | bull-only |
| `rank(anl4_ebit_mean / close)` | TOP500 | 0.21 | 0.11 | 36.4% | 60% | bull-only |
| `rank(ts_delta(anl4_ebit_mean, 5))` | TOP1000 | 0.43 | 0.10 | 12.2% | 80% | mixed |
| `rank(anl4_ebit_mean)` | TOP1000 | 0.15 | 0.07 | 42.7% | 60% | bull-only |
| `rank(anl4_ebit_mean)` | TOP500 | 0.12 | 0.05 | 51.4% | 60% | bull-only |
| `rank(ts_delta(anl4_ebit_mean, 5))` | TOP3000 | 0.24 | 0.03 | 8.7% | 60% | weak |
| `rank(ts_delta(anl4_ebit_mean, 5))` | TOP500 | 0.15 | 0.02 | 17.8% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_ebit_median: 1.000 (strongly positively correlated)
- est_ebit: 0.997 (strongly positively correlated)
- anl4_ebit_low: 0.996 (strongly positively correlated)
- anl4_ebit_high: 0.993 (strongly positively correlated)
- anl4_ptp_high: 0.985 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
