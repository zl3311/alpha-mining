---
field: fnd6_dcvsr
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.92
best_fitness: 0.9
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 6
max_drawdown: 0.3932
ann_vol: 0.1266
hit_rate: 0.4964
rolling_sharpe_min: -2.062
rolling_sharpe_max: 4.958
negated_best_sharpe: 0.92
negated_best_template: rank_neg_delta
negated_best_fitness: 0.9
n_negated_sims: 10
direction_gap: 0.52
---
# fnd6_dcvsr (fundamental6)

*Debt - Senior Convertible*

## Signal Profile
- `rank(fnd6_dcvsr)`: S=0.37, F=0.22, T=3.1%, INFERIOR (TOP500)
- `rank(fnd6_dcvsr / close)`: S=0.40, F=0.26, T=3.1%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_dcvsr, 5))`: S=-0.27, F=-0.12, T=23.6%, INFERIOR (TOP3000)
- `-rank(fnd6_dcvsr)`: S=0.19, F=0.07, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dcvsr, 5))`: S=0.92, F=0.90, T=17.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_dcvsr, 22)`: S=-0.32, F=-0.27, T=9.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dcvsr, 10)`: S=-0.14, F=-0.05, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dcvsr, 22))`: S=-0.33, F=-0.22, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dcvsr)`: S=0.19, F=0.07, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dcvsr / close)`: S=0.17, F=0.06, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 14F/18P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.42, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-1.12 (negative), ret=-9.3%
  - 2020: S=4.31 (strong), ret=+41.8%
  - 2021: S=-0.16 (negative), ret=-1.9%
  - 2022: S=-1.20 (negative), ret=-21.2%
  - 2023: S=1.35 (moderate), ret=+16.6%

## Risk & Drawdown
- Max drawdown: 39.32% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +5.3%, volatility 12.7% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +0.17, excess kurtosis +1.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.06, max 4.96, latest 1.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +9.59%; worst month: -8.35%
Positive months: 51%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.43
- Sideways: S=-0.85
- Bear: S=3.71

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dcvsr, 5))` S=0.92, F=0.90, INFERIOR
Direction gap: +0.52 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_dcvsr)`: S=0.19, F=0.07, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dcvsr / close)`: S=0.17, F=0.06, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dcvsr, 5))`: S=0.92, F=0.90, T=17.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dcvsr / close)` | TOP500 | 0.42 | 0.26 | 39.3% | 40% | bear-only |
| `rank(fnd6_dcvsr)` | TOP500 | 0.39 | 0.22 | 37.5% | 40% | bear-only |
| `rank(fnd6_dcvsr / close)` | TOP3000 | 0.30 | 0.10 | 13.9% | 80% | bear-only |
| `rank(fnd6_dcvsr)` | TOP3000 | 0.31 | 0.10 | 13.1% | 80% | bear-only |
| `rank(fnd6_dcvsr / close)` | TOP200 | 0.18 | 0.08 | 61.6% | 40% | bear-only |
| `rank(fnd6_dcvsr)` | TOP200 | 0.13 | 0.05 | 59.5% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_dcvt: 0.994 (strongly positively correlated)
- fnd6_dcpstk: 0.938 (strongly positively correlated)
- cashflow_fin: 0.757 (strongly positively correlated)
- fnd6_newa1v1300_fincf: 0.756 (strongly positively correlated)
- cash_flow_from_financing: 0.753 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
