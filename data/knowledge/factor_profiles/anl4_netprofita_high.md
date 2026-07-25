---
field: anl4_netprofita_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.57
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.2139
ann_vol: 0.084
hit_rate: 0.5004
rolling_sharpe_min: -2.762
rolling_sharpe_max: 2.505
redundancy_cluster: 13
negated_best_sharpe: 0.23
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.34
---
# anl4_netprofita_high (analyst4)

*Adjusted Net Income - the highest estimation*

## Signal Profile
- `rank(anl4_netprofita_high)`: S=0.29, F=0.15, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_netprofita_high / close)`: S=0.57, F=0.35, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netprofita_high, 5))`: S=0.39, F=0.08, T=36.4%, INFERIOR (TOP3000)
- `-rank(anl4_netprofita_high)`: S=-0.07, F=-0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofita_high, 5))`: S=0.23, F=0.06, T=35.5%, INFERIOR (TOP3000)
- `ts_zscore(anl4_netprofita_high, 22)`: S=0.25, F=0.05, T=35.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_netprofita_high, 10)`: S=0.11, F=0.04, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netprofita_high, 22))`: S=0.39, F=0.13, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_high)`: S=0.01, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_high / close)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.13 (weak), ret=+0.6%
  - 2020: S=-2.02 (negative), ret=-12.2%
  - 2021: S=1.06 (moderate), ret=+11.4%
  - 2022: S=2.08 (strong), ret=+23.4%
  - 2023: S=-0.00 (negative), ret=-0.0%

## Risk & Drawdown
- Max drawdown: 21.39% over 805 days (recovered)
- Annualized: return +4.7%, volatility 8.4% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.12, excess kurtosis +1.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.76, max 2.50, latest -0.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.92%; worst month: -3.62%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.28
- Sideways: S=0.88
- Bear: S=-3.17

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netprofita_high, 5))` S=0.23, F=0.06, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_netprofita_high)`: S=0.01, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_high / close)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofita_high, 5))`: S=0.23, F=0.06, T=35.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netprofita_high / close)` | TOP3000 | 0.56 | 0.35 | 21.4% | 60% | bull-only |
| `rank(anl4_netprofita_high)` | TOP3000 | 0.29 | 0.15 | 39.1% | 60% | bull-only |
| `rank(ts_delta(anl4_netprofita_high, 5))` | TOP3000 | 0.41 | 0.08 | 7.9% | 80% | weak |
| `rank(anl4_netprofita_high / close)` | TOP1000 | 0.17 | 0.06 | 30.1% | 60% | bull-only |
| `rank(ts_delta(anl4_netprofita_high, 5))` | TOP1000 | 0.19 | 0.03 | 8.9% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_netprofita_median: 0.996 (strongly positively correlated)
- anl4_netprofita_mean: 0.996 (strongly positively correlated)
- est_netprofit_adj: 0.990 (strongly positively correlated)
- anl4_netprofita_low: 0.986 (strongly positively correlated)
- anl4_netprofit_high: 0.979 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
