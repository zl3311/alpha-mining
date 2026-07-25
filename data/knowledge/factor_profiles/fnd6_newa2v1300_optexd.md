---
field: fnd6_newa2v1300_optexd
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.59
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.159
ann_vol: 0.103
hit_rate: 0.5077
rolling_sharpe_min: -0.843
rolling_sharpe_max: 2.187
negated_best_sharpe: 0.73
negated_best_template: rank_neg_delta
negated_best_fitness: 0.42
n_negated_sims: 10
direction_gap: 0.14
---
# fnd6_newa2v1300_optexd (fundamental6)

*Options - Exercised (-)*

## Signal Profile
- `rank(fnd6_newa2v1300_optexd)`: S=0.32, F=0.17, T=3.6%, INFERIOR (TOP200)
- `rank(fnd6_newa2v1300_optexd / close)`: S=0.39, F=0.22, T=3.8%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newa2v1300_optexd, 5))`: S=-0.01, F=0.00, T=21.0%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_optexd)`: S=0.06, F=0.01, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_optexd, 5))`: S=0.73, F=0.42, T=40.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_optexd, 63)`: S=0.59, F=0.45, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_optexd, 10)`: S=0.35, F=0.17, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_optexd, 22))`: S=-0.17, F=-0.06, T=20.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_optexd)`: S=0.13, F=0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_optexd / close)`: S=0.13, F=0.03, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.40, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.03 (negative), ret=-0.2%
  - 2020: S=2.01 (strong), ret=+18.5%
  - 2021: S=0.22 (weak), ret=+2.1%
  - 2022: S=-0.60 (negative), ret=-8.7%
  - 2023: S=0.91 (moderate), ret=+8.5%

## Risk & Drawdown
- Max drawdown: 15.90% over 640 days (not yet recovered, ongoing at window end)
- Annualized: return +4.1%, volatility 10.3% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.19, excess kurtosis +2.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.84, max 2.19, latest 1.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +8.58%; worst month: -6.93%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.18
- Sideways: S=0.07
- Bear: S=0.94

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_optexd, 5))` S=0.73, F=0.42, INFERIOR
Direction gap: +0.14 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_optexd)`: S=0.13, F=0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_optexd / close)`: S=0.13, F=0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_optexd, 5))`: S=0.73, F=0.42, T=40.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_optexd / close)` | TOP200 | 0.40 | 0.22 | 15.9% | 60% | mixed |
| `rank(fnd6_newa2v1300_optexd)` | TOP200 | 0.33 | 0.17 | 14.4% | 60% | weak |
| `rank(fnd6_newa2v1300_optexd / close)` | TOP500 | 0.37 | 0.17 | 13.4% | 60% | mixed |
| `rank(fnd6_newa2v1300_optexd)` | TOP500 | 0.18 | 0.06 | 9.8% | 80% | mixed |
| `rank(fnd6_newa2v1300_optexd / close)` | TOP1000 | 0.19 | 0.06 | 15.7% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_optex: 0.836 (strongly positively correlated)
- fn_comp_options_out_intrinsic_value_a: 0.643 (moderately positively correlated)
- fn_comp_options_out_number_q: 0.569 (moderately positively correlated)
- fn_proceeds_from_stock_options_exercised_q: 0.532 (moderately positively correlated)
- fnd6_optosey: 0.500 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
