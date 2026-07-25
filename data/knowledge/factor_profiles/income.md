---
field: income
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.76
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.4188
ann_vol: 0.1231
hit_rate: 0.5142
rolling_sharpe_min: -4.092
rolling_sharpe_max: 2.537
negated_best_sharpe: 0.76
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.34
---
# income (fundamental6)

*Net Income*

## Signal Profile
- `rank(income)`: S=0.19, F=0.08, T=2.0%, INFERIOR (TOP3000)
- `rank(income / close)`: S=0.20, F=0.08, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(income, 5))`: S=-0.02, F=0.00, T=36.8%, INFERIOR (TOP200)
- `ts_decay_linear(rank(income), 5)`: S=0.20, F=0.09, T=1.9%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(income), ts_std_dev(returns,20)<0.01)`: S=0.15, F=0.06, T=2.8%, INFERIOR (TOP3000)
- `-rank(income)`: S=-0.06, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(income, 5))`: S=0.76, F=0.24, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(income, 22)`: S=0.42, F=0.14, T=37.5%, INFERIOR (TOP3000)
- `ts_mean(income, 10)`: S=0.10, F=0.03, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(income, 22))`: S=0.18, F=0.04, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * income)`: S=-0.19, F=-0.08, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * income / close)`: S=-0.20, F=-0.08, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/26P
- LOW_FITNESS: 37F/0P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/19P

## Temporal Behavior
Headline (decay_linear): Overall Sharpe 0.19, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.29 (weak), ret=+1.8%
  - 2020: S=-3.32 (negative), ret=-28.1%
  - 2021: S=1.27 (moderate), ret=+16.5%
  - 2022: S=1.36 (moderate), ret=+24.0%
  - 2023: S=-0.23 (negative), ret=-2.8%

## Risk & Drawdown
- Max drawdown: 41.88% over 942 days (recovered)
- Annualized: return +2.3%, volatility 12.3% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew -0.18, excess kurtosis +1.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.09, max 2.54, latest -0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.33%; worst month: -10.28%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.50
- Sideways: S=0.85
- Bear: S=-3.43

## Negated Direction
Best negated: `rank(-1 * ts_delta(income, 5))` S=0.76, F=0.24, INFERIOR
Direction gap: +0.34 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * income)`: S=-0.19, F=-0.08, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * income / close)`: S=-0.20, F=-0.08, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(income, 5))`: S=0.76, F=0.24, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `ts_decay_linear(rank(income), 5)` | TOP3000 | 0.19 | 0.09 | 41.9% | 60% | bull-only |
| `rank(income)` | TOP3000 | 0.18 | 0.08 | 41.9% | 60% | bull-only |
| `rank(income / close)` | TOP3000 | 0.19 | 0.08 | 38.9% | 60% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(income), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.15 | 0.06 | 41.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfmq_ibcomq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_cibegniq: 0.996 (strongly positively correlated)
- fnd6_newqv1300_dilavq: 0.989 (strongly positively correlated)
- fnd6_newqv1300_ibadjq: 0.989 (strongly positively correlated)
- fnd6_newqv1300_ibcomq: 0.989 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
