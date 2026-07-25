---
field: max_reported_eps_guidance_2
dataset: analyst4
best_template: rank_level
best_sharpe: 0.64
best_fitness: 0.36
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1509
ann_vol: 0.0634
hit_rate: 0.5093
rolling_sharpe_min: -3.547
rolling_sharpe_max: 2.682
redundancy_cluster: 13
negated_best_sharpe: 0.33
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.31
---
# max_reported_eps_guidance_2 (analyst4)

*Reported Earnings Per Share - Maximum guidance value for the annual period*

## Signal Profile
- `rank(max_reported_eps_guidance_2)`: S=0.64, F=0.36, T=0.8%, INFERIOR (TOP3000)
- `rank(max_reported_eps_guidance_2 / close)`: S=0.26, F=0.13, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(max_reported_eps_guidance_2, 5))`: S=0.51, F=0.20, T=33.3%, INFERIOR (TOP200)
- `-rank(max_reported_eps_guidance_2)`: S=-0.03, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_reported_eps_guidance_2, 5))`: S=-0.51, F=-0.20, T=33.3%, INFERIOR (TOP3000)
- `-ts_zscore(max_reported_eps_guidance_2, 63)`: S=0.57, F=0.24, T=20.6%, INFERIOR (TOP3000)
- `ts_mean(max_reported_eps_guidance_2, 10)`: S=0.02, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(max_reported_eps_guidance_2, 22))`: S=-0.06, F=-0.01, T=12.5%, INFERIOR (TOP3000)
- `rank(-1 * max_reported_eps_guidance_2)`: S=0.33, F=0.18, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * max_reported_eps_guidance_2 / close)`: S=0.33, F=0.19, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.62, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.99 (moderate), ret=+2.5%
  - 2020: S=-2.60 (negative), ret=-8.8%
  - 2021: S=1.79 (strong), ret=+14.2%
  - 2022: S=1.24 (moderate), ret=+11.7%
  - 2023: S=-0.06 (negative), ret=-0.3%

## Risk & Drawdown
- Max drawdown: 15.09% over 751 days (recovered)
- Annualized: return +4.0%, volatility 6.3% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.10, excess kurtosis +2.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.55, max 2.68, latest -0.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.76%; worst month: -2.29%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.53
- Sideways: S=0.84
- Bear: S=-2.41

## Negated Direction
Best negated: `rank(-1 * max_reported_eps_guidance_2 / close)` S=0.33, F=0.19, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_reported_eps_guidance_2)`: S=0.33, F=0.18, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * max_reported_eps_guidance_2 / close)`: S=0.33, F=0.19, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_reported_eps_guidance_2, 5))`: S=-0.51, F=-0.20, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_reported_eps_guidance_2)` | TOP3000 | 0.62 | 0.36 | 15.1% | 60% | bull-only |
| `rank(ts_delta(max_reported_eps_guidance_2, 5))` | TOP200 | 0.52 | 0.20 | 13.0% | 80% | mixed |
| `rank(max_reported_eps_guidance_2 / close)` | TOP3000 | 0.26 | 0.13 | 43.0% | 60% | bull-only |
| `rank(ts_delta(max_reported_eps_guidance_2, 5))` | TOP3000 | 0.32 | 0.06 | 14.3% | 40% | bear-only |
| `rank(ts_delta(max_reported_eps_guidance_2, 5))` | TOP1000 | 0.29 | 0.06 | 9.8% | 60% | bear-only |

## Correlation Notes
Top correlates:
- min_reported_eps_guidance: 1.000 (strongly positively correlated)
- earnings_per_share_max_guidance: 0.949 (strongly positively correlated)
- earnings_per_share_min_guidance: 0.947 (strongly positively correlated)
- eps_reported_min_guidance_qtr: 0.899 (strongly positively correlated)
- eps_min_guidance_quarterly: 0.899 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
