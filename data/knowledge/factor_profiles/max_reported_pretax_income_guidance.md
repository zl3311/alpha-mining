---
field: max_reported_pretax_income_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.72
best_fitness: 0.64
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1883
ann_vol: 0.1366
hit_rate: 0.5053
rolling_sharpe_min: -1.985
rolling_sharpe_max: 2.162
redundancy_cluster: 73
negated_best_sharpe: 0.54
negated_best_template: neg_rank_level
negated_best_fitness: 0.56
n_negated_sims: 10
direction_gap: -0.18
---
# max_reported_pretax_income_guidance (analyst4)

*Reported Pretax income- maximum guidance value*

## Signal Profile
- `rank(max_reported_pretax_income_guidance)`: S=0.72, F=0.64, T=0.9%, INFERIOR (TOP3000)
- `rank(max_reported_pretax_income_guidance / close)`: S=0.09, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_reported_pretax_income_guidance, 5))`: S=0.59, F=0.23, T=33.7%, INFERIOR (TOP200)
- `-rank(max_reported_pretax_income_guidance)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_reported_pretax_income_guidance, 5))`: S=-0.59, F=-0.23, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(max_reported_pretax_income_guidance, 63)`: S=0.17, F=0.03, T=22.4%, INFERIOR (TOP3000)
- `ts_mean(max_reported_pretax_income_guidance, 10)`: S=0.03, F=0.01, T=4.6%, INFERIOR (TOP3000)
- `rank(ts_rank(max_reported_pretax_income_guidance, 22))`: S=-0.12, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_reported_pretax_income_guidance)`: S=0.54, F=0.56, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * max_reported_pretax_income_guidance / close)`: S=0.23, F=0.10, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/17P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.72, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.19 (negative), ret=-1.4%
  - 2020: S=0.80 (moderate), ret=+14.0%
  - 2021: S=0.72 (moderate), ret=+7.8%
  - 2022: S=1.53 (strong), ret=+24.4%
  - 2023: S=0.28 (weak), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 18.83% over 570 days (recovered)
- Annualized: return +9.8%, volatility 13.7% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +1.33, excess kurtosis +14.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.99, max 2.16, latest 0.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +9.62%; worst month: -8.38%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.42
- Sideways: S=0.74
- Bear: S=0.05

## Negated Direction
Best negated: `rank(-1 * max_reported_pretax_income_guidance)` S=0.54, F=0.56, INFERIOR
Direction gap: -0.18 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_reported_pretax_income_guidance)`: S=0.54, F=0.56, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * max_reported_pretax_income_guidance / close)`: S=0.23, F=0.10, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_reported_pretax_income_guidance, 5))`: S=-0.59, F=-0.23, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_reported_pretax_income_guidance)` | TOP3000 | 0.72 | 0.64 | 18.8% | 80% | mixed |
| `rank(ts_delta(max_reported_pretax_income_guidance, 5))` | TOP200 | 0.60 | 0.23 | 14.5% | 60% | bear-only |
| `rank(max_reported_pretax_income_guidance / close)` | TOP3000 | 0.09 | 0.03 | 52.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pretax_income_reported_min_guidance_qtr: 1.000 (strongly positively correlated)
- min_pretax_profit_guidance: 0.640 (moderately positively correlated)
- pretax_income_max_guidance_qtr: 0.640 (moderately positively correlated)
- eps_min_guidance_quarterly: 0.423 (moderately positively correlated)
- eps_max_guidance_quarterly: 0.423 (moderately positively correlated)

Redundancy cluster #73: 2 similar fields, mean |rho| 1.0 (representative: pretax_income_reported_min_guidance_qtr). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
