---
field: fnd6_ceql
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.98
best_fitness: 0.88
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0892
ann_vol: 0.0694
hit_rate: 0.4802
rolling_sharpe_min: -1.044
rolling_sharpe_max: 1.999
redundancy_cluster: 1
negated_best_sharpe: 0.45
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.53
---
# fnd6_ceql (fundamental6)

*Common Equity - Liquidation Value*

## Signal Profile
- `rank(fnd6_ceql)`: S=0.47, F=0.28, T=1.7%, INFERIOR (TOP3000)
- `rank(fnd6_ceql / close)`: S=0.52, F=0.28, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_ceql, 5))`: S=-0.01, F=0.00, T=35.8%, INFERIOR (TOP500)
- `-rank(fnd6_ceql)`: S=-0.14, F=-0.05, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ceql, 5))`: S=0.45, F=0.17, T=38.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_ceql, 63)`: S=0.98, F=0.88, T=20.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ceql, 10)`: S=-0.02, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ceql, 22))`: S=-0.39, F=-0.18, T=18.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ceql)`: S=-0.47, F=-0.28, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ceql / close)`: S=-0.52, F=-0.28, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.51, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.15 (negative), ret=-0.7%
  - 2020: S=-0.11 (negative), ret=-0.9%
  - 2021: S=1.02 (moderate), ret=+9.0%
  - 2022: S=0.82 (moderate), ret=+5.4%
  - 2023: S=0.86 (moderate), ret=+4.6%

## Risk & Drawdown
- Max drawdown: 8.92% over 577 days (not yet recovered, ongoing at window end)
- Annualized: return +3.5%, volatility 6.9% (fraction of booksize)
- Hit rate: 48.0% positive days
- Tail shape: skew +0.71, excess kurtosis +4.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.04, max 2.00, latest 0.96

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.24%; worst month: -3.18%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.20
- Sideways: S=0.24
- Bear: S=-1.27

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_ceql, 5))` S=0.45, F=0.17, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_ceql)`: S=-0.47, F=-0.28, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ceql / close)`: S=-0.52, F=-0.28, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ceql, 5))`: S=0.45, F=0.17, T=38.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_ceql)` | TOP3000 | 0.46 | 0.28 | 30.3% | 80% | bull-only |
| `rank(fnd6_ceql / close)` | TOP3000 | 0.51 | 0.28 | 8.9% | 60% | bull-only |
| `rank(fnd6_ceql / close)` | TOP1000 | 0.30 | 0.14 | 15.0% | 60% | bull-only |
| `rank(fnd6_ceql)` | TOP1000 | 0.13 | 0.05 | 35.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ceq: 0.996 (strongly positively correlated)
- fnd6_newa2v1300_seq: 0.993 (strongly positively correlated)
- fnd6_teq: 0.992 (strongly positively correlated)
- fnd6_newa1v1300_icapt: 0.965 (strongly positively correlated)
- fnd6_newa1v1300_at: 0.955 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
