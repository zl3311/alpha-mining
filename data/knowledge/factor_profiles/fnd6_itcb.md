---
field: fnd6_itcb
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.47
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.2708
ann_vol: 0.1225
hit_rate: 0.4632
rolling_sharpe_min: -1.957
rolling_sharpe_max: 2.056
negated_best_sharpe: 0.47
negated_best_template: neg_rank_level
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: 0.2
---
# fnd6_itcb (fundamental6)

*Investment Tax Credit (Balance Sheet)*

## Signal Profile
- `rank(fnd6_itcb)`: S=0.00, F=0.00, T=0.7%, INFERIOR (TOP3000)
- `rank(fnd6_itcb / close)`: S=0.00, F=0.00, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_itcb, 5))`: S=0.27, F=0.14, T=4.0%, INFERIOR (TOP200)
- `-rank(fnd6_itcb)`: S=0.45, F=0.34, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_itcb, 5))`: S=-0.16, F=-0.06, T=6.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_itcb, 63)`: S=-0.07, F=-0.01, T=4.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_itcb, 10)`: S=0.05, F=0.01, T=0.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_itcb, 22))`: S=-0.18, F=-0.07, T=6.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_itcb)`: S=0.47, F=0.37, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_itcb / close)`: S=0.47, F=0.37, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 30F/2P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.26, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.55 (moderate), ret=+3.7%
  - 2020: S=-1.36 (negative), ret=-15.5%
  - 2021: S=0.98 (moderate), ret=+17.5%
  - 2022: S=0.66 (moderate), ret=+8.7%
  - 2023: S=0.16 (weak), ret=+1.2%

## Risk & Drawdown
- Max drawdown: 27.08% over 756 days (recovered)
- Annualized: return +3.2%, volatility 12.2% (fraction of booksize)
- Hit rate: 46.3% positive days
- Tail shape: skew -0.28, excess kurtosis +3.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.96, max 2.06, latest 0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.37%; worst month: -9.85%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.92
- Sideways: S=0.02
- Bear: S=-1.82

## Negated Direction
Best negated: `rank(-1 * fnd6_itcb)` S=0.47, F=0.37, INFERIOR
Direction gap: +0.20 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_itcb)`: S=0.47, F=0.37, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_itcb / close)`: S=0.47, F=0.37, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_itcb, 5))`: S=-0.16, F=-0.06, T=6.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_itcb, 5))` | TOP200 | 0.26 | 0.14 | 27.1% | 80% | bull-only |
| `rank(ts_delta(fnd6_itcb, 5))` | TOP3000 | 0.11 | 0.04 | 37.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- min_stock_option_expense_guidance: 0.853 (strongly positively correlated)
- stock_option_expense_max_guidance_qtr: 0.853 (strongly positively correlated)
- unsystematic_risk_last_30_days: -0.797 (strongly negatively correlated)
- min_free_cashflow_per_share_guidance: 0.784 (strongly positively correlated)
- shareholders_equity_min_guidance: 0.784 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
