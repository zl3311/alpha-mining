---
field: fnd6_optfvgr
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.61
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2749
ann_vol: 0.1611
hit_rate: 0.4988
rolling_sharpe_min: -1.016
rolling_sharpe_max: 2.845
negated_best_sharpe: 0.61
negated_best_template: rank_neg_delta
negated_best_fitness: 0.59
n_negated_sims: 10
direction_gap: 0.07
---
# fnd6_optfvgr (fundamental6)

*Options - Fair Value of Options Granted*

## Signal Profile
- `rank(fnd6_optfvgr)`: S=0.43, F=0.25, T=2.1%, INFERIOR (TOP3000)
- `rank(fnd6_optfvgr / close)`: S=0.54, F=0.45, T=4.7%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_optfvgr, 5))`: S=0.35, F=0.16, T=33.8%, INFERIOR (TOP1000)
- `-rank(fnd6_optfvgr)`: S=0.10, F=0.03, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optfvgr, 5))`: S=0.61, F=0.59, T=18.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optfvgr, 22)`: S=-0.26, F=-0.15, T=14.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optfvgr, 10)`: S=-0.19, F=-0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optfvgr, 22))`: S=-0.14, F=-0.05, T=20.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optfvgr)`: S=0.31, F=0.18, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optfvgr / close)`: S=-0.54, F=-0.45, T=4.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.53, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.31 (moderate), ret=+10.9%
  - 2020: S=1.59 (strong), ret=+22.1%
  - 2021: S=0.17 (weak), ret=+3.2%
  - 2022: S=-0.29 (negative), ret=-6.7%
  - 2023: S=1.22 (moderate), ret=+12.5%

## Risk & Drawdown
- Max drawdown: 27.49% over 640 days (not yet recovered, ongoing at window end)
- Annualized: return +8.6%, volatility 16.1% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.28, excess kurtosis +2.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.02, max 2.85, latest 1.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +10.37%; worst month: -10.58%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.24
- Sideways: S=0.52
- Bear: S=0.90

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_optfvgr, 5))` S=0.61, F=0.59, INFERIOR
Direction gap: +0.07 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_optfvgr)`: S=0.31, F=0.18, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optfvgr / close)`: S=-0.54, F=-0.45, T=4.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optfvgr, 5))`: S=0.61, F=0.59, T=18.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optfvgr / close)` | TOP200 | 0.53 | 0.45 | 27.5% | 80% | mixed |
| `rank(fnd6_optfvgr)` | TOP3000 | 0.43 | 0.25 | 34.6% | 80% | bull-only |
| `rank(ts_delta(fnd6_optfvgr, 5))` | TOP1000 | 0.35 | 0.16 | 26.5% | 80% | mixed |
| `rank(fnd6_optfvgr / close)` | TOP500 | 0.23 | 0.11 | 26.9% | 60% | mixed |
| `rank(fnd6_optfvgr / close)` | TOP3000 | 0.11 | 0.04 | 34.1% | 40% | bear-only |
| `rank(fnd6_optfvgr / close)` | TOP1000 | 0.12 | 0.04 | 26.8% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_prch: 0.577 (moderately positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.556 (moderately positively correlated)
- fn_comp_not_rec_a: 0.552 (moderately positively correlated)
- fn_oth_comp_fair_value_a: 0.534 (moderately positively correlated)
- fnd6_prcc: 0.529 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
