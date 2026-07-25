---
field: cash_flow_from_financing
dataset: analyst4
best_template: rank_level
best_sharpe: 0.42
best_fitness: 0.25
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 6
max_drawdown: 0.3313
ann_vol: 0.1027
hit_rate: 0.5182
rolling_sharpe_min: -1.979
rolling_sharpe_max: 5.313
negated_best_sharpe: 0.39
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.03
---
# cash_flow_from_financing (analyst4)

*Cash Flow From Financing - Value*

## Signal Profile
- `rank(cash_flow_from_financing)`: S=0.42, F=0.25, T=2.0%, INFERIOR (TOP500)
- `rank(cash_flow_from_financing / close)`: S=0.37, F=0.21, T=2.3%, INFERIOR (TOP500)
- `rank(ts_delta(cash_flow_from_financing, 5))`: S=0.66, F=0.19, T=36.7%, INFERIOR (TOP3000)
- `-rank(cash_flow_from_financing)`: S=-0.09, F=-0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cash_flow_from_financing, 5))`: S=-0.66, F=-0.19, T=36.7%, INFERIOR (TOP3000)
- `ts_zscore(cash_flow_from_financing, 22)`: S=0.01, F=0.00, T=37.6%, INFERIOR (TOP3000)
- `ts_mean(cash_flow_from_financing, 10)`: S=-0.34, F=-0.19, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(cash_flow_from_financing, 22))`: S=0.58, F=0.25, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * cash_flow_from_financing)`: S=0.15, F=0.05, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * cash_flow_from_financing / close)`: S=0.39, F=0.22, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.45, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.14 (negative), ret=-0.8%
  - 2020: S=4.73 (strong), ret=+35.6%
  - 2021: S=-0.56 (negative), ret=-6.7%
  - 2022: S=-0.92 (negative), ret=-13.2%
  - 2023: S=0.91 (moderate), ret=+7.6%

## Risk & Drawdown
- Max drawdown: 33.13% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +4.6%, volatility 10.3% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.34, excess kurtosis +3.40

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.98, max 5.31, latest 0.94

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +6.68%; worst month: -5.92%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.56
- Sideways: S=-0.02
- Bear: S=3.81

## Negated Direction
Best negated: `rank(-1 * cash_flow_from_financing / close)` S=0.39, F=0.22, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cash_flow_from_financing)`: S=0.15, F=0.05, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * cash_flow_from_financing / close)`: S=0.39, F=0.22, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cash_flow_from_financing, 5))`: S=-0.66, F=-0.19, T=36.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cash_flow_from_financing)` | TOP500 | 0.45 | 0.25 | 33.1% | 40% | bear-only |
| `rank(cash_flow_from_financing / close)` | TOP500 | 0.39 | 0.21 | 41.0% | 60% | bear-only |
| `rank(ts_delta(cash_flow_from_financing, 5))` | TOP3000 | 0.66 | 0.19 | 6.8% | 80% | bear-only |
| `rank(cash_flow_from_financing / close)` | TOP200 | 0.16 | 0.05 | 49.4% | 40% | bear-only |
| `rank(cash_flow_from_financing)` | TOP200 | 0.13 | 0.04 | 44.5% | 40% | bear-only |
| `rank(ts_delta(cash_flow_from_financing, 5))` | TOP1000 | 0.24 | 0.04 | 13.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- cashflow_fin: 0.966 (strongly positively correlated)
- fnd6_newa1v1300_fincf: 0.966 (strongly positively correlated)
- cashflow_dividends: -0.854 (strongly negatively correlated)
- fnd6_newa1v1300_dv: -0.853 (strongly negatively correlated)
- pv13_revere_term_sector_total: -0.834 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
