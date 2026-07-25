---
field: fnd6_newqv1300_lqpl1q
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.75
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1914
ann_vol: 0.1533
hit_rate: 0.4721
rolling_sharpe_min: -0.97
rolling_sharpe_max: 1.705
negated_best_sharpe: 0.75
negated_best_template: rank_neg_delta
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: 0.36
---
# fnd6_newqv1300_lqpl1q (fundamental6)

*Liabilities Level 1 (Quoted Prices)*

## Signal Profile
- `rank(fnd6_newqv1300_lqpl1q)`: S=0.36, F=0.15, T=9.5%, INFERIOR (TOP500)
- `rank(fnd6_newqv1300_lqpl1q / close)`: S=0.36, F=0.15, T=9.5%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_lqpl1q, 5))`: S=0.44, F=0.16, T=53.6%, INFERIOR (TOP1000)
- `-rank(fnd6_newqv1300_lqpl1q)`: S=-0.18, F=-0.05, T=8.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lqpl1q, 5))`: S=0.75, F=0.37, T=57.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_lqpl1q, 63)`: S=-0.46, F=-0.19, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_lqpl1q, 10)`: S=0.39, F=0.21, T=7.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_lqpl1q, 22))`: S=-0.27, F=-0.09, T=23.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lqpl1q)`: S=-0.36, F=-0.15, T=9.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lqpl1q / close)`: S=-0.36, F=-0.15, T=9.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/17P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.43, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+9.3%
  - 2020: S=-0.25 (negative), ret=-3.3%
  - 2021: S=0.35 (weak), ret=+6.7%
  - 2022: S=1.18 (moderate), ret=+17.6%
  - 2023: S=0.15 (weak), ret=+2.0%

## Risk & Drawdown
- Max drawdown: 19.14% over 457 days (recovered)
- Annualized: return +6.6%, volatility 15.3% (fraction of booksize)
- Hit rate: 47.2% positive days
- Tail shape: skew +0.74, excess kurtosis +6.48

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.97, max 1.71, latest 0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +14.93%; worst month: -9.82%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.65
- Sideways: S=-0.67
- Bear: S=0.36

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_lqpl1q, 5))` S=0.75, F=0.37, INFERIOR
Direction gap: +0.36 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_lqpl1q)`: S=-0.36, F=-0.15, T=9.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lqpl1q / close)`: S=-0.36, F=-0.15, T=9.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lqpl1q, 5))`: S=0.75, F=0.37, T=57.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_lqpl1q, 5))` | TOP1000 | 0.43 | 0.16 | 19.1% | 80% | mixed |
| `rank(fnd6_newqv1300_lqpl1q / close)` | TOP500 | 0.34 | 0.15 | 15.1% | 80% | bull-only |
| `rank(fnd6_newqv1300_lqpl1q)` | TOP500 | 0.34 | 0.15 | 15.2% | 80% | bull-only |
| `rank(fnd6_newqv1300_lqpl1q)` | TOP1000 | 0.16 | 0.05 | 11.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_lqpl1q / close)` | TOP1000 | 0.13 | 0.04 | 11.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_lqpl1: 0.131 (weakly positively correlated)
- fn_payments_for_repurchase_of_common_stock_q: -0.103 (weakly negatively correlated)
- anl4_afv4_cfps_high: -0.098 (weakly negatively correlated)
- fnd6_dltis: -0.098 (weakly negatively correlated)
- anl4_afv4_cfps_mean: -0.095 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
