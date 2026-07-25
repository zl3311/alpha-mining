---
field: anl4_ptp_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.68
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2476
ann_vol: 0.0922
hit_rate: 0.5012
rolling_sharpe_min: -3.085
rolling_sharpe_max: 2.902
redundancy_cluster: 13
negated_best_sharpe: 0.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.38
---
# anl4_ptp_high (analyst4)

*Pretax income - the highest estimation*

## Signal Profile
- `rank(anl4_ptp_high)`: S=0.43, F=0.28, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_ptp_high / close)`: S=0.68, F=0.48, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ptp_high, 5))`: S=0.37, F=0.08, T=36.9%, INFERIOR (TOP1000)
- `-rank(anl4_ptp_high)`: S=-0.18, F=-0.08, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptp_high, 5))`: S=0.30, F=0.09, T=35.4%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ptp_high, 22)`: S=0.11, F=0.02, T=35.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_ptp_high, 10)`: S=0.16, F=0.06, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ptp_high, 22))`: S=0.11, F=0.02, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_high)`: S=-0.01, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_high / close)`: S=0.04, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.67, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.03 (negative), ret=-0.1%
  - 2020: S=-2.37 (negative), ret=-14.8%
  - 2021: S=1.56 (strong), ret=+18.4%
  - 2022: S=2.15 (strong), ret=+26.4%
  - 2023: S=0.07 (weak), ret=+0.6%

## Risk & Drawdown
- Max drawdown: 24.76% over 785 days (recovered)
- Annualized: return +6.2%, volatility 9.2% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.06, excess kurtosis +1.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.08, max 2.90, latest -0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.48%; worst month: -5.03%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.54
- Sideways: S=0.83
- Bear: S=-3.17

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ptp_high, 5))` S=0.30, F=0.09, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_ptp_high)`: S=-0.01, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_high / close)`: S=0.04, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptp_high, 5))`: S=0.30, F=0.09, T=35.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ptp_high / close)` | TOP3000 | 0.67 | 0.48 | 24.8% | 60% | bull-only |
| `rank(anl4_ptp_high)` | TOP3000 | 0.42 | 0.28 | 40.3% | 60% | bull-only |
| `rank(anl4_ptp_high / close)` | TOP1000 | 0.27 | 0.14 | 29.4% | 60% | bull-only |
| `rank(anl4_ptp_high)` | TOP1000 | 0.17 | 0.08 | 44.3% | 60% | bull-only |
| `rank(ts_delta(anl4_ptp_high, 5))` | TOP1000 | 0.38 | 0.08 | 10.3% | 60% | mixed |
| `rank(anl4_ptp_high / close)` | TOP500 | 0.17 | 0.07 | 39.4% | 60% | bull-only |
| `rank(anl4_ptp_high)` | TOP500 | 0.13 | 0.06 | 51.3% | 60% | bull-only |
| `rank(ts_delta(anl4_ptp_high, 5))` | TOP3000 | 0.19 | 0.02 | 9.4% | 40% | weak |

## Correlation Notes
Top correlates:
- anl4_netprofit_high: 0.994 (strongly positively correlated)
- anl4_ptp_median: 0.994 (strongly positively correlated)
- anl4_ptp_mean: 0.993 (strongly positively correlated)
- est_ptp: 0.992 (strongly positively correlated)
- anl4_netprofit_median: 0.990 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
