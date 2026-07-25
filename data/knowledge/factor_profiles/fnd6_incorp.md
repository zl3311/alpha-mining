---
field: fnd6_incorp
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.68
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.2148
ann_vol: 0.0866
hit_rate: 0.5223
rolling_sharpe_min: -2.754
rolling_sharpe_max: 2.173
negated_best_sharpe: 0.68
negated_best_template: rank_neg_delta
negated_best_fitness: 0.6
n_negated_sims: 10
direction_gap: 0.04
---
# fnd6_incorp (fundamental6)

*Incorporated*

## Signal Profile
- `rank(fnd6_incorp)`: S=0.56, F=0.36, T=1.9%, INFERIOR (TOP200)
- `rank(fnd6_incorp / close)`: S=0.64, F=0.43, T=2.1%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_incorp, 5))`: S=0.06, F=0.02, T=11.1%, INFERIOR (TOP3000)
- `-rank(fnd6_incorp)`: S=-0.21, F=-0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_incorp, 5))`: S=0.68, F=0.60, T=4.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_incorp, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_incorp, 10)`: S=-0.30, F=-0.10, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_incorp, 22))`: S=-0.48, F=-0.51, T=6.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_incorp)`: S=-0.19, F=-0.06, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_incorp / close)`: S=-0.30, F=-0.12, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/14P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.64, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.09 (weak), ret=+0.5%
  - 2020: S=-0.80 (negative), ret=-7.4%
  - 2021: S=1.33 (moderate), ret=+14.5%
  - 2022: S=1.17 (moderate), ret=+10.9%
  - 2023: S=1.42 (moderate), ret=+8.8%

## Risk & Drawdown
- Max drawdown: 21.48% over 644 days (recovered)
- Annualized: return +5.6%, volatility 8.7% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew -0.26, excess kurtosis +4.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.75, max 2.17, latest 1.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +5.42%; worst month: -6.70%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.85
- Sideways: S=0.45
- Bear: S=0.59

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_incorp, 5))` S=0.68, F=0.60, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_incorp)`: S=-0.19, F=-0.06, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_incorp / close)`: S=-0.30, F=-0.12, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_incorp, 5))`: S=0.68, F=0.60, T=4.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_incorp / close)` | TOP200 | 0.64 | 0.43 | 21.5% | 80% | all-weather |
| `rank(fnd6_incorp)` | TOP200 | 0.56 | 0.36 | 19.2% | 60% | bull-only |
| `rank(fnd6_incorp)` | TOP3000 | 0.33 | 0.14 | 9.5% | 60% | weak |
| `rank(fnd6_incorp / close)` | TOP500 | 0.30 | 0.12 | 12.5% | 80% | mixed |
| `rank(fnd6_incorp / close)` | TOP1000 | 0.25 | 0.10 | 13.8% | 60% | bear-only |
| `rank(fnd6_incorp)` | TOP1000 | 0.20 | 0.07 | 10.4% | 60% | weak |
| `rank(fnd6_incorp)` | TOP500 | 0.17 | 0.06 | 13.0% | 60% | weak |
| `rank(fnd6_incorp / close)` | TOP3000 | 0.14 | 0.05 | 20.4% | 40% | bear-only |
| `rank(ts_delta(fnd6_incorp, 5))` | TOP3000 | 0.06 | 0.02 | 52.7% | 40% | mixed |

## Correlation Notes
Top correlates:
- fn_entity_common_stock_shares_out_q: 0.462 (moderately positively correlated)
- fnd6_newa2v1300_spi: -0.459 (moderately negatively correlated)
- anl4_capex_number: 0.455 (moderately positively correlated)
- reporting_currency_code_9: 0.454 (moderately positively correlated)
- fn_comp_options_exercises_weighted_avg_a: 0.445 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
