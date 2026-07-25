---
field: fnd2_dfdlocalitxexp
dataset: fundamental2
best_template: rank_ts_rank
best_sharpe: 0.65
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.376
ann_vol: 0.1428
hit_rate: 0.5069
rolling_sharpe_min: -1.689
rolling_sharpe_max: 2.204
negated_best_sharpe: 0.62
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.03
---
# fnd2_dfdlocalitxexp (fundamental2)

*Income Tax Expense, Deferred*

## Signal Profile
- `rank(fnd2_dfdlocalitxexp)`: S=-0.31, F=-0.09, T=1.5%, INFERIOR (TOP1000)
- `rank(fnd2_dfdlocalitxexp / close)`: S=-0.06, F=-0.01, T=1.7%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd2_dfdlocalitxexp, 5))`: S=0.35, F=0.13, T=34.8%, INFERIOR (TOP1000)
- `-rank(fnd2_dfdlocalitxexp)`: S=0.31, F=0.09, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdlocalitxexp, 5))`: S=-0.04, F=0.00, T=34.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_dfdlocalitxexp, 22)`: S=-0.42, F=-0.25, T=21.6%, INFERIOR (TOP3000)
- `ts_mean(fnd2_dfdlocalitxexp, 10)`: S=-0.20, F=-0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_dfdlocalitxexp, 22))`: S=0.65, F=0.41, T=15.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdlocalitxexp)`: S=0.63, F=0.22, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdlocalitxexp / close)`: S=0.62, F=0.22, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.35, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.63 (moderate), ret=+6.8%
  - 2020: S=-1.15 (negative), ret=-19.1%
  - 2021: S=0.40 (weak), ret=+5.2%
  - 2022: S=1.63 (strong), ret=+23.4%
  - 2023: S=0.56 (moderate), ret=+7.9%

## Risk & Drawdown
- Max drawdown: 37.60% over 805 days (recovered)
- Annualized: return +4.9%, volatility 14.3% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.10, excess kurtosis +3.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.69, max 2.20, latest 0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +13.11%; worst month: -9.95%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.18
- Sideways: S=-0.33
- Bear: S=0.10

## Negated Direction
Best negated: `rank(-1 * fnd2_dfdlocalitxexp / close)` S=0.62, F=0.22, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_dfdlocalitxexp)`: S=0.63, F=0.22, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdlocalitxexp / close)`: S=0.62, F=0.22, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdlocalitxexp, 5))`: S=-0.04, F=0.00, T=34.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_dfdlocalitxexp, 5))` | TOP1000 | 0.35 | 0.13 | 37.6% | 80% | mixed |
| `rank(ts_delta(fnd2_dfdlocalitxexp, 5))` | TOP200 | 0.24 | 0.10 | 42.9% | 80% | weak |

## Correlation Notes
Top correlates:
- fnd2_dfdfeditxexp: 0.233 (weakly positively correlated)
- fnd6_txds: 0.184 (weakly positively correlated)
- fn_def_income_tax_expense_a: 0.171 (weakly positively correlated)
- parkinson_volatility_90: -0.137 (weakly negatively correlated)
- historical_volatility_90: -0.135 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
