---
field: fnd2_a_sbcpnargtbysbpmtwpwrr
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.57
best_fitness: 0.69
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.1006
ann_vol: 0.0715
hit_rate: 0.4777
rolling_sharpe_min: -1.717
rolling_sharpe_max: 2.707
redundancy_cluster: 33
negated_best_sharpe: 0.36
negated_best_template: neg_rank_level
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.21
---
# fnd2_a_sbcpnargtbysbpmtwpwrr (fundamental2)

*Weighted average price at which grantees could have acquired the underlying shares with respect to stock options of the plan that expired.*

## Signal Profile
- `rank(fnd2_a_sbcpnargtbysbpmtwpwrr)`: S=0.30, F=0.12, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_a_sbcpnargtbysbpmtwpwrr / close)`: S=0.63, F=0.38, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_sbcpnargtbysbpmtwpwrr, 5))`: S=0.46, F=0.23, T=33.1%, INFERIOR (TOP3000)
- `-rank(fnd2_a_sbcpnargtbysbpmtwpwrr)`: S=0.20, F=0.07, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_sbcpnargtbysbpmtwpwrr, 5))`: S=0.06, F=0.01, T=25.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_sbcpnargtbysbpmtwpwrr, 63)`: S=0.57, F=0.69, T=12.5%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_sbcpnargtbysbpmtwpwrr, 10)`: S=-0.32, F=-0.19, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_sbcpnargtbysbpmtwpwrr, 22))`: S=0.32, F=0.20, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnargtbysbpmtwpwrr)`: S=0.36, F=0.17, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnargtbysbpmtwpwrr / close)`: S=-0.07, F=-0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.40 (negative), ret=-2.0%
  - 2020: S=1.46 (moderate), ret=+12.2%
  - 2021: S=0.54 (moderate), ret=+3.6%
  - 2022: S=0.45 (weak), ret=+2.9%
  - 2023: S=0.61 (moderate), ret=+4.8%

## Risk & Drawdown
- Max drawdown: 10.06% over 394 days (recovered)
- Annualized: return +4.4%, volatility 7.1% (fraction of booksize)
- Hit rate: 47.8% positive days
- Tail shape: skew +0.74, excess kurtosis +2.68

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.72, max 2.71, latest 0.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +5.81%; worst month: -4.11%
Positive months: 51%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.86
- Sideways: S=-0.78
- Bear: S=1.69

## Negated Direction
Best negated: `rank(-1 * fnd2_a_sbcpnargtbysbpmtwpwrr)` S=0.36, F=0.17, INFERIOR
Direction gap: -0.21 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_sbcpnargtbysbpmtwpwrr)`: S=0.36, F=0.17, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnargtbysbpmtwpwrr / close)`: S=-0.07, F=-0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_sbcpnargtbysbpmtwpwrr, 5))`: S=0.06, F=0.01, T=25.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_sbcpnargtbysbpmtwpwrr / close)` | TOP3000 | 0.62 | 0.38 | 10.1% | 80% | all-weather |
| `rank(ts_delta(fnd2_a_sbcpnargtbysbpmtwpwrr, 5))` | TOP3000 | 0.46 | 0.23 | 44.6% | 80% | mixed |
| `rank(fnd2_a_sbcpnargtbysbpmtwpwrr)` | TOP3000 | 0.29 | 0.12 | 21.9% | 80% | bull-only |
| `rank(fnd2_a_sbcpnargtbysbpmtwpwrr / close)` | TOP1000 | 0.22 | 0.09 | 12.9% | 60% | mixed |
| `rank(ts_delta(fnd2_a_sbcpnargtbysbpmtwpwrr, 5))` | TOP1000 | 0.13 | 0.04 | 59.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_comp_options_out_weighted_avg_a: 0.919 (strongly positively correlated)
- fnd6_optprcca: 0.904 (strongly positively correlated)
- fnd6_optprcey: 0.895 (strongly positively correlated)
- fn_comp_options_exercisable_weighted_avg_a: 0.880 (strongly positively correlated)
- fn_oth_comp_forfeitures_fair_value_a: 0.865 (strongly positively correlated)

Redundancy cluster #33: 12 similar fields, mean |rho| 0.787 (representative: anl4_afv4_eps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
