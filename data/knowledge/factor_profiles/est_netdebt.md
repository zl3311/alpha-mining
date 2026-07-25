---
field: est_netdebt
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.46
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0764
ann_vol: 0.0515
hit_rate: 0.4923
rolling_sharpe_min: -1.437
rolling_sharpe_max: 2.097
negated_best_sharpe: 0.32
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.14
---
# est_netdebt (analyst4)

*Net debt - mean of estimations*

## Signal Profile
- `rank(est_netdebt)`: S=0.10, F=0.02, T=0.8%, INFERIOR (TOP3000)
- `rank(est_netdebt / close)`: S=0.39, F=0.16, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(est_netdebt, 5))`: S=0.10, F=0.02, T=35.9%, INFERIOR (TOP500)
- `-rank(est_netdebt)`: S=-0.02, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_netdebt, 5))`: S=0.30, F=0.10, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(est_netdebt, 63)`: S=0.46, F=0.17, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(est_netdebt, 10)`: S=-0.15, F=-0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(est_netdebt, 22))`: S=-0.86, F=-0.46, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * est_netdebt)`: S=0.24, F=0.09, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * est_netdebt / close)`: S=0.32, F=0.14, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.38, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.14 (weak), ret=+0.5%
  - 2020: S=0.41 (weak), ret=+2.7%
  - 2021: S=0.86 (moderate), ret=+4.1%
  - 2022: S=0.67 (moderate), ret=+4.0%
  - 2023: S=-0.46 (negative), ret=-1.6%

## Risk & Drawdown
- Max drawdown: 7.64% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +2.0%, volatility 5.1% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew +0.23, excess kurtosis +2.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.44, max 2.10, latest -0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +3.57%; worst month: -2.70%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.14
- Sideways: S=0.44
- Bear: S=-1.51

## Negated Direction
Best negated: `rank(-1 * est_netdebt / close)` S=0.32, F=0.14, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * est_netdebt)`: S=0.24, F=0.09, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * est_netdebt / close)`: S=0.32, F=0.14, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_netdebt, 5))`: S=0.30, F=0.10, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_netdebt / close)` | TOP3000 | 0.38 | 0.16 | 7.6% | 80% | bull-only |
| `rank(est_netdebt / close)` | TOP1000 | 0.20 | 0.07 | 10.7% | 80% | bull-only |
| `rank(ts_delta(est_netdebt, 5))` | TOP500 | 0.10 | 0.02 | 22.0% | 40% | mixed |
| `rank(est_netdebt)` | TOP3000 | 0.08 | 0.02 | 8.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_netdebt_mean: 0.921 (strongly positively correlated)
- anl4_netdebt_median: 0.920 (strongly positively correlated)
- anl4_netdebt_high: 0.920 (strongly positively correlated)
- anl4_netdebt_low: 0.916 (strongly positively correlated)
- net_debt_actual_value: 0.877 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
