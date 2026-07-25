---
field: operating_cashflow_reported_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.53
best_fitness: 0.36
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.3306
ann_vol: 0.1111
hit_rate: 0.5198
rolling_sharpe_min: -4.252
rolling_sharpe_max: 2.986
redundancy_cluster: 13
negated_best_sharpe: 0.69
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: 0.16
---
# operating_cashflow_reported_value (analyst4)

*Cash Flow from Operations - Value*

## Signal Profile
- `rank(operating_cashflow_reported_value)`: S=0.29, F=0.16, T=3.4%, INFERIOR (TOP3000)
- `rank(operating_cashflow_reported_value / close)`: S=0.53, F=0.36, T=3.9%, INFERIOR (TOP3000)
- `rank(ts_delta(operating_cashflow_reported_value, 5))`: S=0.14, F=0.03, T=36.4%, INFERIOR (TOP200)
- `-rank(operating_cashflow_reported_value)`: S=-0.23, F=-0.11, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_cashflow_reported_value, 5))`: S=0.69, F=0.20, T=38.3%, INFERIOR (TOP3000)
- `-ts_zscore(operating_cashflow_reported_value, 63)`: S=0.67, F=0.27, T=17.6%, INFERIOR (TOP3000)
- `ts_mean(operating_cashflow_reported_value, 10)`: S=-0.05, F=-0.01, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(operating_cashflow_reported_value, 22))`: S=-0.45, F=-0.16, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * operating_cashflow_reported_value)`: S=-0.29, F=-0.16, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * operating_cashflow_reported_value / close)`: S=-0.53, F=-0.36, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.52, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.24 (weak), ret=+1.2%
  - 2020: S=-3.37 (negative), ret=-22.2%
  - 2021: S=1.67 (strong), ret=+20.2%
  - 2022: S=1.66 (strong), ret=+27.3%
  - 2023: S=0.17 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 33.06% over 807 days (recovered)
- Annualized: return +5.8%, volatility 11.1% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew -0.16, excess kurtosis +1.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.25, max 2.99, latest -0.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.98%; worst month: -7.31%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.29
- Sideways: S=0.84
- Bear: S=-3.30

## Negated Direction
Best negated: `rank(-1 * ts_delta(operating_cashflow_reported_value, 5))` S=0.69, F=0.20, INFERIOR
Direction gap: +0.16 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * operating_cashflow_reported_value)`: S=-0.29, F=-0.16, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * operating_cashflow_reported_value / close)`: S=-0.53, F=-0.36, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_cashflow_reported_value, 5))`: S=0.69, F=0.20, T=38.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(operating_cashflow_reported_value / close)` | TOP3000 | 0.52 | 0.36 | 33.1% | 80% | bull-only |
| `rank(operating_cashflow_reported_value / close)` | TOP1000 | 0.35 | 0.20 | 30.9% | 40% | bull-only |
| `rank(operating_cashflow_reported_value)` | TOP3000 | 0.29 | 0.16 | 43.1% | 60% | bull-only |
| `rank(operating_cashflow_reported_value)` | TOP1000 | 0.22 | 0.11 | 40.4% | 60% | bull-only |
| `rank(ts_delta(operating_cashflow_reported_value, 5))` | TOP200 | 0.13 | 0.03 | 18.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_cfo_value: 1.000 (strongly positively correlated)
- free_cash_flow_reported_value: 0.954 (strongly positively correlated)
- anl4_fcf_value: 0.954 (strongly positively correlated)
- anl4_ebit_value: 0.950 (strongly positively correlated)
- ebit_reported_value: 0.950 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
