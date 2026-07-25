---
field: fnd6_pstkl
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.63
best_fitness: 0.52
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.1895
ann_vol: 0.1344
hit_rate: 0.4988
rolling_sharpe_min: -1.254
rolling_sharpe_max: 2.587
redundancy_cluster: 81
negated_best_sharpe: 0.4
negated_best_template: neg_rank_level
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.23
---
# fnd6_pstkl (fundamental6)

*Preferred Stock - Liquidating Value*

## Signal Profile
- `rank(fnd6_pstkl)`: S=0.63, F=0.51, T=4.0%, INFERIOR (TOP200)
- `rank(fnd6_pstkl / close)`: S=0.63, F=0.52, T=4.0%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_pstkl, 5))`: S=0.59, F=0.43, T=14.4%, INFERIOR (TOP500)
- `-rank(fnd6_pstkl)`: S=-0.06, F=-0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_pstkl, 5))`: S=-0.48, F=-0.29, T=26.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_pstkl, 22)`: S=0.29, F=0.14, T=7.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_pstkl, 10)`: S=-0.08, F=-0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_pstkl, 22))`: S=0.03, F=0.01, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pstkl)`: S=0.40, F=0.15, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pstkl / close)`: S=0.38, F=0.14, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/17P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.27 (weak), ret=+3.1%
  - 2020: S=1.15 (moderate), ret=+15.3%
  - 2021: S=1.00 (moderate), ret=+19.0%
  - 2022: S=-0.95 (negative), ret=-10.7%
  - 2023: S=1.80 (strong), ret=+15.1%

## Risk & Drawdown
- Max drawdown: 18.95% over 652 days (recovered)
- Annualized: return +8.5%, volatility 13.4% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.57, excess kurtosis +6.96

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.25, max 2.59, latest 1.78

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +13.17%; worst month: -7.44%
Positive months: 46%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.29
- Sideways: S=0.14
- Bear: S=1.36

## Negated Direction
Best negated: `rank(-1 * fnd6_pstkl)` S=0.40, F=0.15, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_pstkl)`: S=0.40, F=0.15, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pstkl / close)`: S=0.38, F=0.14, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_pstkl, 5))`: S=-0.48, F=-0.29, T=26.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_pstkl / close)` | TOP200 | 0.63 | 0.52 | 18.9% | 80% | mixed |
| `rank(fnd6_pstkl)` | TOP200 | 0.63 | 0.51 | 19.1% | 80% | mixed |
| `rank(ts_delta(fnd6_pstkl, 5))` | TOP500 | 0.59 | 0.43 | 30.8% | 80% | mixed |
| `rank(ts_delta(fnd6_pstkl, 5))` | TOP3000 | 0.55 | 0.36 | 39.4% | 80% | bear-only |
| `rank(ts_delta(fnd6_pstkl, 5))` | TOP200 | 0.45 | 0.28 | 15.0% | 40% | mixed |
| `rank(ts_delta(fnd6_pstkl, 5))` | TOP1000 | 0.10 | 0.03 | 40.0% | 60% | weak |
| `rank(fnd6_pstkl / close)` | TOP1000 | 0.09 | 0.02 | 15.7% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_pstkrv: 0.999 (strongly positively correlated)
- fnd6_newa2v1300_prsho: 0.504 (moderately positively correlated)
- sales_min_guidance_quarterly: -0.293 (weakly negatively correlated)
- volume: 0.259 (weakly positively correlated)
- sales_min_guidance_value: -0.252 (weakly negatively correlated)

Redundancy cluster #81: 2 similar fields, mean |rho| 0.999 (representative: fnd6_pstkrv). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
