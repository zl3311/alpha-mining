---
field: anl4_cff_high
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.69
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.2364
ann_vol: 0.1287
hit_rate: 0.5093
rolling_sharpe_min: -2.262
rolling_sharpe_max: 2.585
negated_best_sharpe: 0.69
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: 0.32
---
# anl4_cff_high (analyst4)

*Cash Flow From Financing - The highest of forecasted values*

## Signal Profile
- `rank(anl4_cff_high)`: S=0.12, F=0.04, T=2.7%, INFERIOR (TOP500)
- `rank(anl4_cff_high / close)`: S=0.20, F=0.09, T=2.8%, INFERIOR (TOP500)
- `rank(ts_delta(anl4_cff_high, 5))`: S=0.37, F=0.14, T=33.9%, INFERIOR (TOP200)
- `-rank(anl4_cff_high)`: S=0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_high, 5))`: S=0.69, F=0.25, T=37.1%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_cff_high, 63)`: S=0.01, F=0.00, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_cff_high, 10)`: S=-0.43, F=-0.26, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cff_high, 22))`: S=-0.78, F=-0.41, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_high)`: S=0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_high / close)`: S=0.03, F=0.00, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/24P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.37, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.69 (moderate), ret=+6.3%
  - 2020: S=-0.78 (negative), ret=-10.5%
  - 2021: S=1.14 (moderate), ret=+17.9%
  - 2022: S=1.79 (strong), ret=+24.3%
  - 2023: S=-1.49 (negative), ret=-14.5%

## Risk & Drawdown
- Max drawdown: 23.64% over 413 days (not yet recovered, ongoing at window end)
- Annualized: return +4.8%, volatility 12.9% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew -0.46, excess kurtosis +11.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.26, max 2.58, latest -1.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +9.07%; worst month: -6.20%
Positive months: 44%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.63
- Sideways: S=0.70
- Bear: S=-0.25

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cff_high, 5))` S=0.69, F=0.25, INFERIOR
Direction gap: +0.32 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_cff_high)`: S=0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_high / close)`: S=0.03, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_high, 5))`: S=0.69, F=0.25, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_cff_high, 5))` | TOP200 | 0.37 | 0.14 | 23.6% | 60% | mixed |
| `rank(anl4_cff_high / close)` | TOP500 | 0.21 | 0.09 | 41.9% | 40% | bear-only |
| `rank(ts_delta(anl4_cff_high, 5))` | TOP3000 | 0.19 | 0.04 | 21.9% | 60% | mixed |
| `rank(anl4_cff_high)` | TOP500 | 0.13 | 0.04 | 46.1% | 40% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cff_mean: 0.746 (strongly positively correlated)
- pv13_ustomergraphrank_page_rank: -0.181 (weakly negatively correlated)
- parkinson_volatility_30: 0.181 (weakly positively correlated)
- parkinson_volatility_20: 0.141 (weakly positively correlated)
- parkinson_volatility_10: 0.138 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
