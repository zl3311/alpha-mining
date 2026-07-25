---
field: cashflow_per_share_maximum
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.72
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.123
ann_vol: 0.0455
hit_rate: 0.5085
rolling_sharpe_min: -1.908
rolling_sharpe_max: 2.267
negated_best_sharpe: 0.41
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.31
---
# cashflow_per_share_maximum (analyst4)

*Cash Flow - The highest estimation, per share, with a delay of 1 quarter*

## Signal Profile
- `rank(cashflow_per_share_maximum)`: S=0.31, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(cashflow_per_share_maximum / close)`: S=0.72, F=0.49, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(cashflow_per_share_maximum, 5))`: S=0.21, F=0.03, T=35.6%, INFERIOR (TOP3000)
- `-rank(cashflow_per_share_maximum)`: S=-0.02, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_maximum, 5))`: S=0.47, F=0.17, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(cashflow_per_share_maximum, 63)`: S=0.08, F=0.01, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(cashflow_per_share_maximum, 10)`: S=-0.08, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow_per_share_maximum, 22))`: S=0.07, F=0.01, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_maximum)`: S=0.34, F=0.17, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_maximum / close)`: S=0.41, F=0.25, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.21, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.86 (strong), ret=+6.8%
  - 2020: S=-1.17 (negative), ret=-5.5%
  - 2021: S=0.01 (weak), ret=+0.1%
  - 2022: S=0.62 (moderate), ret=+3.1%
  - 2023: S=0.09 (weak), ret=+0.3%

## Risk & Drawdown
- Max drawdown: 12.30% over 1520 days (not yet recovered, ongoing at window end)
- Annualized: return +1.0%, volatility 4.5% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.02, excess kurtosis +0.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.91, max 2.27, latest 0.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +2.70%; worst month: -3.01%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.63
- Sideways: S=0.48
- Bear: S=-1.51

## Negated Direction
Best negated: `rank(-1 * cashflow_per_share_maximum / close)` S=0.41, F=0.25, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cashflow_per_share_maximum)`: S=0.34, F=0.17, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_maximum / close)`: S=0.41, F=0.25, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_maximum, 5))`: S=0.47, F=0.17, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(cashflow_per_share_maximum, 5))` | TOP3000 | 0.21 | 0.03 | 12.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- cashflow_per_share_median_value: 0.927 (strongly positively correlated)
- cashflow_per_share_minimum: 0.817 (strongly positively correlated)
- anl4_qfv4_cfps_high: 0.739 (strongly positively correlated)
- est_cashflow_ps: 0.621 (moderately positively correlated)
- anl4_qf_az_wol_spfc: 0.510 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
