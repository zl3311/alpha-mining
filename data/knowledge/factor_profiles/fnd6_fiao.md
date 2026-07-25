---
field: fnd6_fiao
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.7
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.4547
ann_vol: 0.2181
hit_rate: 0.4842
rolling_sharpe_min: -1.879
rolling_sharpe_max: 2.543
negated_best_sharpe: 0.85
negated_best_template: rank_neg_delta
negated_best_fitness: 0.44
n_negated_sims: 10
direction_gap: 0.15
---
# fnd6_fiao (fundamental6)

*Financing Activities - Other*

## Signal Profile
- `rank(fnd6_fiao)`: S=-0.13, F=-0.03, T=1.8%, INFERIOR (TOP1000)
- `rank(fnd6_fiao / close)`: S=-0.15, F=-0.03, T=2.0%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_fiao, 5))`: S=0.45, F=0.25, T=32.9%, INFERIOR (TOP200)
- `-rank(fnd6_fiao)`: S=0.13, F=0.03, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fiao, 5))`: S=0.85, F=0.44, T=35.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_fiao, 22)`: S=0.70, F=0.60, T=27.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_fiao, 10)`: S=0.34, F=0.16, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_fiao, 22))`: S=0.25, F=0.09, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fiao)`: S=0.63, F=0.28, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fiao / close)`: S=0.76, F=0.34, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 23F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.45, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.43 (weak), ret=+5.8%
  - 2020: S=-1.41 (negative), ret=-25.7%
  - 2021: S=0.73 (moderate), ret=+18.1%
  - 2022: S=1.79 (strong), ret=+55.4%
  - 2023: S=-0.41 (negative), ret=-5.9%

## Risk & Drawdown
- Max drawdown: 45.47% over 778 days (recovered)
- Annualized: return +9.7%, volatility 21.8% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew +1.53, excess kurtosis +18.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.88, max 2.54, latest -0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +24.60%; worst month: -10.32%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.18
- Sideways: S=0.15
- Bear: S=-0.29

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_fiao, 5))` S=0.85, F=0.44, INFERIOR
Direction gap: +0.15 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_fiao)`: S=0.63, F=0.28, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fiao / close)`: S=0.76, F=0.34, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fiao, 5))`: S=0.85, F=0.44, T=35.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_fiao, 5))` | TOP200 | 0.45 | 0.25 | 45.5% | 60% | mixed |
| `rank(ts_delta(fnd6_fiao, 5))` | TOP1000 | 0.32 | 0.11 | 21.0% | 80% | bear-only |
| `rank(ts_delta(fnd6_fiao, 5))` | TOP500 | 0.16 | 0.05 | 59.9% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_txpd: 0.351 (weakly positively correlated)
- fnd6_tfvl: 0.299 (weakly positively correlated)
- fnd6_mrcta: 0.243 (weakly positively correlated)
- fnd6_txr: 0.240 (weakly positively correlated)
- fnd6_optrfr: 0.227 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
