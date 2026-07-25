---
field: fnd2_a_fedstyitxrt
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.48
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.3708
ann_vol: 0.1622
hit_rate: 0.4713
rolling_sharpe_min: -1.634
rolling_sharpe_max: 2.239
negated_best_sharpe: 0.3
negated_best_template: neg_rank
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.18
---
# fnd2_a_fedstyitxrt (fundamental2)

*Effective Income Tax Rate Reconciliation - Federal Statutory Income Tax Rate %*

## Signal Profile
- `rank(fnd2_a_fedstyitxrt)`: S=0.02, F=0.00, T=2.8%, INFERIOR (TOP200)
- `rank(fnd2_a_fedstyitxrt / close)`: S=0.39, F=0.23, T=2.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd2_a_fedstyitxrt, 5))`: S=0.39, F=0.28, T=11.7%, INFERIOR (TOP200)
- `-rank(fnd2_a_fedstyitxrt)`: S=0.30, F=0.11, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_fedstyitxrt, 5))`: S=0.07, F=0.02, T=16.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_fedstyitxrt, 22)`: S=0.48, F=0.35, T=13.2%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_fedstyitxrt, 10)`: S=-0.14, F=-0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_fedstyitxrt, 22))`: S=-0.34, F=-0.28, T=11.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_fedstyitxrt)`: S=0.30, F=0.11, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_fedstyitxrt / close)`: S=-0.21, F=-0.09, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.39, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.43 (moderate), ret=+24.3%
  - 2020: S=-0.84 (negative), ret=-14.1%
  - 2021: S=0.48 (weak), ret=+10.3%
  - 2022: S=0.68 (moderate), ret=+9.2%
  - 2023: S=0.12 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 37.08% over 657 days (recovered)
- Annualized: return +6.2%, volatility 16.2% (fraction of booksize)
- Hit rate: 47.1% positive days
- Tail shape: skew -0.25, excess kurtosis +14.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.63, max 2.24, latest 0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +13.22%; worst month: -9.25%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.30
- Sideways: S=0.01
- Bear: S=-1.05

## Negated Direction
Best negated: `-rank(fnd2_a_fedstyitxrt)` S=0.30, F=0.11, INFERIOR
Direction gap: -0.18 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_fedstyitxrt)`: S=0.30, F=0.11, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_fedstyitxrt / close)`: S=-0.21, F=-0.09, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_fedstyitxrt, 5))`: S=0.07, F=0.02, T=16.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_a_fedstyitxrt, 5))` | TOP200 | 0.39 | 0.28 | 37.1% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_fedstyitxrt, 5))` | TOP500 | 0.40 | 0.27 | 39.0% | 40% | bull-only |
| `rank(fnd2_a_fedstyitxrt / close)` | TOP500 | 0.40 | 0.23 | 22.7% | 80% | mixed |
| `rank(fnd2_a_fedstyitxrt / close)` | TOP200 | 0.40 | 0.23 | 17.8% | 100% | mixed |
| `rank(fnd2_a_fedstyitxrt / close)` | TOP1000 | 0.22 | 0.09 | 32.1% | 60% | bear-only |
| `rank(fnd2_a_fedstyitxrt / close)` | TOP3000 | 0.10 | 0.03 | 45.5% | 20% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_itcb: 0.594 (moderately positively correlated)
- min_stock_option_expense_guidance: 0.523 (moderately positively correlated)
- stock_option_expense_max_guidance_qtr: 0.523 (moderately positively correlated)
- unsystematic_risk_last_30_days: -0.489 (moderately negatively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: -0.487 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
