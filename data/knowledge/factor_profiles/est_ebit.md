---
field: est_ebit
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.67
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.1992
ann_vol: 0.0893
hit_rate: 0.5012
rolling_sharpe_min: -2.262
rolling_sharpe_max: 2.63
redundancy_cluster: 13
negated_best_sharpe: 0.6
negated_best_template: rank_neg_delta
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.07
---
# est_ebit (analyst4)

*Earnings before interest and taxes - mean of estimations*

## Signal Profile
- `rank(est_ebit)`: S=0.40, F=0.25, T=1.1%, INFERIOR (TOP3000)
- `rank(est_ebit / close)`: S=0.67, F=0.46, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(est_ebit, 5))`: S=0.33, F=0.07, T=36.2%, INFERIOR (TOP1000)
- `-rank(est_ebit)`: S=-0.15, F=-0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_ebit, 5))`: S=0.60, F=0.22, T=36.2%, INFERIOR (TOP3000)
- `ts_zscore(est_ebit, 22)`: S=0.25, F=0.05, T=33.8%, INFERIOR (TOP3000)
- `ts_mean(est_ebit, 10)`: S=0.02, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(est_ebit, 22))`: S=-0.02, F=0.00, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * est_ebit)`: S=-0.05, F=-0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * est_ebit / close)`: S=-0.08, F=-0.02, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.66, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.02 (weak), ret=+0.1%
  - 2020: S=-1.53 (negative), ret=-10.4%
  - 2021: S=1.29 (moderate), ret=+14.8%
  - 2022: S=1.96 (strong), ret=+23.1%
  - 2023: S=0.20 (weak), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 19.92% over 779 days (recovered)
- Annualized: return +5.9%, volatility 8.9% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.06, excess kurtosis +1.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.26, max 2.63, latest -0.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.95%; worst month: -3.85%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.47
- Sideways: S=0.88
- Bear: S=-3.10

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_ebit, 5))` S=0.60, F=0.22, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * est_ebit)`: S=-0.05, F=-0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * est_ebit / close)`: S=-0.08, F=-0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_ebit, 5))`: S=0.60, F=0.22, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_ebit / close)` | TOP3000 | 0.66 | 0.46 | 19.9% | 80% | bull-only |
| `rank(est_ebit)` | TOP3000 | 0.40 | 0.25 | 37.5% | 60% | bull-only |
| `rank(est_ebit / close)` | TOP1000 | 0.35 | 0.20 | 23.4% | 60% | bull-only |
| `rank(est_ebit / close)` | TOP500 | 0.25 | 0.13 | 34.6% | 60% | bull-only |
| `rank(ts_delta(est_ebit, 5))` | TOP1000 | 0.34 | 0.07 | 11.5% | 60% | mixed |
| `rank(est_ebit)` | TOP1000 | 0.14 | 0.06 | 42.3% | 60% | bull-only |
| `rank(est_ebit)` | TOP500 | 0.13 | 0.06 | 49.7% | 60% | bull-only |
| `rank(ts_delta(est_ebit, 5))` | TOP3000 | 0.23 | 0.03 | 9.4% | 60% | weak |
| `rank(ts_delta(est_ebit, 5))` | TOP500 | 0.18 | 0.03 | 16.3% | 60% | weak |
| `rank(est_ebit / close)` | TOP200 | 0.07 | 0.02 | 41.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ebit_mean: 0.997 (strongly positively correlated)
- anl4_ebit_median: 0.996 (strongly positively correlated)
- anl4_ebit_high: 0.992 (strongly positively correlated)
- anl4_ebit_low: 0.991 (strongly positively correlated)
- est_ptp: 0.981 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
