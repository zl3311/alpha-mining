---
field: fnd6_pifo
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.5
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.287
ann_vol: 0.0895
hit_rate: 0.5036
rolling_sharpe_min: -3.5
rolling_sharpe_max: 2.361
negated_best_sharpe: 0.5
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: 0.31
---
# fnd6_pifo (fundamental6)

*Pretax Income - Foreign*

## Signal Profile
- `rank(fnd6_pifo)`: S=0.10, F=0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_pifo / close)`: S=0.19, F=0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_pifo, 5))`: S=-0.02, F=0.00, T=43.7%, INFERIOR (TOP3000)
- `-rank(fnd6_pifo)`: S=0.02, F=0.00, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_pifo, 5))`: S=0.50, F=0.26, T=34.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_pifo, 63)`: S=-0.32, F=-0.19, T=18.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_pifo, 10)`: S=0.15, F=0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_pifo, 22))`: S=-0.15, F=-0.05, T=20.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pifo)`: S=0.22, F=0.10, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pifo / close)`: S=0.17, F=0.07, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.18, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.15 (weak), ret=+0.7%
  - 2020: S=-2.32 (negative), ret=-14.3%
  - 2021: S=0.82 (moderate), ret=+8.6%
  - 2022: S=1.17 (moderate), ret=+14.9%
  - 2023: S=-0.29 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 28.70% over 911 days (recovered)
- Annualized: return +1.6%, volatility 8.9% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.02, excess kurtosis +1.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.50, max 2.36, latest -0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.42%; worst month: -7.88%
Positive months: 46%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.61
- Sideways: S=0.44
- Bear: S=-3.34

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_pifo, 5))` S=0.50, F=0.26, INFERIOR
Direction gap: +0.31 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_pifo)`: S=0.22, F=0.10, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pifo / close)`: S=0.17, F=0.07, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_pifo, 5))`: S=0.50, F=0.26, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_pifo / close)` | TOP3000 | 0.18 | 0.07 | 28.7% | 60% | bull-only |
| `rank(fnd6_pifo)` | TOP3000 | 0.09 | 0.03 | 39.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pretax_income_total: 0.934 (strongly positively correlated)
- net_income_total_2: 0.933 (strongly positively correlated)
- fnd6_ci: 0.930 (strongly positively correlated)
- net_income_adjusted: 0.927 (strongly positively correlated)
- free_cash_flow_total: 0.918 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
