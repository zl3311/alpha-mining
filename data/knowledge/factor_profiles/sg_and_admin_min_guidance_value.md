---
field: sg_and_admin_min_guidance_value
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.53
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.247
ann_vol: 0.0784
hit_rate: 0.519
rolling_sharpe_min: -2.372
rolling_sharpe_max: 3.204
redundancy_cluster: 88
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.44
n_negated_sims: 10
direction_gap: -0.08
---
# sg_and_admin_min_guidance_value (analyst4)

*Minimum guidance value for Selling, General & Administrative Expense on an annual basis.*

## Signal Profile
- `rank(sg_and_admin_min_guidance_value)`: S=0.61, F=0.38, T=1.2%, INFERIOR (TOP3000)
- `rank(sg_and_admin_min_guidance_value / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(sg_and_admin_min_guidance_value, 5))`: S=0.19, F=0.07, T=19.3%, INFERIOR (TOP1000)
- `-rank(sg_and_admin_min_guidance_value)`: S=-0.26, F=-0.11, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sg_and_admin_min_guidance_value, 5))`: S=0.53, F=0.44, T=12.5%, INFERIOR (TOP3000)
- `-ts_zscore(sg_and_admin_min_guidance_value, 63)`: S=0.16, F=0.09, T=6.1%, INFERIOR (TOP3000)
- `ts_mean(sg_and_admin_min_guidance_value, 10)`: S=0.23, F=0.10, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(sg_and_admin_min_guidance_value, 22))`: S=-0.96, F=-1.11, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * sg_and_admin_min_guidance_value)`: S=-0.06, F=-0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * sg_and_admin_min_guidance_value / close)`: S=0.30, F=0.15, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/16P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.25 (weak), ret=+1.5%
  - 2020: S=-1.45 (negative), ret=-11.0%
  - 2021: S=1.43 (moderate), ret=+13.0%
  - 2022: S=1.71 (strong), ret=+14.8%
  - 2023: S=0.83 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 24.70% over 820 days (recovered)
- Annualized: return +4.9%, volatility 7.8% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew -0.20, excess kurtosis +1.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.37, max 3.20, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.09%; worst month: -5.57%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.47
- Sideways: S=0.21
- Bear: S=-1.06

## Negated Direction
Best negated: `rank(-1 * ts_delta(sg_and_admin_min_guidance_value, 5))` S=0.53, F=0.44, INFERIOR
Direction gap: -0.08 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sg_and_admin_min_guidance_value)`: S=-0.06, F=-0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * sg_and_admin_min_guidance_value / close)`: S=0.30, F=0.15, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sg_and_admin_min_guidance_value, 5))`: S=0.53, F=0.44, T=12.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sg_and_admin_min_guidance_value)` | TOP3000 | 0.62 | 0.38 | 24.7% | 80% | bull-only |
| `rank(sg_and_admin_min_guidance_value)` | TOP1000 | 0.25 | 0.11 | 35.3% | 80% | bull-only |
| `rank(ts_delta(sg_and_admin_min_guidance_value, 5))` | TOP1000 | 0.18 | 0.07 | 27.1% | 60% | bull-only |
| `rank(sg_and_admin_min_guidance_value / close)` | TOP3000 | 0.11 | 0.04 | 51.6% | 60% | bull-only |
| `rank(sg_and_admin_min_guidance_value)` | TOP500 | 0.09 | 0.03 | 48.5% | 80% | bull-only |
| `rank(ts_delta(sg_and_admin_min_guidance_value, 5))` | TOP500 | 0.09 | 0.03 | 34.3% | 60% | bull-only |
| `rank(ts_delta(sg_and_admin_min_guidance_value, 5))` | TOP3000 | 0.08 | 0.02 | 32.6% | 40% | bull-only |
| `rank(sg_and_admin_min_guidance_value)` | TOP200 | 0.06 | 0.02 | 59.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_selling_general_admin_guidance: 1.000 (strongly positively correlated)
- est_eps: 0.613 (moderately positively correlated)
- anl4_qfv4_eps_high: 0.613 (moderately positively correlated)
- return_assets: 0.604 (moderately positively correlated)
- income: 0.600 (moderately positively correlated)

Redundancy cluster #88: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
