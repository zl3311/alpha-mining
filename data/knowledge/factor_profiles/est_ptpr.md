---
field: est_ptpr
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.4
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2144
ann_vol: 0.092
hit_rate: 0.5045
rolling_sharpe_min: -2.836
rolling_sharpe_max: 2.134
negated_best_sharpe: 0.44
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: 0.04
---
# est_ptpr (analyst4)

*Reported pretax income - mean of estimations*

## Signal Profile
- `rank(est_ptpr)`: S=0.12, F=0.04, T=0.9%, INFERIOR (TOP3000)
- `rank(est_ptpr / close)`: S=0.40, F=0.22, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(est_ptpr, 5))`: S=0.19, F=0.03, T=36.3%, INFERIOR (TOP3000)
- `-rank(est_ptpr)`: S=0.05, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_ptpr, 5))`: S=0.44, F=0.15, T=35.0%, INFERIOR (TOP3000)
- `-ts_zscore(est_ptpr, 63)`: S=-0.25, F=-0.07, T=16.1%, INFERIOR (TOP3000)
- `ts_mean(est_ptpr, 10)`: S=-0.13, F=-0.04, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(est_ptpr, 22))`: S=-0.25, F=-0.07, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * est_ptpr)`: S=0.17, F=0.07, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * est_ptpr / close)`: S=0.15, F=0.06, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.39, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.52 (moderate), ret=+2.5%
  - 2020: S=-1.94 (negative), ret=-12.0%
  - 2021: S=0.79 (moderate), ret=+8.5%
  - 2022: S=1.46 (moderate), ret=+18.8%
  - 2023: S=-0.01 (negative), ret=-0.0%

## Risk & Drawdown
- Max drawdown: 21.44% over 645 days (recovered)
- Annualized: return +3.6%, volatility 9.2% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.12, excess kurtosis +1.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.84, max 2.13, latest -0.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.97%; worst month: -5.22%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.12
- Sideways: S=0.90
- Bear: S=-3.58

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_ptpr, 5))` S=0.44, F=0.15, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * est_ptpr)`: S=0.17, F=0.07, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * est_ptpr / close)`: S=0.15, F=0.06, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_ptpr, 5))`: S=0.44, F=0.15, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_ptpr / close)` | TOP3000 | 0.39 | 0.22 | 21.4% | 60% | bull-only |
| `rank(est_ptpr)` | TOP3000 | 0.11 | 0.04 | 37.9% | 60% | bull-only |
| `rank(ts_delta(est_ptpr, 5))` | TOP3000 | 0.20 | 0.03 | 8.6% | 40% | weak |
| `rank(est_ptpr / close)` | TOP1000 | 0.08 | 0.03 | 27.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ptpr_mean: 0.975 (strongly positively correlated)
- anl4_ptpr_median: 0.975 (strongly positively correlated)
- anl4_ptpr_low: 0.970 (strongly positively correlated)
- anl4_netprofita_low: 0.957 (strongly positively correlated)
- anl4_ptp_median: 0.955 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
