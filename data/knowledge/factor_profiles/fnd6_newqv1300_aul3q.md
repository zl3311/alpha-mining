---
field: fnd6_newqv1300_aul3q
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.87
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.2113
ann_vol: 0.1561
hit_rate: 0.4915
rolling_sharpe_min: -1.391
rolling_sharpe_max: 2.021
negated_best_sharpe: 0.15
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.72
---
# fnd6_newqv1300_aul3q (fundamental6)

*Assets Level 3 (Unobservable)*

## Signal Profile
- `rank(fnd6_newqv1300_aul3q)`: S=0.25, F=0.08, T=7.8%, INFERIOR (TOP1000)
- `rank(fnd6_newqv1300_aul3q / close)`: S=0.26, F=0.09, T=7.8%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_aul3q, 5))`: S=0.40, F=0.14, T=46.8%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_aul3q)`: S=-0.25, F=-0.08, T=7.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aul3q, 5))`: S=0.15, F=0.03, T=48.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_aul3q, 63)`: S=-0.55, F=-0.29, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_aul3q, 10)`: S=0.87, F=0.62, T=5.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_aul3q, 22))`: S=-0.28, F=-0.10, T=23.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aul3q)`: S=-0.25, F=-0.08, T=7.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aul3q / close)`: S=-0.26, F=-0.09, T=7.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 14F/18P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.38, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.02 (negative), ret=-0.2%
  - 2020: S=1.39 (moderate), ret=+29.0%
  - 2021: S=0.58 (moderate), ret=+8.7%
  - 2022: S=0.48 (weak), ret=+6.8%
  - 2023: S=-1.19 (negative), ret=-15.1%

## Risk & Drawdown
- Max drawdown: 21.13% over 449 days (not yet recovered, ongoing at window end)
- Annualized: return +6.0%, volatility 15.6% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +1.87, excess kurtosis +19.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.39, max 2.02, latest -1.32

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +29.98%; worst month: -6.62%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.45
- Sideways: S=-0.05
- Bear: S=1.43

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_aul3q, 5))` S=0.15, F=0.03, INFERIOR
Direction gap: -0.72 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_aul3q)`: S=-0.25, F=-0.08, T=7.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aul3q / close)`: S=-0.26, F=-0.09, T=7.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aul3q, 5))`: S=0.15, F=0.03, T=48.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_aul3q, 5))` | TOP3000 | 0.38 | 0.14 | 21.1% | 60% | mixed |
| `rank(fnd6_newqv1300_aul3q / close)` | TOP1000 | 0.26 | 0.09 | 12.8% | 60% | mixed |
| `rank(fnd6_newqv1300_aul3q)` | TOP1000 | 0.25 | 0.08 | 11.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_profit_loss_a: 0.118 (weakly positively correlated)
- parkinson_volatility_90: -0.116 (weakly negatively correlated)
- max_adjusted_net_income_guidance: 0.110 (weakly positively correlated)
- parkinson_volatility_120: -0.107 (weakly negatively correlated)
- fnd6_cipen: 0.107 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
