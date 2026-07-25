---
field: fnd2_unrgtxbnfinregfcrps
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.37
best_fitness: 0.21
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.0865
ann_vol: 0.046
hit_rate: 0.4996
rolling_sharpe_min: -1.148
rolling_sharpe_max: 1.698
negated_best_sharpe: 0.26
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.11
---
# fnd2_unrgtxbnfinregfcrps (fundamental2)

*Amount of increase in unrecognized tax benefits resulting from tax positions that have been or will be taken in current period tax return.*

## Signal Profile
- `rank(fnd2_unrgtxbnfinregfcrps)`: S=0.13, F=0.03, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_unrgtxbnfinregfcrps / close)`: S=0.29, F=0.09, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_unrgtxbnfinregfcrps, 5))`: S=-0.07, F=-0.01, T=34.4%, INFERIOR (TOP3000)
- `-rank(fnd2_unrgtxbnfinregfcrps)`: S=0.04, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_unrgtxbnfinregfcrps, 5))`: S=0.26, F=0.09, T=32.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_unrgtxbnfinregfcrps, 63)`: S=0.37, F=0.21, T=16.4%, INFERIOR (TOP3000)
- `ts_mean(fnd2_unrgtxbnfinregfcrps, 10)`: S=0.22, F=0.09, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_unrgtxbnfinregfcrps, 22))`: S=-0.28, F=-0.11, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfinregfcrps)`: S=0.13, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfinregfcrps / close)`: S=-0.07, F=-0.01, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.28, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.86 (moderate), ret=+2.8%
  - 2020: S=1.06 (moderate), ret=+4.0%
  - 2021: S=0.26 (weak), ret=+1.1%
  - 2022: S=-0.71 (negative), ret=-4.1%
  - 2023: S=0.51 (moderate), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 8.65% over 708 days (not yet recovered, ongoing at window end)
- Annualized: return +1.3%, volatility 4.6% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.32, excess kurtosis +1.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 1.70, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +3.00%; worst month: -2.41%
Positive months: 52%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.33
- Sideways: S=0.65
- Bear: S=-0.10

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_unrgtxbnfinregfcrps, 5))` S=0.26, F=0.09, INFERIOR
Direction gap: -0.11 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_unrgtxbnfinregfcrps)`: S=0.13, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfinregfcrps / close)`: S=-0.07, F=-0.01, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_unrgtxbnfinregfcrps, 5))`: S=0.26, F=0.09, T=32.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_unrgtxbnfinregfcrps / close)` | TOP3000 | 0.28 | 0.09 | 8.6% | 80% | weak |
| `rank(fnd2_unrgtxbnfinregfcrps)` | TOP3000 | 0.13 | 0.03 | 17.4% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fn_allocated_share_based_compensation_expense_a: 0.723 (strongly positively correlated)
- fnd6_newa2v1300_xrd: 0.720 (strongly positively correlated)
- fnd2_a_dfdtxava: 0.713 (strongly positively correlated)
- fn_comp_not_rec_a: 0.703 (strongly positively correlated)
- fnd6_mkvalt: 0.698 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
