---
field: eps_adjusted_min_guidance_qtr
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.33
best_fitness: 0.2
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.2807
ann_vol: 0.0937
hit_rate: 0.4923
rolling_sharpe_min: -3.967
rolling_sharpe_max: 2.555
negated_best_sharpe: 0.33
negated_best_template: neg_rank_level
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: 0.06
---
# eps_adjusted_min_guidance_qtr (analyst4)

*Minimum guidance value for adjusted Earnings per share excluding extraordinary items and stock option expenses.*

## Signal Profile
- `rank(eps_adjusted_min_guidance_qtr)`: S=0.27, F=0.12, T=0.7%, INFERIOR (TOP3000)
- `rank(eps_adjusted_min_guidance_qtr / close)`: S=0.12, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(eps_adjusted_min_guidance_qtr, 5))`: S=0.32, F=0.09, T=33.4%, INFERIOR (TOP200)
- `-rank(eps_adjusted_min_guidance_qtr)`: S=0.10, F=0.03, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(eps_adjusted_min_guidance_qtr, 5))`: S=-0.32, F=-0.09, T=33.4%, INFERIOR (TOP3000)
- `-ts_zscore(eps_adjusted_min_guidance_qtr, 63)`: S=0.03, F=0.00, T=21.9%, INFERIOR (TOP3000)
- `ts_mean(eps_adjusted_min_guidance_qtr, 10)`: S=-0.11, F=-0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(eps_adjusted_min_guidance_qtr, 22))`: S=-0.18, F=-0.05, T=12.9%, INFERIOR (TOP3000)
- `rank(-1 * eps_adjusted_min_guidance_qtr)`: S=0.33, F=0.20, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * eps_adjusted_min_guidance_qtr / close)`: S=0.23, F=0.11, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.27, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.45 (negative), ret=-1.7%
  - 2020: S=-3.23 (negative), ret=-16.1%
  - 2021: S=1.43 (moderate), ret=+16.4%
  - 2022: S=1.14 (moderate), ret=+15.8%
  - 2023: S=-0.27 (negative), ret=-2.1%

## Risk & Drawdown
- Max drawdown: 28.07% over 814 days (recovered)
- Annualized: return +2.5%, volatility 9.4% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew -0.04, excess kurtosis +2.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.97, max 2.56, latest -0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +6.83%; worst month: -3.94%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.39
- Sideways: S=0.42
- Bear: S=-2.95

## Negated Direction
Best negated: `rank(-1 * eps_adjusted_min_guidance_qtr)` S=0.33, F=0.20, INFERIOR
Direction gap: +0.06 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * eps_adjusted_min_guidance_qtr)`: S=0.33, F=0.20, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * eps_adjusted_min_guidance_qtr / close)`: S=0.23, F=0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(eps_adjusted_min_guidance_qtr, 5))`: S=-0.32, F=-0.09, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(eps_adjusted_min_guidance_qtr)` | TOP3000 | 0.27 | 0.12 | 28.1% | 40% | bull-only |
| `rank(ts_delta(eps_adjusted_min_guidance_qtr, 5))` | TOP200 | 0.34 | 0.09 | 15.0% | 80% | mixed |
| `rank(eps_adjusted_min_guidance_qtr / close)` | TOP3000 | 0.11 | 0.04 | 51.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_adjusted_eps_guidance: 1.000 (strongly positively correlated)
- earnings_per_share_max_guidance: 0.881 (strongly positively correlated)
- earnings_per_share_min_guidance: 0.879 (strongly positively correlated)
- fnd6_cptnewqv1300_oiadpq: 0.879 (strongly positively correlated)
- operating_income: 0.879 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
