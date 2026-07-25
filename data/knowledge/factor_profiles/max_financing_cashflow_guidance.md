---
field: max_financing_cashflow_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.7
best_fitness: 0.73
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.2297
ann_vol: 0.1836
hit_rate: 0.4858
rolling_sharpe_min: -1.085
rolling_sharpe_max: 2.738
redundancy_cluster: 78
negated_best_sharpe: 0.59
negated_best_template: neg_rank_level
negated_best_fitness: 0.56
n_negated_sims: 10
direction_gap: -0.11
---
# max_financing_cashflow_guidance (analyst4)

*Cash Flow From Financing - Maximum guidance value*

## Signal Profile
- `rank(max_financing_cashflow_guidance)`: S=0.70, F=0.73, T=2.4%, INFERIOR (TOP3000)
- `rank(max_financing_cashflow_guidance / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_financing_cashflow_guidance, 5))`: S=0.54, F=0.20, T=33.7%, INFERIOR (TOP200)
- `-rank(max_financing_cashflow_guidance)`: S=-0.25, F=-0.17, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_financing_cashflow_guidance, 5))`: S=0.24, F=0.05, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(max_financing_cashflow_guidance, 63)`: S=0.14, F=0.03, T=22.4%, INFERIOR (TOP3000)
- `ts_mean(max_financing_cashflow_guidance, 10)`: S=0.02, F=0.00, T=20.2%, INFERIOR (TOP3000)
- `rank(ts_rank(max_financing_cashflow_guidance, 22))`: S=-0.13, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_financing_cashflow_guidance)`: S=0.59, F=0.56, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * max_financing_cashflow_guidance / close)`: S=0.08, F=0.02, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.66, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.48 (negative), ret=-4.1%
  - 2020: S=0.82 (moderate), ret=+17.0%
  - 2021: S=1.56 (strong), ret=+32.3%
  - 2022: S=0.64 (moderate), ret=+14.6%
  - 2023: S=-0.02 (negative), ret=-0.2%

## Risk & Drawdown
- Max drawdown: 22.97% over 177 days (recovered)
- Annualized: return +12.2%, volatility 18.4% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew +0.12, excess kurtosis +5.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.08, max 2.74, latest -0.11

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +13.41%; worst month: -9.47%
Positive months: 50%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.24
- Sideways: S=-0.03
- Bear: S=-0.34

## Negated Direction
Best negated: `rank(-1 * max_financing_cashflow_guidance)` S=0.59, F=0.56, INFERIOR
Direction gap: -0.11 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_financing_cashflow_guidance)`: S=0.59, F=0.56, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * max_financing_cashflow_guidance / close)`: S=0.08, F=0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_financing_cashflow_guidance, 5))`: S=0.24, F=0.05, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_financing_cashflow_guidance)` | TOP3000 | 0.66 | 0.73 | 23.0% | 60% | mixed |
| `rank(ts_delta(max_financing_cashflow_guidance, 5))` | TOP200 | 0.56 | 0.20 | 15.4% | 60% | bear-only |
| `rank(max_financing_cashflow_guidance)` | TOP1000 | 0.24 | 0.17 | 35.1% | 60% | mixed |
| `rank(max_financing_cashflow_guidance)` | TOP200 | 0.15 | 0.07 | 30.7% | 60% | bull-only |
| `rank(max_financing_cashflow_guidance / close)` | TOP3000 | 0.07 | 0.02 | 53.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_financing_cashflow_guidance: 1.000 (strongly positively correlated)
- max_investing_cashflow_guidance: 0.983 (strongly positively correlated)
- min_investing_cashflow_guidance: 0.983 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.617 (moderately positively correlated)
- ebitda: 0.617 (moderately positively correlated)

Redundancy cluster #78: 4 similar fields, mean |rho| 0.989 (representative: min_financing_cashflow_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
