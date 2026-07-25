---
field: anl4_ebit_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.59
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.251
ann_vol: 0.097
hit_rate: 0.5101
rolling_sharpe_min: -2.885
rolling_sharpe_max: 2.542
redundancy_cluster: 13
negated_best_sharpe: 0.27
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.32
---
# anl4_ebit_low (analyst4)

*Earnings before interest and taxes - The lowest estimation*

## Signal Profile
- `rank(anl4_ebit_low)`: S=0.37, F=0.22, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_ebit_low / close)`: S=0.59, F=0.40, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ebit_low, 5))`: S=0.64, F=0.19, T=37.0%, INFERIOR (TOP1000)
- `-rank(anl4_ebit_low)`: S=-0.12, F=-0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebit_low, 5))`: S=0.27, F=0.07, T=35.6%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ebit_low, 22)`: S=0.23, F=0.05, T=35.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebit_low, 10)`: S=0.00, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebit_low, 22))`: S=0.06, F=0.01, T=14.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_low)`: S=-0.03, F=-0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_low / close)`: S=-0.07, F=-0.02, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.09 (weak), ret=+0.4%
  - 2020: S=-1.98 (negative), ret=-13.4%
  - 2021: S=1.24 (moderate), ret=+15.0%
  - 2022: S=1.79 (strong), ret=+23.9%
  - 2023: S=0.22 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 25.10% over 805 days (recovered)
- Annualized: return +5.6%, volatility 9.7% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.00, excess kurtosis +1.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.88, max 2.54, latest 0.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.08%; worst month: -4.06%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.37
- Sideways: S=0.86
- Bear: S=-3.26

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ebit_low, 5))` S=0.27, F=0.07, INFERIOR
Direction gap: -0.32 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_ebit_low)`: S=-0.03, F=-0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_low / close)`: S=-0.07, F=-0.02, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebit_low, 5))`: S=0.27, F=0.07, T=35.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ebit_low / close)` | TOP3000 | 0.58 | 0.40 | 25.1% | 80% | bull-only |
| `rank(anl4_ebit_low)` | TOP3000 | 0.36 | 0.22 | 40.3% | 60% | bull-only |
| `rank(ts_delta(anl4_ebit_low, 5))` | TOP1000 | 0.65 | 0.19 | 9.7% | 80% | mixed |
| `rank(ts_delta(anl4_ebit_low, 5))` | TOP500 | 0.53 | 0.16 | 11.3% | 40% | mixed |
| `rank(anl4_ebit_low / close)` | TOP1000 | 0.29 | 0.15 | 26.5% | 60% | bull-only |
| `rank(ts_delta(anl4_ebit_low, 5))` | TOP3000 | 0.35 | 0.06 | 7.5% | 80% | mixed |
| `rank(anl4_ebit_low)` | TOP1000 | 0.11 | 0.04 | 43.7% | 60% | bull-only |
| `rank(anl4_ebit_low / close)` | TOP500 | 0.11 | 0.04 | 39.9% | 60% | bull-only |
| `rank(anl4_ebit_low)` | TOP500 | 0.07 | 0.02 | 52.7% | 60% | bull-only |
| `rank(anl4_ebit_low / close)` | TOP200 | 0.06 | 0.02 | 42.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ebit_mean: 0.996 (strongly positively correlated)
- anl4_ebit_median: 0.995 (strongly positively correlated)
- est_ebit: 0.991 (strongly positively correlated)
- est_ptp: 0.987 (strongly positively correlated)
- anl4_ptp_mean: 0.986 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
