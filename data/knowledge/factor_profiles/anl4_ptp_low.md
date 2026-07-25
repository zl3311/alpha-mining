---
field: anl4_ptp_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.51
best_fitness: 0.33
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.3054
ann_vol: 0.1039
hit_rate: 0.5069
rolling_sharpe_min: -3.754
rolling_sharpe_max: 2.571
redundancy_cluster: 13
negated_best_sharpe: 0.19
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.32
---
# anl4_ptp_low (analyst4)

*Pretax income - the lowest estimation*

## Signal Profile
- `rank(anl4_ptp_low)`: S=0.34, F=0.20, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_ptp_low / close)`: S=0.51, F=0.33, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ptp_low, 5))`: S=0.45, F=0.13, T=37.3%, INFERIOR (TOP500)
- `-rank(anl4_ptp_low)`: S=-0.08, F=-0.02, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptp_low, 5))`: S=0.19, F=0.04, T=35.7%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_ptp_low, 63)`: S=-0.01, F=0.00, T=16.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_ptp_low, 10)`: S=0.11, F=0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ptp_low, 22))`: S=-0.25, F=-0.07, T=14.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_low)`: S=0.06, F=0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_low / close)`: S=0.04, F=0.01, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.50, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.31 (weak), ret=+1.4%
  - 2020: S=-2.85 (negative), ret=-18.5%
  - 2021: S=1.29 (moderate), ret=+16.2%
  - 2022: S=1.82 (strong), ret=+26.5%
  - 2023: S=-0.01 (negative), ret=-0.1%

## Risk & Drawdown
- Max drawdown: 30.54% over 812 days (recovered)
- Annualized: return +5.2%, volatility 10.4% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew -0.03, excess kurtosis +1.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.75, max 2.57, latest -0.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.30%; worst month: -6.11%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.28
- Sideways: S=0.97
- Bear: S=-3.56

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ptp_low, 5))` S=0.19, F=0.04, INFERIOR
Direction gap: -0.32 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_ptp_low)`: S=0.06, F=0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptp_low / close)`: S=0.04, F=0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptp_low, 5))`: S=0.19, F=0.04, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ptp_low / close)` | TOP3000 | 0.50 | 0.33 | 30.5% | 60% | bull-only |
| `rank(anl4_ptp_low)` | TOP3000 | 0.33 | 0.20 | 42.6% | 60% | bull-only |
| `rank(ts_delta(anl4_ptp_low, 5))` | TOP500 | 0.44 | 0.13 | 18.5% | 60% | mixed |
| `rank(ts_delta(anl4_ptp_low, 5))` | TOP1000 | 0.33 | 0.07 | 11.0% | 40% | weak |
| `rank(anl4_ptp_low / close)` | TOP1000 | 0.15 | 0.06 | 31.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_netprofit_low: 0.996 (strongly positively correlated)
- anl4_ptp_mean: 0.995 (strongly positively correlated)
- anl4_ptp_median: 0.994 (strongly positively correlated)
- anl4_netprofit_mean: 0.991 (strongly positively correlated)
- anl4_netprofit_median: 0.991 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
