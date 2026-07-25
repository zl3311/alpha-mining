---
field: fnd6_fyrc
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 8.02
best_fitness: 35.59
best_universe: TOP3000
grade: SPECTACULAR
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 3
max_drawdown: 0.1012
ann_vol: 0.0893
hit_rate: 0.498
rolling_sharpe_min: -1.084
rolling_sharpe_max: 1.925
negated_best_sharpe: 0.66
negated_best_template: rank_neg_delta
negated_best_fitness: 0.63
n_negated_sims: 10
direction_gap: -7.36
---
# fnd6_fyrc (fundamental6)

*Unimportant technical code, please ignore for research purposes*

## Signal Profile
- `rank(fnd6_fyrc)`: S=0.22, F=0.09, T=1.9%, INFERIOR (TOP200)
- `rank(fnd6_fyrc / close)`: S=0.17, F=0.06, T=2.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_fyrc, 5))`: S=0.10, F=0.04, T=6.4%, INFERIOR (TOP1000)
- `-rank(fnd6_fyrc)`: S=0.72, F=0.36, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fyrc, 5))`: S=0.66, F=0.63, T=9.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_fyrc, 63)`: S=8.02, F=35.59, T=50.0%, SPECTACULAR (TOP3000)
- `ts_mean(fnd6_fyrc, 10)`: S=-0.50, F=-0.22, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_fyrc, 22))`: S=0.50, F=0.50, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fyrc)`: S=0.95, F=0.53, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fyrc / close)`: S=0.17, F=0.07, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 30F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/14P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.21, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.84 (negative), ret=-5.2%
  - 2020: S=1.25 (moderate), ret=+10.0%
  - 2021: S=0.05 (weak), ret=+0.6%
  - 2022: S=0.02 (weak), ret=+0.2%
  - 2023: S=0.45 (weak), ret=+3.6%

## Risk & Drawdown
- Max drawdown: 10.12% over 589 days (not yet recovered, ongoing at window end)
- Annualized: return +1.9%, volatility 8.9% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew -0.59, excess kurtosis +7.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.08, max 1.93, latest 0.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +5.14%; worst month: -4.24%
Positive months: 46%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.02
- Sideways: S=0.22
- Bear: S=0.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_fyrc, 5))` S=0.66, F=0.63, INFERIOR
Direction gap: -7.36 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_fyrc)`: S=0.95, F=0.53, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fyrc / close)`: S=0.17, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fyrc, 5))`: S=0.66, F=0.63, T=9.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_fyrc)` | TOP200 | 0.21 | 0.09 | 10.1% | 80% | weak |
| `rank(fnd6_fyrc / close)` | TOP200 | 0.17 | 0.06 | 25.8% | 60% | mixed |
| `rank(ts_delta(fnd6_fyrc, 5))` | TOP1000 | 0.09 | 0.04 | 48.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_capex_guidance: 0.267 (weakly positively correlated)
- capital_expenditure_max_guidance_qtr: 0.267 (weakly positively correlated)
- cash_flow_from_investing: 0.205 (weakly positively correlated)
- fnd6_prcl: -0.182 (weakly negatively correlated)
- fn_taxes_payable_a: -0.178 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
