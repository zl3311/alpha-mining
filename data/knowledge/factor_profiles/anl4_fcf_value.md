---
field: anl4_fcf_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.46
best_fitness: 0.27
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.3018
ann_vol: 0.0956
hit_rate: 0.5077
rolling_sharpe_min: -4.229
rolling_sharpe_max: 2.535
negated_best_sharpe: 0.55
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.09
---
# anl4_fcf_value (analyst4)

*Free cash flow- announced financial value*

## Signal Profile
- `rank(anl4_fcf_value)`: S=0.19, F=0.08, T=3.7%, INFERIOR (TOP3000)
- `rank(anl4_fcf_value / close)`: S=0.46, F=0.27, T=4.0%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_fcf_value, 5))`: S=-0.05, F=0.00, T=40.3%, INFERIOR (TOP3000)
- `-rank(anl4_fcf_value)`: S=-0.18, F=-0.07, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_value, 5))`: S=0.55, F=0.24, T=37.5%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_fcf_value, 63)`: S=0.00, F=0.00, T=18.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcf_value, 10)`: S=-0.03, F=0.00, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcf_value, 22))`: S=-0.27, F=-0.07, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_value)`: S=0.10, F=0.03, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_value / close)`: S=0.14, F=0.05, T=4.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.45, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.51 (moderate), ret=+2.4%
  - 2020: S=-3.34 (negative), ret=-20.3%
  - 2021: S=1.25 (moderate), ret=+12.8%
  - 2022: S=1.85 (strong), ret=+25.5%
  - 2023: S=0.07 (weak), ret=+0.7%

## Risk & Drawdown
- Max drawdown: 30.18% over 705 days (recovered)
- Annualized: return +4.3%, volatility 9.6% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.08, excess kurtosis +1.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.23, max 2.54, latest -0.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.96%; worst month: -6.16%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.00
- Sideways: S=0.67
- Bear: S=-2.99

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_fcf_value, 5))` S=0.55, F=0.24, INFERIOR
Direction gap: +0.09 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_fcf_value)`: S=0.10, F=0.03, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_value / close)`: S=0.14, F=0.05, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_value, 5))`: S=0.55, F=0.24, T=37.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_fcf_value / close)` | TOP3000 | 0.45 | 0.27 | 30.2% | 80% | bull-only |
| `rank(anl4_fcf_value / close)` | TOP1000 | 0.35 | 0.19 | 25.8% | 60% | bull-only |
| `rank(anl4_fcf_value)` | TOP3000 | 0.18 | 0.08 | 40.4% | 80% | bull-only |
| `rank(anl4_fcf_value)` | TOP1000 | 0.18 | 0.07 | 35.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- free_cash_flow_reported_value: 1.000 (strongly positively correlated)
- anl4_cfo_value: 0.954 (strongly positively correlated)
- operating_cashflow_reported_value: 0.954 (strongly positively correlated)
- anl4_ptp_value: 0.931 (strongly positively correlated)
- pretax_income_standalone_value: 0.931 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
