---
field: earnings_per_share_min_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.71
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1465
ann_vol: 0.0695
hit_rate: 0.5126
rolling_sharpe_min: -2.64
rolling_sharpe_max: 2.706
redundancy_cluster: 13
negated_best_sharpe: 0.21
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.5
---
# earnings_per_share_min_guidance (analyst4)

*Minimum guidance value for Earnings Per Share on an annual basis.*

## Signal Profile
- `rank(earnings_per_share_min_guidance)`: S=0.71, F=0.44, T=0.8%, INFERIOR (TOP3000)
- `rank(earnings_per_share_min_guidance / close)`: S=0.55, F=0.37, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(earnings_per_share_min_guidance, 5))`: S=0.04, F=0.00, T=36.3%, INFERIOR (TOP1000)
- `-rank(earnings_per_share_min_guidance)`: S=-0.20, F=-0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_min_guidance, 5))`: S=0.21, F=0.03, T=35.3%, INFERIOR (TOP3000)
- `ts_zscore(earnings_per_share_min_guidance, 22)`: S=0.02, F=0.00, T=38.4%, INFERIOR (TOP3000)
- `ts_mean(earnings_per_share_min_guidance, 10)`: S=0.20, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_per_share_min_guidance, 22))`: S=0.60, F=0.22, T=12.4%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_min_guidance)`: S=-0.71, F=-0.44, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_min_guidance / close)`: S=-0.55, F=-0.37, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.69, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.88 (moderate), ret=+2.4%
  - 2020: S=-1.90 (negative), ret=-7.2%
  - 2021: S=1.85 (strong), ret=+16.9%
  - 2022: S=1.52 (strong), ret=+15.3%
  - 2023: S=-0.69 (negative), ret=-3.7%

## Risk & Drawdown
- Max drawdown: 14.65% over 637 days (recovered)
- Annualized: return +4.8%, volatility 7.0% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.07, excess kurtosis +2.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.64, max 2.71, latest -0.86

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.78%; worst month: -2.81%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.69
- Sideways: S=0.81
- Bear: S=-2.28

## Negated Direction
Best negated: `rank(-1 * ts_delta(earnings_per_share_min_guidance, 5))` S=0.21, F=0.03, INFERIOR
Direction gap: -0.50 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * earnings_per_share_min_guidance)`: S=-0.71, F=-0.44, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_min_guidance / close)`: S=-0.55, F=-0.37, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_min_guidance, 5))`: S=0.21, F=0.03, T=35.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(earnings_per_share_min_guidance)` | TOP3000 | 0.69 | 0.44 | 14.6% | 60% | bull-only |
| `rank(earnings_per_share_min_guidance / close)` | TOP3000 | 0.55 | 0.37 | 28.6% | 60% | bull-only |
| `rank(earnings_per_share_min_guidance / close)` | TOP1000 | 0.21 | 0.09 | 24.2% | 40% | bull-only |
| `rank(earnings_per_share_min_guidance)` | TOP1000 | 0.19 | 0.07 | 22.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- earnings_per_share_max_guidance: 0.998 (strongly positively correlated)
- eps_min_guidance_quarterly: 0.949 (strongly positively correlated)
- eps_max_guidance_quarterly: 0.947 (strongly positively correlated)
- min_reported_eps_guidance: 0.947 (strongly positively correlated)
- max_reported_eps_guidance_2: 0.947 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
