---
field: fnd6_newa1v1300_ceq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.69
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0866
ann_vol: 0.0697
hit_rate: 0.4761
rolling_sharpe_min: -0.951
rolling_sharpe_max: 2.006
negated_best_sharpe: 0.26
negated_best_template: neg_rank_level
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.43
---
# fnd6_newa1v1300_ceq (fundamental6)

*Common/Ordinary Equity - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_ceq)`: S=0.43, F=0.25, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_ceq / close)`: S=0.48, F=0.25, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_ceq, 5))`: S=0.23, F=0.09, T=32.7%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_ceq)`: S=-0.13, F=-0.05, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ceq, 5))`: S=-0.21, F=-0.08, T=32.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_ceq, 63)`: S=0.69, F=0.47, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_ceq, 10)`: S=0.06, F=0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_ceq, 22))`: S=0.07, F=0.01, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ceq)`: S=0.26, F=0.14, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ceq / close)`: S=0.19, F=0.08, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.48, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.34 (negative), ret=-1.5%
  - 2020: S=-0.14 (negative), ret=-1.1%
  - 2021: S=0.98 (moderate), ret=+8.7%
  - 2022: S=0.81 (moderate), ret=+5.5%
  - 2023: S=0.90 (moderate), ret=+4.7%

## Risk & Drawdown
- Max drawdown: 8.66% over 270 days (recovered)
- Annualized: return +3.3%, volatility 7.0% (fraction of booksize)
- Hit rate: 47.6% positive days
- Tail shape: skew +0.76, excess kurtosis +4.25

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.95, max 2.01, latest 0.99

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.38%; worst month: -3.20%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.17
- Sideways: S=0.11
- Bear: S=-1.29

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_ceq)` S=0.26, F=0.14, INFERIOR
Direction gap: -0.43 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_ceq)`: S=0.26, F=0.14, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ceq / close)`: S=0.19, F=0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ceq, 5))`: S=-0.21, F=-0.08, T=32.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_ceq / close)` | TOP3000 | 0.48 | 0.25 | 8.7% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ceq)` | TOP3000 | 0.42 | 0.25 | 31.0% | 80% | bull-only |
| `rank(fnd6_newa1v1300_ceq / close)` | TOP1000 | 0.32 | 0.15 | 13.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_ceq, 5))` | TOP200 | 0.23 | 0.09 | 87.2% | 60% | weak |
| `rank(ts_delta(fnd6_newa1v1300_ceq, 5))` | TOP1000 | 0.23 | 0.06 | 16.5% | 80% | mixed |
| `rank(fnd6_newa1v1300_ceq)` | TOP1000 | 0.12 | 0.05 | 33.4% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ceq / close)` | TOP500 | 0.09 | 0.03 | 26.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_seq: 0.997 (strongly positively correlated)
- fnd6_teq: 0.997 (strongly positively correlated)
- fnd6_ceql: 0.996 (strongly positively correlated)
- fnd6_newa1v1300_icapt: 0.968 (strongly positively correlated)
- fnd6_newa1v1300_at: 0.958 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
