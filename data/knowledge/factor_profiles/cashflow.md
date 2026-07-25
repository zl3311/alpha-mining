---
field: cashflow
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.63
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 36
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0722
ann_vol: 0.0479
hit_rate: 0.5045
rolling_sharpe_min: -1.14
rolling_sharpe_max: 1.854
negated_best_sharpe: 0.63
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.29
---
# cashflow (fundamental6)

*Cashflow (Annual)*

## Signal Profile
- `rank(cashflow)`: S=0.34, F=0.12, T=2.2%, INFERIOR (TOP500)
- `rank(cashflow / close)`: S=0.23, F=0.08, T=2.8%, INFERIOR (TOP200)
- `rank(ts_delta(cashflow, 5))`: S=-0.02, F=0.00, T=33.9%, INFERIOR (TOP500)
- `ts_decay_linear(rank(cashflow), 5)`: S=-0.29, F=-0.08, T=1.6%, INFERIOR (TOP3000)
- `-rank(cashflow)`: S=-0.03, F=0.00, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow, 5))`: S=0.63, F=0.30, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(cashflow, 63)`: S=0.27, F=0.12, T=18.4%, INFERIOR (TOP3000)
- `ts_mean(cashflow, 10)`: S=0.30, F=0.11, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow, 22))`: S=-0.58, F=-0.32, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * cashflow)`: S=-0.03, F=0.00, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * cashflow / close)`: S=0.11, F=0.02, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/23P
- LOW_FITNESS: 36F/0P
- LOW_SHARPE: 36F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/19P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.35, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.55 (moderate), ret=+1.4%
  - 2020: S=0.41 (weak), ret=+1.5%
  - 2021: S=0.61 (moderate), ret=+3.7%
  - 2022: S=0.09 (weak), ret=+0.6%
  - 2023: S=0.27 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 7.22% over 154 days (recovered)
- Annualized: return +1.7%, volatility 4.8% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.70, excess kurtosis +7.41

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.14, max 1.85, latest 0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +2.92%; worst month: -4.32%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=0.82
- Sideways: S=0.89
- Bear: S=-0.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(cashflow, 5))` S=0.63, F=0.30, INFERIOR
Direction gap: +0.29 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * cashflow)`: S=-0.03, F=0.00, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * cashflow / close)`: S=0.11, F=0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow, 5))`: S=0.63, F=0.30, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cashflow)` | TOP500 | 0.35 | 0.12 | 7.2% | 100% | bull-only |
| `rank(cashflow / close)` | TOP200 | 0.25 | 0.08 | 12.8% | 40% | weak |
| `rank(cashflow / close)` | TOP500 | 0.23 | 0.07 | 10.1% | 80% | weak |
| `rank(cashflow)` | TOP200 | 0.22 | 0.07 | 17.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_chech: 0.997 (strongly positively correlated)
- fnd2_a_sbcpnargmsptawervl: 0.413 (moderately positively correlated)
- sales_min_guidance_quarterly: 0.359 (weakly positively correlated)
- working_capital: 0.357 (weakly positively correlated)
- fnd6_newqv1300_wcapq: 0.357 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
