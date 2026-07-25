---
field: fnd6_newa2v1300_txp
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.41
best_fitness: 0.23
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1555
ann_vol: 0.0625
hit_rate: 0.5036
rolling_sharpe_min: -2.454
rolling_sharpe_max: 2.024
negated_best_sharpe: 0.41
negated_best_template: neg_rank_level
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: 0.23
---
# fnd6_newa2v1300_txp (fundamental6)

*Income Taxes Payable*

## Signal Profile
- `rank(fnd6_newa2v1300_txp)`: S=0.12, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_txp / close)`: S=0.18, F=0.05, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_txp, 5))`: S=-0.05, F=-0.01, T=35.7%, INFERIOR (TOP3000)
- `-rank(fnd6_newa2v1300_txp)`: S=0.01, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_txp, 5))`: S=0.00, F=0.00, T=27.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_txp, 63)`: S=0.11, F=0.04, T=17.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_txp, 10)`: S=-0.27, F=-0.12, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_txp, 22))`: S=-0.72, F=-0.45, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txp)`: S=0.41, F=0.23, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txp / close)`: S=0.41, F=0.23, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.18, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.98 (negative), ret=-3.5%
  - 2020: S=-1.73 (negative), ret=-8.1%
  - 2021: S=0.71 (moderate), ret=+4.9%
  - 2022: S=1.28 (moderate), ret=+11.3%
  - 2023: S=0.18 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 15.55% over 1094 days (recovered)
- Annualized: return +1.1%, volatility 6.2% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.14, excess kurtosis +1.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.45, max 2.02, latest -0.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.61%; worst month: -4.13%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.96
- Sideways: S=0.55
- Bear: S=-3.70

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_txp)` S=0.41, F=0.23, INFERIOR
Direction gap: +0.23 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_txp)`: S=0.41, F=0.23, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txp / close)`: S=0.41, F=0.23, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_txp, 5))`: S=0.00, F=0.00, T=27.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_txp / close)` | TOP3000 | 0.18 | 0.05 | 15.6% | 60% | bull-only |
| `rank(fnd6_newa2v1300_txp)` | TOP3000 | 0.12 | 0.03 | 20.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txdba: 0.884 (strongly positively correlated)
- fnd6_ivaeq: 0.881 (strongly positively correlated)
- est_netprofit: 0.878 (strongly positively correlated)
- fn_income_taxes_paid_a: 0.878 (strongly positively correlated)
- est_ebit: 0.877 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
