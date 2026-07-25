---
field: fnd6_newqv1300_seqoq
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 0.76
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.2982
ann_vol: 0.1629
hit_rate: 0.5117
rolling_sharpe_min: -1.804
rolling_sharpe_max: 2.01
negated_best_sharpe: 0.42
negated_best_template: neg_rank_level
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.34
---
# fnd6_newqv1300_seqoq (fundamental6)

*Other Stockholders' Equity Adjustments*

## Signal Profile
- `rank(fnd6_newqv1300_seqoq)`: S=0.14, F=0.05, T=4.3%, INFERIOR (TOP1000)
- `rank(fnd6_newqv1300_seqoq / close)`: S=0.14, F=0.05, T=4.3%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_seqoq, 5))`: S=0.46, F=0.22, T=33.5%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_seqoq)`: S=-0.14, F=-0.05, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_seqoq, 5))`: S=-0.41, F=-0.18, T=33.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_seqoq, 63)`: S=0.04, F=0.01, T=10.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_seqoq, 10)`: S=-0.36, F=-0.21, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_seqoq, 22))`: S=0.76, F=0.62, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_seqoq)`: S=0.42, F=0.20, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_seqoq / close)`: S=0.42, F=0.20, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/17P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.47, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.58 (moderate), ret=+7.8%
  - 2020: S=1.42 (moderate), ret=+24.0%
  - 2021: S=0.35 (weak), ret=+6.9%
  - 2022: S=0.60 (moderate), ret=+9.3%
  - 2023: S=-0.82 (negative), ret=-10.8%

## Risk & Drawdown
- Max drawdown: 29.82% over 534 days (not yet recovered, ongoing at window end)
- Annualized: return +7.6%, volatility 16.3% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.28, excess kurtosis +5.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.80, max 2.01, latest -0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +11.54%; worst month: -8.67%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.49
- Sideways: S=0.18
- Bear: S=1.49

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_seqoq)` S=0.42, F=0.20, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_seqoq)`: S=0.42, F=0.20, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_seqoq / close)`: S=0.42, F=0.20, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_seqoq, 5))`: S=-0.41, F=-0.18, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_seqoq, 5))` | TOP3000 | 0.47 | 0.22 | 29.8% | 80% | mixed |
| `rank(fnd6_newqv1300_seqoq / close)` | TOP1000 | 0.15 | 0.05 | 12.0% | 60% | mixed |
| `rank(fnd6_newqv1300_seqoq)` | TOP1000 | 0.15 | 0.05 | 12.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_seqo: 0.121 (weakly positively correlated)
- fnd6_newqv1300_aul3q: 0.104 (weakly positively correlated)
- sales_max_guidance_quarterly: 0.098 (weakly positively correlated)
- fnd6_exre: 0.095 (weakly positively correlated)
- sales_max_guidance_value: 0.091 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
