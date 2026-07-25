---
field: fnd6_newqv1300_invwipq
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.98
best_fitness: 1.09
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1867
ann_vol: 0.0876
hit_rate: 0.4988
rolling_sharpe_min: -2.698
rolling_sharpe_max: 2.524
negated_best_sharpe: 0.98
negated_best_template: neg_rank_level
negated_best_fitness: 1.09
n_negated_sims: 10
direction_gap: 0.55
---
# fnd6_newqv1300_invwipq (fundamental6)

*Inventory - Work in Process*

## Signal Profile
- `rank(fnd6_newqv1300_invwipq)`: S=0.25, F=0.11, T=5.1%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_invwipq / close)`: S=0.31, F=0.14, T=5.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_invwipq, 5))`: S=-0.43, F=-0.18, T=49.9%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_invwipq)`: S=0.01, F=0.00, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_invwipq, 5))`: S=0.56, F=0.27, T=49.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_invwipq, 22)`: S=0.43, F=0.27, T=36.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_invwipq, 10)`: S=0.03, F=0.01, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_invwipq, 22))`: S=-0.72, F=-0.39, T=22.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invwipq)`: S=0.98, F=1.09, T=9.5%, AVERAGE (TOP3000)
- `rank(-1 * fnd6_newqv1300_invwipq / close)`: S=1.01, F=1.09, T=9.9%, AVERAGE (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 26F/6P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.30, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.87 (negative), ret=-5.0%
  - 2020: S=-0.95 (negative), ret=-7.1%
  - 2021: S=1.05 (moderate), ret=+11.5%
  - 2022: S=1.17 (moderate), ret=+13.0%
  - 2023: S=0.07 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 18.67% over 1053 days (recovered)
- Annualized: return +2.6%, volatility 8.8% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew -0.11, excess kurtosis +1.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.70, max 2.52, latest -0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.91%; worst month: -5.35%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.74
- Sideways: S=-0.09
- Bear: S=-2.35

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_invwipq)` S=0.98, F=1.09, AVERAGE
Direction gap: +0.55 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_invwipq)`: S=0.98, F=1.09, T=9.5%, AVERAGE (TOP3000)
- `rank(-1 * fnd6_newqv1300_invwipq / close)`: S=1.01, F=1.09, T=9.9%, AVERAGE (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_invwipq, 5))`: S=0.56, F=0.27, T=49.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_invwipq / close)` | TOP3000 | 0.30 | 0.14 | 18.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_invwipq)` | TOP3000 | 0.24 | 0.11 | 24.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_invwipq)` | TOP500 | 0.17 | 0.07 | 20.4% | 60% | bull-only |
| `rank(fnd6_newqv1300_invwipq / close)` | TOP500 | 0.14 | 0.05 | 16.1% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_invfg: 0.884 (strongly positively correlated)
- inventory: 0.852 (strongly positively correlated)
- fnd6_newqv1300_invtq: 0.852 (strongly positively correlated)
- fnd6_newa1v1300_invt: 0.841 (strongly positively correlated)
- fnd6_fatb: 0.806 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
