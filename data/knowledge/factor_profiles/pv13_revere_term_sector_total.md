---
field: pv13_revere_term_sector_total
dataset: pv13
best_template: rank_neg_delta
best_sharpe: 0.59
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.3599
ann_vol: 0.1004
hit_rate: 0.5061
rolling_sharpe_min: -3.995
rolling_sharpe_max: 2.113
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: 0.36
---
# pv13_revere_term_sector_total (pv13)

*Number of terminal sectors for the company*

## Signal Profile
- `rank(pv13_revere_term_sector_total)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP500)
- `rank(ts_delta(pv13_revere_term_sector_total, 5))`: S=0.05, F=0.01, T=12.2%, INFERIOR (TOP500)
- `-rank(pv13_revere_term_sector_total)`: S=-0.08, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_term_sector_total, 5))`: S=0.59, F=0.41, T=12.6%, INFERIOR (TOP3000)
- `-ts_zscore(pv13_revere_term_sector_total, 63)`: S=-0.17, F=-0.07, T=8.9%, INFERIOR (TOP3000)
- `ts_mean(pv13_revere_term_sector_total, 10)`: S=-0.17, F=-0.06, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_revere_term_sector_total, 22))`: S=0.23, F=0.10, T=7.6%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_term_sector_total)`: S=0.12, F=0.03, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_term_sector_total / close)`: S=-0.37, F=-0.17, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/13P
- LOW_FITNESS: 24F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/15P
- LOW_TURNOVER: 4F/20P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.07, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.68 (moderate), ret=+3.7%
  - 2020: S=-3.03 (negative), ret=-22.1%
  - 2021: S=0.66 (moderate), ret=+9.6%
  - 2022: S=1.25 (moderate), ret=+15.0%
  - 2023: S=-0.39 (negative), ret=-2.8%

## Risk & Drawdown
- Max drawdown: 35.99% over 916 days (recovered)
- Annualized: return +0.7%, volatility 10.0% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew -0.08, excess kurtosis +1.99

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.00, max 2.11, latest -0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.01%; worst month: -5.22%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.31
- Sideways: S=0.45
- Bear: S=-3.35

## Negated Direction
Best negated: `rank(-1 * ts_delta(pv13_revere_term_sector_total, 5))` S=0.59, F=0.41, INFERIOR
Direction gap: +0.36 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * pv13_revere_term_sector_total)`: S=0.12, F=0.03, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_term_sector_total / close)`: S=-0.37, F=-0.17, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_term_sector_total, 5))`: S=0.59, F=0.41, T=12.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pv13_revere_term_sector_total)` | TOP500 | 0.07 | 0.02 | 36.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cashflow_dividends: 0.855 (strongly positively correlated)
- fnd6_newa1v1300_dv: 0.855 (strongly positively correlated)
- cash_flow_from_financing: -0.834 (strongly negatively correlated)
- cashflow_fin: -0.827 (strongly negatively correlated)
- fnd6_newa1v1300_fincf: -0.826 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
