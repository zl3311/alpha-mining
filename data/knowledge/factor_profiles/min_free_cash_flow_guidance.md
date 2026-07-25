---
field: min_free_cash_flow_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.75
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1466
ann_vol: 0.0625
hit_rate: 0.5134
rolling_sharpe_min: -2.304
rolling_sharpe_max: 2.736
redundancy_cluster: 13
negated_best_sharpe: 0.54
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.21
---
# min_free_cash_flow_guidance (analyst4)

*The minimum guidance value for Free Cash Flow on an annual basis.*

## Signal Profile
- `rank(min_free_cash_flow_guidance)`: S=0.75, F=0.46, T=0.9%, INFERIOR (TOP3000)
- `rank(min_free_cash_flow_guidance / close)`: S=0.25, F=0.12, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_free_cash_flow_guidance, 5))`: S=0.44, F=0.14, T=33.5%, INFERIOR (TOP200)
- `-rank(min_free_cash_flow_guidance)`: S=-0.30, F=-0.11, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_free_cash_flow_guidance, 5))`: S=0.54, F=0.14, T=36.2%, INFERIOR (TOP3000)
- `ts_zscore(min_free_cash_flow_guidance, 22)`: S=0.08, F=0.01, T=40.7%, INFERIOR (TOP3000)
- `ts_mean(min_free_cash_flow_guidance, 10)`: S=0.32, F=0.12, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(min_free_cash_flow_guidance, 22))`: S=-0.18, F=-0.04, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * min_free_cash_flow_guidance)`: S=-0.30, F=-0.11, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * min_free_cash_flow_guidance / close)`: S=-0.06, F=-0.01, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+1.8%
  - 2020: S=-1.72 (negative), ret=-8.6%
  - 2021: S=1.70 (strong), ret=+13.8%
  - 2022: S=1.62 (strong), ret=+13.5%
  - 2023: S=0.48 (weak), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 14.66% over 745 days (recovered)
- Annualized: return +4.6%, volatility 6.2% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.07, excess kurtosis +2.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.30, max 2.74, latest 0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.80%; worst month: -1.99%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.61
- Sideways: S=0.63
- Bear: S=-1.68

## Negated Direction
Best negated: `rank(-1 * ts_delta(min_free_cash_flow_guidance, 5))` S=0.54, F=0.14, INFERIOR
Direction gap: -0.21 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * min_free_cash_flow_guidance)`: S=-0.30, F=-0.11, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * min_free_cash_flow_guidance / close)`: S=-0.06, F=-0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_free_cash_flow_guidance, 5))`: S=0.54, F=0.14, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_free_cash_flow_guidance)` | TOP3000 | 0.74 | 0.46 | 14.7% | 80% | bull-only |
| `rank(ts_delta(min_free_cash_flow_guidance, 5))` | TOP200 | 0.46 | 0.14 | 16.4% | 60% | bear-only |
| `rank(min_free_cash_flow_guidance / close)` | TOP3000 | 0.24 | 0.12 | 44.7% | 80% | bull-only |
| `rank(min_free_cash_flow_guidance)` | TOP1000 | 0.29 | 0.11 | 14.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- max_free_cash_flow_guidance: 1.000 (strongly positively correlated)
- fnd6_dn: 0.873 (strongly positively correlated)
- fnd6_txtubxintbs: 0.861 (strongly positively correlated)
- fnd6_fatp: 0.856 (strongly positively correlated)
- fnd6_newa2v1300_tstk: 0.851 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
