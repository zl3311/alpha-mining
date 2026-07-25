---
field: fnd6_newqv1300_mibnq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.62
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0859
ann_vol: 0.0549
hit_rate: 0.4988
rolling_sharpe_min: -1.023
rolling_sharpe_max: 2.363
redundancy_cluster: 100
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.04
---
# fnd6_newqv1300_mibnq (fundamental6)

*Non-Redeemable Noncontrolling Interest (Balance Sheet) - Quarterly*

## Signal Profile
- `rank(fnd6_newqv1300_mibnq)`: S=0.41, F=0.18, T=2.2%, INFERIOR (TOP1000)
- `rank(fnd6_newqv1300_mibnq / close)`: S=0.51, F=0.24, T=2.3%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_mibnq, 5))`: S=-0.21, F=-0.05, T=39.5%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_mibnq)`: S=-0.41, F=-0.18, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_mibnq, 5))`: S=0.58, F=0.20, T=38.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_mibnq, 63)`: S=0.62, F=0.25, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_mibnq, 10)`: S=-0.28, F=-0.11, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_mibnq, 22))`: S=-0.16, F=-0.04, T=17.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_mibnq)`: S=-0.35, F=-0.13, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_mibnq / close)`: S=-0.42, F=-0.17, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.51, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.17 (weak), ret=+0.5%
  - 2020: S=-0.19 (negative), ret=-1.0%
  - 2021: S=0.41 (weak), ret=+3.0%
  - 2022: S=2.03 (strong), ret=+12.5%
  - 2023: S=-0.39 (negative), ret=-1.5%

## Risk & Drawdown
- Max drawdown: 8.59% over 246 days (recovered)
- Annualized: return +2.8%, volatility 5.5% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.13, excess kurtosis +1.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.02, max 2.36, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.82%; worst month: -4.68%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.74
- Sideways: S=0.12
- Bear: S=-1.84

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_mibnq, 5))` S=0.58, F=0.20, INFERIOR
Direction gap: -0.04 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_mibnq)`: S=-0.35, F=-0.13, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_mibnq / close)`: S=-0.42, F=-0.17, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_mibnq, 5))`: S=0.58, F=0.20, T=38.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_mibnq / close)` | TOP1000 | 0.51 | 0.24 | 8.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_mibnq)` | TOP1000 | 0.41 | 0.18 | 10.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_mibnq / close)` | TOP3000 | 0.42 | 0.17 | 11.8% | 80% | bull-only |
| `rank(fnd6_newqv1300_mibnq)` | TOP200 | 0.29 | 0.14 | 23.4% | 60% | bull-only |
| `rank(fnd6_newqv1300_mibnq)` | TOP3000 | 0.34 | 0.13 | 14.4% | 80% | bull-only |
| `rank(fnd6_newqv1300_mibnq / close)` | TOP200 | 0.23 | 0.10 | 25.1% | 60% | bull-only |
| `rank(fnd6_newqv1300_mibnq / close)` | TOP500 | 0.19 | 0.06 | 13.1% | 60% | bull-only |
| `rank(fnd6_newqv1300_mibnq)` | TOP500 | 0.15 | 0.04 | 13.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_mibtq: 0.986 (strongly positively correlated)
- fnd6_mfmq_mibtq: 0.985 (strongly positively correlated)
- fnd6_mibn: 0.958 (strongly positively correlated)
- fnd6_mibt: 0.950 (strongly positively correlated)
- est_ebitda: 0.762 (strongly positively correlated)

Redundancy cluster #100: 2 similar fields, mean |rho| 0.985 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
