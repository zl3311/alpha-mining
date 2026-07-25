---
field: fnd6_optdr
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.96
best_fitness: 0.66
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2372
ann_vol: 0.1321
hit_rate: 0.4988
rolling_sharpe_min: -1.977
rolling_sharpe_max: 1.61
negated_best_sharpe: 0.96
negated_best_template: rank_neg_delta
negated_best_fitness: 0.66
n_negated_sims: 10
direction_gap: 0.6
---
# fnd6_optdr (fundamental6)

*Dividend Rate - Assumption (%)*

## Signal Profile
- `rank(fnd6_optdr)`: S=0.09, F=0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_optdr / close)`: S=0.15, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_optdr, 5))`: S=0.12, F=0.04, T=12.9%, INFERIOR (TOP200)
- `-rank(fnd6_optdr)`: S=-0.02, F=0.00, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optdr, 5))`: S=0.96, F=0.66, T=34.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_optdr, 63)`: S=0.36, F=0.30, T=11.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optdr, 10)`: S=0.05, F=0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optdr, 22))`: S=-0.47, F=-0.28, T=21.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optdr)`: S=-0.09, F=-0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optdr / close)`: S=-0.15, F=-0.06, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.14, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.40 (weak), ret=+2.5%
  - 2020: S=-0.94 (negative), ret=-9.0%
  - 2021: S=0.39 (weak), ret=+6.3%
  - 2022: S=1.20 (moderate), ret=+23.1%
  - 2023: S=-1.56 (negative), ret=-13.7%

## Risk & Drawdown
- Max drawdown: 23.72% over 568 days (recovered)
- Annualized: return +1.9%, volatility 13.2% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.07, excess kurtosis +2.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.98, max 1.61, latest -1.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +8.92%; worst month: -6.44%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.12
- Sideways: S=-0.11
- Bear: S=-2.40

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_optdr, 5))` S=0.96, F=0.66, INFERIOR
Direction gap: +0.60 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_optdr)`: S=-0.09, F=-0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optdr / close)`: S=-0.15, F=-0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optdr, 5))`: S=0.96, F=0.66, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optdr / close)` | TOP1000 | 0.14 | 0.06 | 23.7% | 60% | bull-only |
| `rank(fnd6_optdr / close)` | TOP3000 | 0.14 | 0.06 | 41.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_optdr, 5))` | TOP200 | 0.11 | 0.04 | 42.8% | 80% | bull-only |
| `rank(fnd6_optdr)` | TOP3000 | 0.07 | 0.03 | 46.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_dv: 0.931 (strongly positively correlated)
- cashflow_dividends: 0.930 (strongly positively correlated)
- anl4_af_div_value: 0.926 (strongly positively correlated)
- anl4_afv4_div_mean: 0.907 (strongly positively correlated)
- anl4_afv4_div_median: 0.904 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
