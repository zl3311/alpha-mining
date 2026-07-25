---
field: fnd6_newa1v1300_dvt
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.73
best_fitness: 0.61
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2349
ann_vol: 0.1337
hit_rate: 0.5231
rolling_sharpe_min: -1.069
rolling_sharpe_max: 3.028
negated_best_sharpe: 0.36
negated_best_template: neg_rank_level
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.37
---
# fnd6_newa1v1300_dvt (fundamental6)

*Dividends - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_dvt)`: S=0.10, F=0.03, T=2.5%, INFERIOR (TOP1000)
- `rank(fnd6_newa1v1300_dvt / close)`: S=0.23, F=0.11, T=2.6%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newa1v1300_dvt, 5))`: S=0.40, F=0.15, T=40.0%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_dvt)`: S=-0.10, F=-0.03, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dvt, 5))`: S=0.09, F=0.02, T=27.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_dvt, 63)`: S=0.73, F=0.61, T=19.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_dvt, 10)`: S=0.13, F=0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_dvt, 22))`: S=-0.12, F=-0.03, T=20.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dvt)`: S=0.36, F=0.24, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dvt / close)`: S=0.34, F=0.22, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.41, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.84 (moderate), ret=+9.0%
  - 2020: S=-0.05 (negative), ret=-0.8%
  - 2021: S=0.00 (weak), ret=+0.0%
  - 2022: S=-0.38 (negative), ret=-5.2%
  - 2023: S=1.99 (strong), ret=+23.8%

## Risk & Drawdown
- Max drawdown: 23.49% over 699 days (recovered)
- Annualized: return +5.5%, volatility 13.4% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew -0.45, excess kurtosis +3.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.07, max 3.03, latest 1.96

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +10.14%; worst month: -6.27%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.08
- Sideways: S=1.01
- Bear: S=-0.81

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_dvt)` S=0.36, F=0.24, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_dvt)`: S=0.36, F=0.24, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dvt / close)`: S=0.34, F=0.22, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dvt, 5))`: S=0.09, F=0.02, T=27.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_dvt, 5))` | TOP3000 | 0.41 | 0.15 | 23.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_dvt, 5))` | TOP1000 | 0.37 | 0.14 | 43.8% | 80% | bull-only |
| `rank(fnd6_newa1v1300_dvt / close)` | TOP1000 | 0.23 | 0.11 | 24.4% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dvt / close)` | TOP3000 | 0.21 | 0.10 | 25.5% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dvt / close)` | TOP500 | 0.07 | 0.03 | 35.6% | 40% | bull-only |
| `rank(fnd6_newa1v1300_dvt)` | TOP1000 | 0.09 | 0.03 | 34.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_dvt, 5))` | TOP200 | 0.09 | 0.02 | 37.0% | 80% | mixed |
| `rank(fnd6_newa1v1300_dvt)` | TOP3000 | 0.07 | 0.02 | 34.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_dvc: 0.902 (strongly positively correlated)
- fnd6_newqv1300_cibegniq: 0.166 (weakly positively correlated)
- fnd6_mfmq_ibcomq: 0.162 (weakly positively correlated)
- income: 0.162 (weakly positively correlated)
- fn_income_tax_expense_a: 0.158 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
