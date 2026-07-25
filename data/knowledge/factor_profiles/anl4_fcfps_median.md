---
field: anl4_fcfps_median
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.76
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1573
ann_vol: 0.0887
hit_rate: 0.4834
rolling_sharpe_min: -1.928
rolling_sharpe_max: 2.717
redundancy_cluster: 1
negated_best_sharpe: 0.16
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.6
---
# anl4_fcfps_median (analyst4)

*Free cash flow - summary on estimations, 50th-percentile, per share*

## Signal Profile
- `rank(anl4_fcfps_median)`: S=0.48, F=0.29, T=1.8%, INFERIOR (TOP3000)
- `rank(anl4_fcfps_median / close)`: S=0.76, F=0.56, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_fcfps_median, 5))`: S=0.52, F=0.21, T=33.9%, INFERIOR (TOP200)
- `-rank(anl4_fcfps_median)`: S=-0.31, F=-0.15, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcfps_median, 5))`: S=-0.46, F=-0.14, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_fcfps_median, 63)`: S=0.13, F=0.03, T=15.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcfps_median, 10)`: S=0.26, F=0.11, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcfps_median, 22))`: S=0.10, F=0.02, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_median)`: S=0.12, F=0.04, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_median / close)`: S=0.16, F=0.06, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.74, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.11 (negative), ret=-5.9%
  - 2020: S=-0.65 (negative), ret=-6.6%
  - 2021: S=1.98 (strong), ret=+19.5%
  - 2022: S=2.25 (strong), ret=+23.4%
  - 2023: S=0.30 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 15.73% over 805 days (recovered)
- Annualized: return +6.6%, volatility 8.9% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.52, excess kurtosis +2.41

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.93, max 2.72, latest 0.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.59%; worst month: -4.04%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.16
- Sideways: S=-0.80
- Bear: S=-0.73

## Negated Direction
Best negated: `rank(-1 * anl4_fcfps_median / close)` S=0.16, F=0.06, INFERIOR
Direction gap: -0.60 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_fcfps_median)`: S=0.12, F=0.04, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_median / close)`: S=0.16, F=0.06, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcfps_median, 5))`: S=-0.46, F=-0.14, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_fcfps_median / close)` | TOP3000 | 0.74 | 0.56 | 15.7% | 60% | bull-only |
| `rank(anl4_fcfps_median / close)` | TOP1000 | 0.49 | 0.32 | 17.1% | 60% | bull-only |
| `rank(anl4_fcfps_median)` | TOP3000 | 0.46 | 0.29 | 27.6% | 80% | bull-only |
| `rank(ts_delta(anl4_fcfps_median, 5))` | TOP200 | 0.53 | 0.21 | 20.2% | 80% | mixed |
| `rank(anl4_fcfps_median)` | TOP1000 | 0.30 | 0.15 | 28.4% | 80% | bull-only |
| `rank(ts_delta(anl4_fcfps_median, 5))` | TOP500 | 0.47 | 0.14 | 20.0% | 40% | mixed |
| `rank(ts_delta(anl4_fcfps_median, 5))` | TOP1000 | 0.35 | 0.08 | 18.9% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_fcfps_mean: 0.999 (strongly positively correlated)
- anl4_fcfps_high: 0.993 (strongly positively correlated)
- anl4_fcfps_low: 0.991 (strongly positively correlated)
- est_fcf_ps: 0.964 (strongly positively correlated)
- anl4_qfd1_az_hgih_spe: 0.872 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
