---
field: anl4_af_div_value
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.85
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.2023
ann_vol: 0.1135
hit_rate: 0.4939
rolling_sharpe_min: -1.83
rolling_sharpe_max: 1.852
negated_best_sharpe: 0.85
negated_best_template: rank_neg_delta
negated_best_fitness: 0.42
n_negated_sims: 10
direction_gap: 0.63
---
# anl4_af_div_value (analyst4)

*Dividend - Actual value*

## Signal Profile
- `rank(anl4_af_div_value)`: S=0.03, F=0.01, T=1.2%, INFERIOR (TOP1000)
- `rank(anl4_af_div_value / close)`: S=0.22, F=0.10, T=1.7%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_af_div_value, 5))`: S=-0.34, F=-0.12, T=34.8%, INFERIOR (TOP500)
- `-rank(anl4_af_div_value)`: S=-0.03, F=-0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_af_div_value, 5))`: S=0.85, F=0.42, T=34.7%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_af_div_value, 63)`: S=0.06, F=0.01, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_af_div_value, 10)`: S=-0.01, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_af_div_value, 22))`: S=-0.05, F=-0.01, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_af_div_value)`: S=-0.03, F=-0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_af_div_value / close)`: S=-0.22, F=-0.10, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.21, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.46 (weak), ret=+2.2%
  - 2020: S=-1.43 (negative), ret=-13.6%
  - 2021: S=0.96 (moderate), ret=+12.8%
  - 2022: S=1.20 (moderate), ret=+19.8%
  - 2023: S=-1.28 (negative), ret=-9.7%

## Risk & Drawdown
- Max drawdown: 20.23% over 786 days (recovered)
- Annualized: return +2.3%, volatility 11.3% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.19, excess kurtosis +2.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.83, max 1.85, latest -1.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.03%; worst month: -4.85%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.41
- Sideways: S=-0.38
- Bear: S=-2.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_af_div_value, 5))` S=0.85, F=0.42, INFERIOR
Direction gap: +0.63 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * anl4_af_div_value)`: S=-0.03, F=-0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_af_div_value / close)`: S=-0.22, F=-0.10, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_af_div_value, 5))`: S=0.85, F=0.42, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_af_div_value / close)` | TOP1000 | 0.21 | 0.10 | 20.2% | 60% | bull-only |
| `rank(anl4_af_div_value / close)` | TOP3000 | 0.20 | 0.09 | 19.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cashflow_dividends: 0.966 (strongly positively correlated)
- fnd6_newa1v1300_dv: 0.965 (strongly positively correlated)
- anl4_afv4_div_mean: 0.951 (strongly positively correlated)
- anl4_afv4_div_median: 0.949 (strongly positively correlated)
- anl4_afv4_div_high: 0.945 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
