---
field: fnd6_newqv1300_tfvlq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.96
best_fitness: 0.52
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1152
ann_vol: 0.0515
hit_rate: 0.5045
rolling_sharpe_min: -2.252
rolling_sharpe_max: 2.173
negated_best_sharpe: 0.96
negated_best_template: rank_neg_delta
negated_best_fitness: 0.52
n_negated_sims: 10
direction_gap: 0.55
---
# fnd6_newqv1300_tfvlq (fundamental6)

*Total Fair Value Liabilities*

## Signal Profile
- `rank(fnd6_newqv1300_tfvlq)`: S=0.21, F=0.06, T=6.4%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_tfvlq / close)`: S=0.01, F=0.00, T=6.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_tfvlq, 5))`: S=0.13, F=0.02, T=50.3%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_tfvlq)`: S=0.03, F=0.00, T=8.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_tfvlq, 5))`: S=0.96, F=0.52, T=60.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_tfvlq, 22)`: S=0.39, F=0.15, T=39.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_tfvlq, 10)`: S=0.41, F=0.23, T=5.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_tfvlq, 22))`: S=-0.43, F=-0.15, T=22.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tfvlq)`: S=0.09, F=0.02, T=8.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tfvlq / close)`: S=0.11, F=0.03, T=8.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.20, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.32 (weak), ret=+1.2%
  - 2020: S=-1.39 (negative), ret=-6.0%
  - 2021: S=1.30 (moderate), ret=+8.2%
  - 2022: S=0.77 (moderate), ret=+4.7%
  - 2023: S=-0.68 (negative), ret=-2.9%

## Risk & Drawdown
- Max drawdown: 11.52% over 793 days (recovered)
- Annualized: return +1.1%, volatility 5.1% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.15, excess kurtosis +1.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.25, max 2.17, latest -0.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +3.49%; worst month: -3.78%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.28
- Sideways: S=0.42
- Bear: S=-2.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_tfvlq, 5))` S=0.96, F=0.52, INFERIOR
Direction gap: +0.55 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_tfvlq)`: S=0.09, F=0.02, T=8.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tfvlq / close)`: S=0.11, F=0.03, T=8.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_tfvlq, 5))`: S=0.96, F=0.52, T=60.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_tfvlq)` | TOP3000 | 0.20 | 0.06 | 11.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_tfvlq, 5))` | TOP3000 | 0.12 | 0.02 | 30.5% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_lol2q: 0.869 (strongly positively correlated)
- est_netprofit_adj: 0.808 (strongly positively correlated)
- est_netprofit: 0.801 (strongly positively correlated)
- anl4_netprofita_mean: 0.800 (strongly positively correlated)
- est_ptp: 0.799 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
