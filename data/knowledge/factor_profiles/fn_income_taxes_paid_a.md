---
field: fn_income_taxes_paid_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.46
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1726
ann_vol: 0.0831
hit_rate: 0.4972
rolling_sharpe_min: -2.142
rolling_sharpe_max: 2.032
negated_best_sharpe: 0.54
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: 0.08
---
# fn_income_taxes_paid_a (fundamental2)

*The amount of cash paid during the current period to foreign, federal, state, and local authorities as taxes on income.*

## Signal Profile
- `rank(fn_income_taxes_paid_a)`: S=0.25, F=0.12, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_income_taxes_paid_a / close)`: S=0.46, F=0.25, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_income_taxes_paid_a, 5))`: S=0.04, F=0.01, T=34.5%, INFERIOR (TOP1000)
- `-rank(fn_income_taxes_paid_a)`: S=-0.08, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_income_taxes_paid_a, 5))`: S=0.54, F=0.23, T=34.7%, INFERIOR (TOP3000)
- `-ts_zscore(fn_income_taxes_paid_a, 63)`: S=0.37, F=0.20, T=17.5%, INFERIOR (TOP3000)
- `ts_mean(fn_income_taxes_paid_a, 10)`: S=0.11, F=0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_income_taxes_paid_a, 22))`: S=-0.64, F=-0.39, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_taxes_paid_a)`: S=-0.25, F=-0.12, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_taxes_paid_a / close)`: S=-0.46, F=-0.25, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 23F/6P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.45, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.10 (weak), ret=+0.4%
  - 2020: S=-0.99 (negative), ret=-6.2%
  - 2021: S=0.53 (moderate), ret=+5.8%
  - 2022: S=1.69 (strong), ret=+19.0%
  - 2023: S=-0.13 (negative), ret=-0.7%

## Risk & Drawdown
- Max drawdown: 17.26% over 807 days (recovered)
- Annualized: return +3.7%, volatility 8.3% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew +0.12, excess kurtosis +2.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.14, max 2.03, latest -0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.06%; worst month: -4.85%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.87
- Sideways: S=0.71
- Bear: S=-3.18

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_income_taxes_paid_a, 5))` S=0.54, F=0.23, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_income_taxes_paid_a)`: S=-0.25, F=-0.12, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_taxes_paid_a / close)`: S=-0.46, F=-0.25, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_income_taxes_paid_a, 5))`: S=0.54, F=0.23, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_income_taxes_paid_a / close)` | TOP3000 | 0.45 | 0.25 | 17.3% | 60% | bull-only |
| `rank(fn_income_taxes_paid_a)` | TOP3000 | 0.24 | 0.12 | 33.5% | 60% | bull-only |
| `rank(fn_income_taxes_paid_a / close)` | TOP1000 | 0.19 | 0.08 | 26.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_curritxexp: 0.970 (strongly positively correlated)
- fnd6_txc: 0.947 (strongly positively correlated)
- ebitda: 0.946 (strongly positively correlated)
- operating_profit_before_depr_amort: 0.946 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.946 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
