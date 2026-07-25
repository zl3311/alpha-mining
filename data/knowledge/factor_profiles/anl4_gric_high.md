---
field: anl4_gric_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.7
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0978
ann_vol: 0.0773
hit_rate: 0.4947
rolling_sharpe_min: -1.14
rolling_sharpe_max: 2.232
redundancy_cluster: 1
negated_best_sharpe: 0.81
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: 0.11
---
# anl4_gric_high (analyst4)

*Gross income - The highest estimation*

## Signal Profile
- `rank(anl4_gric_high)`: S=0.48, F=0.33, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_gric_high / close)`: S=0.70, F=0.46, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_gric_high, 5))`: S=0.16, F=0.02, T=36.2%, INFERIOR (TOP3000)
- `-rank(anl4_gric_high)`: S=-0.23, F=-0.11, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_high, 5))`: S=0.81, F=0.41, T=34.3%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_gric_high, 63)`: S=0.02, F=0.00, T=17.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_gric_high, 10)`: S=0.15, F=0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_gric_high, 22))`: S=0.17, F=0.04, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_high)`: S=0.07, F=0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_high / close)`: S=-0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.70, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.29 (negative), ret=-1.6%
  - 2020: S=-0.01 (negative), ret=-0.1%
  - 2021: S=1.22 (moderate), ret=+12.3%
  - 2022: S=1.24 (moderate), ret=+8.6%
  - 2023: S=1.41 (moderate), ret=+7.2%

## Risk & Drawdown
- Max drawdown: 9.78% over 419 days (recovered)
- Annualized: return +5.4%, volatility 7.7% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.41, excess kurtosis +2.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.14, max 2.23, latest 1.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +8.08%; worst month: -4.18%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.06
- Sideways: S=0.10
- Bear: S=-1.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_gric_high, 5))` S=0.81, F=0.41, INFERIOR
Direction gap: +0.11 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_gric_high)`: S=0.07, F=0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_high / close)`: S=-0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_high, 5))`: S=0.81, F=0.41, T=34.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_gric_high / close)` | TOP3000 | 0.70 | 0.46 | 9.8% | 60% | bull-only |
| `rank(anl4_gric_high)` | TOP3000 | 0.48 | 0.33 | 38.0% | 80% | bull-only |
| `rank(anl4_gric_high / close)` | TOP1000 | 0.29 | 0.15 | 17.7% | 80% | bull-only |
| `rank(anl4_gric_high)` | TOP1000 | 0.22 | 0.11 | 41.9% | 60% | bull-only |
| `rank(anl4_gric_high / close)` | TOP500 | 0.16 | 0.06 | 30.5% | 80% | bull-only |
| `rank(ts_delta(anl4_gric_high, 5))` | TOP3000 | 0.17 | 0.02 | 8.4% | 80% | mixed |

## Correlation Notes
Top correlates:
- anl4_gric_median: 0.999 (strongly positively correlated)
- anl4_gric_mean: 0.998 (strongly positively correlated)
- est_grossincome: 0.992 (strongly positively correlated)
- anl4_gric_low: 0.989 (strongly positively correlated)
- sales_estimate_minimum: 0.962 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
