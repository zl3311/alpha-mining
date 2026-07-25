---
field: pcr_oi_10
dataset: option9
best_template: rank_level
best_sharpe: 0.64
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1125
ann_vol: 0.0394
hit_rate: 0.5182
rolling_sharpe_min: -2.311
rolling_sharpe_max: 2.506
redundancy_cluster: 82
negated_best_sharpe: -0.03
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.67
---
# pcr_oi_10 (option9)

*Ratio of put open interest to call open interest for options expiring in 10 days, indicating short-term positioning*

## Signal Profile
- `rank(pcr_oi_10)`: S=0.64, F=0.29, T=12.1%, INFERIOR (TOP3000)
- `rank(pcr_oi_10 / close)`: S=0.15, F=0.05, T=11.4%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_10, 5))`: S=0.84, F=0.24, T=39.4%, INFERIOR (TOP500)
- `-rank(pcr_oi_10)`: S=-0.34, F=-0.10, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_10, 5))`: S=-0.11, F=-0.01, T=33.1%, INFERIOR (TOP3000)
- `ts_zscore(pcr_oi_10, 22)`: S=0.28, F=0.05, T=24.8%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_10, 10)`: S=0.26, F=0.09, T=11.8%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_10, 22))`: S=0.16, F=0.02, T=25.3%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_10)`: S=-0.64, F=-0.29, T=12.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_10 / close)`: S=-0.03, F=0.00, T=10.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.64, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.35 (moderate), ret=+2.8%
  - 2020: S=-1.98 (negative), ret=-6.9%
  - 2021: S=1.48 (moderate), ret=+7.3%
  - 2022: S=1.49 (moderate), ret=+7.3%
  - 2023: S=0.61 (moderate), ret=+1.9%

## Risk & Drawdown
- Max drawdown: 11.25% over 651 days (recovered)
- Annualized: return +2.5%, volatility 3.9% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.22, excess kurtosis +1.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.31, max 2.51, latest 0.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.13%; worst month: -2.89%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.30
- Sideways: S=1.03
- Bear: S=-1.53

## Negated Direction
Best negated: `rank(-1 * pcr_oi_10 / close)` S=-0.03, F=0.00, INFERIOR
Direction gap: -0.67 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_oi_10)`: S=-0.64, F=-0.29, T=12.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_10 / close)`: S=-0.03, F=0.00, T=10.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_10, 5))`: S=-0.11, F=-0.01, T=33.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_10)` | TOP3000 | 0.64 | 0.29 | 11.2% | 80% | bull-only |
| `rank(pcr_oi_10)` | TOP500 | 0.62 | 0.25 | 8.0% | 60% | mixed |
| `rank(ts_delta(pcr_oi_10, 5))` | TOP500 | 0.83 | 0.24 | 4.7% | 80% | all-weather |
| `rank(ts_delta(pcr_oi_10, 5))` | TOP200 | 0.49 | 0.14 | 10.0% | 80% | all-weather |
| `rank(pcr_oi_10)` | TOP1000 | 0.35 | 0.10 | 8.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pcr_oi_20: 0.972 (strongly positively correlated)
- pcr_oi_30: 0.925 (strongly positively correlated)
- pcr_oi_all: 0.910 (strongly positively correlated)
- cap: 0.786 (strongly positively correlated)
- put_breakeven_120: 0.786 (strongly positively correlated)

Redundancy cluster #82: 3 similar fields, mean |rho| 0.844 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
