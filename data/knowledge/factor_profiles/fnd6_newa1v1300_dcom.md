---
field: fnd6_newa1v1300_dcom
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.5
best_fitness: 0.32
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.332
ann_vol: 0.1012
hit_rate: 0.4623
rolling_sharpe_min: -2.247
rolling_sharpe_max: 2.788
negated_best_sharpe: 0.1
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.4
---
# fnd6_newa1v1300_dcom (fundamental6)

*Deferred Compensation*

## Signal Profile
- `rank(fnd6_newa1v1300_dcom)`: S=0.40, F=0.25, T=1.8%, INFERIOR (TOP500)
- `rank(fnd6_newa1v1300_dcom / close)`: S=0.40, F=0.25, T=1.8%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newa1v1300_dcom, 5))`: S=0.50, F=0.32, T=6.7%, INFERIOR (TOP500)
- `-rank(fnd6_newa1v1300_dcom)`: S=-0.23, F=-0.10, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dcom, 5))`: S=0.10, F=0.03, T=7.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_dcom, 63)`: S=0.33, F=0.18, T=0.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_dcom, 10)`: S=0.07, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_dcom, 22))`: S=-0.23, F=-0.13, T=7.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dcom)`: S=-0.23, F=-0.10, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dcom / close)`: S=-0.23, F=-0.10, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/15P
- LOW_FITNESS: 31F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/16P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.50, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.14 (negative), ret=-0.9%
  - 2020: S=-0.95 (negative), ret=-9.4%
  - 2021: S=0.34 (weak), ret=+4.9%
  - 2022: S=2.26 (strong), ret=+20.2%
  - 2023: S=1.16 (moderate), ret=+9.8%

## Risk & Drawdown
- Max drawdown: 33.20% over 805 days (recovered)
- Annualized: return +5.0%, volatility 10.1% (fraction of booksize)
- Hit rate: 46.2% positive days
- Tail shape: skew +1.23, excess kurtosis +14.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.25, max 2.79, latest 1.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +12.95%; worst month: -7.80%
Positive months: 57%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.42
- Sideways: S=0.69
- Bear: S=-2.13

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_dcom, 5))` S=0.10, F=0.03, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_dcom)`: S=-0.23, F=-0.10, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dcom / close)`: S=-0.23, F=-0.10, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dcom, 5))`: S=0.10, F=0.03, T=7.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_dcom, 5))` | TOP500 | 0.50 | 0.32 | 33.2% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dcom / close)` | TOP500 | 0.41 | 0.25 | 16.7% | 60% | mixed |
| `rank(fnd6_newa1v1300_dcom)` | TOP500 | 0.41 | 0.25 | 16.7% | 60% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_dcom, 5))` | TOP3000 | 0.26 | 0.13 | 18.9% | 60% | mixed |
| `rank(fnd6_newa1v1300_dcom)` | TOP1000 | 0.23 | 0.10 | 32.9% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dcom / close)` | TOP1000 | 0.23 | 0.10 | 32.9% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dcom)` | TOP200 | 0.18 | 0.08 | 40.5% | 60% | mixed |
| `rank(fnd6_newa1v1300_dcom / close)` | TOP200 | 0.18 | 0.08 | 40.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_esopnr: 0.633 (moderately positively correlated)
- min_free_cashflow_per_share_guidance: 0.625 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.625 (moderately positively correlated)
- min_total_assets_guidance: 0.625 (moderately positively correlated)
- max_free_cashflow_per_share_guidance: 0.625 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
