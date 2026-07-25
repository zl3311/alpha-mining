---
field: fnd6_lul3
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 1.16
best_fitness: 1.01
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.2955
ann_vol: 0.0938
hit_rate: 0.4907
rolling_sharpe_min: -2.51
rolling_sharpe_max: 2.076
negated_best_sharpe: 1.16
negated_best_template: rank_neg_delta
negated_best_fitness: 1.01
n_negated_sims: 10
direction_gap: 0.63
---
# fnd6_lul3 (fundamental6)

*Liabilities Level 3 (Unobservable)*

## Signal Profile
- `rank(fnd6_lul3)`: S=0.04, F=0.01, T=3.3%, INFERIOR (TOP200)
- `rank(fnd6_lul3 / close)`: S=0.08, F=0.02, T=3.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_lul3, 5))`: S=-0.12, F=-0.03, T=36.3%, INFERIOR (TOP3000)
- `-rank(fnd6_lul3)`: S=0.42, F=0.15, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lul3, 5))`: S=1.16, F=1.01, T=25.9%, AVERAGE (TOP3000)
- `ts_zscore(fnd6_lul3, 22)`: S=0.53, F=0.57, T=11.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_lul3, 10)`: S=0.53, F=0.28, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_lul3, 22))`: S=-0.10, F=-0.03, T=19.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lul3)`: S=0.42, F=0.15, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lul3 / close)`: S=0.41, F=0.15, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 29F/3P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.10, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.90 (moderate), ret=+5.7%
  - 2020: S=-0.03 (negative), ret=-0.2%
  - 2021: S=-1.80 (negative), ret=-22.1%
  - 2022: S=0.87 (moderate), ret=+8.9%
  - 2023: S=1.90 (strong), ret=+12.2%

## Risk & Drawdown
- Max drawdown: 29.55% over 1186 days (not yet recovered, ongoing at window end)
- Annualized: return +0.9%, volatility 9.4% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.09, excess kurtosis +2.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.51, max 2.08, latest 1.93

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +5.58%; worst month: -7.26%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.51
- Sideways: S=-0.14
- Bear: S=-0.13

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_lul3, 5))` S=1.16, F=1.01, AVERAGE
Direction gap: +0.63 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_lul3)`: S=0.42, F=0.15, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lul3 / close)`: S=0.41, F=0.15, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lul3, 5))`: S=1.16, F=1.01, T=25.9%, AVERAGE (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_lul3 / close)` | TOP200 | 0.10 | 0.02 | 29.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- pcr_oi_120: -0.203 (weakly negatively correlated)
- fnd6_optlifeq: 0.200 (weakly positively correlated)
- fnd6_newa2v1300_mii: -0.199 (weakly negatively correlated)
- pcr_oi_20: -0.187 (weakly negatively correlated)
- pcr_oi_10: -0.186 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
