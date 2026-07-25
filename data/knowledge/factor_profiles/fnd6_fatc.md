---
field: fnd6_fatc
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.77
best_fitness: 0.49
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0715
ann_vol: 0.0672
hit_rate: 0.519
rolling_sharpe_min: -0.856
rolling_sharpe_max: 2.254
negated_best_sharpe: 0.27
negated_best_template: neg_rank_level
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.5
---
# fnd6_fatc (fundamental6)

*Plant, Property and Equipment at Cost - Construction in Progress*

## Signal Profile
- `rank(fnd6_fatc)`: S=0.74, F=0.41, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_fatc / close)`: S=0.77, F=0.49, T=2.8%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_fatc, 5))`: S=0.16, F=0.06, T=21.0%, INFERIOR (TOP200)
- `-rank(fnd6_fatc)`: S=-0.63, F=-0.38, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fatc, 5))`: S=-0.02, F=0.00, T=20.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_fatc, 22)`: S=0.06, F=0.02, T=16.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_fatc, 10)`: S=-0.11, F=-0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_fatc, 22))`: S=-0.14, F=-0.05, T=19.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatc)`: S=0.27, F=0.14, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatc / close)`: S=0.09, F=0.03, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.75 (negative), ret=-3.1%
  - 2020: S=0.54 (moderate), ret=+3.5%
  - 2021: S=0.87 (moderate), ret=+8.6%
  - 2022: S=1.16 (moderate), ret=+6.7%
  - 2023: S=1.87 (strong), ret=+9.7%

## Risk & Drawdown
- Max drawdown: 7.15% over 91 days (recovered)
- Annualized: return +5.2%, volatility 6.7% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +0.05, excess kurtosis +3.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.86, max 2.25, latest 1.93

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +5.56%; worst month: -3.53%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.83
- Sideways: S=0.35
- Bear: S=-0.07

## Negated Direction
Best negated: `rank(-1 * fnd6_fatc)` S=0.27, F=0.14, INFERIOR
Direction gap: -0.50 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_fatc)`: S=0.27, F=0.14, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatc / close)`: S=0.09, F=0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fatc, 5))`: S=-0.02, F=0.00, T=20.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_fatc / close)` | TOP1000 | 0.77 | 0.49 | 7.1% | 80% | mixed |
| `rank(fnd6_fatc)` | TOP3000 | 0.73 | 0.41 | 9.6% | 60% | bull-only |
| `rank(fnd6_fatc / close)` | TOP3000 | 0.77 | 0.41 | 5.3% | 80% | bull-only |
| `rank(fnd6_fatc)` | TOP1000 | 0.63 | 0.38 | 15.3% | 60% | bull-only |
| `rank(fnd6_fatc / close)` | TOP500 | 0.41 | 0.21 | 18.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_fatc, 5))` | TOP200 | 0.15 | 0.06 | 52.5% | 60% | weak |
| `rank(fnd6_fatc)` | TOP500 | 0.17 | 0.05 | 32.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- ppent: 0.716 (strongly positively correlated)
- fnd6_newqv1300_ppentq: 0.716 (strongly positively correlated)
- fnd6_newa2v1300_ppent: 0.715 (strongly positively correlated)
- fnd6_ppeveb: 0.710 (strongly positively correlated)
- fnd6_cptmfmq_dpq: 0.710 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
