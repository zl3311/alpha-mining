---
field: min_share_count_guidance
dataset: analyst4
best_template: rank_ts_rank
best_sharpe: 1.25
best_fitness: 1.82
best_universe: TOP3000
grade: GOOD
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.7033
ann_vol: 0.2734
hit_rate: 0.5182
rolling_sharpe_min: -1.507
rolling_sharpe_max: 3.431
redundancy_cluster: 76
negated_best_sharpe: 0.83
negated_best_template: rank_neg_delta
negated_best_fitness: 0.88
n_negated_sims: 10
direction_gap: -0.42
---
# min_share_count_guidance (analyst4)

*Minimum guidance for shares on an annual basis*

## Signal Profile
- `rank(min_share_count_guidance)`: S=0.51, F=0.35, T=2.4%, INFERIOR (TOP3000)
- `rank(min_share_count_guidance / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_share_count_guidance, 5))`: S=0.60, F=0.53, T=21.3%, INFERIOR (TOP3000)
- `-rank(min_share_count_guidance)`: S=-0.04, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_share_count_guidance, 5))`: S=0.83, F=0.88, T=11.2%, INFERIOR (TOP3000)
- `-ts_zscore(min_share_count_guidance, 63)`: S=-0.60, F=-0.52, T=2.1%, INFERIOR (TOP3000)
- `ts_mean(min_share_count_guidance, 10)`: S=-0.31, F=-0.23, T=14.3%, INFERIOR (TOP3000)
- `rank(ts_rank(min_share_count_guidance, 22))`: S=1.25, F=1.82, T=11.5%, GOOD (TOP3000)
- `rank(-1 * min_share_count_guidance)`: S=0.50, F=0.33, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * min_share_count_guidance / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 23F/9P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 11F/17P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.76 (moderate), ret=+23.0%
  - 2020: S=-0.34 (negative), ret=-11.9%
  - 2021: S=0.12 (weak), ret=+3.6%
  - 2022: S=2.62 (strong), ret=+45.6%
  - 2023: S=1.47 (moderate), ret=+22.4%

## Risk & Drawdown
- Max drawdown: 70.33% over 804 days (recovered)
- Annualized: return +16.9%, volatility 27.3% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.14, excess kurtosis +21.84

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.51, max 3.43, latest 1.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +18.32%; worst month: -18.16%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.28
- Sideways: S=0.89
- Bear: S=-0.15

## Negated Direction
Best negated: `rank(-1 * ts_delta(min_share_count_guidance, 5))` S=0.83, F=0.88, INFERIOR
Direction gap: -0.42 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * min_share_count_guidance)`: S=0.50, F=0.33, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * min_share_count_guidance / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_share_count_guidance, 5))`: S=0.83, F=0.88, T=11.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(min_share_count_guidance, 5))` | TOP3000 | 0.62 | 0.53 | 70.3% | 80% | mixed |
| `rank(min_share_count_guidance)` | TOP3000 | 0.48 | 0.35 | 37.6% | 40% | bull-only |
| `rank(min_share_count_guidance)` | TOP500 | 0.47 | 0.33 | 32.4% | 60% | bull-only |
| `rank(min_share_count_guidance)` | TOP200 | 0.15 | 0.07 | 30.7% | 60% | bull-only |
| `rank(min_share_count_guidance / close)` | TOP3000 | 0.07 | 0.02 | 53.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- shares_outstanding_max_guidance: 1.000 (strongly positively correlated)
- min_basic_shares_guidance: 1.000 (strongly positively correlated)
- basic_shares_max_guidance_qtr: 1.000 (strongly positively correlated)
- max_shares_outstanding_guidance: 1.000 (strongly positively correlated)
- min_shares_outstanding_guidance: 1.000 (strongly positively correlated)

Redundancy cluster #76: 8 similar fields, mean |rho| 0.997 (representative: max_shareholders_equity_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
