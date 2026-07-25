---
field: pv13_reveremap
dataset: pv13
best_template: ts_zscore
best_sharpe: 0.89
best_fitness: 1.5
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 25
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.3599
ann_vol: 0.2745
hit_rate: 0.481
rolling_sharpe_min: -0.899
rolling_sharpe_max: 1.6
negated_best_sharpe: 0.82
negated_best_template: rank_neg_delta
negated_best_fitness: 0.96
n_negated_sims: 10
direction_gap: -0.07
---
# pv13_reveremap (pv13)

*Mapping data*

## Signal Profile
- `rank(pv13_reveremap)`: S=0.01, F=0.00, T=1.8%, INFERIOR (TOP200)
- `rank(pv13_reveremap / close)`: S=-0.27, F=-0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(pv13_reveremap, 5))`: S=0.39, F=0.34, T=14.1%, INFERIOR (TOP1000)
- `-rank(pv13_reveremap)`: S=0.37, F=0.19, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_reveremap, 5))`: S=0.82, F=0.96, T=23.2%, INFERIOR (TOP3000)
- `-ts_zscore(pv13_reveremap, 63)`: S=0.89, F=1.50, T=2.3%, AVERAGE (TOP3000)
- `ts_mean(pv13_reveremap, 10)`: S=-0.47, F=-0.28, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_reveremap, 22))`: S=-0.48, F=-0.56, T=12.0%, INFERIOR (TOP3000)
- `rank(-1 * pv13_reveremap)`: S=0.64, F=0.41, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * pv13_reveremap / close)`: S=0.45, F=0.28, T=1.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/14P
- LOW_FITNESS: 24F/1P
- LOW_SHARPE: 25F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/13P
- LOW_TURNOVER: 4F/21P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.39, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.61 (moderate), ret=+23.0%
  - 2020: S=0.33 (weak), ret=+6.3%
  - 2021: S=0.29 (weak), ret=+11.6%
  - 2022: S=0.45 (weak), ret=+5.8%
  - 2023: S=0.55 (moderate), ret=+5.7%

## Risk & Drawdown
- Max drawdown: 35.99% over 597 days (recovered)
- Annualized: return +10.7%, volatility 27.5% (fraction of booksize)
- Hit rate: 48.1% positive days
- Tail shape: skew +5.37, excess kurtosis +93.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.90, max 1.60, latest 0.47

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +42.02%; worst month: -25.73%
Positive months: 53%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.44
- Sideways: S=0.75
- Bear: S=-1.35

## Negated Direction
Best negated: `rank(-1 * ts_delta(pv13_reveremap, 5))` S=0.82, F=0.96, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pv13_reveremap)`: S=0.64, F=0.41, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * pv13_reveremap / close)`: S=0.45, F=0.28, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_reveremap, 5))`: S=0.82, F=0.96, T=23.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pv13_reveremap, 5))` | TOP1000 | 0.39 | 0.34 | 36.0% | 100% | bull-only |

## Correlation Notes
Top correlates:
- actual_dividend_value_quarterly: 0.210 (weakly positively correlated)
- net_income_adjusted: 0.208 (weakly positively correlated)
- net_income_total_2: 0.207 (weakly positively correlated)
- fnd6_pifo: 0.207 (weakly positively correlated)
- fnd6_txtubsoflimit: 0.205 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
