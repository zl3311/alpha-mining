---
field: min_ebit_guidance_2
dataset: analyst4
best_template: rank_level
best_sharpe: 0.77
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1863
ann_vol: 0.0557
hit_rate: 0.532
rolling_sharpe_min: -2.881
rolling_sharpe_max: 2.87
redundancy_cluster: 61
negated_best_sharpe: 0.42
negated_best_template: rank_neg_delta
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.35
---
# min_ebit_guidance_2 (analyst4)

*Minimum guidance value for Earnings Before Interest and Taxes (EBIT) on an annual basis.*

## Signal Profile
- `rank(min_ebit_guidance_2)`: S=0.77, F=0.45, T=0.9%, INFERIOR (TOP3000)
- `rank(min_ebit_guidance_2 / close)`: S=0.17, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_ebit_guidance_2, 5))`: S=0.31, F=0.09, T=33.7%, INFERIOR (TOP200)
- `-rank(min_ebit_guidance_2)`: S=-0.48, F=-0.24, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_ebit_guidance_2, 5))`: S=0.42, F=0.11, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(min_ebit_guidance_2, 63)`: S=0.57, F=0.24, T=20.9%, INFERIOR (TOP3000)
- `ts_mean(min_ebit_guidance_2, 10)`: S=0.48, F=0.23, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(min_ebit_guidance_2, 22))`: S=-0.09, F=-0.02, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * min_ebit_guidance_2)`: S=-0.57, F=-0.32, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * min_ebit_guidance_2 / close)`: S=-0.14, F=-0.05, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.78, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.39 (weak), ret=+1.2%
  - 2020: S=-2.07 (negative), ret=-9.2%
  - 2021: S=1.81 (strong), ret=+13.6%
  - 2022: S=0.76 (moderate), ret=+4.8%
  - 2023: S=2.24 (strong), ret=+10.9%

## Risk & Drawdown
- Max drawdown: 18.63% over 839 days (recovered)
- Annualized: return +4.3%, volatility 5.6% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.12, excess kurtosis +1.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.88, max 2.87, latest 2.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +5.55%; worst month: -3.59%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.29
- Sideways: S=1.19
- Bear: S=-0.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(min_ebit_guidance_2, 5))` S=0.42, F=0.11, INFERIOR
Direction gap: -0.35 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * min_ebit_guidance_2)`: S=-0.57, F=-0.32, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * min_ebit_guidance_2 / close)`: S=-0.14, F=-0.05, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_ebit_guidance_2, 5))`: S=0.42, F=0.11, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_ebit_guidance_2)` | TOP3000 | 0.78 | 0.45 | 18.6% | 80% | mixed |
| `rank(min_ebit_guidance_2)` | TOP500 | 0.57 | 0.32 | 18.8% | 40% | all-weather |
| `rank(min_ebit_guidance_2)` | TOP1000 | 0.49 | 0.24 | 21.8% | 60% | weak |
| `rank(min_ebit_guidance_2)` | TOP200 | 0.30 | 0.14 | 34.4% | 40% | mixed |
| `rank(ts_delta(min_ebit_guidance_2, 5))` | TOP200 | 0.33 | 0.09 | 12.8% | 60% | bear-only |
| `rank(min_ebit_guidance_2 / close)` | TOP3000 | 0.17 | 0.07 | 50.4% | 80% | bull-only |
| `rank(min_ebit_guidance_2 / close)` | TOP500 | 0.14 | 0.05 | 33.6% | 40% | bull-only |
| `rank(min_ebit_guidance_2 / close)` | TOP200 | 0.10 | 0.03 | 32.9% | 40% | mixed |

## Correlation Notes
Top correlates:
- max_ebit_guidance: 1.000 (strongly positively correlated)
- cap: 0.695 (moderately positively correlated)
- low: 0.695 (moderately positively correlated)
- close: 0.695 (moderately positively correlated)
- open: 0.694 (moderately positively correlated)

Redundancy cluster #61: 2 similar fields, mean |rho| 1.0 (representative: max_ebit_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
