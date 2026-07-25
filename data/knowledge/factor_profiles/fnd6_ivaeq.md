---
field: fnd6_ivaeq
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 0.75
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1401
ann_vol: 0.0576
hit_rate: 0.4955
rolling_sharpe_min: -2.376
rolling_sharpe_max: 2.327
negated_best_sharpe: 0.48
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: -0.27
---
# fnd6_ivaeq (fundamental6)

*Investment and Advances - Equity*

## Signal Profile
- `rank(fnd6_ivaeq)`: S=0.31, F=0.12, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_ivaeq / close)`: S=0.39, F=0.17, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_ivaeq, 5))`: S=0.06, F=0.01, T=34.4%, INFERIOR (TOP1000)
- `-rank(fnd6_ivaeq)`: S=-0.21, F=-0.08, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ivaeq, 5))`: S=0.48, F=0.30, T=22.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_ivaeq, 22)`: S=0.50, F=0.41, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ivaeq, 10)`: S=-0.49, F=-0.28, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ivaeq, 22))`: S=0.75, F=0.57, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivaeq)`: S=0.06, F=0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivaeq / close)`: S=0.05, F=0.01, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.38, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.84 (negative), ret=-2.9%
  - 2020: S=-1.94 (negative), ret=-8.5%
  - 2021: S=1.29 (moderate), ret=+8.6%
  - 2022: S=1.61 (strong), ret=+12.9%
  - 2023: S=0.17 (weak), ret=+0.7%

## Risk & Drawdown
- Max drawdown: 14.01% over 932 days (recovered)
- Annualized: return +2.2%, volatility 5.8% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew -0.05, excess kurtosis +1.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.38, max 2.33, latest -0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.68%; worst month: -3.26%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.67
- Sideways: S=0.73
- Bear: S=-2.90

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_ivaeq, 5))` S=0.48, F=0.30, INFERIOR
Direction gap: -0.27 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_ivaeq)`: S=0.06, F=0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivaeq / close)`: S=0.05, F=0.01, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ivaeq, 5))`: S=0.48, F=0.30, T=22.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_ivaeq / close)` | TOP3000 | 0.38 | 0.17 | 14.0% | 60% | bull-only |
| `rank(fnd6_ivaeq / close)` | TOP1000 | 0.30 | 0.13 | 12.9% | 40% | bull-only |
| `rank(fnd6_ivaeq)` | TOP3000 | 0.31 | 0.12 | 17.4% | 60% | bull-only |
| `rank(fnd6_ivaeq)` | TOP1000 | 0.20 | 0.08 | 17.2% | 40% | bull-only |
| `rank(fnd6_ivaeq / close)` | TOP500 | 0.16 | 0.05 | 13.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_txp: 0.881 (strongly positively correlated)
- fn_income_taxes_paid_a: 0.880 (strongly positively correlated)
- est_ebit: 0.875 (strongly positively correlated)
- est_netprofit_adj: 0.871 (strongly positively correlated)
- anl4_netprofita_high: 0.871 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
