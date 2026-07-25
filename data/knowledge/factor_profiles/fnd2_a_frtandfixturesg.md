---
field: fnd2_a_frtandfixturesg
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.94
best_fitness: 1.19
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1037
ann_vol: 0.0866
hit_rate: 0.4794
rolling_sharpe_min: -1.16
rolling_sharpe_max: 2.228
redundancy_cluster: 1
negated_best_sharpe: 0.2
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.74
---
# fnd2_a_frtandfixturesg (fundamental2)

*Amount before accumulated depreciation of equipment commonly used in offices and stores that have no permanent connection to the structure of a building or utilities. Examples include, but are not limited to, desks, chairs, tables, and bookcases.*

## Signal Profile
- `rank(fnd2_a_frtandfixturesg)`: S=0.56, F=0.41, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd2_a_frtandfixturesg / close)`: S=0.72, F=0.51, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_frtandfixturesg, 5))`: S=0.62, F=0.47, T=25.7%, INFERIOR (TOP200)
- `-rank(fnd2_a_frtandfixturesg)`: S=-0.22, F=-0.12, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_frtandfixturesg, 5))`: S=0.20, F=0.07, T=33.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_frtandfixturesg, 63)`: S=0.94, F=1.19, T=16.2%, AVERAGE (TOP3000)
- `ts_mean(fnd2_a_frtandfixturesg, 10)`: S=0.21, F=0.09, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_frtandfixturesg, 22))`: S=0.01, F=0.00, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_frtandfixturesg)`: S=-0.56, F=-0.41, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_frtandfixturesg / close)`: S=-0.72, F=-0.51, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.70, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.12 (negative), ret=-0.7%
  - 2020: S=-0.26 (negative), ret=-2.6%
  - 2021: S=1.29 (moderate), ret=+14.0%
  - 2022: S=1.81 (strong), ret=+15.8%
  - 2023: S=0.67 (moderate), ret=+3.4%

## Risk & Drawdown
- Max drawdown: 10.37% over 237 days (recovered)
- Annualized: return +6.1%, volatility 8.7% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.60, excess kurtosis +3.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 2.23, latest 0.78

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.15%; worst month: -3.81%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.82
- Sideways: S=-0.19
- Bear: S=-1.15

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_frtandfixturesg, 5))` S=0.20, F=0.07, INFERIOR
Direction gap: -0.74 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd2_a_frtandfixturesg)`: S=-0.56, F=-0.41, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_frtandfixturesg / close)`: S=-0.72, F=-0.51, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_frtandfixturesg, 5))`: S=0.20, F=0.07, T=33.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_frtandfixturesg / close)` | TOP3000 | 0.70 | 0.51 | 10.4% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_frtandfixturesg, 5))` | TOP200 | 0.62 | 0.47 | 53.5% | 80% | all-weather |
| `rank(fnd2_a_frtandfixturesg)` | TOP3000 | 0.56 | 0.41 | 33.1% | 80% | bull-only |
| `rank(fnd2_a_frtandfixturesg / close)` | TOP1000 | 0.30 | 0.18 | 31.7% | 40% | bull-only |
| `rank(fnd2_a_frtandfixturesg)` | TOP1000 | 0.21 | 0.12 | 52.1% | 40% | bull-only |
| `rank(ts_delta(fnd2_a_frtandfixturesg, 5))` | TOP1000 | 0.23 | 0.09 | 39.5% | 40% | mixed |
| `rank(fnd2_a_frtandfixturesg / close)` | TOP500 | 0.10 | 0.04 | 41.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.936 (strongly positively correlated)
- fn_mne_a: 0.934 (strongly positively correlated)
- fn_ppne_gross_a: 0.920 (strongly positively correlated)
- fnd6_dpvieb: 0.905 (strongly positively correlated)
- fnd6_newa1v1300_dp: 0.903 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
