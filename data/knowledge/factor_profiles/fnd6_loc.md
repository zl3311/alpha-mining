---
field: fnd6_loc
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.65
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.3989
ann_vol: 0.1394
hit_rate: 0.4623
rolling_sharpe_min: -3.418
rolling_sharpe_max: 1.746
negated_best_sharpe: 0.65
negated_best_template: neg_rank_level
negated_best_fitness: 0.43
n_negated_sims: 10
direction_gap: 0.52
---
# fnd6_loc (fundamental6)

*string for locating the Headquarters of the company*

## Signal Profile
- `rank(fnd6_loc)`: S=-0.14, F=-0.05, T=1.9%, INFERIOR (TOP500)
- `rank(fnd6_loc / close)`: S=-0.01, F=0.00, T=2.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_loc, 5))`: S=0.13, F=0.05, T=6.3%, INFERIOR (TOP500)
- `-rank(fnd6_loc)`: S=0.21, F=0.08, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_loc, 5))`: S=0.40, F=0.31, T=12.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_loc, 63)`: S=-0.02, F=0.00, T=0.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_loc, 10)`: S=0.09, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_loc, 22))`: S=0.00, F=0.00, T=7.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_loc)`: S=0.65, F=0.43, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_loc / close)`: S=0.29, F=0.14, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/17P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.14, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.61 (moderate), ret=+8.1%
  - 2020: S=-2.28 (negative), ret=-22.5%
  - 2021: S=0.99 (moderate), ret=+18.2%
  - 2022: S=0.21 (weak), ret=+3.4%
  - 2023: S=0.30 (weak), ret=+2.3%

## Risk & Drawdown
- Max drawdown: 39.89% over 1513 days (not yet recovered, ongoing at window end)
- Annualized: return +1.9%, volatility 13.9% (fraction of booksize)
- Hit rate: 46.2% positive days
- Tail shape: skew -0.41, excess kurtosis +14.96

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.42, max 1.75, latest 0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +11.23%; worst month: -10.12%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=0.92
- Sideways: S=0.77
- Bear: S=-1.65

## Negated Direction
Best negated: `rank(-1 * fnd6_loc)` S=0.65, F=0.43, INFERIOR
Direction gap: +0.52 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_loc)`: S=0.65, F=0.43, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_loc / close)`: S=0.29, F=0.14, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_loc, 5))`: S=0.40, F=0.31, T=12.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_loc, 5))` | TOP500 | 0.14 | 0.05 | 39.9% | 80% | bull-only |
| `rank(ts_delta(fnd6_loc, 5))` | TOP3000 | 0.08 | 0.03 | 52.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- min_free_cashflow_per_share_guidance: 0.712 (strongly positively correlated)
- shareholders_equity_min_guidance: 0.712 (strongly positively correlated)
- min_total_assets_guidance: 0.712 (strongly positively correlated)
- max_free_cashflow_per_share_guidance: 0.712 (strongly positively correlated)
- shareholders_equity_max_guidance: 0.712 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
