---
field: anl4_gric_mean
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.7
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0998
ann_vol: 0.0778
hit_rate: 0.4988
rolling_sharpe_min: -1.092
rolling_sharpe_max: 2.246
redundancy_cluster: 1
negated_best_sharpe: 0.08
negated_best_template: neg_rank_level
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.62
---
# anl4_gric_mean (analyst4)

*Gross income - mean of estimations*

## Signal Profile
- `rank(anl4_gric_mean)`: S=0.47, F=0.32, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_gric_mean / close)`: S=0.70, F=0.46, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_gric_mean, 5))`: S=0.76, F=0.25, T=36.0%, INFERIOR (TOP1000)
- `-rank(anl4_gric_mean)`: S=-0.21, F=-0.10, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_mean, 5))`: S=0.08, F=0.01, T=35.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_gric_mean, 22)`: S=0.33, F=0.09, T=35.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_gric_mean, 10)`: S=0.13, F=0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_gric_mean, 22))`: S=0.55, F=0.23, T=14.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_mean)`: S=0.08, F=0.03, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_mean / close)`: S=0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.70, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.24 (negative), ret=-1.3%
  - 2020: S=-0.09 (negative), ret=-0.8%
  - 2021: S=1.20 (moderate), ret=+12.4%
  - 2022: S=1.31 (moderate), ret=+9.2%
  - 2023: S=1.43 (moderate), ret=+7.2%

## Risk & Drawdown
- Max drawdown: 9.98% over 419 days (recovered)
- Annualized: return +5.4%, volatility 7.8% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.40, excess kurtosis +2.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 2.25, latest 1.49

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +8.14%; worst month: -4.07%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.11
- Sideways: S=0.14
- Bear: S=-1.62

## Negated Direction
Best negated: `rank(-1 * anl4_gric_mean)` S=0.08, F=0.03, INFERIOR
Direction gap: -0.62 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_gric_mean)`: S=0.08, F=0.03, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_mean / close)`: S=0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_mean, 5))`: S=0.08, F=0.01, T=35.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_gric_mean / close)` | TOP3000 | 0.70 | 0.46 | 10.0% | 60% | bull-only |
| `rank(anl4_gric_mean)` | TOP3000 | 0.47 | 0.32 | 39.0% | 80% | bull-only |
| `rank(ts_delta(anl4_gric_mean, 5))` | TOP1000 | 0.73 | 0.25 | 8.4% | 60% | mixed |
| `rank(ts_delta(anl4_gric_mean, 5))` | TOP500 | 0.61 | 0.21 | 10.1% | 60% | mixed |
| `rank(ts_delta(anl4_gric_mean, 5))` | TOP3000 | 0.61 | 0.17 | 5.8% | 100% | weak |
| `rank(anl4_gric_mean / close)` | TOP1000 | 0.28 | 0.14 | 19.4% | 80% | bull-only |
| `rank(anl4_gric_mean)` | TOP1000 | 0.21 | 0.10 | 43.7% | 60% | bull-only |
| `rank(anl4_gric_mean / close)` | TOP500 | 0.12 | 0.04 | 33.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- anl4_gric_median: 1.000 (strongly positively correlated)
- anl4_gric_high: 0.998 (strongly positively correlated)
- anl4_gric_low: 0.996 (strongly positively correlated)
- est_grossincome: 0.991 (strongly positively correlated)
- sales_estimate_minimum: 0.961 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
