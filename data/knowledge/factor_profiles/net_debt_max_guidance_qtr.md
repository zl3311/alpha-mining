---
field: net_debt_max_guidance_qtr
dataset: analyst4
best_template: ts_mean
best_sharpe: 0.75
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.257
ann_vol: 0.234
hit_rate: 0.5093
rolling_sharpe_min: -0.846
rolling_sharpe_max: 2.233
redundancy_cluster: 93
negated_best_sharpe: 0.23
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.52
---
# net_debt_max_guidance_qtr (analyst4)

*Maximum guidance value for Net Debt*

## Signal Profile
- `rank(net_debt_max_guidance_qtr)`: S=0.58, F=0.61, T=1.5%, INFERIOR (TOP3000)
- `rank(net_debt_max_guidance_qtr / close)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(net_debt_max_guidance_qtr, 5))`: S=0.59, F=0.23, T=33.7%, INFERIOR (TOP200)
- `-rank(net_debt_max_guidance_qtr)`: S=-0.30, F=-0.18, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_debt_max_guidance_qtr, 5))`: S=0.23, F=0.05, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(net_debt_max_guidance_qtr, 63)`: S=0.74, F=0.32, T=22.3%, INFERIOR (TOP3000)
- `ts_mean(net_debt_max_guidance_qtr, 10)`: S=0.75, F=0.63, T=15.4%, INFERIOR (TOP3000)
- `rank(ts_rank(net_debt_max_guidance_qtr, 22))`: S=-0.22, F=-0.07, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * net_debt_max_guidance_qtr)`: S=-0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * net_debt_max_guidance_qtr / close)`: S=0.05, F=0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.58, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.35 (moderate), ret=+46.2%
  - 2020: S=-0.23 (negative), ret=-6.5%
  - 2021: S=1.34 (moderate), ret=+23.5%
  - 2022: S=0.69 (moderate), ret=+9.8%
  - 2023: S=-0.51 (negative), ret=-6.9%

## Risk & Drawdown
- Max drawdown: 25.70% over 419 days (recovered)
- Annualized: return +13.5%, volatility 23.4% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.14, excess kurtosis +3.64

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.85, max 2.23, latest -0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +24.35%; worst month: -10.15%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.80
- Sideways: S=0.61
- Bear: S=0.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(net_debt_max_guidance_qtr, 5))` S=0.23, F=0.05, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * net_debt_max_guidance_qtr)`: S=-0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * net_debt_max_guidance_qtr / close)`: S=0.05, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_debt_max_guidance_qtr, 5))`: S=0.23, F=0.05, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(net_debt_max_guidance_qtr)` | TOP3000 | 0.58 | 0.61 | 25.7% | 60% | mixed |
| `rank(net_debt_max_guidance_qtr)` | TOP200 | 0.45 | 0.33 | 40.1% | 60% | bull-only |
| `rank(ts_delta(net_debt_max_guidance_qtr, 5))` | TOP200 | 0.61 | 0.23 | 12.7% | 80% | bear-only |
| `rank(net_debt_max_guidance_qtr)` | TOP1000 | 0.28 | 0.18 | 50.7% | 80% | bull-only |
| `rank(net_debt_max_guidance_qtr / close)` | TOP3000 | 0.08 | 0.02 | 53.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- net_debt_min_guidance_qtr: 1.000 (strongly positively correlated)
- cashflow_per_share_min_guidance_quarterly: 0.525 (moderately positively correlated)
- cashflow_per_share_max_guidance_quarterly: 0.525 (moderately positively correlated)
- fnd6_cld5: 0.142 (weakly positively correlated)
- fnd6_cld4: 0.139 (weakly positively correlated)

Redundancy cluster #93: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
