---
field: net_debt_actual_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.61
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0952
ann_vol: 0.0752
hit_rate: 0.5036
rolling_sharpe_min: -1.145
rolling_sharpe_max: 2.122
redundancy_cluster: 90
negated_best_sharpe: 0.63
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: 0.02
---
# net_debt_actual_value (analyst4)

*Net debt- announced financial value*

## Signal Profile
- `rank(net_debt_actual_value)`: S=0.22, F=0.08, T=2.8%, INFERIOR (TOP3000)
- `rank(net_debt_actual_value / close)`: S=0.61, F=0.37, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_delta(net_debt_actual_value, 5))`: S=0.57, F=0.23, T=36.8%, INFERIOR (TOP200)
- `-rank(net_debt_actual_value)`: S=0.00, F=0.00, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_debt_actual_value, 5))`: S=0.63, F=0.18, T=39.7%, INFERIOR (TOP3000)
- `-ts_zscore(net_debt_actual_value, 63)`: S=0.00, F=0.00, T=18.3%, INFERIOR (TOP3000)
- `ts_mean(net_debt_actual_value, 10)`: S=-0.25, F=-0.11, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(net_debt_actual_value, 22))`: S=0.18, F=0.04, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * net_debt_actual_value)`: S=-0.22, F=-0.08, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * net_debt_actual_value / close)`: S=-0.61, F=-0.37, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.60, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.25 (negative), ret=-1.1%
  - 2020: S=0.70 (moderate), ret=+6.6%
  - 2021: S=0.91 (moderate), ret=+6.5%
  - 2022: S=1.26 (moderate), ret=+11.5%
  - 2023: S=-0.27 (negative), ret=-1.4%

## Risk & Drawdown
- Max drawdown: 9.52% over 250 days (recovered)
- Annualized: return +4.5%, volatility 7.5% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.22, excess kurtosis +2.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 2.12, latest -0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +5.30%; worst month: -3.71%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.40
- Sideways: S=-0.15
- Bear: S=-0.68

## Negated Direction
Best negated: `rank(-1 * ts_delta(net_debt_actual_value, 5))` S=0.63, F=0.18, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * net_debt_actual_value)`: S=-0.22, F=-0.08, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * net_debt_actual_value / close)`: S=-0.61, F=-0.37, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_debt_actual_value, 5))`: S=0.63, F=0.18, T=39.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(net_debt_actual_value / close)` | TOP3000 | 0.60 | 0.37 | 9.5% | 60% | bull-only |
| `rank(ts_delta(net_debt_actual_value, 5))` | TOP200 | 0.57 | 0.23 | 17.6% | 60% | mixed |
| `rank(net_debt_actual_value / close)` | TOP1000 | 0.41 | 0.22 | 7.9% | 60% | bull-only |
| `rank(net_debt_actual_value)` | TOP3000 | 0.20 | 0.08 | 11.3% | 60% | bull-only |
| `rank(ts_delta(net_debt_actual_value, 5))` | TOP500 | 0.31 | 0.08 | 11.2% | 80% | mixed |
| `rank(net_debt_actual_value / close)` | TOP500 | 0.11 | 0.04 | 15.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- net_debt_reported_value: 1.000 (strongly positively correlated)
- anl4_netdebt_mean: 0.887 (strongly positively correlated)
- anl4_netdebt_median: 0.886 (strongly positively correlated)
- anl4_netdebt_high: 0.886 (strongly positively correlated)
- anl4_netdebt_low: 0.883 (strongly positively correlated)

Redundancy cluster #90: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
