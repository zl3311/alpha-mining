---
field: fnd6_pstkrv
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.63
best_fitness: 0.52
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1904
ann_vol: 0.1331
hit_rate: 0.4964
rolling_sharpe_min: -1.258
rolling_sharpe_max: 2.742
redundancy_cluster: 81
negated_best_sharpe: 0.38
negated_best_template: neg_rank_level
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.25
---
# fnd6_pstkrv (fundamental6)

*Preferred Stock - Redemption Value*

## Signal Profile
- `rank(fnd6_pstkrv)`: S=0.63, F=0.52, T=3.9%, INFERIOR (TOP200)
- `rank(fnd6_pstkrv / close)`: S=0.63, F=0.52, T=4.0%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_pstkrv, 5))`: S=0.49, F=0.32, T=13.8%, INFERIOR (TOP500)
- `-rank(fnd6_pstkrv)`: S=-0.07, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_pstkrv, 5))`: S=-0.21, F=-0.08, T=26.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_pstkrv, 22)`: S=0.31, F=0.15, T=8.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_pstkrv, 10)`: S=-0.08, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_pstkrv, 22))`: S=-0.06, F=-0.02, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pstkrv)`: S=0.38, F=0.14, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pstkrv / close)`: S=0.35, F=0.12, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/17P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.64, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.25 (weak), ret=+2.8%
  - 2020: S=1.16 (moderate), ret=+15.3%
  - 2021: S=0.98 (moderate), ret=+18.5%
  - 2022: S=-0.96 (negative), ret=-10.7%
  - 2023: S=1.91 (strong), ret=+16.0%

## Risk & Drawdown
- Max drawdown: 19.04% over 632 days (recovered)
- Annualized: return +8.6%, volatility 13.3% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +0.51, excess kurtosis +6.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 2.74, latest 1.89

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +12.85%; worst month: -7.39%
Positive months: 48%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.28
- Sideways: S=0.17
- Bear: S=1.36

## Negated Direction
Best negated: `rank(-1 * fnd6_pstkrv)` S=0.38, F=0.14, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_pstkrv)`: S=0.38, F=0.14, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pstkrv / close)`: S=0.35, F=0.12, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_pstkrv, 5))`: S=-0.21, F=-0.08, T=26.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_pstkrv)` | TOP200 | 0.64 | 0.52 | 19.0% | 80% | mixed |
| `rank(fnd6_pstkrv / close)` | TOP200 | 0.64 | 0.52 | 18.9% | 80% | mixed |
| `rank(ts_delta(fnd6_pstkrv, 5))` | TOP500 | 0.49 | 0.32 | 37.8% | 80% | mixed |
| `rank(ts_delta(fnd6_pstkrv, 5))` | TOP3000 | 0.48 | 0.29 | 36.6% | 80% | bear-only |
| `rank(ts_delta(fnd6_pstkrv, 5))` | TOP200 | 0.34 | 0.19 | 17.9% | 60% | mixed |
| `rank(fnd6_pstkrv / close)` | TOP1000 | 0.11 | 0.02 | 15.3% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_pstkl: 0.999 (strongly positively correlated)
- fnd6_newa2v1300_prsho: 0.496 (moderately positively correlated)
- sales_min_guidance_quarterly: -0.289 (weakly negatively correlated)
- min_investing_cashflow_guidance_2: -0.252 (weakly negatively correlated)
- max_investing_cashflow_guidance_2: -0.252 (weakly negatively correlated)

Redundancy cluster #81: 2 similar fields, mean |rho| 0.999 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
