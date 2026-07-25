---
field: pcr_oi_20
dataset: option9
best_template: ts_mean
best_sharpe: 0.39
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1359
ann_vol: 0.0396
hit_rate: 0.4988
rolling_sharpe_min: -2.899
rolling_sharpe_max: 2.288
negated_best_sharpe: 0.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.23
---
# pcr_oi_20 (option9)

*Ratio of put open interest to call open interest on a stock's options with expiration 20 days in the future*

## Signal Profile
- `rank(pcr_oi_20)`: S=0.37, F=0.13, T=12.4%, INFERIOR (TOP3000)
- `rank(pcr_oi_20 / close)`: S=0.12, F=0.04, T=12.0%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_20, 5))`: S=-0.16, F=-0.02, T=31.2%, INFERIOR (TOP3000)
- `-rank(pcr_oi_20)`: S=-0.17, F=-0.04, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_20, 5))`: S=0.16, F=0.02, T=31.2%, INFERIOR (TOP3000)
- `ts_zscore(pcr_oi_20, 22)`: S=0.09, F=0.01, T=24.7%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_20, 10)`: S=0.39, F=0.17, T=12.3%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_20, 22))`: S=-0.28, F=-0.05, T=24.7%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_20)`: S=-0.37, F=-0.13, T=12.4%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_20 / close)`: S=0.01, F=0.00, T=10.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.37, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.08 (moderate), ret=+2.1%
  - 2020: S=-2.57 (negative), ret=-9.2%
  - 2021: S=1.22 (moderate), ret=+6.1%
  - 2022: S=1.25 (moderate), ret=+6.2%
  - 2023: S=0.66 (moderate), ret=+2.0%

## Risk & Drawdown
- Max drawdown: 13.59% over 1074 days (recovered)
- Annualized: return +1.5%, volatility 4.0% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.22, excess kurtosis +1.25

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.90, max 2.29, latest 0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +2.87%; worst month: -2.93%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.85
- Sideways: S=0.75
- Bear: S=-1.64

## Negated Direction
Best negated: `rank(-1 * ts_delta(pcr_oi_20, 5))` S=0.16, F=0.02, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pcr_oi_20)`: S=-0.37, F=-0.13, T=12.4%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_20 / close)`: S=0.01, F=0.00, T=10.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_20, 5))`: S=0.16, F=0.02, T=31.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_20)` | TOP3000 | 0.37 | 0.13 | 13.6% | 80% | bull-only |
| `rank(pcr_oi_20)` | TOP500 | 0.30 | 0.08 | 11.2% | 60% | weak |
| `rank(pcr_oi_20)` | TOP1000 | 0.17 | 0.04 | 10.1% | 80% | bull-only |

## Correlation Notes
Top correlates:
- pcr_oi_10: 0.972 (strongly positively correlated)
- pcr_oi_30: 0.962 (strongly positively correlated)
- pcr_oi_all: 0.905 (strongly positively correlated)
- pcr_oi_360: 0.782 (strongly positively correlated)
- put_breakeven_120: 0.770 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
