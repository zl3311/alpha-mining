---
field: historical_volatility_120
dataset: option8
best_template: rank_delta
best_sharpe: 0.76
best_fitness: 0.33
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.1126
ann_vol: 0.0836
hit_rate: 0.5215
rolling_sharpe_min: -0.495
rolling_sharpe_max: 2.089
redundancy_cluster: 48
negated_best_sharpe: 0.03
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.73
---
# historical_volatility_120 (option8)

*Historical close-to-close volatility for approximately 120 calendar days*

## Signal Profile
- `rank(historical_volatility_120)`: S=0.19, F=0.11, T=5.6%, INFERIOR (TOP200)
- `rank(historical_volatility_120 / close)`: S=0.02, F=0.00, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_delta(historical_volatility_120, 5))`: S=0.76, F=0.33, T=33.9%, INFERIOR (TOP1000)
- `-rank(historical_volatility_120)`: S=-0.05, F=-0.01, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_120, 5))`: S=-0.77, F=-0.31, T=32.8%, INFERIOR (TOP3000)
- `ts_zscore(historical_volatility_120, 22)`: S=0.38, F=0.13, T=23.1%, INFERIOR (TOP3000)
- `ts_mean(historical_volatility_120, 10)`: S=-0.14, F=-0.08, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(historical_volatility_120, 22))`: S=0.57, F=0.21, T=26.1%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_120)`: S=0.01, F=0.00, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_120 / close)`: S=0.03, F=0.01, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.76, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.63 (strong), ret=+6.4%
  - 2020: S=0.12 (weak), ret=+1.2%
  - 2021: S=0.92 (moderate), ret=+9.1%
  - 2022: S=1.34 (moderate), ret=+13.8%
  - 2023: S=0.16 (weak), ret=+0.7%

## Risk & Drawdown
- Max drawdown: 11.26% over 245 days (recovered)
- Annualized: return +6.4%, volatility 8.4% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.99, excess kurtosis +8.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.49, max 2.09, latest 0.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +7.38%; worst month: -2.66%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.17
- Sideways: S=-0.78
- Bear: S=1.48

## Negated Direction
Best negated: `rank(-1 * historical_volatility_120 / close)` S=0.03, F=0.01, INFERIOR
Direction gap: -0.73 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * historical_volatility_120)`: S=0.01, F=0.00, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * historical_volatility_120 / close)`: S=0.03, F=0.01, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(historical_volatility_120, 5))`: S=-0.77, F=-0.31, T=32.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(historical_volatility_120, 5))` | TOP1000 | 0.76 | 0.33 | 11.3% | 100% | all-weather |
| `rank(ts_delta(historical_volatility_120, 5))` | TOP3000 | 0.77 | 0.31 | 10.4% | 80% | all-weather |
| `rank(ts_delta(historical_volatility_120, 5))` | TOP500 | 0.63 | 0.26 | 14.4% | 80% | all-weather |
| `rank(historical_volatility_120)` | TOP200 | 0.19 | 0.11 | 60.7% | 60% | bear-only |
| `rank(historical_volatility_120)` | TOP500 | 0.17 | 0.08 | 65.8% | 60% | bear-only |
| `rank(ts_delta(historical_volatility_120, 5))` | TOP200 | 0.07 | 0.02 | 32.6% | 60% | weak |

## Correlation Notes
Top correlates:
- parkinson_volatility_120: 0.819 (strongly positively correlated)
- historical_volatility_90: 0.653 (moderately positively correlated)
- parkinson_volatility_90: 0.640 (moderately positively correlated)
- historical_volatility_10 - historical_volatility_180: 0.552 (moderately positively correlated)
- historical_volatility_30: 0.541 (moderately positively correlated)

Redundancy cluster #48: 4 similar fields, mean |rho| 0.738 (representative: parkinson_volatility_120). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
