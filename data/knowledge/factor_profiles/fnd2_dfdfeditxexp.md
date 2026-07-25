---
field: fnd2_dfdfeditxexp
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.66
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.361
ann_vol: 0.165
hit_rate: 0.4988
rolling_sharpe_min: -1.492
rolling_sharpe_max: 2.087
negated_best_sharpe: 0.67
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: 0.01
---
# fnd2_dfdfeditxexp (fundamental2)

*Income Tax Expense, Deferred - Federal*

## Signal Profile
- `rank(fnd2_dfdfeditxexp)`: S=0.11, F=0.02, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd2_dfdfeditxexp / close)`: S=0.14, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_dfdfeditxexp, 5))`: S=0.49, F=0.24, T=33.9%, INFERIOR (TOP500)
- `-rank(fnd2_dfdfeditxexp)`: S=0.21, F=0.05, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdfeditxexp, 5))`: S=-0.43, F=-0.20, T=34.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_dfdfeditxexp, 22)`: S=0.66, F=0.47, T=23.0%, INFERIOR (TOP3000)
- `ts_mean(fnd2_dfdfeditxexp, 10)`: S=-0.45, F=-0.21, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_dfdfeditxexp, 22))`: S=0.17, F=0.05, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdfeditxexp)`: S=0.55, F=0.23, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdfeditxexp / close)`: S=0.67, F=0.31, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.47, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.07 (moderate), ret=+12.7%
  - 2020: S=-1.06 (negative), ret=-17.4%
  - 2021: S=0.50 (weak), ret=+7.6%
  - 2022: S=1.22 (moderate), ret=+25.4%
  - 2023: S=0.66 (moderate), ret=+9.9%

## Risk & Drawdown
- Max drawdown: 36.10% over 790 days (recovered)
- Annualized: return +7.8%, volatility 16.5% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.13, excess kurtosis +8.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.49, max 2.09, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +26.27%; worst month: -25.68%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.66
- Sideways: S=0.77
- Bear: S=-1.40

## Negated Direction
Best negated: `rank(-1 * fnd2_dfdfeditxexp / close)` S=0.67, F=0.31, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_dfdfeditxexp)`: S=0.55, F=0.23, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdfeditxexp / close)`: S=0.67, F=0.31, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdfeditxexp, 5))`: S=-0.43, F=-0.20, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_dfdfeditxexp, 5))` | TOP500 | 0.47 | 0.24 | 36.1% | 80% | bull-only |
| `rank(ts_delta(fnd2_dfdfeditxexp, 5))` | TOP200 | 0.28 | 0.12 | 32.3% | 60% | mixed |
| `rank(fnd2_dfdfeditxexp)` | TOP3000 | 0.12 | 0.02 | 5.7% | 60% | mixed |
| `rank(fnd2_dfdfeditxexp / close)` | TOP3000 | 0.15 | 0.02 | 5.8% | 80% | mixed |

## Correlation Notes
Top correlates:
- fn_def_income_tax_expense_a: 0.475 (moderately positively correlated)
- fnd2_dfdlocalitxexp: 0.233 (weakly positively correlated)
- fnd6_txdfed: 0.219 (weakly positively correlated)
- fnd2_currfedtxexp: 0.175 (weakly positively correlated)
- fn_assets_fair_val_a: 0.163 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
