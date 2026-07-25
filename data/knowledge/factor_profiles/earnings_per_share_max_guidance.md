---
field: earnings_per_share_max_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.71
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.146
ann_vol: 0.0705
hit_rate: 0.5117
rolling_sharpe_min: -2.593
rolling_sharpe_max: 2.739
redundancy_cluster: 13
negated_best_sharpe: 0.19
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.52
---
# earnings_per_share_max_guidance (analyst4)

*The maximum guidance value for Earnings Per Share on an annual basis.*

## Signal Profile
- `rank(earnings_per_share_max_guidance)`: S=0.71, F=0.45, T=0.8%, INFERIOR (TOP3000)
- `rank(earnings_per_share_max_guidance / close)`: S=0.46, F=0.29, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(earnings_per_share_max_guidance, 5))`: S=0.48, F=0.18, T=32.4%, INFERIOR (TOP200)
- `-rank(earnings_per_share_max_guidance)`: S=-0.19, F=-0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_max_guidance, 5))`: S=-0.48, F=-0.18, T=32.4%, INFERIOR (TOP3000)
- `ts_zscore(earnings_per_share_max_guidance, 22)`: S=0.67, F=0.32, T=40.5%, INFERIOR (TOP3000)
- `ts_mean(earnings_per_share_max_guidance, 10)`: S=0.17, F=0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_per_share_max_guidance, 22))`: S=0.46, F=0.18, T=12.3%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_max_guidance)`: S=0.13, F=0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_max_guidance / close)`: S=0.19, F=0.09, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.69, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.91 (moderate), ret=+2.5%
  - 2020: S=-1.81 (negative), ret=-6.9%
  - 2021: S=1.88 (strong), ret=+17.4%
  - 2022: S=1.51 (strong), ret=+15.4%
  - 2023: S=-0.80 (negative), ret=-4.3%

## Risk & Drawdown
- Max drawdown: 14.60% over 634 days (recovered)
- Annualized: return +4.9%, volatility 7.0% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.07, excess kurtosis +2.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.59, max 2.74, latest -0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.06%; worst month: -2.82%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.68
- Sideways: S=0.82
- Bear: S=-2.27

## Negated Direction
Best negated: `rank(-1 * earnings_per_share_max_guidance / close)` S=0.19, F=0.09, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * earnings_per_share_max_guidance)`: S=0.13, F=0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_max_guidance / close)`: S=0.19, F=0.09, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_max_guidance, 5))`: S=-0.48, F=-0.18, T=32.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(earnings_per_share_max_guidance)` | TOP3000 | 0.69 | 0.45 | 14.6% | 60% | bull-only |
| `rank(earnings_per_share_max_guidance / close)` | TOP3000 | 0.45 | 0.29 | 34.0% | 60% | bull-only |
| `rank(ts_delta(earnings_per_share_max_guidance, 5))` | TOP200 | 0.51 | 0.18 | 11.4% | 100% | weak |
| `rank(ts_delta(earnings_per_share_max_guidance, 5))` | TOP3000 | 0.33 | 0.07 | 9.6% | 60% | bear-only |
| `rank(earnings_per_share_max_guidance)` | TOP1000 | 0.18 | 0.07 | 22.1% | 40% | bull-only |
| `rank(ts_delta(earnings_per_share_max_guidance, 5))` | TOP1000 | 0.28 | 0.06 | 9.3% | 40% | bear-only |
| `rank(earnings_per_share_max_guidance / close)` | TOP1000 | 0.11 | 0.04 | 32.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- earnings_per_share_min_guidance: 0.998 (strongly positively correlated)
- eps_min_guidance_quarterly: 0.949 (strongly positively correlated)
- min_reported_eps_guidance: 0.949 (strongly positively correlated)
- max_reported_eps_guidance_2: 0.949 (strongly positively correlated)
- eps_max_guidance_quarterly: 0.948 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
