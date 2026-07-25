---
field: fn_derivative_fair_value_of_derivative_asset_q
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.78
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0385
ann_vol: 0.0353
hit_rate: 0.5101
rolling_sharpe_min: -0.509
rolling_sharpe_max: 2.018
negated_best_sharpe: 0.7
negated_best_template: neg_rank_level
negated_best_fitness: 0.48
n_negated_sims: 10
direction_gap: -0.08
---
# fn_derivative_fair_value_of_derivative_asset_q (fundamental2)

*Fair value, before effects of master netting arrangements, of a financial asset or other contract with one or more underlyings, notional amount or payment provision or both, and the contract can be net settled by means outside the contract or delivery of an asset. Includes assets elected not to be offset. Excludes assets not subject to a master netting arrangement.*

## Signal Profile
- `rank(fn_derivative_fair_value_of_derivative_asset_q)`: S=0.38, F=0.14, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_derivative_fair_value_of_derivative_asset_q / close)`: S=0.64, F=0.27, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_derivative_fair_value_of_derivative_asset_q, 5))`: S=0.33, F=0.13, T=37.1%, INFERIOR (TOP200)
- `-rank(fn_derivative_fair_value_of_derivative_asset_q)`: S=-0.39, F=-0.14, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_derivative_fair_value_of_derivative_asset_q, 5))`: S=-0.28, F=-0.10, T=37.0%, INFERIOR (TOP3000)
- `ts_zscore(fn_derivative_fair_value_of_derivative_asset_q, 22)`: S=0.78, F=0.48, T=32.4%, INFERIOR (TOP3000)
- `ts_mean(fn_derivative_fair_value_of_derivative_asset_q, 10)`: S=-0.15, F=-0.05, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_derivative_fair_value_of_derivative_asset_q, 22))`: S=0.20, F=0.06, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_fair_value_of_derivative_asset_q)`: S=0.70, F=0.48, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_fair_value_of_derivative_asset_q / close)`: S=0.44, F=0.24, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.64, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.56 (moderate), ret=+1.5%
  - 2020: S=-0.13 (negative), ret=-0.5%
  - 2021: S=1.06 (moderate), ret=+4.3%
  - 2022: S=0.05 (weak), ret=+0.2%
  - 2023: S=1.86 (strong), ret=+5.7%

## Risk & Drawdown
- Max drawdown: 3.85% over 433 days (recovered)
- Annualized: return +2.3%, volatility 3.5% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.53, excess kurtosis +2.70

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.51, max 2.02, latest 1.94

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +2.15%; worst month: -2.44%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.60
- Sideways: S=0.45
- Bear: S=-0.18

## Negated Direction
Best negated: `rank(-1 * fn_derivative_fair_value_of_derivative_asset_q)` S=0.70, F=0.48, INFERIOR
Direction gap: -0.08 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_derivative_fair_value_of_derivative_asset_q)`: S=0.70, F=0.48, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_derivative_fair_value_of_derivative_asset_q / close)`: S=0.44, F=0.24, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_derivative_fair_value_of_derivative_asset_q, 5))`: S=-0.28, F=-0.10, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_derivative_fair_value_of_derivative_asset_q / close)` | TOP3000 | 0.64 | 0.27 | 3.9% | 80% | mixed |
| `rank(fn_derivative_fair_value_of_derivative_asset_q / close)` | TOP1000 | 0.58 | 0.27 | 6.7% | 80% | mixed |
| `rank(fn_derivative_fair_value_of_derivative_asset_q)` | TOP1000 | 0.39 | 0.14 | 12.7% | 80% | bull-only |
| `rank(fn_derivative_fair_value_of_derivative_asset_q)` | TOP3000 | 0.37 | 0.14 | 12.4% | 80% | bull-only |
| `rank(ts_delta(fn_derivative_fair_value_of_derivative_asset_q, 5))` | TOP200 | 0.33 | 0.13 | 24.8% | 80% | mixed |
| `rank(fn_derivative_fair_value_of_derivative_asset_q / close)` | TOP500 | 0.14 | 0.03 | 13.5% | 80% | mixed |
| `rank(ts_delta(fn_derivative_fair_value_of_derivative_asset_q, 5))` | TOP500 | 0.11 | 0.02 | 20.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_derivative_fair_value_of_derivative_asset_a: 0.818 (strongly positively correlated)
- fn_derivative_notional_amount_a: 0.712 (strongly positively correlated)
- est_tot_assets: 0.696 (moderately positively correlated)
- fn_derivative_notional_amount_q: 0.695 (moderately positively correlated)
- anl4_totassets_high: 0.694 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
