---
field: fnd6_newa1v1300_ano
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 1.02
best_fitness: 0.94
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.0819
ann_vol: 0.0393
hit_rate: 0.5126
rolling_sharpe_min: -1.141
rolling_sharpe_max: 2.431
negated_best_sharpe: 1.02
negated_best_template: rank_neg_delta
negated_best_fitness: 0.94
n_negated_sims: 10
direction_gap: 0.53
---
# fnd6_newa1v1300_ano (fundamental6)

*Assets Netting & Other Adjustments*

## Signal Profile
- `rank(fnd6_newa1v1300_ano)`: S=0.49, F=0.19, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_ano / close)`: S=0.49, F=0.19, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_ano, 5))`: S=0.32, F=0.16, T=17.6%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_ano)`: S=-0.26, F=-0.09, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ano, 5))`: S=1.02, F=0.94, T=10.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_ano, 22)`: S=-0.16, F=-0.05, T=5.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_ano, 10)`: S=-0.04, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_ano, 22))`: S=-0.39, F=-0.24, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ano)`: S=0.22, F=0.09, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ano / close)`: S=0.21, F=0.09, T=4.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/11P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.51, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.32 (negative), ret=-1.2%
  - 2020: S=-0.46 (negative), ret=-1.7%
  - 2021: S=0.47 (weak), ret=+1.9%
  - 2022: S=1.98 (strong), ret=+7.8%
  - 2023: S=0.76 (moderate), ret=+2.9%

## Risk & Drawdown
- Max drawdown: 8.19% over 1226 days (recovered)
- Annualized: return +2.0%, volatility 3.9% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.85, excess kurtosis +10.82

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.14, max 2.43, latest 0.75

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +2.04%; worst month: -2.26%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.32
- Sideways: S=0.24
- Bear: S=0.88

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_ano, 5))` S=1.02, F=0.94, INFERIOR
Direction gap: +0.53 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_ano)`: S=0.22, F=0.09, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ano / close)`: S=0.21, F=0.09, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ano, 5))`: S=1.02, F=0.94, T=10.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_ano / close)` | TOP3000 | 0.51 | 0.19 | 8.2% | 60% | mixed |
| `rank(fnd6_newa1v1300_ano)` | TOP3000 | 0.50 | 0.19 | 8.2% | 60% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_ano, 5))` | TOP3000 | 0.32 | 0.16 | 33.0% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ano / close)` | TOP1000 | 0.29 | 0.10 | 13.0% | 60% | all-weather |
| `rank(fnd6_newa1v1300_ano / close)` | TOP500 | 0.28 | 0.10 | 13.9% | 40% | mixed |
| `rank(fnd6_newa1v1300_ano)` | TOP500 | 0.26 | 0.09 | 13.9% | 40% | mixed |
| `rank(fnd6_newa1v1300_ano)` | TOP1000 | 0.28 | 0.09 | 13.0% | 60% | all-weather |
| `rank(ts_delta(fnd6_newa1v1300_ano, 5))` | TOP500 | 0.17 | 0.07 | 28.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_anoq: 0.421 (moderately positively correlated)
- return_equity: 0.287 (weakly positively correlated)
- return_assets: 0.285 (weakly positively correlated)
- earnings_per_share_reported_value: 0.279 (weakly positively correlated)
- anl4_epsr_value: 0.279 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
