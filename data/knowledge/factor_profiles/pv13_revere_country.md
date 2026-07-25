---
field: pv13_revere_country
dataset: pv13
best_template: rank_neg_delta
best_sharpe: 0.6
best_fitness: 0.61
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.2372
ann_vol: 0.1263
hit_rate: 0.4494
rolling_sharpe_min: -1.779
rolling_sharpe_max: 3.182
negated_best_sharpe: 0.6
negated_best_template: rank_neg_delta
negated_best_fitness: 0.61
n_negated_sims: 10
direction_gap: 0.11
---
# pv13_revere_country (pv13)

*Country code*

## Signal Profile
- `rank(pv13_revere_country)`: S=-0.17, F=-0.07, T=1.9%, INFERIOR (TOP500)
- `rank(ts_delta(pv13_revere_country, 5))`: S=0.49, F=0.35, T=5.7%, INFERIOR (TOP500)
- `-rank(pv13_revere_country)`: S=0.29, F=0.14, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_country, 5))`: S=0.60, F=0.61, T=12.0%, INFERIOR (TOP3000)
- `ts_zscore(pv13_revere_country, 22)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(pv13_revere_country, 10)`: S=-0.69, F=-0.51, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_revere_country, 22))`: S=-0.60, F=-0.68, T=7.7%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_country)`: S=0.57, F=0.36, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_country / close)`: S=0.25, F=0.11, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/13P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/10P
- LOW_TURNOVER: 5F/19P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.49, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+7.1%
  - 2020: S=-0.46 (negative), ret=-4.7%
  - 2021: S=0.72 (moderate), ret=+14.2%
  - 2022: S=1.07 (moderate), ret=+12.2%
  - 2023: S=0.34 (weak), ret=+2.0%

## Risk & Drawdown
- Max drawdown: 23.72% over 215 days (recovered)
- Annualized: return +6.3%, volatility 12.6% (fraction of booksize)
- Hit rate: 44.9% positive days
- Tail shape: skew +0.03, excess kurtosis +14.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.78, max 3.18, latest 0.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +16.31%; worst month: -10.66%
Positive months: 57%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.19
- Sideways: S=0.69
- Bear: S=-2.06

## Negated Direction
Best negated: `rank(-1 * ts_delta(pv13_revere_country, 5))` S=0.60, F=0.61, INFERIOR
Direction gap: +0.11 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * pv13_revere_country)`: S=0.57, F=0.36, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_country / close)`: S=0.25, F=0.11, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_country, 5))`: S=0.60, F=0.61, T=12.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pv13_revere_country, 5))` | TOP500 | 0.49 | 0.35 | 23.7% | 80% | bull-only |
| `rank(ts_delta(pv13_revere_country, 5))` | TOP200 | 0.25 | 0.15 | 28.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_free_cashflow_per_share_guidance: 0.776 (strongly positively correlated)
- shareholders_equity_min_guidance: 0.776 (strongly positively correlated)
- min_total_assets_guidance: 0.776 (strongly positively correlated)
- max_free_cashflow_per_share_guidance: 0.776 (strongly positively correlated)
- shareholders_equity_max_guidance: 0.776 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
