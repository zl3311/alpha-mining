---
field: fn_proceeds_from_lt_debt_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.68
best_fitness: 0.41
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: mixed
n_variations_with_pnl: 11
max_drawdown: 0.0949
ann_vol: 0.0681
hit_rate: 0.5182
rolling_sharpe_min: -0.94
rolling_sharpe_max: 1.956
negated_best_sharpe: -0.08
negated_best_template: rank_neg_delta
negated_best_fitness: -0.02
n_negated_sims: 4
direction_gap: -0.76
---
# fn_proceeds_from_lt_debt_a (fundamental2)

*Proceeds From Issuance Of Debt, Long Term*

## Signal Profile
- `rank(fn_proceeds_from_lt_debt_a)`: S=0.64, F=0.39, T=2.2%, INFERIOR (TOP200)
- `rank(fn_proceeds_from_lt_debt_a / close)`: S=0.68, F=0.41, T=2.3%, INFERIOR (TOP200)
- `rank(ts_delta(fn_proceeds_from_lt_debt_a, 5))`: S=0.33, F=0.18, T=20.2%, INFERIOR (TOP200)
- `-rank(fn_proceeds_from_lt_debt_a)`: S=-0.39, F=-0.17, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_lt_debt_a, 5))`: S=-0.08, F=-0.02, T=32.3%, INFERIOR (TOP3000)
- `ts_zscore(fn_proceeds_from_lt_debt_a, 22)`: S=0.44, F=0.28, T=9.2%, INFERIOR (TOP3000)
- `ts_mean(fn_proceeds_from_lt_debt_a, 10)`: S=0.13, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_proceeds_from_lt_debt_a, 22))`: S=-0.05, F=-0.01, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_lt_debt_a)`: S=-0.35, F=-0.15, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_lt_debt_a / close)`: S=-0.60, F=-0.30, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/16P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/16P
- LOW_TURNOVER: 2F/24P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.69, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.31 (moderate), ret=+6.6%
  - 2020: S=0.55 (moderate), ret=+4.0%
  - 2021: S=0.51 (moderate), ret=+4.0%
  - 2022: S=0.60 (moderate), ret=+4.2%
  - 2023: S=0.73 (moderate), ret=+4.1%

## Risk & Drawdown
- Max drawdown: 9.49% over 346 days (recovered)
- Annualized: return +4.7%, volatility 6.8% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.28, excess kurtosis +1.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.94, max 1.96, latest 0.69

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +4.09%; worst month: -3.73%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.51
- Sideways: S=1.53
- Bear: S=0.12

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_proceeds_from_lt_debt_a, 5))` S=-0.08, F=-0.02, INFERIOR
Direction gap: -0.76 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_proceeds_from_lt_debt_a)`: S=-0.35, F=-0.15, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_lt_debt_a / close)`: S=-0.60, F=-0.30, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_lt_debt_a, 5))`: S=-0.08, F=-0.02, T=32.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_proceeds_from_lt_debt_a / close)` | TOP200 | 0.69 | 0.41 | 9.5% | 100% | mixed |
| `rank(fn_proceeds_from_lt_debt_a)` | TOP200 | 0.63 | 0.39 | 10.1% | 100% | mixed |
| `rank(fn_proceeds_from_lt_debt_a / close)` | TOP3000 | 0.59 | 0.30 | 9.5% | 80% | mixed |
| `rank(fn_proceeds_from_lt_debt_a / close)` | TOP1000 | 0.56 | 0.30 | 7.3% | 80% | mixed |
| `rank(ts_delta(fn_proceeds_from_lt_debt_a, 5))` | TOP200 | 0.32 | 0.18 | 37.6% | 80% | mixed |
| `rank(fn_proceeds_from_lt_debt_a)` | TOP1000 | 0.38 | 0.17 | 11.2% | 80% | bull-only |
| `rank(fn_proceeds_from_lt_debt_a)` | TOP3000 | 0.34 | 0.15 | 14.9% | 60% | bull-only |
| `rank(fn_proceeds_from_lt_debt_a / close)` | TOP500 | 0.34 | 0.14 | 9.2% | 40% | bull-only |
| `rank(ts_delta(fn_proceeds_from_lt_debt_a, 5))` | TOP3000 | 0.18 | 0.06 | 31.3% | 40% | mixed |
| `rank(fn_proceeds_from_lt_debt_a)` | TOP500 | 0.16 | 0.05 | 16.4% | 80% | bull-only |
| `rank(ts_delta(fn_proceeds_from_lt_debt_a, 5))` | TOP500 | 0.10 | 0.03 | 32.5% | 40% | mixed |

## Correlation Notes
Top correlates:
- fn_debt_instrument_face_amount_q: 0.456 (moderately positively correlated)
- fnd6_newa2v1300_stkco: 0.449 (moderately positively correlated)
- fnd6_newa1v1300_cshi: 0.444 (moderately positively correlated)
- fnd6_cshpri: 0.444 (moderately positively correlated)
- fnd6_newa1v1300_cshfd: 0.443 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
