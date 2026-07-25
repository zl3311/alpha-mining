---
field: min_reported_eps_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.65
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1493
ann_vol: 0.0632
hit_rate: 0.5061
rolling_sharpe_min: -3.488
rolling_sharpe_max: 2.678
redundancy_cluster: 13
negated_best_sharpe: 0.33
negated_best_template: neg_rank_level
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.32
---
# min_reported_eps_guidance (analyst4)

*Reported Earnings Per Share - Minimum guidance value for the annual period*

## Signal Profile
- `rank(min_reported_eps_guidance)`: S=0.65, F=0.37, T=0.8%, INFERIOR (TOP3000)
- `rank(min_reported_eps_guidance / close)`: S=0.28, F=0.15, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_reported_eps_guidance, 5))`: S=0.34, F=0.10, T=33.3%, INFERIOR (TOP200)
- `-rank(min_reported_eps_guidance)`: S=-0.06, F=-0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_reported_eps_guidance, 5))`: S=-0.33, F=-0.10, T=33.3%, INFERIOR (TOP3000)
- `-ts_zscore(min_reported_eps_guidance, 63)`: S=0.16, F=0.03, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(min_reported_eps_guidance, 10)`: S=0.12, F=0.03, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(min_reported_eps_guidance, 22))`: S=0.13, F=0.02, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * min_reported_eps_guidance)`: S=0.33, F=0.18, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * min_reported_eps_guidance / close)`: S=0.29, F=0.15, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.64, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.03 (moderate), ret=+2.6%
  - 2020: S=-2.55 (negative), ret=-8.6%
  - 2021: S=1.79 (strong), ret=+14.2%
  - 2022: S=1.26 (moderate), ret=+11.9%
  - 2023: S=-0.08 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 14.93% over 750 days (recovered)
- Annualized: return +4.0%, volatility 6.3% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.11, excess kurtosis +2.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.49, max 2.68, latest -0.22

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.78%; worst month: -2.31%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.54
- Sideways: S=0.86
- Bear: S=-2.39

## Negated Direction
Best negated: `rank(-1 * min_reported_eps_guidance)` S=0.33, F=0.18, INFERIOR
Direction gap: -0.32 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * min_reported_eps_guidance)`: S=0.33, F=0.18, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * min_reported_eps_guidance / close)`: S=0.29, F=0.15, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_reported_eps_guidance, 5))`: S=-0.33, F=-0.10, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_reported_eps_guidance)` | TOP3000 | 0.64 | 0.37 | 14.9% | 60% | bull-only |
| `rank(min_reported_eps_guidance / close)` | TOP3000 | 0.28 | 0.15 | 41.7% | 60% | bull-only |
| `rank(ts_delta(min_reported_eps_guidance, 5))` | TOP200 | 0.35 | 0.10 | 19.4% | 60% | mixed |
| `rank(ts_delta(min_reported_eps_guidance, 5))` | TOP3000 | 0.33 | 0.06 | 12.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- max_reported_eps_guidance_2: 1.000 (strongly positively correlated)
- earnings_per_share_max_guidance: 0.949 (strongly positively correlated)
- earnings_per_share_min_guidance: 0.947 (strongly positively correlated)
- eps_reported_min_guidance_qtr: 0.900 (strongly positively correlated)
- eps_min_guidance_quarterly: 0.899 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
