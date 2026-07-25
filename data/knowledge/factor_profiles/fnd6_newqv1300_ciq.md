---
field: fnd6_newqv1300_ciq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.71
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1954
ann_vol: 0.1583
hit_rate: 0.5061
rolling_sharpe_min: -0.99
rolling_sharpe_max: 1.61
negated_best_sharpe: 0.71
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.29
---
# fnd6_newqv1300_ciq (fundamental6)

*Comprehensive Income - Total*

## Signal Profile
- `rank(fnd6_newqv1300_ciq)`: S=0.19, F=0.08, T=6.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_ciq / close)`: S=0.13, F=0.05, T=6.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_ciq, 5))`: S=0.42, F=0.14, T=56.4%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_ciq)`: S=-0.12, F=-0.04, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ciq, 5))`: S=0.71, F=0.24, T=46.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_ciq, 22)`: S=-0.02, F=0.00, T=42.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ciq, 10)`: S=0.23, F=0.10, T=4.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ciq, 22))`: S=0.43, F=0.14, T=21.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ciq)`: S=-0.19, F=-0.08, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ciq / close)`: S=-0.13, F=-0.05, T=6.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.41, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.15 (negative), ret=-1.6%
  - 2020: S=0.96 (moderate), ret=+16.5%
  - 2021: S=0.27 (weak), ret=+4.8%
  - 2022: S=0.70 (moderate), ret=+12.6%
  - 2023: S=-0.01 (negative), ret=-0.1%

## Risk & Drawdown
- Max drawdown: 19.54% over 452 days (not yet recovered, ongoing at window end)
- Annualized: return +6.6%, volatility 15.8% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.46, excess kurtosis +6.01

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 1.61, latest 0.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +12.40%; worst month: -8.32%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.55
- Sideways: S=0.35
- Bear: S=0.35

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_ciq, 5))` S=0.71, F=0.24, INFERIOR
Direction gap: +0.29 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ciq)`: S=-0.19, F=-0.08, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ciq / close)`: S=-0.13, F=-0.05, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ciq, 5))`: S=0.71, F=0.24, T=46.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_ciq, 5))` | TOP500 | 0.41 | 0.14 | 19.5% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_ciq, 5))` | TOP1000 | 0.32 | 0.08 | 25.2% | 60% | all-weather |
| `rank(fnd6_newqv1300_ciq)` | TOP3000 | 0.18 | 0.08 | 38.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_ciq / close)` | TOP3000 | 0.13 | 0.05 | 37.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_ciq)` | TOP1000 | 0.12 | 0.04 | 40.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_ciq / close)` | TOP1000 | 0.07 | 0.02 | 34.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_citotalq: 0.987 (strongly positively correlated)
- fnd6_cptnewqv1300_nopiq: 0.181 (weakly positively correlated)
- anl4_qfd1_az_cfps_number: -0.115 (weakly negatively correlated)
- anl4_qf_az_cfps_number: -0.115 (weakly negatively correlated)
- fnd6_cidergl: -0.115 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
