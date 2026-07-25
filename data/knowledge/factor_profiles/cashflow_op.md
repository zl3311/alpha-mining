---
field: cashflow_op
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.62
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 36
regime_profile: bull-only
n_variations_with_pnl: 11
max_drawdown: 0.2382
ann_vol: 0.1061
hit_rate: 0.5069
rolling_sharpe_min: -2.668
rolling_sharpe_max: 2.544
redundancy_cluster: 13
negated_best_sharpe: 0.08
negated_best_template: neg_rank_level
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.54
---
# cashflow_op (fundamental6)

*Operating Activities - Net Cash Flow*

## Signal Profile
- `rank(cashflow_op)`: S=0.34, F=0.20, T=1.2%, INFERIOR (TOP3000)
- `rank(cashflow_op / close)`: S=0.62, F=0.45, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(cashflow_op, 5))`: S=0.59, F=0.28, T=34.6%, INFERIOR (TOP1000)
- `ts_decay_linear(rank(cashflow_op), 5)`: S=0.34, F=0.20, T=1.2%, INFERIOR (TOP3000)
- `-rank(cashflow_op)`: S=-0.20, F=-0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_op, 5))`: S=-0.01, F=0.00, T=32.6%, INFERIOR (TOP3000)
- `ts_zscore(cashflow_op, 22)`: S=0.38, F=0.20, T=27.9%, INFERIOR (TOP3000)
- `ts_mean(cashflow_op, 10)`: S=0.31, F=0.16, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow_op, 22))`: S=-0.34, F=-0.14, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_op)`: S=0.08, F=0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_op / close)`: S=0.05, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/23P
- LOW_FITNESS: 36F/0P
- LOW_SHARPE: 36F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/2P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.61, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.08 (negative), ret=-0.4%
  - 2020: S=-1.55 (negative), ret=-11.6%
  - 2021: S=1.23 (moderate), ret=+16.6%
  - 2022: S=1.72 (strong), ret=+25.1%
  - 2023: S=0.21 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 23.82% over 772 days (recovered)
- Annualized: return +6.4%, volatility 10.6% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.05, excess kurtosis +1.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.67, max 2.54, latest 0.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.30%; worst month: -5.02%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.23
- Sideways: S=0.89
- Bear: S=-3.15

## Negated Direction
Best negated: `rank(-1 * cashflow_op)` S=0.08, F=0.03, INFERIOR
Direction gap: -0.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * cashflow_op)`: S=0.08, F=0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_op / close)`: S=0.05, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_op, 5))`: S=-0.01, F=0.00, T=32.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cashflow_op / close)` | TOP3000 | 0.61 | 0.45 | 23.8% | 60% | bull-only |
| `rank(ts_delta(cashflow_op, 5))` | TOP1000 | 0.61 | 0.28 | 22.9% | 80% | bull-only |
| `rank(cashflow_op / close)` | TOP1000 | 0.35 | 0.21 | 26.4% | 60% | bull-only |
| `rank(cashflow_op)` | TOP3000 | 0.33 | 0.20 | 38.5% | 60% | bull-only |
| `ts_decay_linear(rank(cashflow_op), 5)` | TOP3000 | 0.33 | 0.20 | 38.5% | 60% | bull-only |
| `rank(ts_delta(cashflow_op, 5))` | TOP3000 | 0.46 | 0.15 | 20.9% | 80% | bull-only |
| `rank(ts_delta(cashflow_op, 5))` | TOP500 | 0.35 | 0.15 | 50.4% | 80% | mixed |
| `rank(cashflow_op / close)` | TOP500 | 0.19 | 0.10 | 42.5% | 40% | bull-only |
| `rank(cashflow_op)` | TOP1000 | 0.19 | 0.09 | 40.8% | 60% | bull-only |
| `rank(cashflow_op)` | TOP500 | 0.10 | 0.04 | 51.6% | 60% | bull-only |
| `rank(ts_delta(cashflow_op, 5))` | TOP200 | 0.10 | 0.02 | 45.0% | 20% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_oancf: 1.000 (strongly positively correlated)
- fnd6_mfma2_oancf: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.987 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.987 (strongly positively correlated)
- ebitda: 0.987 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
