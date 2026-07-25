---
field: max_selling_general_admin_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.61
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.2478
ann_vol: 0.0786
hit_rate: 0.5174
rolling_sharpe_min: -2.374
rolling_sharpe_max: 3.201
redundancy_cluster: 88
negated_best_sharpe: 0.3
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.31
---
# max_selling_general_admin_guidance (analyst4)

*The maximum guidance value for Selling, General & Administrative Expense*

## Signal Profile
- `rank(max_selling_general_admin_guidance)`: S=0.61, F=0.38, T=1.2%, INFERIOR (TOP3000)
- `rank(max_selling_general_admin_guidance / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_selling_general_admin_guidance, 5))`: S=0.46, F=0.16, T=34.0%, INFERIOR (TOP200)
- `-rank(max_selling_general_admin_guidance)`: S=-0.26, F=-0.11, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_selling_general_admin_guidance, 5))`: S=-0.46, F=-0.16, T=34.0%, INFERIOR (TOP3000)
- `-ts_zscore(max_selling_general_admin_guidance, 63)`: S=0.68, F=0.29, T=21.9%, INFERIOR (TOP3000)
- `ts_mean(max_selling_general_admin_guidance, 10)`: S=0.38, F=0.21, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_rank(max_selling_general_admin_guidance, 22))`: S=-0.22, F=-0.07, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_selling_general_admin_guidance)`: S=-0.06, F=-0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * max_selling_general_admin_guidance / close)`: S=0.30, F=0.15, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.25 (weak), ret=+1.5%
  - 2020: S=-1.46 (negative), ret=-11.1%
  - 2021: S=1.42 (moderate), ret=+12.9%
  - 2022: S=1.73 (strong), ret=+15.0%
  - 2023: S=0.81 (moderate), ret=+5.4%

## Risk & Drawdown
- Max drawdown: 24.78% over 820 days (recovered)
- Annualized: return +4.8%, volatility 7.9% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew -0.20, excess kurtosis +1.30

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.37, max 3.20, latest 0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.06%; worst month: -5.60%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.47
- Sideways: S=0.21
- Bear: S=-1.08

## Negated Direction
Best negated: `rank(-1 * max_selling_general_admin_guidance / close)` S=0.30, F=0.15, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_selling_general_admin_guidance)`: S=-0.06, F=-0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * max_selling_general_admin_guidance / close)`: S=0.30, F=0.15, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_selling_general_admin_guidance, 5))`: S=-0.46, F=-0.16, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_selling_general_admin_guidance)` | TOP3000 | 0.62 | 0.38 | 24.8% | 80% | bull-only |
| `rank(ts_delta(max_selling_general_admin_guidance, 5))` | TOP200 | 0.48 | 0.16 | 14.5% | 60% | bear-only |
| `rank(max_selling_general_admin_guidance)` | TOP1000 | 0.25 | 0.11 | 35.4% | 80% | bull-only |
| `rank(max_selling_general_admin_guidance / close)` | TOP3000 | 0.11 | 0.04 | 51.6% | 60% | bull-only |
| `rank(max_selling_general_admin_guidance)` | TOP500 | 0.09 | 0.03 | 48.8% | 80% | bull-only |
| `rank(max_selling_general_admin_guidance)` | TOP200 | 0.05 | 0.02 | 60.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- sg_and_admin_min_guidance_value: 1.000 (strongly positively correlated)
- anl4_qfv4_eps_high: 0.615 (moderately positively correlated)
- est_eps: 0.615 (moderately positively correlated)
- return_assets: 0.606 (moderately positively correlated)
- income: 0.602 (moderately positively correlated)

Redundancy cluster #88: 2 similar fields, mean |rho| 1.0 (representative: sg_and_admin_min_guidance_value). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
