---
field: fnd6_txtubsoflimit
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.51
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1947
ann_vol: 0.0729
hit_rate: 0.4947
rolling_sharpe_min: -3.289
rolling_sharpe_max: 2.39
negated_best_sharpe: 0.62
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: 0.11
---
# fnd6_txtubsoflimit (fundamental6)

*Lapse of Statute of Limitations*

## Signal Profile
- `rank(fnd6_txtubsoflimit)`: S=0.34, F=0.16, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_txtubsoflimit / close)`: S=0.40, F=0.19, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txtubsoflimit, 5))`: S=0.02, F=0.00, T=37.5%, INFERIOR (TOP1000)
- `-rank(fnd6_txtubsoflimit)`: S=-0.04, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubsoflimit, 5))`: S=0.62, F=0.31, T=40.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txtubsoflimit, 22)`: S=0.51, F=0.34, T=19.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txtubsoflimit, 10)`: S=-0.11, F=-0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txtubsoflimit, 22))`: S=0.05, F=0.01, T=20.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubsoflimit)`: S=-0.34, F=-0.16, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubsoflimit / close)`: S=-0.40, F=-0.19, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.39, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.05 (weak), ret=+0.2%
  - 2020: S=-2.48 (negative), ret=-10.9%
  - 2021: S=1.32 (moderate), ret=+12.0%
  - 2022: S=1.22 (moderate), ret=+12.7%
  - 2023: S=-0.04 (negative), ret=-0.2%

## Risk & Drawdown
- Max drawdown: 19.47% over 805 days (recovered)
- Annualized: return +2.8%, volatility 7.3% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew -0.00, excess kurtosis +1.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.29, max 2.39, latest -0.22

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.74%; worst month: -2.77%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.70
- Sideways: S=0.39
- Bear: S=-2.83

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txtubsoflimit, 5))` S=0.62, F=0.31, INFERIOR
Direction gap: +0.11 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txtubsoflimit)`: S=-0.34, F=-0.16, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubsoflimit / close)`: S=-0.40, F=-0.19, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubsoflimit, 5))`: S=0.62, F=0.31, T=40.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txtubsoflimit / close)` | TOP3000 | 0.39 | 0.19 | 19.5% | 60% | bull-only |
| `rank(fnd6_txtubsoflimit)` | TOP3000 | 0.33 | 0.16 | 22.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txtubxintbs: 0.945 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.928 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.928 (strongly positively correlated)
- ebitda: 0.928 (strongly positively correlated)
- operating_profit_before_interest_tax: 0.927 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
