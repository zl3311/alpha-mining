---
field: fnd2_currfrtxexp
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 1.0
best_fitness: 0.99
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 3
max_drawdown: 0.2931
ann_vol: 0.1394
hit_rate: 0.4826
rolling_sharpe_min: -1.209
rolling_sharpe_max: 1.879
negated_best_sharpe: 0.29
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.71
---
# fnd2_currfrtxexp (fundamental2)

*Income Tax Expense, Current - Foreign*

## Signal Profile
- `rank(fnd2_currfrtxexp)`: S=0.05, F=0.01, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_currfrtxexp / close)`: S=0.21, F=0.07, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_currfrtxexp, 5))`: S=0.49, F=0.22, T=33.4%, INFERIOR (TOP500)
- `-rank(fnd2_currfrtxexp)`: S=-0.04, F=-0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_currfrtxexp, 5))`: S=-0.08, F=-0.02, T=28.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_currfrtxexp, 63)`: S=1.00, F=0.99, T=16.5%, INFERIOR (TOP3000)
- `ts_mean(fnd2_currfrtxexp, 10)`: S=-0.12, F=-0.04, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_currfrtxexp, 22))`: S=0.03, F=0.00, T=15.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_currfrtxexp)`: S=0.25, F=0.14, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_currfrtxexp / close)`: S=0.29, F=0.17, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.50, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.99 (moderate), ret=+12.0%
  - 2020: S=0.93 (moderate), ret=+11.6%
  - 2021: S=-0.86 (negative), ret=-12.1%
  - 2022: S=-0.01 (negative), ret=-0.2%
  - 2023: S=1.81 (strong), ret=+23.1%

## Risk & Drawdown
- Max drawdown: 29.31% over 1076 days (recovered)
- Annualized: return +7.0%, volatility 13.9% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.07, excess kurtosis +3.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.21, max 1.88, latest 1.77

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +15.17%; worst month: -7.03%
Positive months: 49%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.36
- Sideways: S=0.97
- Bear: S=0.23

## Negated Direction
Best negated: `rank(-1 * fnd2_currfrtxexp / close)` S=0.29, F=0.17, INFERIOR
Direction gap: -0.71 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd2_currfrtxexp)`: S=0.25, F=0.14, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_currfrtxexp / close)`: S=0.29, F=0.17, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_currfrtxexp, 5))`: S=-0.08, F=-0.02, T=28.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_currfrtxexp, 5))` | TOP500 | 0.50 | 0.22 | 29.3% | 60% | weak |
| `rank(fnd2_currfrtxexp / close)` | TOP3000 | 0.20 | 0.07 | 18.9% | 60% | bull-only |
| `rank(ts_delta(fnd2_currfrtxexp, 5))` | TOP3000 | 0.13 | 0.03 | 19.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_unrgtxbnfinregfprtxps: 0.184 (weakly positively correlated)
- fnd2_ebitfr: 0.163 (weakly positively correlated)
- return_assets: 0.153 (weakly positively correlated)
- earnings_per_share_nongaap_value: 0.150 (weakly positively correlated)
- fnd6_cptmfmq_opepsq: 0.149 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
