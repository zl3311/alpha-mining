---
field: split
dataset: pv1
cluster: pv1_ratio
coverage: 1.0
community_alphas: 18459
best_template: ts_mean
best_sharpe: 0.94
best_fitness: 1.24
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.5399
ann_vol: 0.1533
hit_rate: 0.4866
rolling_sharpe_min: -1.951
rolling_sharpe_max: 2.494
negated_best_sharpe: 1.02
negated_best_template: rank_neg_delta
negated_best_fitness: 0.94
n_negated_sims: 4
direction_gap: 0.08
---
# split (pv1)

*Stock split ratio*

## Signal Profile
- `rank(split)`: S=0.18, F=0.08, T=18.4%, INFERIOR (TOP3000)
- `rank(split / close)`: S=0.06, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(split, 5))`: S=0.26, F=0.14, T=13.2%, INFERIOR (TOP500)
- `-rank(split)`: S=0.06, F=0.02, T=12.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(split, 5))`: S=1.02, F=0.94, T=26.1%, INFERIOR (TOP3000)
- `-ts_zscore(split, 63)`: S=0.87, F=0.59, T=2.4%, INFERIOR (TOP3000)
- `ts_mean(split, 10)`: S=0.94, F=1.24, T=10.2%, AVERAGE (TOP3000)
- `rank(ts_rank(split, 22))`: S=-1.16, F=-1.39, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * split)`: S=0.44, F=0.29, T=18.5%, INFERIOR (TOP3000)
- `rank(-1 * split / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/2P
- LOW_FITNESS: 20F/1P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.26, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.40 (strong), ret=+23.8%
  - 2020: S=-1.11 (negative), ret=-24.7%
  - 2021: S=0.80 (moderate), ret=+13.2%
  - 2022: S=0.42 (weak), ret=+5.8%
  - 2023: S=0.19 (weak), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 53.99% over 1352 days (not yet recovered, ongoing at window end)
- Annualized: return +4.0%, volatility 15.3% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew -1.73, excess kurtosis +28.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.95, max 2.49, latest 0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +11.74%; worst month: -24.14%
Positive months: 53%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=0.87
- Sideways: S=1.43
- Bear: S=-1.40

## Negated Direction
Best negated: `rank(-1 * ts_delta(split, 5))` S=1.02, F=0.94, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * split)`: S=0.44, F=0.29, T=18.5%, INFERIOR (TOP3000)
- `rank(-1 * split / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(split, 5))`: S=1.02, F=0.94, T=26.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(split, 5))` | TOP500 | 0.26 | 0.14 | 54.0% | 80% | bull-only |
| `rank(split)` | TOP3000 | 0.17 | 0.08 | 56.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_free_cashflow_per_share_guidance: 0.597 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.597 (moderately positively correlated)
- min_total_assets_guidance: 0.597 (moderately positively correlated)
- max_free_cashflow_per_share_guidance: 0.597 (moderately positively correlated)
- shareholders_equity_max_guidance: 0.597 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
