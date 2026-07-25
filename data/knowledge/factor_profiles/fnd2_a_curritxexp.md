---
field: fnd2_a_curritxexp
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.82
best_fitness: 0.65
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1662
ann_vol: 0.0854
hit_rate: 0.5134
rolling_sharpe_min: -2.222
rolling_sharpe_max: 2.248
redundancy_cluster: 13
negated_best_sharpe: 0.37
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.45
---
# fnd2_a_curritxexp (fundamental2)

*Income Tax Expense, Current*

## Signal Profile
- `rank(fnd2_a_curritxexp)`: S=0.31, F=0.16, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_a_curritxexp / close)`: S=0.57, F=0.36, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_curritxexp, 5))`: S=0.68, F=0.33, T=34.6%, INFERIOR (TOP3000)
- `-rank(fnd2_a_curritxexp)`: S=-0.11, F=-0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_curritxexp, 5))`: S=0.37, F=0.15, T=34.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_curritxexp, 63)`: S=0.82, F=0.65, T=17.0%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_curritxexp, 10)`: S=0.17, F=0.06, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_curritxexp, 22))`: S=-0.37, F=-0.17, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_curritxexp)`: S=0.06, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_curritxexp / close)`: S=0.04, F=0.01, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.72 (moderate), ret=+3.0%
  - 2020: S=-1.23 (negative), ret=-7.8%
  - 2021: S=0.78 (moderate), ret=+7.9%
  - 2022: S=1.76 (strong), ret=+21.4%
  - 2023: S=-0.17 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 16.62% over 790 days (recovered)
- Annualized: return +4.8%, volatility 8.5% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.06, excess kurtosis +1.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.22, max 2.25, latest -0.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.92%; worst month: -4.32%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.90
- Sideways: S=1.05
- Bear: S=-3.03

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_curritxexp, 5))` S=0.37, F=0.15, INFERIOR
Direction gap: -0.45 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_curritxexp)`: S=0.06, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_curritxexp / close)`: S=0.04, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_curritxexp, 5))`: S=0.37, F=0.15, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_curritxexp / close)` | TOP3000 | 0.56 | 0.36 | 16.6% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_curritxexp, 5))` | TOP3000 | 0.68 | 0.33 | 11.9% | 80% | mixed |
| `rank(ts_delta(fnd2_a_curritxexp, 5))` | TOP1000 | 0.43 | 0.17 | 26.4% | 60% | mixed |
| `rank(fnd2_a_curritxexp)` | TOP3000 | 0.30 | 0.16 | 33.6% | 60% | bull-only |
| `rank(fnd2_a_curritxexp / close)` | TOP1000 | 0.18 | 0.08 | 25.9% | 60% | bull-only |
| `rank(fnd2_a_curritxexp)` | TOP1000 | 0.09 | 0.04 | 41.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_income_taxes_paid_a: 0.970 (strongly positively correlated)
- fnd6_txc: 0.969 (strongly positively correlated)
- fn_income_tax_expense_a: 0.960 (strongly positively correlated)
- ebitda: 0.951 (strongly positively correlated)
- operating_profit_before_interest_tax: 0.951 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
