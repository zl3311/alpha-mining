---
field: cashflow_per_share_min_guidance_quarterly
dataset: analyst4
best_template: rank_level
best_sharpe: 0.75
best_fitness: 1.08
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.4169
ann_vol: 0.3482
hit_rate: 0.4721
rolling_sharpe_min: -0.461
rolling_sharpe_max: 2.249
redundancy_cluster: 66
negated_best_sharpe: 0.5
negated_best_template: neg_rank_level
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: -0.25
---
# cashflow_per_share_min_guidance_quarterly (analyst4)

*Minimum guidance value for Cash Flow Per Share*

## Signal Profile
- `rank(cashflow_per_share_min_guidance_quarterly)`: S=0.75, F=1.08, T=1.1%, AVERAGE (TOP3000)
- `rank(cashflow_per_share_min_guidance_quarterly / close)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(cashflow_per_share_min_guidance_quarterly, 5))`: S=0.56, F=0.22, T=33.7%, INFERIOR (TOP200)
- `-rank(cashflow_per_share_min_guidance_quarterly)`: S=-0.15, F=-0.06, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_min_guidance_quarterly, 5))`: S=0.22, F=0.04, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(cashflow_per_share_min_guidance_quarterly, 63)`: S=0.57, F=0.21, T=22.3%, INFERIOR (TOP3000)
- `ts_mean(cashflow_per_share_min_guidance_quarterly, 10)`: S=0.60, F=0.34, T=24.9%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow_per_share_min_guidance_quarterly, 22))`: S=-0.21, F=-0.06, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_min_guidance_quarterly)`: S=0.50, F=0.33, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_min_guidance_quarterly / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.76, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.55 (strong), ret=+63.8%
  - 2020: S=1.33 (moderate), ret=+54.6%
  - 2021: S=0.15 (weak), ret=+5.8%
  - 2022: S=0.01 (weak), ret=+0.2%
  - 2023: S=0.27 (weak), ret=+4.4%

## Risk & Drawdown
- Max drawdown: 41.69% over 455 days (recovered)
- Annualized: return +26.3%, volatility 34.8% (fraction of booksize)
- Hit rate: 47.2% positive days
- Tail shape: skew +1.69, excess kurtosis +15.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.46, max 2.25, latest 0.35

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +24.35%; worst month: -16.25%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.50
- Sideways: S=0.95
- Bear: S=0.79

## Negated Direction
Best negated: `rank(-1 * cashflow_per_share_min_guidance_quarterly)` S=0.50, F=0.33, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cashflow_per_share_min_guidance_quarterly)`: S=0.50, F=0.33, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_min_guidance_quarterly / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_min_guidance_quarterly, 5))`: S=0.22, F=0.04, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cashflow_per_share_min_guidance_quarterly)` | TOP3000 | 0.76 | 1.08 | 41.7% | 100% | all-weather |
| `rank(cashflow_per_share_min_guidance_quarterly)` | TOP500 | 0.47 | 0.33 | 32.4% | 60% | bull-only |
| `rank(ts_delta(cashflow_per_share_min_guidance_quarterly, 5))` | TOP200 | 0.57 | 0.22 | 15.4% | 40% | bear-only |
| `rank(cashflow_per_share_min_guidance_quarterly)` | TOP200 | 0.15 | 0.07 | 30.7% | 60% | bull-only |
| `rank(cashflow_per_share_min_guidance_quarterly)` | TOP1000 | 0.14 | 0.06 | 35.0% | 40% | bull-only |
| `rank(cashflow_per_share_min_guidance_quarterly / close)` | TOP3000 | 0.08 | 0.02 | 53.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cashflow_per_share_max_guidance_quarterly: 1.000 (strongly positively correlated)
- net_debt_max_guidance_qtr: 0.525 (moderately positively correlated)
- net_debt_min_guidance_qtr: 0.525 (moderately positively correlated)
- fnd6_idesindq_curcd: -0.246 (weakly negatively correlated)
- fnd6_adesinda_curcd: -0.235 (weakly negatively correlated)

Redundancy cluster #66: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
