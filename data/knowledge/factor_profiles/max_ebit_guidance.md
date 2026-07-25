---
field: max_ebit_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.78
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1866
ann_vol: 0.0556
hit_rate: 0.5312
rolling_sharpe_min: -2.899
rolling_sharpe_max: 2.897
redundancy_cluster: 61
negated_best_sharpe: 0.27
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.51
---
# max_ebit_guidance (analyst4)

*The maximum guidance value for Earnings Before Interest and Taxes (EBIT) on an annual basis.*

## Signal Profile
- `rank(max_ebit_guidance)`: S=0.78, F=0.46, T=0.9%, INFERIOR (TOP3000)
- `rank(max_ebit_guidance / close)`: S=0.16, F=0.06, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_ebit_guidance, 5))`: S=0.58, F=0.23, T=33.8%, INFERIOR (TOP200)
- `-rank(max_ebit_guidance)`: S=-0.46, F=-0.22, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_ebit_guidance, 5))`: S=0.27, F=0.06, T=36.1%, INFERIOR (TOP3000)
- `-ts_zscore(max_ebit_guidance, 63)`: S=0.05, F=0.01, T=21.3%, INFERIOR (TOP3000)
- `ts_mean(max_ebit_guidance, 10)`: S=0.39, F=0.18, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(max_ebit_guidance, 22))`: S=-0.02, F=0.00, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_ebit_guidance)`: S=-0.53, F=-0.29, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * max_ebit_guidance / close)`: S=-0.13, F=-0.04, T=2.3%, INFERIOR (TOP3000)

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
  - 2020: S=-2.10 (negative), ret=-9.3%
  - 2021: S=1.82 (strong), ret=+13.7%
  - 2022: S=0.74 (moderate), ret=+4.7%
  - 2023: S=2.29 (strong), ret=+11.0%

## Risk & Drawdown
- Max drawdown: 18.66% over 839 days (recovered)
- Annualized: return +4.3%, volatility 5.6% (fraction of booksize)
- Hit rate: 53.1% positive days
- Tail shape: skew -0.12, excess kurtosis +1.08

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.90, max 2.90, latest 2.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +5.53%; worst month: -3.63%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.28
- Sideways: S=1.18
- Bear: S=-0.19

## Negated Direction
Best negated: `rank(-1 * ts_delta(max_ebit_guidance, 5))` S=0.27, F=0.06, INFERIOR
Direction gap: -0.51 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * max_ebit_guidance)`: S=-0.53, F=-0.29, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * max_ebit_guidance / close)`: S=-0.13, F=-0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_ebit_guidance, 5))`: S=0.27, F=0.06, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_ebit_guidance)` | TOP3000 | 0.78 | 0.46 | 18.7% | 80% | mixed |
| `rank(max_ebit_guidance)` | TOP500 | 0.53 | 0.29 | 18.7% | 40% | mixed |
| `rank(ts_delta(max_ebit_guidance, 5))` | TOP200 | 0.60 | 0.23 | 16.9% | 80% | bear-only |
| `rank(max_ebit_guidance)` | TOP1000 | 0.47 | 0.22 | 21.9% | 60% | weak |
| `rank(max_ebit_guidance)` | TOP200 | 0.31 | 0.15 | 34.7% | 40% | bear-only |
| `rank(max_ebit_guidance / close)` | TOP3000 | 0.16 | 0.06 | 50.6% | 80% | bull-only |
| `rank(max_ebit_guidance / close)` | TOP500 | 0.12 | 0.04 | 33.3% | 40% | bull-only |
| `rank(max_ebit_guidance / close)` | TOP200 | 0.07 | 0.02 | 31.7% | 40% | mixed |

## Correlation Notes
Top correlates:
- min_ebit_guidance_2: 1.000 (strongly positively correlated)
- cap: 0.693 (moderately positively correlated)
- low: 0.691 (moderately positively correlated)
- close: 0.691 (moderately positively correlated)
- open: 0.690 (moderately positively correlated)

Redundancy cluster #61: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
