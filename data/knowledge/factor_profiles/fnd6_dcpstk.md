---
field: fnd6_dcpstk
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.81
best_fitness: 0.67
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 3
max_drawdown: 0.4348
ann_vol: 0.1197
hit_rate: 0.4955
rolling_sharpe_min: -2.035
rolling_sharpe_max: 4.972
negated_best_sharpe: 0.81
negated_best_template: rank_neg_delta
negated_best_fitness: 0.67
n_negated_sims: 10
direction_gap: 0.55
---
# fnd6_dcpstk (fundamental6)

*Convertible Debt and Preferred Stock*

## Signal Profile
- `rank(fnd6_dcpstk)`: S=0.21, F=0.09, T=3.0%, INFERIOR (TOP500)
- `rank(fnd6_dcpstk / close)`: S=0.26, F=0.13, T=3.1%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_dcpstk, 5))`: S=-0.20, F=-0.08, T=29.2%, INFERIOR (TOP3000)
- `-rank(fnd6_dcpstk)`: S=0.23, F=0.09, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dcpstk, 5))`: S=0.81, F=0.67, T=22.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dcpstk, 63)`: S=-0.29, F=-0.26, T=11.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dcpstk, 10)`: S=-0.45, F=-0.26, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dcpstk, 22))`: S=-0.67, F=-0.57, T=19.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dcpstk)`: S=0.23, F=0.09, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dcpstk / close)`: S=0.19, F=0.07, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.27, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-1.41 (negative), ret=-9.1%
  - 2020: S=4.19 (strong), ret=+35.5%
  - 2021: S=-0.36 (negative), ret=-4.9%
  - 2022: S=-1.28 (negative), ret=-21.4%
  - 2023: S=1.48 (moderate), ret=+15.9%

## Risk & Drawdown
- Max drawdown: 43.48% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +3.3%, volatility 12.0% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.23, excess kurtosis +2.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.04, max 4.97, latest 1.53

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +7.34%; worst month: -7.63%
Positive months: 52%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.47
- Sideways: S=-1.19
- Bear: S=3.64

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dcpstk, 5))` S=0.81, F=0.67, INFERIOR
Direction gap: +0.55 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_dcpstk)`: S=0.23, F=0.09, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dcpstk / close)`: S=0.19, F=0.07, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dcpstk, 5))`: S=0.81, F=0.67, T=22.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dcpstk / close)` | TOP500 | 0.27 | 0.13 | 43.5% | 40% | bear-only |
| `rank(fnd6_dcpstk)` | TOP500 | 0.22 | 0.09 | 41.8% | 40% | bear-only |
| `rank(fnd6_dcpstk / close)` | TOP200 | 0.11 | 0.03 | 58.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_dcvt: 0.942 (strongly positively correlated)
- fnd6_dcvsr: 0.938 (strongly positively correlated)
- cashflow_fin: 0.786 (strongly positively correlated)
- fnd6_newa1v1300_fincf: 0.786 (strongly positively correlated)
- cash_flow_from_financing: 0.780 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
