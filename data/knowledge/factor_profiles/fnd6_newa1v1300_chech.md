---
field: fnd6_newa1v1300_chech
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.69
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.068
ann_vol: 0.048
hit_rate: 0.5069
rolling_sharpe_min: -0.991
rolling_sharpe_max: 1.933
negated_best_sharpe: 0.69
negated_best_template: rank_neg_delta
negated_best_fitness: 0.44
n_negated_sims: 10
direction_gap: 0.29
---
# fnd6_newa1v1300_chech (fundamental6)

*Cash and Cash Equivalents - Increase/(Decrease)*

## Signal Profile
- `rank(fnd6_newa1v1300_chech)`: S=0.40, F=0.16, T=2.2%, INFERIOR (TOP500)
- `rank(fnd6_newa1v1300_chech / close)`: S=0.29, F=0.12, T=2.8%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newa1v1300_chech, 5))`: S=0.07, F=0.01, T=33.8%, INFERIOR (TOP500)
- `-rank(fnd6_newa1v1300_chech)`: S=-0.06, F=-0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_chech, 5))`: S=0.69, F=0.44, T=32.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_chech, 63)`: S=0.24, F=0.10, T=18.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_chech, 10)`: S=0.27, F=0.09, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_chech, 22))`: S=-0.62, F=-0.36, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_chech)`: S=-0.27, F=-0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_chech / close)`: S=-0.29, F=-0.12, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.41, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.68 (moderate), ret=+1.7%
  - 2020: S=0.55 (moderate), ret=+1.9%
  - 2021: S=0.73 (moderate), ret=+4.5%
  - 2022: S=0.06 (weak), ret=+0.4%
  - 2023: S=0.32 (weak), ret=+1.2%

## Risk & Drawdown
- Max drawdown: 6.80% over 154 days (recovered)
- Annualized: return +2.0%, volatility 4.8% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.67, excess kurtosis +7.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 1.93, latest 0.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +3.05%; worst month: -4.10%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.79
- Sideways: S=0.96
- Bear: S=-0.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_chech, 5))` S=0.69, F=0.44, INFERIOR
Direction gap: +0.29 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_chech)`: S=-0.27, F=-0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_chech / close)`: S=-0.29, F=-0.12, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_chech, 5))`: S=0.69, F=0.44, T=32.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_chech)` | TOP500 | 0.41 | 0.16 | 6.8% | 100% | mixed |
| `rank(fnd6_newa1v1300_chech / close)` | TOP200 | 0.30 | 0.12 | 12.2% | 60% | weak |
| `rank(fnd6_newa1v1300_chech)` | TOP200 | 0.29 | 0.11 | 15.1% | 60% | mixed |
| `rank(fnd6_newa1v1300_chech / close)` | TOP500 | 0.29 | 0.09 | 9.5% | 80% | weak |

## Correlation Notes
Top correlates:
- cashflow: 0.997 (strongly positively correlated)
- fnd2_a_sbcpnargmsptawervl: 0.421 (moderately positively correlated)
- sales_min_guidance_quarterly: 0.359 (weakly positively correlated)
- working_capital: 0.347 (weakly positively correlated)
- fnd6_newqv1300_wcapq: 0.347 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
