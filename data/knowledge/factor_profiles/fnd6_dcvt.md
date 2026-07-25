---
field: fnd6_dcvt
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.92
best_fitness: 0.89
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.3572
ann_vol: 0.1207
hit_rate: 0.5028
rolling_sharpe_min: -1.97
rolling_sharpe_max: 4.836
negated_best_sharpe: 0.92
negated_best_template: rank_neg_delta
negated_best_fitness: 0.89
n_negated_sims: 10
direction_gap: 0.53
---
# fnd6_dcvt (fundamental6)

*Debt - Convertible*

## Signal Profile
- `rank(fnd6_dcvt)`: S=0.35, F=0.20, T=3.0%, INFERIOR (TOP500)
- `rank(fnd6_dcvt / close)`: S=0.39, F=0.24, T=3.0%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_dcvt, 5))`: S=-0.39, F=-0.22, T=24.3%, INFERIOR (TOP3000)
- `-rank(fnd6_dcvt)`: S=0.26, F=0.11, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dcvt, 5))`: S=0.92, F=0.89, T=18.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_dcvt, 22)`: S=-0.21, F=-0.14, T=9.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dcvt, 10)`: S=-0.17, F=-0.06, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dcvt, 22))`: S=-0.61, F=-0.52, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dcvt)`: S=0.26, F=0.11, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dcvt / close)`: S=0.25, F=0.11, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.40, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-1.47 (negative), ret=-10.8%
  - 2020: S=4.15 (strong), ret=+37.9%
  - 2021: S=-0.04 (negative), ret=-0.4%
  - 2022: S=-1.14 (negative), ret=-19.6%
  - 2023: S=1.42 (moderate), ret=+16.7%

## Risk & Drawdown
- Max drawdown: 35.72% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +4.9%, volatility 12.1% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.21, excess kurtosis +1.52

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.97, max 4.84, latest 1.47

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +8.81%; worst month: -8.16%
Positive months: 52%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.31
- Sideways: S=-1.02
- Bear: S=3.69

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dcvt, 5))` S=0.92, F=0.89, INFERIOR
Direction gap: +0.53 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_dcvt)`: S=0.26, F=0.11, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dcvt / close)`: S=0.25, F=0.11, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dcvt, 5))`: S=0.92, F=0.89, T=18.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dcvt / close)` | TOP500 | 0.40 | 0.24 | 35.7% | 40% | bear-only |
| `rank(fnd6_dcvt)` | TOP500 | 0.36 | 0.20 | 34.2% | 40% | bear-only |
| `rank(fnd6_dcvt)` | TOP3000 | 0.18 | 0.04 | 13.8% | 60% | bear-only |
| `rank(fnd6_dcvt / close)` | TOP3000 | 0.17 | 0.04 | 15.1% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_dcvsr: 0.994 (strongly positively correlated)
- fnd6_dcpstk: 0.942 (strongly positively correlated)
- cashflow_fin: 0.750 (strongly positively correlated)
- fnd6_newa1v1300_fincf: 0.749 (strongly positively correlated)
- cash_flow_from_financing: 0.746 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
