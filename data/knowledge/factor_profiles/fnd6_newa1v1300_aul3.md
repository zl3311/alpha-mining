---
field: fnd6_newa1v1300_aul3
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.92
best_fitness: 0.83
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.0993
ann_vol: 0.0541
hit_rate: 0.5012
rolling_sharpe_min: -2.204
rolling_sharpe_max: 1.774
negated_best_sharpe: 0.92
negated_best_template: rank_neg_delta
negated_best_fitness: 0.83
n_negated_sims: 10
direction_gap: 0.31
---
# fnd6_newa1v1300_aul3 (fundamental6)

*Assets Level 3 (Unobservable)*

## Signal Profile
- `rank(fnd6_newa1v1300_aul3)`: S=0.33, F=0.12, T=2.4%, INFERIOR (TOP1000)
- `rank(fnd6_newa1v1300_aul3 / close)`: S=0.39, F=0.16, T=2.4%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newa1v1300_aul3, 5))`: S=-0.07, F=-0.02, T=33.2%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_aul3)`: S=-0.33, F=-0.12, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aul3, 5))`: S=0.92, F=0.83, T=19.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_aul3, 63)`: S=-0.13, F=-0.06, T=12.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_aul3, 10)`: S=0.61, F=0.36, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_aul3, 22))`: S=-0.60, F=-0.44, T=18.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aul3)`: S=0.30, F=0.14, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aul3 / close)`: S=0.21, F=0.08, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.39, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.12 (negative), ret=-4.2%
  - 2020: S=-0.52 (negative), ret=-3.0%
  - 2021: S=1.02 (moderate), ret=+6.9%
  - 2022: S=1.31 (moderate), ret=+6.9%
  - 2023: S=0.83 (moderate), ret=+3.7%

## Risk & Drawdown
- Max drawdown: 9.93% over 805 days (recovered)
- Annualized: return +2.1%, volatility 5.4% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +1.36, excess kurtosis +14.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.20, max 1.77, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.11%; worst month: -3.52%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.64
- Sideways: S=-0.50
- Bear: S=0.02

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_aul3, 5))` S=0.92, F=0.83, INFERIOR
Direction gap: +0.31 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_aul3)`: S=0.30, F=0.14, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aul3 / close)`: S=0.21, F=0.08, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aul3, 5))`: S=0.92, F=0.83, T=19.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_aul3 / close)` | TOP1000 | 0.39 | 0.16 | 9.9% | 60% | mixed |
| `rank(fnd6_newa1v1300_aul3)` | TOP1000 | 0.34 | 0.12 | 9.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- capital_expenditure_amount: 0.437 (moderately positively correlated)
- total_assets_amount: 0.433 (moderately positively correlated)
- est_shequity: 0.412 (moderately positively correlated)
- est_tot_assets: 0.410 (moderately positively correlated)
- anl4_capex_low: 0.409 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
