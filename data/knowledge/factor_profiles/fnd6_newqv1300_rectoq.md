---
field: fnd6_newqv1300_rectoq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.31
best_fitness: 0.12
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.2604
ann_vol: 0.1513
hit_rate: 0.4947
rolling_sharpe_min: -1.476
rolling_sharpe_max: 1.383
negated_best_sharpe: 0.31
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: 0.06
---
# fnd6_newqv1300_rectoq (fundamental6)

*Receivables - Current Other incl Tax Refunds*

## Signal Profile
- `rank(fnd6_newqv1300_rectoq)`: S=0.13, F=0.03, T=2.6%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_rectoq / close)`: S=0.11, F=0.02, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_rectoq, 5))`: S=0.25, F=0.08, T=40.3%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_rectoq)`: S=0.11, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rectoq, 5))`: S=0.31, F=0.12, T=40.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_rectoq, 22)`: S=-0.12, F=-0.03, T=37.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_rectoq, 10)`: S=0.00, F=0.00, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_rectoq, 22))`: S=-0.31, F=-0.10, T=18.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rectoq)`: S=0.00, F=0.00, T=5.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rectoq / close)`: S=0.00, F=0.00, T=5.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.25, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.04 (moderate), ret=+13.4%
  - 2020: S=0.06 (weak), ret=+0.9%
  - 2021: S=0.39 (weak), ret=+5.3%
  - 2022: S=0.78 (moderate), ret=+12.6%
  - 2023: S=-1.02 (negative), ret=-14.0%

## Risk & Drawdown
- Max drawdown: 26.04% over 299 days (recovered)
- Annualized: return +3.7%, volatility 15.1% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew -0.05, excess kurtosis +7.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.48, max 1.38, latest -1.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +8.02%; worst month: -14.89%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.24
- Sideways: S=-0.55
- Bear: S=1.48

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_rectoq, 5))` S=0.31, F=0.12, INFERIOR
Direction gap: +0.06 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_rectoq)`: S=0.00, F=0.00, T=5.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rectoq / close)`: S=0.00, F=0.00, T=5.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rectoq, 5))`: S=0.31, F=0.12, T=40.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_rectoq, 5))` | TOP500 | 0.25 | 0.08 | 26.0% | 80% | mixed |
| `rank(fnd6_newqv1300_rectoq)` | TOP3000 | 0.13 | 0.03 | 15.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_rectoq / close)` | TOP3000 | 0.11 | 0.02 | 11.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- snt_social_volume: 0.128 (weakly positively correlated)
- fnd6_invrm: -0.115 (weakly negatively correlated)
- fnd6_newqv1300_rectaq: 0.110 (weakly positively correlated)
- sales_max_guidance_quarterly: 0.105 (weakly positively correlated)
- historical_volatility_10: 0.104 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
