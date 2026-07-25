---
field: fnd6_newqv1300_ancq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.61
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1121
ann_vol: 0.0902
hit_rate: 0.4858
rolling_sharpe_min: -1.071
rolling_sharpe_max: 2.394
redundancy_cluster: 1
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.14
---
# fnd6_newqv1300_ancq (fundamental6)

*Non-Current Assets - Total*

## Signal Profile
- `rank(fnd6_newqv1300_ancq)`: S=0.52, F=0.38, T=1.5%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_ancq / close)`: S=0.61, F=0.40, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_ancq, 5))`: S=0.35, F=0.09, T=37.6%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_ancq)`: S=-0.15, F=-0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ancq, 5))`: S=0.47, F=0.17, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_ancq, 22)`: S=0.15, F=0.04, T=40.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ancq, 10)`: S=0.01, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ancq, 22))`: S=-0.32, F=-0.10, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ancq)`: S=0.04, F=0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ancq / close)`: S=-0.07, F=-0.02, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.60, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.23 (negative), ret=-1.3%
  - 2020: S=-0.16 (negative), ret=-1.6%
  - 2021: S=1.32 (moderate), ret=+16.5%
  - 2022: S=1.19 (moderate), ret=+10.2%
  - 2023: S=0.55 (moderate), ret=+2.9%

## Risk & Drawdown
- Max drawdown: 11.21% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +5.4%, volatility 9.0% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew +0.47, excess kurtosis +3.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.07, max 2.39, latest 0.61

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.25%; worst month: -3.76%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.80
- Sideways: S=0.03
- Bear: S=-1.68

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_ancq, 5))` S=0.47, F=0.17, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ancq)`: S=0.04, F=0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ancq / close)`: S=-0.07, F=-0.02, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ancq, 5))`: S=0.47, F=0.17, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_ancq / close)` | TOP3000 | 0.60 | 0.40 | 11.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_ancq)` | TOP3000 | 0.51 | 0.38 | 36.4% | 80% | bull-only |
| `rank(fnd6_newqv1300_ancq / close)` | TOP1000 | 0.26 | 0.13 | 20.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_ancq, 5))` | TOP3000 | 0.35 | 0.09 | 11.7% | 60% | weak |
| `rank(fnd6_newqv1300_ancq)` | TOP1000 | 0.14 | 0.06 | 41.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_ancq / close)` | TOP500 | 0.06 | 0.02 | 37.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_aoq: 0.976 (strongly positively correlated)
- fnd6_mfma1_dp: 0.973 (strongly positively correlated)
- fnd6_newa1v1300_dp: 0.973 (strongly positively correlated)
- fnd6_newqv1300_lltq: 0.969 (strongly positively correlated)
- depre_amort: 0.966 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
