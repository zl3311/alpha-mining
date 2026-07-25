---
field: fnd6_prchq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.34
best_fitness: 0.23
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.3914
ann_vol: 0.1687
hit_rate: 0.4915
rolling_sharpe_min: -1.395
rolling_sharpe_max: 1.781
negated_best_sharpe: 0.5
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: 0.16
---
# fnd6_prchq (fundamental6)

*Price High - Quarter*

## Signal Profile
- `rank(fnd6_prchq)`: S=0.25, F=0.12, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_prchq / close)`: S=0.34, F=0.23, T=7.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_prchq, 5))`: S=0.43, F=0.12, T=36.2%, INFERIOR (TOP500)
- `-rank(fnd6_prchq)`: S=-0.08, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prchq, 5))`: S=0.50, F=0.18, T=34.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_prchq, 22)`: S=-0.04, F=0.00, T=32.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_prchq, 10)`: S=0.22, F=0.09, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_prchq, 22))`: S=0.05, F=0.01, T=12.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prchq)`: S=0.13, F=0.04, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prchq / close)`: S=-0.14, F=-0.06, T=8.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.33, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.80 (moderate), ret=+6.6%
  - 2020: S=0.88 (moderate), ret=+13.5%
  - 2021: S=-0.49 (negative), ret=-9.0%
  - 2022: S=-0.03 (negative), ret=-0.6%
  - 2023: S=1.55 (strong), ret=+16.8%

## Risk & Drawdown
- Max drawdown: 39.14% over 1299 days (not yet recovered, ongoing at window end)
- Annualized: return +5.6%, volatility 16.9% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.67, excess kurtosis +3.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.40, max 1.78, latest 1.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +15.69%; worst month: -8.76%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.26
- Sideways: S=-0.44
- Bear: S=1.73

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_prchq, 5))` S=0.50, F=0.18, INFERIOR
Direction gap: +0.16 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_prchq)`: S=0.13, F=0.04, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prchq / close)`: S=-0.14, F=-0.06, T=8.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prchq, 5))`: S=0.50, F=0.18, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_prchq / close)` | TOP500 | 0.33 | 0.23 | 39.1% | 60% | mixed |
| `rank(fnd6_prchq / close)` | TOP1000 | 0.27 | 0.17 | 34.6% | 60% | bear-only |
| `rank(fnd6_prchq / close)` | TOP3000 | 0.26 | 0.16 | 37.9% | 60% | bear-only |
| `rank(fnd6_prchq)` | TOP3000 | 0.25 | 0.12 | 44.0% | 80% | bull-only |
| `rank(ts_delta(fnd6_prchq, 5))` | TOP500 | 0.43 | 0.12 | 10.0% | 80% | bull-only |
| `rank(fnd6_prchq / close)` | TOP200 | 0.13 | 0.06 | 47.2% | 40% | mixed |
| `rank(ts_delta(fnd6_prchq, 5))` | TOP3000 | 0.25 | 0.05 | 12.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_prchq, 5))` | TOP1000 | 0.24 | 0.05 | 7.8% | 60% | bull-only |
| `rank(fnd6_prchq)` | TOP1000 | 0.07 | 0.02 | 39.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_prch: 0.848 (strongly positively correlated)
- fnd6_prccq: 0.776 (strongly positively correlated)
- beta_last_90_days_spy: 0.745 (strongly positively correlated)
- systematic_risk_last_90_days: 0.734 (strongly positively correlated)
- fnd6_prcc: 0.723 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
