---
field: fscore_bfl_growth
dataset: model16
best_template: rank_delta
best_sharpe: 0.2
best_fitness: 0.05
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1369
ann_vol: 0.0458
hit_rate: 0.4704
rolling_sharpe_min: -2.116
rolling_sharpe_max: 2.315
negated_best_sharpe: 0.14
negated_best_template: neg_rank
negated_best_fitness: 0.03
n_negated_sims: 4
direction_gap: -0.06
---
# fscore_bfl_growth (model16)

*Growth composite estimating expected medium-term growth potential (e.g., revenues, earnings); higher is better (0–100)*

## Signal Profile
- `rank(fscore_bfl_growth)`: S=0.04, F=0.01, T=3.4%, INFERIOR (TOP500)
- `rank(ts_delta(fscore_bfl_growth, 5))`: S=0.20, F=0.05, T=15.5%, INFERIOR (TOP500)
- `-rank(fscore_bfl_growth)`: S=0.14, F=0.03, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_growth, 5))`: S=-0.27, F=-0.08, T=15.2%, INFERIOR (TOP3000)
- `ts_zscore(fscore_bfl_growth, 22)`: S=-0.04, F=0.00, T=14.8%, INFERIOR (TOP3000)
- `ts_mean(fscore_bfl_growth, 10)`: S=-0.12, F=-0.03, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fscore_bfl_growth, 22))`: S=-0.34, F=-0.10, T=8.6%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_growth)`: S=0.13, F=0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_growth / close)`: S=-0.52, F=-0.29, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/11P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.20, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=2.20 (strong), ret=+7.5%
  - 2020: S=-1.40 (negative), ret=-6.3%
  - 2021: S=-0.64 (negative), ret=-3.7%
  - 2022: S=-0.19 (negative), ret=-0.9%
  - 2023: S=2.06 (strong), ret=+7.9%

## Risk & Drawdown
- Max drawdown: 13.69% over 1513 days (not yet recovered, ongoing at window end)
- Annualized: return +0.9%, volatility 4.6% (fraction of booksize)
- Hit rate: 47.0% positive days
- Tail shape: skew -0.09, excess kurtosis +2.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.12, max 2.31, latest 2.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +3.19%; worst month: -2.61%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.11
- Sideways: S=1.23
- Bear: S=-0.55

## Negated Direction
Best negated: `-rank(fscore_bfl_growth)` S=0.14, F=0.03, INFERIOR
Direction gap: -0.06 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fscore_bfl_growth)`: S=0.13, F=0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fscore_bfl_growth / close)`: S=-0.52, F=-0.29, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fscore_bfl_growth, 5))`: S=-0.27, F=-0.08, T=15.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fscore_bfl_growth, 5))` | TOP500 | 0.20 | 0.05 | 13.7% | 40% | mixed |

## Correlation Notes
Top correlates:
- fscore_bfl_surface: 0.769 (strongly positively correlated)
- fscore_bfl_total: 0.740 (strongly positively correlated)
- fscore_bfl_surface_accel: 0.711 (strongly positively correlated)
- min_free_cashflow_per_share_guidance: 0.292 (weakly positively correlated)
- shareholders_equity_min_guidance: 0.292 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
