---
field: fnd6_ivstch
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.71
best_fitness: 0.59
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.3079
ann_vol: 0.2371
hit_rate: 0.4988
rolling_sharpe_min: -0.987
rolling_sharpe_max: 2.225
negated_best_sharpe: 0.45
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.26
---
# fnd6_ivstch (fundamental6)

*Short-Term Investments - Change*

## Signal Profile
- `rank(fnd6_ivstch)`: S=0.59, F=0.30, T=2.4%, INFERIOR (TOP1000)
- `rank(fnd6_ivstch / close)`: S=0.57, F=0.33, T=2.6%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_ivstch, 5))`: S=0.71, F=0.59, T=24.0%, INFERIOR (TOP500)
- `-rank(fnd6_ivstch)`: S=-0.59, F=-0.30, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ivstch, 5))`: S=0.45, F=0.24, T=33.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_ivstch, 22)`: S=0.19, F=0.10, T=13.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ivstch, 10)`: S=0.57, F=0.32, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ivstch, 22))`: S=0.43, F=0.27, T=17.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivstch)`: S=-0.04, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivstch / close)`: S=-0.07, F=-0.01, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.70, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.42 (moderate), ret=+29.2%
  - 2020: S=0.74 (moderate), ret=+17.7%
  - 2021: S=0.21 (weak), ret=+5.4%
  - 2022: S=1.21 (moderate), ret=+34.8%
  - 2023: S=-0.36 (negative), ret=-5.9%

## Risk & Drawdown
- Max drawdown: 30.79% over 489 days (recovered)
- Annualized: return +16.6%, volatility 23.7% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.76, excess kurtosis +11.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 2.23, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +22.92%; worst month: -10.65%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.76
- Sideways: S=1.34
- Bear: S=-0.03

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_ivstch, 5))` S=0.45, F=0.24, INFERIOR
Direction gap: -0.26 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_ivstch)`: S=-0.04, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivstch / close)`: S=-0.07, F=-0.01, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ivstch, 5))`: S=0.45, F=0.24, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_ivstch, 5))` | TOP500 | 0.70 | 0.59 | 30.8% | 80% | mixed |
| `rank(ts_delta(fnd6_ivstch, 5))` | TOP200 | 0.62 | 0.52 | 26.3% | 80% | mixed |
| `rank(fnd6_ivstch / close)` | TOP500 | 0.58 | 0.33 | 13.6% | 60% | mixed |
| `rank(fnd6_ivstch / close)` | TOP1000 | 0.60 | 0.31 | 7.6% | 80% | weak |
| `rank(fnd6_ivstch)` | TOP1000 | 0.60 | 0.30 | 8.0% | 80% | weak |
| `rank(fnd6_ivstch)` | TOP500 | 0.54 | 0.29 | 15.8% | 60% | mixed |
| `rank(fnd6_ivstch / close)` | TOP200 | 0.27 | 0.14 | 21.0% | 60% | weak |
| `rank(fnd6_ivstch)` | TOP200 | 0.26 | 0.13 | 23.3% | 60% | weak |
| `rank(ts_delta(fnd6_ivstch, 5))` | TOP1000 | 0.23 | 0.10 | 40.0% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ivncf: 0.327 (weakly positively correlated)
- cashflow_invst: 0.324 (weakly positively correlated)
- fnd6_optrfr: 0.227 (weakly positively correlated)
- fnd6_recco: 0.217 (weakly positively correlated)
- fnd6_fiao: 0.195 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
