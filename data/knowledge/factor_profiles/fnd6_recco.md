---
field: fnd6_recco
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.95
best_fitness: 0.69
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.3118
ann_vol: 0.2061
hit_rate: 0.468
rolling_sharpe_min: -0.97
rolling_sharpe_max: 1.831
negated_best_sharpe: 0.61
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.34
---
# fnd6_recco (fundamental6)

*Receivables - Current - Other*

## Signal Profile
- `rank(fnd6_recco)`: S=0.06, F=0.01, T=2.0%, INFERIOR (TOP200)
- `rank(fnd6_recco / close)`: S=0.09, F=0.02, T=2.1%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_recco, 5))`: S=0.60, F=0.44, T=22.8%, INFERIOR (TOP200)
- `-rank(fnd6_recco)`: S=-0.04, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_recco, 5))`: S=0.61, F=0.31, T=36.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_recco, 63)`: S=0.44, F=0.43, T=17.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_recco, 10)`: S=0.95, F=0.69, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_recco, 22))`: S=0.47, F=0.30, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_recco)`: S=0.19, F=0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_recco / close)`: S=0.20, F=0.05, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.12 (moderate), ret=+17.2%
  - 2020: S=-0.58 (negative), ret=-11.0%
  - 2021: S=0.43 (weak), ret=+9.8%
  - 2022: S=1.31 (moderate), ret=+36.1%
  - 2023: S=0.57 (moderate), ret=+7.8%

## Risk & Drawdown
- Max drawdown: 31.18% over 693 days (recovered)
- Annualized: return +12.2%, volatility 20.6% (fraction of booksize)
- Hit rate: 46.8% positive days
- Tail shape: skew +1.73, excess kurtosis +19.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.97, max 1.83, latest 0.68

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +20.69%; worst month: -10.95%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.38
- Sideways: S=0.45
- Bear: S=-0.11

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_recco, 5))` S=0.61, F=0.31, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_recco)`: S=0.19, F=0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_recco / close)`: S=0.20, F=0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_recco, 5))`: S=0.61, F=0.31, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_recco, 5))` | TOP200 | 0.59 | 0.44 | 31.2% | 80% | mixed |
| `rank(ts_delta(fnd6_recco, 5))` | TOP500 | 0.45 | 0.27 | 33.8% | 60% | mixed |
| `rank(fnd6_recco / close)` | TOP200 | 0.11 | 0.02 | 17.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txpd: 0.244 (weakly positively correlated)
- fnd6_tfvl: 0.232 (weakly positively correlated)
- fnd6_ivstch: 0.217 (weakly positively correlated)
- fnd6_optrfr: 0.204 (weakly positively correlated)
- fnd6_pidom: 0.195 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
