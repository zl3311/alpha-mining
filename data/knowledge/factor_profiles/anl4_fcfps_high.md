---
field: anl4_fcfps_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.78
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1495
ann_vol: 0.0888
hit_rate: 0.4883
rolling_sharpe_min: -1.798
rolling_sharpe_max: 2.689
redundancy_cluster: 1
negated_best_sharpe: 0.14
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.64
---
# anl4_fcfps_high (analyst4)

*Free Cash Flow Per Share - the highest estimation*

## Signal Profile
- `rank(anl4_fcfps_high)`: S=0.51, F=0.31, T=1.8%, INFERIOR (TOP3000)
- `rank(anl4_fcfps_high / close)`: S=0.78, F=0.58, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_fcfps_high, 5))`: S=0.68, F=0.33, T=33.7%, INFERIOR (TOP200)
- `-rank(anl4_fcfps_high)`: S=-0.34, F=-0.17, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcfps_high, 5))`: S=-0.54, F=-0.19, T=36.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_fcfps_high, 22)`: S=0.08, F=0.01, T=33.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcfps_high, 10)`: S=0.25, F=0.11, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcfps_high, 22))`: S=0.41, F=0.14, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_high)`: S=0.07, F=0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_high / close)`: S=0.14, F=0.05, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.07 (negative), ret=-6.1%
  - 2020: S=-0.45 (negative), ret=-4.8%
  - 2021: S=1.99 (strong), ret=+19.7%
  - 2022: S=2.21 (strong), ret=+21.9%
  - 2023: S=0.45 (weak), ret=+2.7%

## Risk & Drawdown
- Max drawdown: 14.95% over 784 days (recovered)
- Annualized: return +6.8%, volatility 8.9% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +0.59, excess kurtosis +2.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.80, max 2.69, latest 0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.43%; worst month: -4.28%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.20
- Sideways: S=-0.88
- Bear: S=-0.61

## Negated Direction
Best negated: `rank(-1 * anl4_fcfps_high / close)` S=0.14, F=0.05, INFERIOR
Direction gap: -0.64 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_fcfps_high)`: S=0.07, F=0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_high / close)`: S=0.14, F=0.05, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcfps_high, 5))`: S=-0.54, F=-0.19, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_fcfps_high / close)` | TOP3000 | 0.77 | 0.58 | 14.9% | 60% | bull-only |
| `rank(ts_delta(anl4_fcfps_high, 5))` | TOP200 | 0.69 | 0.33 | 22.6% | 60% | mixed |
| `rank(anl4_fcfps_high)` | TOP3000 | 0.49 | 0.31 | 27.4% | 80% | bull-only |
| `rank(anl4_fcfps_high / close)` | TOP1000 | 0.47 | 0.30 | 16.2% | 60% | bull-only |
| `rank(ts_delta(anl4_fcfps_high, 5))` | TOP1000 | 0.77 | 0.28 | 12.0% | 60% | bear-only |
| `rank(ts_delta(anl4_fcfps_high, 5))` | TOP500 | 0.53 | 0.19 | 16.1% | 60% | bear-only |
| `rank(anl4_fcfps_high)` | TOP1000 | 0.33 | 0.17 | 27.0% | 80% | bull-only |
| `rank(ts_delta(anl4_fcfps_high, 5))` | TOP3000 | 0.14 | 0.02 | 14.7% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_fcfps_mean: 0.994 (strongly positively correlated)
- anl4_fcfps_median: 0.993 (strongly positively correlated)
- anl4_fcfps_low: 0.976 (strongly positively correlated)
- est_fcf_ps: 0.958 (strongly positively correlated)
- anl4_qf_az_hgih_spe: 0.868 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
