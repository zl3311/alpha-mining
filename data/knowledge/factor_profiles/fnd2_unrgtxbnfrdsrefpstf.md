---
field: fnd2_unrgtxbnfrdsrefpstf
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 1.04
best_fitness: 1.17
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.0502
ann_vol: 0.0412
hit_rate: 0.4939
rolling_sharpe_min: -1.223
rolling_sharpe_max: 1.97
negated_best_sharpe: 0.75
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: -0.29
---
# fnd2_unrgtxbnfrdsrefpstf (fundamental2)

*Amount of decrease in unrecognized tax benefits resulting from lapses of applicable statutes of limitations.*

## Signal Profile
- `rank(fnd2_unrgtxbnfrdsrefpstf)`: S=0.11, F=0.02, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_unrgtxbnfrdsrefpstf / close)`: S=0.38, F=0.13, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_unrgtxbnfrdsrefpstf, 5))`: S=-0.22, F=-0.07, T=31.8%, INFERIOR (TOP500)
- `-rank(fnd2_unrgtxbnfrdsrefpstf)`: S=0.28, F=0.09, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_unrgtxbnfrdsrefpstf, 5))`: S=0.75, F=0.41, T=34.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_unrgtxbnfrdsrefpstf, 63)`: S=1.04, F=1.17, T=15.8%, AVERAGE (TOP3000)
- `ts_mean(fnd2_unrgtxbnfrdsrefpstf, 10)`: S=-0.15, F=-0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_unrgtxbnfrdsrefpstf, 22))`: S=0.05, F=0.01, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfrdsrefpstf)`: S=0.28, F=0.09, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfrdsrefpstf / close)`: S=0.17, F=0.05, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.37, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.11 (negative), ret=-0.4%
  - 2020: S=0.34 (weak), ret=+1.6%
  - 2021: S=0.82 (moderate), ret=+3.5%
  - 2022: S=1.02 (moderate), ret=+4.5%
  - 2023: S=-0.50 (negative), ret=-1.6%

## Risk & Drawdown
- Max drawdown: 5.02% over 187 days (recovered)
- Annualized: return +1.5%, volatility 4.1% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.15, excess kurtosis +0.99

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.22, max 1.97, latest -0.55

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +2.89%; worst month: -1.93%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.02
- Sideways: S=-0.08
- Bear: S=-0.99

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_unrgtxbnfrdsrefpstf, 5))` S=0.75, F=0.41, INFERIOR
Direction gap: -0.29 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_unrgtxbnfrdsrefpstf)`: S=0.28, F=0.09, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfrdsrefpstf / close)`: S=0.17, F=0.05, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_unrgtxbnfrdsrefpstf, 5))`: S=0.75, F=0.41, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_unrgtxbnfrdsrefpstf / close)` | TOP3000 | 0.37 | 0.13 | 5.0% | 60% | bull-only |
| `rank(fnd2_unrgtxbnfrdsrefpstf)` | TOP3000 | 0.11 | 0.02 | 12.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_intangible_assets_accum_amort_a: 0.753 (strongly positively correlated)
- fnd6_intpn: 0.751 (strongly positively correlated)
- fnd2_a_rvndm: 0.751 (strongly positively correlated)
- fn_allowance_for_doubtful_accounts_receivable_a: 0.750 (strongly positively correlated)
- fn_interest_paid_net_a: 0.749 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
