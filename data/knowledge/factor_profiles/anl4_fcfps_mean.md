---
field: anl4_fcfps_mean
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.77
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.15
ann_vol: 0.089
hit_rate: 0.4842
rolling_sharpe_min: -1.694
rolling_sharpe_max: 2.715
redundancy_cluster: 1
negated_best_sharpe: 0.15
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.62
---
# anl4_fcfps_mean (analyst4)

*Free cash flow per share - mean of estimations*

## Signal Profile
- `rank(anl4_fcfps_mean)`: S=0.48, F=0.29, T=1.8%, INFERIOR (TOP3000)
- `rank(anl4_fcfps_mean / close)`: S=0.77, F=0.57, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_fcfps_mean, 5))`: S=0.40, F=0.11, T=36.3%, INFERIOR (TOP500)
- `-rank(anl4_fcfps_mean)`: S=-0.32, F=-0.15, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcfps_mean, 5))`: S=-0.40, F=-0.11, T=36.3%, INFERIOR (TOP3000)
- `ts_zscore(anl4_fcfps_mean, 22)`: S=0.10, F=0.01, T=33.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcfps_mean, 10)`: S=0.26, F=0.11, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcfps_mean, 22))`: S=0.09, F=0.01, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_mean)`: S=0.10, F=0.03, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_mean / close)`: S=0.15, F=0.05, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.75, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.91 (negative), ret=-5.0%
  - 2020: S=-0.66 (negative), ret=-6.8%
  - 2021: S=1.98 (strong), ret=+19.5%
  - 2022: S=2.25 (strong), ret=+23.5%
  - 2023: S=0.29 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 15.00% over 784 days (recovered)
- Annualized: return +6.7%, volatility 8.9% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew +0.52, excess kurtosis +2.38

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.69, max 2.71, latest 0.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.64%; worst month: -4.04%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.17
- Sideways: S=-0.78
- Bear: S=-0.73

## Negated Direction
Best negated: `rank(-1 * anl4_fcfps_mean / close)` S=0.15, F=0.05, INFERIOR
Direction gap: -0.62 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_fcfps_mean)`: S=0.10, F=0.03, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_mean / close)`: S=0.15, F=0.05, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcfps_mean, 5))`: S=-0.40, F=-0.11, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_fcfps_mean / close)` | TOP3000 | 0.75 | 0.57 | 15.0% | 60% | bull-only |
| `rank(anl4_fcfps_mean / close)` | TOP1000 | 0.49 | 0.31 | 17.2% | 60% | bull-only |
| `rank(anl4_fcfps_mean)` | TOP3000 | 0.47 | 0.29 | 27.8% | 80% | bull-only |
| `rank(anl4_fcfps_mean)` | TOP1000 | 0.30 | 0.15 | 28.4% | 80% | bull-only |
| `rank(ts_delta(anl4_fcfps_mean, 5))` | TOP500 | 0.41 | 0.11 | 19.2% | 40% | mixed |
| `rank(ts_delta(anl4_fcfps_mean, 5))` | TOP1000 | 0.26 | 0.05 | 20.5% | 40% | bear-only |
| `rank(ts_delta(anl4_fcfps_mean, 5))` | TOP200 | 0.16 | 0.04 | 22.9% | 40% | mixed |

## Correlation Notes
Top correlates:
- anl4_fcfps_median: 0.999 (strongly positively correlated)
- anl4_fcfps_high: 0.994 (strongly positively correlated)
- anl4_fcfps_low: 0.990 (strongly positively correlated)
- est_fcf_ps: 0.965 (strongly positively correlated)
- anl4_qf_az_hgih_spe: 0.872 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
