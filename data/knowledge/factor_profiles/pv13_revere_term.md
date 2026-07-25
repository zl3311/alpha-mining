---
field: pv13_revere_term
dataset: pv13
best_template: rank_level
best_sharpe: 0.5
best_fitness: 0.42
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 25
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.3835
ann_vol: 0.17
hit_rate: 0.4502
rolling_sharpe_min: -2.309
rolling_sharpe_max: 2.057
negated_best_sharpe: -0.43
negated_best_template: neg_rank
negated_best_fitness: -0.32
n_negated_sims: 10
direction_gap: -0.93
---
# pv13_revere_term (pv13)

*Indicates when a sector is the terminal sector (i.e., no sub-sectors)*

## Signal Profile
- `rank(pv13_revere_term)`: S=0.50, F=0.42, T=3.1%, INFERIOR (TOP500)
- `rank(pv13_revere_term / close)`: S=-0.25, F=-0.14, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_delta(pv13_revere_term, 5))`: S=0.50, F=0.42, T=3.1%, INFERIOR (TOP500)
- `-rank(pv13_revere_term)`: S=-0.43, F=-0.32, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_term, 5))`: S=-0.38, F=-0.34, T=3.3%, INFERIOR (TOP3000)
- `-ts_zscore(pv13_revere_term, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(pv13_revere_term, 10)`: S=-0.04, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_revere_term, 22))`: S=0.43, F=0.32, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_term)`: S=-0.38, F=-0.34, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_term / close)`: S=-0.64, F=-0.62, T=3.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 24F/1P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 25F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/8P
- LOW_TURNOVER: 2F/23P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.47, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.57 (strong), ret=+13.4%
  - 2020: S=-1.01 (negative), ret=-13.0%
  - 2021: S=1.08 (moderate), ret=+27.3%
  - 2022: S=1.00 (moderate), ret=+18.8%
  - 2023: S=-0.54 (negative), ret=-7.0%

## Risk & Drawdown
- Max drawdown: 38.35% over 757 days (recovered)
- Annualized: return +8.0%, volatility 17.0% (fraction of booksize)
- Hit rate: 45.0% positive days
- Tail shape: skew -0.15, excess kurtosis +2.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.31, max 2.06, latest -0.59

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +15.89%; worst month: -12.03%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.50
- Sideways: S=1.00
- Bear: S=-1.16

## Negated Direction
Best negated: `-rank(pv13_revere_term)` S=-0.43, F=-0.32, INFERIOR
Direction gap: -0.93 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pv13_revere_term)`: S=-0.38, F=-0.34, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_term / close)`: S=-0.64, F=-0.62, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_term, 5))`: S=-0.38, F=-0.34, T=3.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pv13_revere_term)` | TOP500 | 0.47 | 0.42 | 38.4% | 60% | bull-only |
| `rank(ts_delta(pv13_revere_term, 5))` | TOP500 | 0.47 | 0.42 | 38.4% | 60% | bull-only |
| `rank(ts_delta(pv13_revere_term, 5))` | TOP3000 | 0.43 | 0.33 | 31.4% | 40% | bull-only |
| `rank(ts_delta(pv13_revere_term, 5))` | TOP1000 | 0.39 | 0.32 | 38.1% | 40% | bull-only |
| `rank(pv13_revere_term)` | TOP3000 | 0.43 | 0.32 | 31.7% | 40% | bull-only |
| `rank(pv13_revere_term)` | TOP1000 | 0.40 | 0.32 | 38.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- min_free_cashflow_per_share_guidance: 0.728 (strongly positively correlated)
- shareholders_equity_min_guidance: 0.728 (strongly positively correlated)
- min_total_assets_guidance: 0.728 (strongly positively correlated)
- max_free_cashflow_per_share_guidance: 0.728 (strongly positively correlated)
- shareholders_equity_max_guidance: 0.728 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
