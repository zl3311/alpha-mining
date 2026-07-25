---
field: est_grossincome
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.78
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.0888
ann_vol: 0.0736
hit_rate: 0.4996
rolling_sharpe_min: -0.997
rolling_sharpe_max: 2.319
redundancy_cluster: 1
negated_best_sharpe: 0.21
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.57
---
# est_grossincome (analyst4)

*Gross income - Mean of estimations*

## Signal Profile
- `rank(est_grossincome)`: S=0.53, F=0.38, T=1.0%, INFERIOR (TOP3000)
- `rank(est_grossincome / close)`: S=0.78, F=0.53, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(est_grossincome, 5))`: S=0.67, F=0.21, T=36.0%, INFERIOR (TOP1000)
- `-rank(est_grossincome)`: S=-0.24, F=-0.12, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_grossincome, 5))`: S=0.21, F=0.05, T=35.1%, INFERIOR (TOP3000)
- `ts_zscore(est_grossincome, 22)`: S=0.28, F=0.07, T=35.4%, INFERIOR (TOP3000)
- `ts_mean(est_grossincome, 10)`: S=0.15, F=0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(est_grossincome, 22))`: S=0.52, F=0.21, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * est_grossincome)`: S=0.03, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * est_grossincome / close)`: S=-0.09, F=-0.03, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.78, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.05 (negative), ret=-0.3%
  - 2020: S=0.09 (weak), ret=+0.8%
  - 2021: S=1.21 (moderate), ret=+11.6%
  - 2022: S=1.35 (moderate), ret=+9.2%
  - 2023: S=1.37 (moderate), ret=+6.8%

## Risk & Drawdown
- Max drawdown: 8.88% over 408 days (recovered)
- Annualized: return +5.7%, volatility 7.4% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.41, excess kurtosis +2.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.00, max 2.32, latest 1.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +7.77%; worst month: -3.75%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.19
- Sideways: S=0.19
- Bear: S=-1.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_grossincome, 5))` S=0.21, F=0.05, INFERIOR
Direction gap: -0.57 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * est_grossincome)`: S=0.03, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * est_grossincome / close)`: S=-0.09, F=-0.03, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_grossincome, 5))`: S=0.21, F=0.05, T=35.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_grossincome / close)` | TOP3000 | 0.78 | 0.53 | 8.9% | 80% | bull-only |
| `rank(est_grossincome)` | TOP3000 | 0.53 | 0.38 | 36.9% | 80% | bull-only |
| `rank(ts_delta(est_grossincome, 5))` | TOP1000 | 0.66 | 0.21 | 8.5% | 60% | mixed |
| `rank(ts_delta(est_grossincome, 5))` | TOP500 | 0.54 | 0.17 | 10.5% | 60% | mixed |
| `rank(est_grossincome / close)` | TOP500 | 0.30 | 0.16 | 27.7% | 80% | bull-only |
| `rank(est_grossincome / close)` | TOP1000 | 0.29 | 0.14 | 16.5% | 60% | bull-only |
| `rank(est_grossincome)` | TOP1000 | 0.23 | 0.12 | 39.8% | 60% | bull-only |
| `rank(ts_delta(est_grossincome, 5))` | TOP3000 | 0.46 | 0.11 | 5.9% | 100% | mixed |
| `rank(est_grossincome)` | TOP500 | 0.12 | 0.05 | 54.0% | 60% | bull-only |
| `rank(est_grossincome / close)` | TOP200 | 0.09 | 0.03 | 31.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_gric_high: 0.992 (strongly positively correlated)
- anl4_gric_median: 0.992 (strongly positively correlated)
- anl4_gric_mean: 0.991 (strongly positively correlated)
- anl4_gric_low: 0.985 (strongly positively correlated)
- sales_estimate_minimum: 0.969 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
