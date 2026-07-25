---
field: earnings_per_share_guidance_value
dataset: analyst4
best_template: rank_ts_rank
best_sharpe: 0.78
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.076
ann_vol: 0.0648
hit_rate: 0.4988
rolling_sharpe_min: -0.4
rolling_sharpe_max: 2.09
negated_best_sharpe: 0.03
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.75
---
# earnings_per_share_guidance_value (analyst4)

*Earnings Per Share - guidance value for annual frequency*

## Signal Profile
- `rank(earnings_per_share_guidance_value)`: S=0.42, F=0.20, T=2.0%, INFERIOR (TOP500)
- `rank(earnings_per_share_guidance_value / close)`: S=0.59, F=0.33, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(earnings_per_share_guidance_value, 5))`: S=0.74, F=0.26, T=35.1%, INFERIOR (TOP500)
- `-rank(earnings_per_share_guidance_value)`: S=-0.23, F=-0.08, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_guidance_value, 5))`: S=-0.34, F=-0.12, T=32.3%, INFERIOR (TOP3000)
- `-ts_zscore(earnings_per_share_guidance_value, 63)`: S=0.55, F=0.25, T=17.7%, INFERIOR (TOP3000)
- `ts_mean(earnings_per_share_guidance_value, 10)`: S=0.10, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_per_share_guidance_value, 22))`: S=0.78, F=0.38, T=12.9%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_guidance_value)`: S=-0.21, F=-0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_guidance_value / close)`: S=0.03, F=0.00, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.57, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.02 (negative), ret=-0.1%
  - 2020: S=0.12 (weak), ret=+1.1%
  - 2021: S=1.23 (moderate), ret=+6.9%
  - 2022: S=1.36 (moderate), ret=+10.1%
  - 2023: S=0.10 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 7.60% over 335 days (recovered)
- Annualized: return +3.7%, volatility 6.5% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.64, excess kurtosis +3.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.40, max 2.09, latest 0.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +5.21%; worst month: -2.59%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.61
- Sideways: S=0.05
- Bear: S=-1.01

## Negated Direction
Best negated: `rank(-1 * earnings_per_share_guidance_value / close)` S=0.03, F=0.00, INFERIOR
Direction gap: -0.75 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * earnings_per_share_guidance_value)`: S=-0.21, F=-0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_guidance_value / close)`: S=0.03, F=0.00, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_guidance_value, 5))`: S=-0.34, F=-0.12, T=32.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(earnings_per_share_guidance_value / close)` | TOP3000 | 0.57 | 0.33 | 7.6% | 80% | bull-only |
| `rank(ts_delta(earnings_per_share_guidance_value, 5))` | TOP500 | 0.75 | 0.26 | 10.1% | 60% | bull-only |
| `rank(ts_delta(earnings_per_share_guidance_value, 5))` | TOP1000 | 0.79 | 0.26 | 11.4% | 80% | mixed |
| `rank(earnings_per_share_guidance_value)` | TOP500 | 0.41 | 0.20 | 18.4% | 80% | bull-only |
| `rank(ts_delta(earnings_per_share_guidance_value, 5))` | TOP200 | 0.33 | 0.11 | 30.3% | 80% | mixed |
| `rank(earnings_per_share_guidance_value / close)` | TOP1000 | 0.21 | 0.09 | 12.2% | 60% | bull-only |
| `rank(earnings_per_share_guidance_value / close)` | TOP500 | 0.20 | 0.09 | 11.8% | 60% | bull-only |
| `rank(earnings_per_share_guidance_value)` | TOP1000 | 0.23 | 0.08 | 19.5% | 80% | bull-only |
| `rank(earnings_per_share_guidance_value)` | TOP200 | 0.20 | 0.08 | 16.5% | 80% | bull-only |
| `rank(earnings_per_share_guidance_value)` | TOP3000 | 0.20 | 0.06 | 18.2% | 80% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qf_az_hgih_spe: 0.750 (strongly positively correlated)
- anl4_qfd1_az_hgih_spe: 0.750 (strongly positively correlated)
- anl4_qfd1_azeps: 0.746 (strongly positively correlated)
- anl4_qf_az_eps: 0.746 (strongly positively correlated)
- earnings_per_share_average: 0.745 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
