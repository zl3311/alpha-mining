---
field: fnd6_newa1v1300_fincf
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.96
best_fitness: 0.69
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.2833
ann_vol: 0.0908
hit_rate: 0.5166
rolling_sharpe_min: -1.626
rolling_sharpe_max: 5.13
negated_best_sharpe: 0.96
negated_best_template: rank_neg_delta
negated_best_fitness: 0.69
n_negated_sims: 10
direction_gap: 0.19
---
# fnd6_newa1v1300_fincf (fundamental6)

*Financing Activities - Net Cash Flow*

## Signal Profile
- `rank(fnd6_newa1v1300_fincf)`: S=0.36, F=0.18, T=2.1%, INFERIOR (TOP500)
- `rank(fnd6_newa1v1300_fincf / close)`: S=0.32, F=0.16, T=2.4%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newa1v1300_fincf, 5))`: S=-0.67, F=-0.43, T=32.7%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_fincf)`: S=-0.01, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_fincf, 5))`: S=0.96, F=0.69, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_fincf, 63)`: S=0.77, F=0.57, T=18.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_fincf, 10)`: S=-0.02, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_fincf, 22))`: S=-0.46, F=-0.23, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_fincf)`: S=-0.36, F=-0.18, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_fincf / close)`: S=-0.32, F=-0.16, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.38, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.12 (negative), ret=-0.5%
  - 2020: S=4.42 (strong), ret=+28.5%
  - 2021: S=-0.32 (negative), ret=-3.3%
  - 2022: S=-1.02 (negative), ret=-13.4%
  - 2023: S=0.77 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 28.33% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +3.4%, volatility 9.1% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.30, excess kurtosis +2.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.63, max 5.13, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +6.78%; worst month: -4.83%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.55
- Sideways: S=-0.34
- Bear: S=3.78

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_fincf, 5))` S=0.96, F=0.69, INFERIOR
Direction gap: +0.19 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_fincf)`: S=-0.36, F=-0.18, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_fincf / close)`: S=-0.32, F=-0.16, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_fincf, 5))`: S=0.96, F=0.69, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_fincf)` | TOP500 | 0.38 | 0.18 | 28.3% | 40% | bear-only |
| `rank(fnd6_newa1v1300_fincf / close)` | TOP500 | 0.34 | 0.16 | 35.1% | 60% | bear-only |
| `rank(fnd6_newa1v1300_fincf / close)` | TOP200 | 0.26 | 0.11 | 40.1% | 40% | bear-only |
| `rank(fnd6_newa1v1300_fincf)` | TOP200 | 0.23 | 0.09 | 37.4% | 40% | bear-only |

## Correlation Notes
Top correlates:
- cashflow_fin: 1.000 (strongly positively correlated)
- cash_flow_from_financing: 0.966 (strongly positively correlated)
- cashflow_dividends: -0.850 (strongly negatively correlated)
- fnd6_newa1v1300_dv: -0.849 (strongly negatively correlated)
- parkinson_volatility_150: 0.834 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
