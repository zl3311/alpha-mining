---
field: max_free_cash_flow_guidance
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
max_drawdown: 0.148
ann_vol: 0.0628
hit_rate: 0.5142
rolling_sharpe_min: -2.333
rolling_sharpe_max: 2.75
redundancy_cluster: 13
negated_best_sharpe: 0.24
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.51
---
# max_free_cash_flow_guidance (analyst4)

*The maximum guidance value for Free Cash Flow on an annual basis.*

## Signal Profile
- `rank(max_free_cash_flow_guidance)`: S=0.75, F=0.46, T=0.9%, INFERIOR (TOP3000)
- `rank(max_free_cash_flow_guidance / close)`: S=0.24, F=0.11, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_free_cash_flow_guidance, 5))`: S=0.67, F=0.28, T=33.3%, INFERIOR (TOP200)
- `-rank(max_free_cash_flow_guidance)`: S=-0.31, F=-0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_free_cash_flow_guidance, 5))`: S=-0.67, F=-0.28, T=33.3%, INFERIOR (TOP3000)
- `ts_zscore(max_free_cash_flow_guidance, 22)`: S=0.15, F=0.03, T=42.9%, INFERIOR (TOP3000)
- `ts_mean(max_free_cash_flow_guidance, 10)`: S=0.36, F=0.15, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(max_free_cash_flow_guidance, 22))`: S=-0.14, F=-0.03, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * max_free_cash_flow_guidance)`: S=0.12, F=0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * max_free_cash_flow_guidance / close)`: S=0.24, F=0.12, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.64 (moderate), ret=+1.8%
  - 2020: S=-1.75 (negative), ret=-8.7%
  - 2021: S=1.71 (strong), ret=+13.9%
  - 2022: S=1.62 (strong), ret=+13.6%
  - 2023: S=0.49 (weak), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 14.80% over 745 days (recovered)
- Annualized: return +4.7%, volatility 6.3% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.07, excess kurtosis +2.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.33, max 2.75, latest 0.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.86%; worst month: -1.95%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.61
- Sideways: S=0.64
- Bear: S=-1.71

## Negated Direction
Best negated: `rank(-1 * max_free_cash_flow_guidance / close)` S=0.24, F=0.12, INFERIOR
Direction gap: -0.51 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * max_free_cash_flow_guidance)`: S=0.12, F=0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * max_free_cash_flow_guidance / close)`: S=0.24, F=0.12, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_free_cash_flow_guidance, 5))`: S=-0.67, F=-0.28, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_free_cash_flow_guidance)` | TOP3000 | 0.74 | 0.46 | 14.8% | 80% | bull-only |
| `rank(ts_delta(max_free_cash_flow_guidance, 5))` | TOP200 | 0.69 | 0.28 | 13.2% | 80% | bear-only |
| `rank(max_free_cash_flow_guidance)` | TOP1000 | 0.30 | 0.12 | 14.9% | 40% | bull-only |
| `rank(max_free_cash_flow_guidance / close)` | TOP3000 | 0.23 | 0.11 | 45.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- min_free_cash_flow_guidance: 1.000 (strongly positively correlated)
- fnd6_dn: 0.874 (strongly positively correlated)
- fnd6_txtubxintbs: 0.862 (strongly positively correlated)
- fnd6_fatp: 0.858 (strongly positively correlated)
- fnd6_newa2v1300_tstk: 0.852 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
