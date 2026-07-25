---
field: put_breakeven_10
dataset: option9
cluster: option9_options_analytics
coverage: 0.9795
community_alphas: 934
best_template: rank_neg_delta
best_sharpe: 1.12
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5368
ann_vol: 0.1353
hit_rate: 0.5377
rolling_sharpe_min: -3.252
rolling_sharpe_max: 2.399
negated_best_sharpe: 1.12
negated_best_template: rank_neg_delta
negated_best_fitness: 0.49
n_negated_sims: 4
direction_gap: 0.57
---
# put_breakeven_10 (option9)

*Open interest-weighted mean breakeven price for put options expiring in 10 days, average price at which put buyers break even*

## Signal Profile
- `rank(put_breakeven_10)`: S=0.08, F=0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(put_breakeven_10 / close)`: S=0.51, F=0.26, T=21.2%, INFERIOR (TOP3000)
- `rank(ts_delta(put_breakeven_10, 5))`: S=-0.87, F=-0.42, T=38.1%, INFERIOR (TOP200)
- `-rank(put_breakeven_10)`: S=0.05, F=0.01, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_10, 5))`: S=1.12, F=0.49, T=40.5%, INFERIOR (TOP3000)
- `-ts_zscore(put_breakeven_10, 63)`: S=0.55, F=0.34, T=16.3%, INFERIOR (TOP3000)
- `ts_mean(put_breakeven_10, 10)`: S=0.26, F=0.13, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(put_breakeven_10, 22))`: S=-0.71, F=-0.35, T=26.5%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_10)`: S=-0.08, F=-0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_10 / close)`: S=-0.87, F=-0.45, T=22.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.08, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.53 (moderate), ret=+4.2%
  - 2020: S=-1.88 (negative), ret=-24.2%
  - 2021: S=0.48 (weak), ret=+7.0%
  - 2022: S=1.24 (moderate), ret=+20.5%
  - 2023: S=-0.17 (negative), ret=-2.1%

## Risk & Drawdown
- Max drawdown: 53.68% over 1507 days (recovered)
- Annualized: return +1.1%, volatility 13.5% (fraction of booksize)
- Hit rate: 53.8% positive days
- Tail shape: skew -0.27, excess kurtosis +0.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.25, max 2.40, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.26%; worst month: -11.16%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.57
- Sideways: S=1.04
- Bear: S=-2.52

## Negated Direction
Best negated: `rank(-1 * ts_delta(put_breakeven_10, 5))` S=1.12, F=0.49, INFERIOR
Direction gap: +0.57 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * put_breakeven_10)`: S=-0.08, F=-0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_10 / close)`: S=-0.87, F=-0.45, T=22.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_10, 5))`: S=1.12, F=0.49, T=40.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(put_breakeven_10)` | TOP3000 | 0.08 | 0.02 | 53.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- put_breakeven_20: 1.000 (strongly positively correlated)
- put_breakeven_30: 1.000 (strongly positively correlated)
- put_breakeven_60: 1.000 (strongly positively correlated)
- put_breakeven_90: 0.999 (strongly positively correlated)
- put_breakeven_120: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
