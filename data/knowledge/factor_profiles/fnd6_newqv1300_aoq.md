---
field: fnd6_newqv1300_aoq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.62
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1236
ann_vol: 0.0788
hit_rate: 0.481
rolling_sharpe_min: -0.814
rolling_sharpe_max: 2.271
redundancy_cluster: 1
negated_best_sharpe: 0.21
negated_best_template: neg_rank_level
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.41
---
# fnd6_newqv1300_aoq (fundamental6)

*Assets - Other - Total*

## Signal Profile
- `rank(fnd6_newqv1300_aoq)`: S=0.44, F=0.28, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_aoq / close)`: S=0.62, F=0.39, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_aoq, 5))`: S=0.55, F=0.15, T=38.6%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_aoq)`: S=-0.14, F=-0.05, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aoq, 5))`: S=0.31, F=0.10, T=38.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_aoq, 22)`: S=0.03, F=0.00, T=39.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_aoq, 10)`: S=-0.10, F=-0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_aoq, 22))`: S=-0.23, F=-0.06, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aoq)`: S=0.21, F=0.12, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aoq / close)`: S=0.04, F=0.01, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.61, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.03 (weak), ret=+0.1%
  - 2020: S=-0.21 (negative), ret=-1.9%
  - 2021: S=1.19 (moderate), ret=+12.9%
  - 2022: S=1.40 (moderate), ret=+11.0%
  - 2023: S=0.36 (weak), ret=+1.6%

## Risk & Drawdown
- Max drawdown: 12.36% over 294 days (recovered)
- Annualized: return +4.8%, volatility 7.9% (fraction of booksize)
- Hit rate: 48.1% positive days
- Tail shape: skew +0.39, excess kurtosis +3.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.81, max 2.27, latest 0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.83%; worst month: -3.12%
Positive months: 46%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.83
- Sideways: S=0.64
- Bear: S=-2.19

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_aoq)` S=0.21, F=0.12, INFERIOR
Direction gap: -0.41 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_aoq)`: S=0.21, F=0.12, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aoq / close)`: S=0.04, F=0.01, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aoq, 5))`: S=0.31, F=0.10, T=38.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_aoq / close)` | TOP3000 | 0.61 | 0.39 | 12.4% | 80% | bull-only |
| `rank(fnd6_newqv1300_aoq)` | TOP3000 | 0.43 | 0.28 | 31.8% | 80% | bull-only |
| `rank(fnd6_newqv1300_aoq / close)` | TOP1000 | 0.34 | 0.19 | 15.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_aoq, 5))` | TOP3000 | 0.56 | 0.15 | 6.0% | 60% | all-weather |
| `rank(ts_delta(fnd6_newqv1300_aoq, 5))` | TOP1000 | 0.31 | 0.08 | 11.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_aoq / close)` | TOP500 | 0.14 | 0.06 | 31.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_aoq)` | TOP1000 | 0.13 | 0.05 | 38.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_aoq, 5))` | TOP500 | 0.16 | 0.03 | 17.2% | 60% | all-weather |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_ancq: 0.976 (strongly positively correlated)
- fnd6_newa1v1300_ao: 0.963 (strongly positively correlated)
- fnd6_aox: 0.961 (strongly positively correlated)
- fnd6_newqv1300_altoq: 0.961 (strongly positively correlated)
- fnd6_aodo: 0.961 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
