---
field: fn_prepaid_expense_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 1.3
best_fitness: 0.76
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 10
max_drawdown: 0.1652
ann_vol: 0.0959
hit_rate: 0.5223
rolling_sharpe_min: -0.897
rolling_sharpe_max: 2.936
top_merge_partner: rank(scl12_buzz * (-1 * returns))
negated_best_sharpe: 0.35
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.95
---
# fn_prepaid_expense_q (fundamental2)

*Carrying amount for an unclassified balance sheet date of expenditures made in advance of when the economic benefit of the cost will be realized, and which will be expensed in future periods with the passage of time or when a triggering event occurs. For a classified balance sheet, represents the noncurrent portion of prepaid expenses (the current portion has a separate concept).*

## Signal Profile
- `rank(fn_prepaid_expense_q)`: S=0.77, F=0.59, T=1.2%, INFERIOR (TOP3000)
- `rank(fn_prepaid_expense_q / close)`: S=0.71, F=0.54, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_prepaid_expense_q, 5))`: S=1.30, F=0.76, T=36.0%, INFERIOR (TOP3000)
- `-rank(fn_prepaid_expense_q)`: S=-0.39, F=-0.25, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_prepaid_expense_q, 5))`: S=0.35, F=0.15, T=37.0%, INFERIOR (TOP3000)
- `ts_zscore(fn_prepaid_expense_q, 22)`: S=0.04, F=0.01, T=32.8%, INFERIOR (TOP3000)
- `ts_mean(fn_prepaid_expense_q, 10)`: S=0.32, F=0.19, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_prepaid_expense_q, 22))`: S=0.60, F=0.31, T=16.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_prepaid_expense_q)`: S=0.20, F=0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_prepaid_expense_q / close)`: S=-0.08, F=-0.02, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.28, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.76 (moderate), ret=+6.2%
  - 2020: S=2.35 (strong), ret=+23.2%
  - 2021: S=2.04 (strong), ret=+18.5%
  - 2022: S=1.36 (moderate), ret=+12.8%
  - 2023: S=-0.05 (negative), ret=-0.5%

## Risk & Drawdown
- Max drawdown: 16.52% over 323 days (not yet recovered, ongoing at window end)
- Annualized: return +12.3%, volatility 9.6% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.60, excess kurtosis +3.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.90, max 2.94, latest -0.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +10.18%; worst month: -3.65%
Positive months: 52%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.77
- Sideways: S=1.16
- Bear: S=0.92

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_prepaid_expense_q, 5))` S=0.35, F=0.15, INFERIOR
Direction gap: -0.95 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_prepaid_expense_q)`: S=0.20, F=0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_prepaid_expense_q / close)`: S=-0.08, F=-0.02, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_prepaid_expense_q, 5))`: S=0.35, F=0.15, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_prepaid_expense_q, 5))` | TOP3000 | 1.28 | 0.76 | 16.5% | 80% | all-weather |
| `rank(fn_prepaid_expense_q)` | TOP3000 | 0.76 | 0.59 | 22.1% | 80% | bull-only |
| `rank(fn_prepaid_expense_q / close)` | TOP1000 | 0.70 | 0.54 | 11.3% | 80% | bull-only |
| `rank(fn_prepaid_expense_q / close)` | TOP3000 | 0.70 | 0.47 | 11.8% | 100% | mixed |
| `rank(ts_delta(fn_prepaid_expense_q, 5))` | TOP500 | 0.60 | 0.30 | 36.9% | 60% | all-weather |
| `rank(fn_prepaid_expense_q / close)` | TOP500 | 0.39 | 0.25 | 18.4% | 80% | bull-only |
| `rank(fn_prepaid_expense_q)` | TOP1000 | 0.38 | 0.25 | 28.5% | 60% | bull-only |
| `rank(ts_delta(fn_prepaid_expense_q, 5))` | TOP1000 | 0.45 | 0.17 | 19.1% | 60% | all-weather |
| `rank(fn_prepaid_expense_q)` | TOP500 | 0.08 | 0.03 | 45.1% | 60% | bull-only |
| `rank(fn_prepaid_expense_q / close)` | TOP200 | 0.09 | 0.02 | 27.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- news_mins_20_pct_up: 0.155 (weakly positively correlated)
- news_mins_20_chg: 0.155 (weakly positively correlated)
- pcr_oi_all: 0.144 (weakly positively correlated)
- fnd6_newqv1300_xrdq: 0.144 (weakly positively correlated)
- fnd6_cptnewqv1300_actq: 0.143 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.10 | 2.16 | +0.53 | -0.20 | yes |
| anl4_netprofit_flag | analyst4 | -0.01 | 1.80 | +0.52 | -0.11 | yes |
| implied_volatility_put_10 | option8 | -0.00 | 1.81 | +0.52 | +0.24 | yes |
| implied_volatility_call_20 | option8 | -0.02 | 1.79 | +0.51 | +0.69 | yes |
| anl4_cfi_flag | analyst_revision | +0.04 | 1.70 | +0.42 | -0.72 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
