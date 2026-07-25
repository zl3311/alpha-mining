---
field: fnd6_recd
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.86
best_fitness: 0.75
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: bull-only
n_variations_with_pnl: 11
max_drawdown: 0.1144
ann_vol: 0.0783
hit_rate: 0.498
rolling_sharpe_min: -1.567
rolling_sharpe_max: 2.61
redundancy_cluster: 1
negated_best_sharpe: -0.31
negated_best_template: rank_neg_delta
negated_best_fitness: -0.11
n_negated_sims: 4
direction_gap: -1.17
---
# fnd6_recd (fundamental6)

*Receivables - Estimated Doubtful*

## Signal Profile
- `rank(fnd6_recd)`: S=0.65, F=0.46, T=1.7%, INFERIOR (TOP3000)
- `rank(fnd6_recd / close)`: S=0.77, F=0.53, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_recd, 5))`: S=0.68, F=0.45, T=32.7%, INFERIOR (TOP500)
- `-rank(fnd6_recd)`: S=-0.41, F=-0.26, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_recd, 5))`: S=-0.31, F=-0.11, T=37.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_recd, 22)`: S=0.05, F=0.01, T=20.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_recd, 10)`: S=0.86, F=0.75, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_recd, 22))`: S=0.01, F=0.00, T=19.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_recd)`: S=-0.65, F=-0.46, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_recd / close)`: S=-0.77, F=-0.53, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/15P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.33 (negative), ret=-1.4%
  - 2020: S=-0.40 (negative), ret=-3.4%
  - 2021: S=1.40 (moderate), ret=+14.5%
  - 2022: S=1.76 (strong), ret=+15.6%
  - 2023: S=0.96 (moderate), ret=+4.1%

## Risk & Drawdown
- Max drawdown: 11.44% over 505 days (recovered)
- Annualized: return +6.0%, volatility 7.8% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.40, excess kurtosis +2.82

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.57, max 2.61, latest 0.95

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.13%; worst month: -4.06%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.36
- Sideways: S=0.08
- Bear: S=-1.91

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_recd, 5))` S=-0.31, F=-0.11, INFERIOR
Direction gap: -1.17 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_recd)`: S=-0.65, F=-0.46, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_recd / close)`: S=-0.77, F=-0.53, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_recd, 5))`: S=-0.31, F=-0.11, T=37.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_recd / close)` | TOP3000 | 0.77 | 0.53 | 11.4% | 60% | bull-only |
| `rank(fnd6_recd)` | TOP3000 | 0.64 | 0.46 | 27.7% | 80% | bull-only |
| `rank(ts_delta(fnd6_recd, 5))` | TOP500 | 0.67 | 0.45 | 22.5% | 80% | mixed |
| `rank(fnd6_recd / close)` | TOP1000 | 0.55 | 0.37 | 17.1% | 40% | bull-only |
| `rank(fnd6_recd / close)` | TOP500 | 0.43 | 0.27 | 25.9% | 60% | bull-only |
| `rank(fnd6_recd)` | TOP1000 | 0.40 | 0.26 | 30.6% | 40% | bull-only |
| `rank(fnd6_recd / close)` | TOP200 | 0.34 | 0.20 | 46.0% | 60% | bull-only |
| `rank(fnd6_recd)` | TOP500 | 0.28 | 0.16 | 42.2% | 40% | bull-only |
| `rank(ts_delta(fnd6_recd, 5))` | TOP3000 | 0.38 | 0.14 | 22.7% | 60% | mixed |
| `rank(ts_delta(fnd6_recd, 5))` | TOP200 | 0.18 | 0.08 | 51.0% | 40% | bull-only |
| `rank(fnd6_recd)` | TOP200 | 0.17 | 0.08 | 60.8% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_rect: 0.951 (strongly positively correlated)
- fnd6_rectr: 0.948 (strongly positively correlated)
- fnd6_cptnewqv1300_rectq: 0.945 (strongly positively correlated)
- receivable: 0.945 (strongly positively correlated)
- fnd6_newa2v1300_sale: 0.942 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
