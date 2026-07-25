---
field: anl4_cff_mean
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 1.0
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 2
max_drawdown: 0.2245
ann_vol: 0.116
hit_rate: 0.5012
rolling_sharpe_min: -2.15
rolling_sharpe_max: 1.735
negated_best_sharpe: 1.0
negated_best_template: rank_neg_delta
negated_best_fitness: 0.42
n_negated_sims: 10
direction_gap: 0.5
---
# anl4_cff_mean (analyst4)

*Cash Flow From Financing - mean of estimations*

## Signal Profile
- `rank(anl4_cff_mean)`: S=0.05, F=0.01, T=2.8%, INFERIOR (TOP200)
- `rank(anl4_cff_mean / close)`: S=0.08, F=0.02, T=2.9%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cff_mean, 5))`: S=0.16, F=0.04, T=34.5%, INFERIOR (TOP200)
- `-rank(anl4_cff_mean)`: S=0.08, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_mean, 5))`: S=1.00, F=0.42, T=37.2%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_cff_mean, 63)`: S=0.50, F=0.19, T=17.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_cff_mean, 10)`: S=-0.35, F=-0.19, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cff_mean, 22))`: S=-1.06, F=-0.62, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_mean)`: S=0.08, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_mean / close)`: S=0.09, F=0.03, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.16, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.02 (moderate), ret=+8.6%
  - 2020: S=-0.85 (negative), ret=-10.0%
  - 2021: S=0.99 (moderate), ret=+13.7%
  - 2022: S=0.57 (moderate), ret=+7.2%
  - 2023: S=-1.13 (negative), ret=-10.2%

## Risk & Drawdown
- Max drawdown: 22.45% over 595 days (not yet recovered, ongoing at window end)
- Annualized: return +1.9%, volatility 11.6% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew -0.11, excess kurtosis +6.82

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.15, max 1.74, latest -1.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +7.10%; worst month: -7.07%
Positive months: 58%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.43
- Sideways: S=0.51
- Bear: S=-0.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cff_mean, 5))` S=1.00, F=0.42, INFERIOR
Direction gap: +0.50 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_cff_mean)`: S=0.08, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_mean / close)`: S=0.09, F=0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_mean, 5))`: S=1.00, F=0.42, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_cff_mean, 5))` | TOP200 | 0.16 | 0.04 | 22.4% | 60% | weak |
| `rank(anl4_cff_mean / close)` | TOP200 | 0.09 | 0.02 | 50.9% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cff_high: 0.746 (strongly positively correlated)
- parkinson_volatility_30: 0.169 (weakly positively correlated)
- parkinson_volatility_10: 0.167 (weakly positively correlated)
- historical_volatility_10: 0.154 (weakly positively correlated)
- pv13_ustomergraphrank_page_rank: -0.140 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
