---
field: cashflow_dividends
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.96
best_fitness: 0.79
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 36
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2391
ann_vol: 0.1191
hit_rate: 0.4972
rolling_sharpe_min: -2.154
rolling_sharpe_max: 1.843
negated_best_sharpe: 0.36
negated_best_template: neg_rank_level
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.6
---
# cashflow_dividends (fundamental6)

*Cash Dividends (Cash Flow)*

## Signal Profile
- `rank(cashflow_dividends)`: S=0.10, F=0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(cashflow_dividends / close)`: S=0.24, F=0.11, T=1.7%, INFERIOR (TOP1000)
- `rank(ts_delta(cashflow_dividends, 5))`: S=0.20, F=0.05, T=34.4%, INFERIOR (TOP3000)
- `ts_decay_linear(rank(cashflow_dividends), 5)`: S=0.10, F=0.03, T=1.0%, INFERIOR (TOP3000)
- `-rank(cashflow_dividends)`: S=-0.10, F=-0.03, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_dividends, 5))`: S=-0.10, F=-0.02, T=29.3%, INFERIOR (TOP3000)
- `-ts_zscore(cashflow_dividends, 63)`: S=0.96, F=0.79, T=19.1%, INFERIOR (TOP3000)
- `ts_mean(cashflow_dividends, 10)`: S=0.11, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow_dividends, 22))`: S=0.11, F=0.03, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_dividends)`: S=0.36, F=0.23, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_dividends / close)`: S=0.30, F=0.18, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/23P
- LOW_FITNESS: 36F/0P
- LOW_SHARPE: 36F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.23, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.37 (weak), ret=+2.0%
  - 2020: S=-1.55 (negative), ret=-12.4%
  - 2021: S=0.92 (moderate), ret=+14.0%
  - 2022: S=1.15 (moderate), ret=+19.7%
  - 2023: S=-1.17 (negative), ret=-9.8%

## Risk & Drawdown
- Max drawdown: 23.91% over 805 days (recovered)
- Annualized: return +2.7%, volatility 11.9% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew +0.07, excess kurtosis +2.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.15, max 1.84, latest -1.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.54%; worst month: -5.68%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.48
- Sideways: S=-0.08
- Bear: S=-2.80

## Negated Direction
Best negated: `rank(-1 * cashflow_dividends)` S=0.36, F=0.23, INFERIOR
Direction gap: -0.60 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * cashflow_dividends)`: S=0.36, F=0.23, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_dividends / close)`: S=0.30, F=0.18, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_dividends, 5))`: S=-0.10, F=-0.02, T=29.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cashflow_dividends / close)` | TOP1000 | 0.23 | 0.11 | 23.9% | 60% | bull-only |
| `rank(cashflow_dividends / close)` | TOP3000 | 0.20 | 0.09 | 27.9% | 60% | bull-only |
| `rank(ts_delta(cashflow_dividends, 5))` | TOP3000 | 0.18 | 0.05 | 35.6% | 60% | mixed |
| `rank(ts_delta(cashflow_dividends, 5))` | TOP500 | 0.13 | 0.04 | 32.7% | 80% | mixed |
| `ts_decay_linear(rank(cashflow_dividends), 5)` | TOP3000 | 0.08 | 0.03 | 36.2% | 60% | bull-only |
| `rank(cashflow_dividends)` | TOP1000 | 0.09 | 0.03 | 34.0% | 60% | bull-only |
| `rank(ts_delta(cashflow_dividends, 5))` | TOP200 | 0.10 | 0.03 | 33.2% | 60% | mixed |
| `rank(cashflow_dividends)` | TOP3000 | 0.08 | 0.03 | 36.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_dv: 1.000 (strongly positively correlated)
- anl4_af_div_value: 0.966 (strongly positively correlated)
- anl4_afv4_div_mean: 0.941 (strongly positively correlated)
- anl4_afv4_div_median: 0.938 (strongly positively correlated)
- anl4_afv4_div_high: 0.931 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
