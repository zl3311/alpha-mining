---
field: anl4_ebitda_value
dataset: analyst4
cluster: analyst4_income_expense
coverage: 0.8133
community_alphas: 14531
best_template: rank_value_norm
best_sharpe: 0.6
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.3102
ann_vol: 0.113
hit_rate: 0.5028
rolling_sharpe_min: -3.694
rolling_sharpe_max: 2.923
redundancy_cluster: 13
negated_best_sharpe: 0.76
negated_best_template: rank_neg_delta
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: 0.16
---
# anl4_ebitda_value (analyst4)

*Earnings before interest, taxes, depreciation and amortization - announced financial value*

## Signal Profile
- `rank(anl4_ebitda_value)`: S=0.35, F=0.22, T=1.6%, INFERIOR (TOP3000)
- `rank(anl4_ebitda_value / close)`: S=0.60, F=0.44, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ebitda_value, 5))`: S=-0.10, F=-0.01, T=38.3%, INFERIOR (TOP3000)
- `-rank(anl4_ebitda_value)`: S=-0.14, F=-0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_value, 5))`: S=0.76, F=0.28, T=38.3%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_ebitda_value, 63)`: S=-0.28, F=-0.07, T=17.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebitda_value, 10)`: S=0.03, F=0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebitda_value, 22))`: S=-0.07, F=-0.01, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_value)`: S=0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_value / close)`: S=0.01, F=0.00, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.18 (weak), ret=+0.9%
  - 2020: S=-2.79 (negative), ret=-19.8%
  - 2021: S=1.62 (strong), ret=+22.5%
  - 2022: S=1.74 (strong), ret=+28.7%
  - 2023: S=0.05 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 31.02% over 770 days (recovered)
- Annualized: return +6.7%, volatility 11.3% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew -0.02, excess kurtosis +2.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.69, max 2.92, latest -0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +11.33%; worst month: -6.05%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.38
- Sideways: S=0.64
- Bear: S=-3.11

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ebitda_value, 5))` S=0.76, F=0.28, INFERIOR
Direction gap: +0.16 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_ebitda_value)`: S=0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_value / close)`: S=0.01, F=0.00, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_value, 5))`: S=0.76, F=0.28, T=38.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ebitda_value / close)` | TOP3000 | 0.59 | 0.44 | 31.0% | 80% | bull-only |
| `rank(anl4_ebitda_value)` | TOP3000 | 0.34 | 0.22 | 47.7% | 60% | bull-only |
| `rank(anl4_ebitda_value / close)` | TOP1000 | 0.23 | 0.11 | 38.0% | 60% | bull-only |
| `rank(anl4_ebitda_value)` | TOP1000 | 0.14 | 0.06 | 50.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- ebitda_reported_value: 1.000 (strongly positively correlated)
- fnd6_cptmfmq_oibdpq: 0.983 (strongly positively correlated)
- fnd6_cptnewqv1300_oibdpq: 0.983 (strongly positively correlated)
- operating_profit_before_depr_amort: 0.966 (strongly positively correlated)
- ebit_reported_value: 0.966 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
