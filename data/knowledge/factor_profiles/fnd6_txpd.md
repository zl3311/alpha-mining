---
field: fnd6_txpd
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.52
best_fitness: 0.32
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.3666
ann_vol: 0.2133
hit_rate: 0.4623
rolling_sharpe_min: -0.813
rolling_sharpe_max: 2.186
negated_best_sharpe: 0.26
negated_best_template: neg_rank_level
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.26
---
# fnd6_txpd (fundamental6)

*Income Taxes Paid*

## Signal Profile
- `rank(fnd6_txpd)`: S=0.28, F=0.14, T=1.7%, INFERIOR (TOP3000)
- `rank(fnd6_txpd / close)`: S=0.51, F=0.29, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txpd, 5))`: S=0.52, F=0.32, T=28.6%, INFERIOR (TOP200)
- `-rank(fnd6_txpd)`: S=-0.07, F=-0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txpd, 5))`: S=-0.58, F=-0.38, T=28.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txpd, 22)`: S=0.20, F=0.08, T=25.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txpd, 10)`: S=0.23, F=0.10, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txpd, 22))`: S=0.18, F=0.06, T=18.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txpd)`: S=0.26, F=0.15, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txpd / close)`: S=0.21, F=0.11, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.51, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.95 (strong), ret=+23.5%
  - 2020: S=0.25 (weak), ret=+3.5%
  - 2021: S=-0.05 (negative), ret=-1.4%
  - 2022: S=0.86 (moderate), ret=+24.1%
  - 2023: S=0.26 (weak), ret=+4.0%

## Risk & Drawdown
- Max drawdown: 36.66% over 606 days (recovered)
- Annualized: return +11.0%, volatility 21.3% (fraction of booksize)
- Hit rate: 46.2% positive days
- Tail shape: skew +0.31, excess kurtosis +38.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.81, max 2.19, latest 0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +11.80%; worst month: -9.21%
Positive months: 46%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.27
- Sideways: S=1.03
- Bear: S=0.56

## Negated Direction
Best negated: `rank(-1 * fnd6_txpd)` S=0.26, F=0.15, INFERIOR
Direction gap: -0.26 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txpd)`: S=0.26, F=0.15, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txpd / close)`: S=0.21, F=0.11, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txpd, 5))`: S=-0.58, F=-0.38, T=28.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txpd, 5))` | TOP200 | 0.51 | 0.32 | 36.7% | 80% | mixed |
| `rank(fnd6_txpd / close)` | TOP3000 | 0.49 | 0.29 | 18.3% | 80% | bull-only |
| `rank(ts_delta(fnd6_txpd, 5))` | TOP500 | 0.35 | 0.16 | 39.4% | 80% | mixed |
| `rank(fnd6_txpd)` | TOP3000 | 0.27 | 0.14 | 33.4% | 80% | bull-only |
| `rank(fnd6_txpd / close)` | TOP1000 | 0.18 | 0.08 | 27.8% | 40% | bull-only |
| `rank(fnd6_txpd / close)` | TOP500 | 0.11 | 0.04 | 33.1% | 40% | bull-only |
| `rank(fnd6_txpd)` | TOP1000 | 0.06 | 0.02 | 43.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_fiao: 0.351 (weakly positively correlated)
- fnd6_mrcta: 0.284 (weakly positively correlated)
- fnd6_lqpl1: 0.280 (weakly positively correlated)
- fnd6_recco: 0.244 (weakly positively correlated)
- fnd6_tfvl: 0.197 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
