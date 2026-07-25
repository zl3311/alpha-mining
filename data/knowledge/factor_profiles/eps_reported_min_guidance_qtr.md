---
field: eps_reported_min_guidance_qtr
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.72
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0626
ann_vol: 0.0495
hit_rate: 0.5045
rolling_sharpe_min: -1.676
rolling_sharpe_max: 2.929
redundancy_cluster: 13
negated_best_sharpe: 0.72
negated_best_template: neg_rank_level
negated_best_fitness: 0.48
n_negated_sims: 10
direction_gap: -0.09
---
# eps_reported_min_guidance_qtr (analyst4)

*Reported Earnings Per Share - Minimum guidance value*

## Signal Profile
- `rank(eps_reported_min_guidance_qtr)`: S=0.81, F=0.46, T=0.7%, INFERIOR (TOP3000)
- `rank(eps_reported_min_guidance_qtr / close)`: S=0.32, F=0.17, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(eps_reported_min_guidance_qtr, 5))`: S=0.18, F=0.04, T=33.1%, INFERIOR (TOP200)
- `-rank(eps_reported_min_guidance_qtr)`: S=-0.30, F=-0.11, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(eps_reported_min_guidance_qtr, 5))`: S=-0.18, F=-0.04, T=33.1%, INFERIOR (TOP3000)
- `-ts_zscore(eps_reported_min_guidance_qtr, 63)`: S=-0.23, F=-0.06, T=18.7%, INFERIOR (TOP3000)
- `ts_mean(eps_reported_min_guidance_qtr, 10)`: S=0.29, F=0.11, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(eps_reported_min_guidance_qtr, 22))`: S=-0.05, F=-0.01, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * eps_reported_min_guidance_qtr)`: S=0.72, F=0.48, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * eps_reported_min_guidance_qtr / close)`: S=0.50, F=0.32, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.80, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.86 (moderate), ret=+2.1%
  - 2020: S=-1.33 (negative), ret=-3.7%
  - 2021: S=2.17 (strong), ret=+13.1%
  - 2022: S=1.62 (strong), ret=+11.8%
  - 2023: S=-0.97 (negative), ret=-3.9%

## Risk & Drawdown
- Max drawdown: 6.26% over 515 days (recovered)
- Annualized: return +3.9%, volatility 5.0% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.21, excess kurtosis +2.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.68, max 2.93, latest -1.11

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +3.73%; worst month: -2.96%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.60
- Sideways: S=0.39
- Bear: S=-1.35

## Negated Direction
Best negated: `rank(-1 * eps_reported_min_guidance_qtr)` S=0.72, F=0.48, INFERIOR
Direction gap: -0.09 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * eps_reported_min_guidance_qtr)`: S=0.72, F=0.48, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * eps_reported_min_guidance_qtr / close)`: S=0.50, F=0.32, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(eps_reported_min_guidance_qtr, 5))`: S=-0.18, F=-0.04, T=33.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(eps_reported_min_guidance_qtr)` | TOP3000 | 0.80 | 0.46 | 6.3% | 60% | bull-only |
| `rank(eps_reported_min_guidance_qtr / close)` | TOP3000 | 0.32 | 0.17 | 37.0% | 60% | bull-only |
| `rank(eps_reported_min_guidance_qtr)` | TOP1000 | 0.29 | 0.11 | 9.5% | 40% | bull-only |
| `rank(ts_delta(eps_reported_min_guidance_qtr, 5))` | TOP200 | 0.19 | 0.04 | 18.9% | 60% | mixed |
| `rank(eps_reported_min_guidance_qtr / close)` | TOP1000 | 0.13 | 0.04 | 28.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_reported_eps_guidance: 1.000 (strongly positively correlated)
- eps_min_guidance_quarterly: 0.925 (strongly positively correlated)
- eps_max_guidance_quarterly: 0.924 (strongly positively correlated)
- min_reported_eps_guidance: 0.900 (strongly positively correlated)
- earnings_per_share_max_guidance: 0.899 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
