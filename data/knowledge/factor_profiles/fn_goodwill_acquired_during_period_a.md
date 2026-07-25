---
field: fn_goodwill_acquired_during_period_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 1.16
best_fitness: 1.64
best_universe: TOP3000
grade: GOOD
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1762
ann_vol: 0.0774
hit_rate: 0.5061
rolling_sharpe_min: -1.802
rolling_sharpe_max: 1.948
negated_best_sharpe: 0.86
negated_best_template: neg_rank_level
negated_best_fitness: 0.49
n_negated_sims: 10
direction_gap: -0.3
---
# fn_goodwill_acquired_during_period_a (fundamental2)

*Amount of increase in asset representing future economic benefits arising from other assets acquired in a business combination that are not individually identified and separately recognized resulting from a business combination.*

## Signal Profile
- `rank(fn_goodwill_acquired_during_period_a)`: S=0.15, F=0.05, T=2.3%, INFERIOR (TOP200)
- `rank(fn_goodwill_acquired_during_period_a / close)`: S=0.28, F=0.12, T=2.4%, INFERIOR (TOP200)
- `rank(ts_delta(fn_goodwill_acquired_during_period_a, 5))`: S=0.24, F=0.08, T=32.2%, INFERIOR (TOP500)
- `-rank(fn_goodwill_acquired_during_period_a)`: S=0.73, F=0.34, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_goodwill_acquired_during_period_a, 5))`: S=-0.16, F=-0.05, T=32.2%, INFERIOR (TOP3000)
- `-ts_zscore(fn_goodwill_acquired_during_period_a, 63)`: S=1.16, F=1.64, T=14.2%, GOOD (TOP3000)
- `ts_mean(fn_goodwill_acquired_during_period_a, 10)`: S=-0.67, F=-0.39, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_goodwill_acquired_during_period_a, 22))`: S=0.42, F=0.23, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_goodwill_acquired_during_period_a)`: S=0.86, F=0.49, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_goodwill_acquired_during_period_a / close)`: S=0.61, F=0.29, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.29, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.38 (weak), ret=+1.8%
  - 2020: S=-0.19 (negative), ret=-1.8%
  - 2021: S=-0.57 (negative), ret=-4.5%
  - 2022: S=0.63 (moderate), ret=+5.5%
  - 2023: S=1.78 (strong), ret=+10.1%

## Risk & Drawdown
- Max drawdown: 17.62% over 924 days (recovered)
- Annualized: return +2.3%, volatility 7.7% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.01, excess kurtosis +3.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.80, max 1.95, latest 1.90

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +5.34%; worst month: -5.92%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.33
- Sideways: S=-0.17
- Bear: S=-0.36

## Negated Direction
Best negated: `rank(-1 * fn_goodwill_acquired_during_period_a)` S=0.86, F=0.49, INFERIOR
Direction gap: -0.30 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_goodwill_acquired_during_period_a)`: S=0.86, F=0.49, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_goodwill_acquired_during_period_a / close)`: S=0.61, F=0.29, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_goodwill_acquired_during_period_a, 5))`: S=-0.16, F=-0.05, T=32.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_goodwill_acquired_during_period_a / close)` | TOP200 | 0.29 | 0.12 | 17.6% | 60% | mixed |
| `rank(fn_goodwill_acquired_during_period_a / close)` | TOP3000 | 0.28 | 0.09 | 11.2% | 80% | weak |
| `rank(ts_delta(fn_goodwill_acquired_during_period_a, 5))` | TOP500 | 0.23 | 0.08 | 34.2% | 40% | mixed |
| `rank(fn_goodwill_acquired_during_period_a)` | TOP200 | 0.17 | 0.05 | 14.4% | 80% | bull-only |
| `rank(ts_delta(fn_goodwill_acquired_during_period_a, 5))` | TOP1000 | 0.10 | 0.03 | 24.6% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_stkco: 0.520 (moderately positively correlated)
- fnd6_newa1v1300_che: 0.518 (moderately positively correlated)
- cash_flow_from_investing: -0.517 (moderately negatively correlated)
- fnd6_mfmq_cheq: 0.517 (moderately positively correlated)
- cash_st: 0.515 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
