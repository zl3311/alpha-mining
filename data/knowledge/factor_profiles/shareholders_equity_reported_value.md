---
field: shareholders_equity_reported_value
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.62
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.278
ann_vol: 0.0873
hit_rate: 0.5053
rolling_sharpe_min: -3.156
rolling_sharpe_max: 2.316
negated_best_sharpe: 0.62
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.13
---
# shareholders_equity_reported_value (analyst4)

*Shareholders' Equity - Total Value*

## Signal Profile
- `rank(shareholders_equity_reported_value)`: S=0.24, F=0.10, T=2.3%, INFERIOR (TOP3000)
- `rank(shareholders_equity_reported_value / close)`: S=0.19, F=0.06, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_delta(shareholders_equity_reported_value, 5))`: S=0.19, F=0.03, T=38.3%, INFERIOR (TOP1000)
- `-rank(shareholders_equity_reported_value)`: S=0.04, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(shareholders_equity_reported_value, 5))`: S=0.62, F=0.24, T=36.7%, INFERIOR (TOP3000)
- `ts_zscore(shareholders_equity_reported_value, 22)`: S=0.49, F=0.16, T=40.2%, INFERIOR (TOP3000)
- `ts_mean(shareholders_equity_reported_value, 10)`: S=-0.27, F=-0.14, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(shareholders_equity_reported_value, 22))`: S=0.06, F=0.01, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * shareholders_equity_reported_value)`: S=0.28, F=0.15, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * shareholders_equity_reported_value / close)`: S=0.15, F=0.05, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.23, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.29 (weak), ret=+1.5%
  - 2020: S=-2.13 (negative), ret=-15.1%
  - 2021: S=0.22 (weak), ret=+2.4%
  - 2022: S=1.71 (strong), ret=+17.8%
  - 2023: S=0.42 (weak), ret=+3.4%

## Risk & Drawdown
- Max drawdown: 27.80% over 959 days (recovered)
- Annualized: return +2.0%, volatility 8.7% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew -0.02, excess kurtosis +0.74

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.16, max 2.32, latest 0.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.16%; worst month: -5.24%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.75
- Sideways: S=1.17
- Bear: S=-3.60

## Negated Direction
Best negated: `rank(-1 * ts_delta(shareholders_equity_reported_value, 5))` S=0.62, F=0.24, INFERIOR
Direction gap: +0.13 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * shareholders_equity_reported_value)`: S=0.28, F=0.15, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * shareholders_equity_reported_value / close)`: S=0.15, F=0.05, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(shareholders_equity_reported_value, 5))`: S=0.62, F=0.24, T=36.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(shareholders_equity_reported_value)` | TOP3000 | 0.23 | 0.10 | 27.8% | 80% | bull-only |
| `rank(shareholders_equity_reported_value / close)` | TOP3000 | 0.18 | 0.06 | 11.6% | 40% | bull-only |
| `rank(ts_delta(shareholders_equity_reported_value, 5))` | TOP1000 | 0.20 | 0.03 | 15.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- shareholders_equity_actual_value: 1.000 (strongly positively correlated)
- fnd6_newqv1300_seqq: 0.963 (strongly positively correlated)
- fnd6_newqv1300_teqq: 0.963 (strongly positively correlated)
- fnd6_cptnewqv1300_ceqq: 0.963 (strongly positively correlated)
- equity: 0.963 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
