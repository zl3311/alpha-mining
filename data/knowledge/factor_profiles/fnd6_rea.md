---
field: fnd6_rea
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.86
best_fitness: 1.26
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.1445
ann_vol: 0.1148
hit_rate: 0.4551
rolling_sharpe_min: -0.827
rolling_sharpe_max: 2.42
negated_best_sharpe: 0.86
negated_best_template: neg_rank_level
negated_best_fitness: 1.26
n_negated_sims: 10
direction_gap: 0.35
---
# fnd6_rea (fundamental6)

*Retained Earnings - Restatement*

## Signal Profile
- `rank(fnd6_rea)`: S=-0.22, F=-0.10, T=3.5%, INFERIOR (TOP1000)
- `rank(fnd6_rea / close)`: S=-0.22, F=-0.10, T=3.5%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_rea, 5))`: S=0.75, F=0.62, T=11.2%, INFERIOR (TOP200)
- `-rank(fnd6_rea)`: S=0.22, F=0.10, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_rea, 5))`: S=-0.10, F=-0.03, T=11.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_rea, 63)`: S=0.51, F=0.65, T=8.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_rea, 10)`: S=0.09, F=0.03, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_rea, 22))`: S=-0.03, F=-0.01, T=14.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_rea)`: S=0.86, F=1.26, T=4.9%, AVERAGE (TOP3000)
- `rank(-1 * fnd6_rea / close)`: S=0.86, F=1.26, T=4.9%, AVERAGE (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 23F/9P
- LOW_FITNESS: 26F/6P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.28 (moderate), ret=+11.7%
  - 2020: S=-0.04 (negative), ret=-0.5%
  - 2021: S=1.44 (moderate), ret=+23.3%
  - 2022: S=0.39 (weak), ret=+4.0%
  - 2023: S=0.49 (weak), ret=+3.1%

## Risk & Drawdown
- Max drawdown: 14.45% over 526 days (recovered)
- Annualized: return +8.5%, volatility 11.5% (fraction of booksize)
- Hit rate: 45.5% positive days
- Tail shape: skew +0.94, excess kurtosis +10.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.83, max 2.42, latest 0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.28%; worst month: -7.90%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.61
- Sideways: S=0.55
- Bear: S=0.12

## Negated Direction
Best negated: `rank(-1 * fnd6_rea)` S=0.86, F=1.26, AVERAGE
Direction gap: +0.35 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_rea)`: S=0.86, F=1.26, T=4.9%, AVERAGE (TOP3000)
- `rank(-1 * fnd6_rea / close)`: S=0.86, F=1.26, T=4.9%, AVERAGE (TOP3000)
- `rank(-1 * ts_delta(fnd6_rea, 5))`: S=-0.10, F=-0.03, T=11.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_rea, 5))` | TOP200 | 0.74 | 0.62 | 14.4% | 80% | mixed |
| `rank(ts_delta(fnd6_rea, 5))` | TOP500 | 0.19 | 0.10 | 44.8% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dcvsub: 0.633 (moderately positively correlated)
- fnd6_itcb: 0.395 (weakly positively correlated)
- fnd6_dvpa: 0.354 (weakly positively correlated)
- min_stock_option_expense_guidance: 0.350 (weakly positively correlated)
- stock_option_expense_max_guidance_qtr: 0.350 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
