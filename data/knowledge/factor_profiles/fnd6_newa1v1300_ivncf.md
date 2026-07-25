---
field: fnd6_newa1v1300_ivncf
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.67
best_fitness: 0.39
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 6
max_drawdown: 0.2182
ann_vol: 0.1723
hit_rate: 0.5182
rolling_sharpe_min: -0.572
rolling_sharpe_max: 2.101
redundancy_cluster: 59
negated_best_sharpe: 0.59
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: -0.08
---
# fnd6_newa1v1300_ivncf (fundamental6)

*Investing Activities - Net Cash Flow*

## Signal Profile
- `rank(fnd6_newa1v1300_ivncf)`: S=0.32, F=0.16, T=2.4%, INFERIOR (TOP200)
- `rank(fnd6_newa1v1300_ivncf / close)`: S=0.27, F=0.12, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newa1v1300_ivncf, 5))`: S=0.67, F=0.39, T=33.6%, INFERIOR (TOP500)
- `-rank(fnd6_newa1v1300_ivncf)`: S=0.23, F=0.08, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ivncf, 5))`: S=-0.72, F=-0.44, T=33.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_ivncf, 63)`: S=-0.10, F=-0.03, T=17.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_ivncf, 10)`: S=-0.12, F=-0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_ivncf, 22))`: S=-0.54, F=-0.28, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ivncf)`: S=0.28, F=0.12, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ivncf / close)`: S=0.59, F=0.34, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.67, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.92 (moderate), ret=+11.8%
  - 2020: S=0.54 (moderate), ret=+8.9%
  - 2021: S=0.01 (weak), ret=+0.2%
  - 2022: S=1.29 (moderate), ret=+27.5%
  - 2023: S=0.62 (moderate), ret=+8.2%

## Risk & Drawdown
- Max drawdown: 21.82% over 341 days (recovered)
- Annualized: return +11.6%, volatility 17.2% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.28, excess kurtosis +4.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.57, max 2.10, latest 0.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +12.60%; worst month: -7.73%
Positive months: 56%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.23
- Sideways: S=1.59
- Bear: S=0.28

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_ivncf / close)` S=0.59, F=0.34, INFERIOR
Direction gap: -0.08 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_ivncf)`: S=0.28, F=0.12, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ivncf / close)`: S=0.59, F=0.34, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ivncf, 5))`: S=-0.72, F=-0.44, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_ivncf, 5))` | TOP500 | 0.67 | 0.39 | 21.8% | 100% | weak |
| `rank(ts_delta(fnd6_newa1v1300_ivncf, 5))` | TOP200 | 0.53 | 0.30 | 34.2% | 60% | weak |
| `rank(ts_delta(fnd6_newa1v1300_ivncf, 5))` | TOP3000 | 0.70 | 0.29 | 14.8% | 80% | all-weather |
| `rank(fnd6_newa1v1300_ivncf)` | TOP200 | 0.35 | 0.16 | 26.3% | 80% | bear-only |
| `rank(fnd6_newa1v1300_ivncf / close)` | TOP200 | 0.29 | 0.12 | 19.3% | 20% | bear-only |
| `rank(ts_delta(fnd6_newa1v1300_ivncf, 5))` | TOP1000 | 0.29 | 0.08 | 25.7% | 60% | weak |

## Correlation Notes
Top correlates:
- cashflow_invst: 0.987 (strongly positively correlated)
- fnd6_ivstch: 0.327 (weakly positively correlated)
- fnd6_optca: 0.200 (weakly positively correlated)
- fnd2_dfdfritxexp: 0.173 (weakly positively correlated)
- fnd6_ivst: -0.156 (weakly negatively correlated)

Redundancy cluster #59: 2 similar fields, mean |rho| 0.987 (representative: cashflow_invst). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
