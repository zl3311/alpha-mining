---
field: shareholders_equity_total_2
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.62
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1349
ann_vol: 0.0469
hit_rate: 0.5085
rolling_sharpe_min: -2.054
rolling_sharpe_max: 2.616
negated_best_sharpe: 0.24
negated_best_template: neg_rank_level
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.38
---
# shareholders_equity_total_2 (analyst4)

*Shareholder's Equity - Total Value*

## Signal Profile
- `rank(shareholders_equity_total_2)`: S=0.24, F=0.10, T=1.0%, INFERIOR (TOP3000)
- `rank(shareholders_equity_total_2 / close)`: S=0.23, F=0.08, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(shareholders_equity_total_2, 5))`: S=0.45, F=0.11, T=36.5%, INFERIOR (TOP1000)
- `-rank(shareholders_equity_total_2)`: S=0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(shareholders_equity_total_2, 5))`: S=0.16, F=0.03, T=34.7%, INFERIOR (TOP3000)
- `ts_zscore(shareholders_equity_total_2, 22)`: S=0.62, F=0.24, T=40.4%, INFERIOR (TOP3000)
- `ts_mean(shareholders_equity_total_2, 10)`: S=-0.28, F=-0.13, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(shareholders_equity_total_2, 22))`: S=0.20, F=0.05, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * shareholders_equity_total_2)`: S=0.24, F=0.12, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * shareholders_equity_total_2 / close)`: S=0.22, F=0.09, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.46, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=2.31 (strong), ret=+7.6%
  - 2020: S=-0.83 (negative), ret=-4.2%
  - 2021: S=-0.00 (negative), ret=-0.0%
  - 2022: S=1.61 (strong), ret=+8.6%
  - 2023: S=-0.41 (negative), ret=-1.6%

## Risk & Drawdown
- Max drawdown: 13.49% over 767 days (recovered)
- Annualized: return +2.1%, volatility 4.7% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.10, excess kurtosis +2.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.05, max 2.62, latest -0.53

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +3.90%; worst month: -4.08%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.63
- Sideways: S=-0.26
- Bear: S=-0.18

## Negated Direction
Best negated: `rank(-1 * shareholders_equity_total_2)` S=0.24, F=0.12, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * shareholders_equity_total_2)`: S=0.24, F=0.12, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * shareholders_equity_total_2 / close)`: S=0.22, F=0.09, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(shareholders_equity_total_2, 5))`: S=0.16, F=0.03, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(shareholders_equity_total_2, 5))` | TOP1000 | 0.46 | 0.11 | 13.5% | 40% | mixed |
| `rank(shareholders_equity_total_2)` | TOP3000 | 0.23 | 0.10 | 30.2% | 80% | bull-only |
| `rank(shareholders_equity_total_2 / close)` | TOP3000 | 0.22 | 0.08 | 10.3% | 60% | bull-only |
| `rank(ts_delta(shareholders_equity_total_2, 5))` | TOP500 | 0.36 | 0.08 | 12.4% | 60% | mixed |
| `rank(ts_delta(shareholders_equity_total_2, 5))` | TOP3000 | 0.19 | 0.03 | 12.9% | 60% | bull-only |
| `rank(shareholders_equity_total_2 / close)` | TOP1000 | 0.12 | 0.03 | 15.0% | 20% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_fincf: -0.404 (moderately negatively correlated)
- cashflow_fin: -0.403 (moderately negatively correlated)
- fnd6_newa1v1300_dv: 0.401 (moderately positively correlated)
- cashflow_dividends: 0.400 (weakly positively correlated)
- cash_flow_from_financing: -0.393 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
