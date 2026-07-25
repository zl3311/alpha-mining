---
field: min_financing_cashflow_guidance_2
dataset: analyst4
best_template: rank_level
best_sharpe: 0.44
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.4281
ann_vol: 0.2634
hit_rate: 0.5101
rolling_sharpe_min: -1.52
rolling_sharpe_max: 1.779
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.38
n_negated_sims: 10
direction_gap: 0.08
---
# min_financing_cashflow_guidance_2 (analyst4)

*Minimum guidance value for Cash Flow From Financing on an annual basis*

## Signal Profile
- `rank(min_financing_cashflow_guidance_2)`: S=0.44, F=0.42, T=1.3%, INFERIOR (TOP3000)
- `rank(min_financing_cashflow_guidance_2 / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_financing_cashflow_guidance_2, 5))`: S=0.54, F=0.20, T=33.7%, INFERIOR (TOP200)
- `-rank(min_financing_cashflow_guidance_2)`: S=0.03, F=0.01, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_financing_cashflow_guidance_2, 5))`: S=0.25, F=0.05, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(min_financing_cashflow_guidance_2, 63)`: S=0.14, F=0.03, T=22.4%, INFERIOR (TOP3000)
- `ts_mean(min_financing_cashflow_guidance_2, 10)`: S=-0.03, F=0.00, T=23.2%, INFERIOR (TOP3000)
- `rank(ts_rank(min_financing_cashflow_guidance_2, 22))`: S=-0.13, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * min_financing_cashflow_guidance_2)`: S=0.52, F=0.38, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * min_financing_cashflow_guidance_2 / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.43, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.28 (negative), ret=-7.2%
  - 2020: S=0.30 (weak), ret=+8.8%
  - 2021: S=0.80 (moderate), ret=+18.7%
  - 2022: S=0.61 (moderate), ret=+15.8%
  - 2023: S=0.80 (moderate), ret=+19.9%

## Risk & Drawdown
- Max drawdown: 42.81% over 752 days (recovered)
- Annualized: return +11.4%, volatility 26.3% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.40, excess kurtosis +8.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.52, max 1.78, latest 0.77

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +20.42%; worst month: -14.49%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.85
- Sideways: S=-0.62
- Bear: S=0.17

## Negated Direction
Best negated: `rank(-1 * min_financing_cashflow_guidance_2)` S=0.52, F=0.38, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * min_financing_cashflow_guidance_2)`: S=0.52, F=0.38, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * min_financing_cashflow_guidance_2 / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_financing_cashflow_guidance_2, 5))`: S=0.25, F=0.05, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_financing_cashflow_guidance_2)` | TOP3000 | 0.43 | 0.42 | 42.8% | 80% | mixed |
| `rank(min_financing_cashflow_guidance_2)` | TOP500 | 0.36 | 0.24 | 39.4% | 60% | bull-only |
| `rank(ts_delta(min_financing_cashflow_guidance_2, 5))` | TOP200 | 0.56 | 0.20 | 15.4% | 60% | bear-only |
| `rank(min_financing_cashflow_guidance_2)` | TOP200 | 0.15 | 0.07 | 30.7% | 60% | bull-only |
| `rank(min_financing_cashflow_guidance_2 / close)` | TOP3000 | 0.07 | 0.02 | 53.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cash_flow_financing_max_guidance: 1.000 (strongly positively correlated)
- fnd6_dltp: 0.387 (weakly positively correlated)
- fnd6_dltr: 0.378 (weakly positively correlated)
- fnd2_a_flintasacmamtzcsrld: 0.375 (weakly positively correlated)
- anl4_afv4_eps_low: 0.366 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
