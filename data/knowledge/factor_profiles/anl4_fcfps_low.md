---
field: anl4_fcfps_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.75
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1517
ann_vol: 0.0856
hit_rate: 0.485
rolling_sharpe_min: -1.901
rolling_sharpe_max: 2.784
redundancy_cluster: 36
negated_best_sharpe: 0.62
negated_best_template: rank_neg_delta
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.13
---
# anl4_fcfps_low (analyst4)

*Free Cash Flow Per Share - the lowest estimation*

## Signal Profile
- `rank(anl4_fcfps_low)`: S=0.51, F=0.31, T=1.8%, INFERIOR (TOP3000)
- `rank(anl4_fcfps_low / close)`: S=0.75, F=0.54, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_fcfps_low, 5))`: S=-0.35, F=-0.10, T=36.0%, INFERIOR (TOP500)
- `-rank(anl4_fcfps_low)`: S=-0.35, F=-0.18, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcfps_low, 5))`: S=0.62, F=0.28, T=34.0%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_fcfps_low, 63)`: S=0.50, F=0.19, T=16.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcfps_low, 10)`: S=0.27, F=0.11, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcfps_low, 22))`: S=-0.78, F=-0.38, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_low)`: S=0.25, F=0.12, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_low / close)`: S=0.23, F=0.11, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/24P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.73, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.20 (negative), ret=-6.0%
  - 2020: S=-0.80 (negative), ret=-7.2%
  - 2021: S=1.94 (strong), ret=+18.5%
  - 2022: S=2.31 (strong), ret=+24.8%
  - 2023: S=0.09 (weak), ret=+0.5%

## Risk & Drawdown
- Max drawdown: 15.17% over 829 days (recovered)
- Annualized: return +6.2%, volatility 8.6% (fraction of booksize)
- Hit rate: 48.5% positive days
- Tail shape: skew +0.43, excess kurtosis +2.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.90, max 2.78, latest 0.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.56%; worst month: -3.48%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.14
- Sideways: S=-0.68
- Bear: S=-0.90

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_fcfps_low, 5))` S=0.62, F=0.28, INFERIOR
Direction gap: -0.13 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_fcfps_low)`: S=0.25, F=0.12, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_low / close)`: S=0.23, F=0.11, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcfps_low, 5))`: S=0.62, F=0.28, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_fcfps_low / close)` | TOP3000 | 0.73 | 0.54 | 15.2% | 60% | bull-only |
| `rank(anl4_fcfps_low / close)` | TOP1000 | 0.50 | 0.31 | 16.4% | 60% | bull-only |
| `rank(anl4_fcfps_low)` | TOP3000 | 0.49 | 0.31 | 25.7% | 60% | bull-only |
| `rank(anl4_fcfps_low)` | TOP1000 | 0.34 | 0.18 | 27.2% | 80% | bull-only |

## Correlation Notes
Top correlates:
- anl4_fcfps_median: 0.991 (strongly positively correlated)
- anl4_fcfps_mean: 0.990 (strongly positively correlated)
- anl4_fcfps_high: 0.976 (strongly positively correlated)
- est_fcf_ps: 0.961 (strongly positively correlated)
- anl4_qf_az_hgih_spe: 0.871 (strongly positively correlated)

Redundancy cluster #36: 4 similar fields, mean |rho| 0.734 (representative: anl4_fcf_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
