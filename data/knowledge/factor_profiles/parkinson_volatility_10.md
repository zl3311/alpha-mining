---
field: parkinson_volatility_10
dataset: option8
best_template: rank_delta
best_sharpe: 0.51
best_fitness: 0.15
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1455
ann_vol: 0.062
hit_rate: 0.5053
rolling_sharpe_min: -2.333
rolling_sharpe_max: 3.072
redundancy_cluster: 98
negated_best_sharpe: 0.39
negated_best_template: rank_neg_delta
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.12
---
# parkinson_volatility_10 (option8)

*Historical Parkinson volatility for approximately 10 calendar days*

## Signal Profile
- `rank(parkinson_volatility_10)`: S=0.12, F=0.05, T=14.3%, INFERIOR (TOP200)
- `rank(parkinson_volatility_10 / close)`: S=0.04, F=0.01, T=5.8%, INFERIOR (TOP3000)
- `rank(ts_delta(parkinson_volatility_10, 5))`: S=0.51, F=0.15, T=38.7%, INFERIOR (TOP3000)
- `-rank(parkinson_volatility_10)`: S=-0.04, F=-0.01, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_10, 5))`: S=0.39, F=0.11, T=40.1%, INFERIOR (TOP3000)
- `ts_zscore(parkinson_volatility_10, 22)`: S=0.23, F=0.05, T=30.3%, INFERIOR (TOP3000)
- `ts_mean(parkinson_volatility_10, 10)`: S=-0.17, F=-0.10, T=8.0%, INFERIOR (TOP3000)
- `rank(ts_rank(parkinson_volatility_10, 22))`: S=0.11, F=0.02, T=31.8%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_10)`: S=-0.07, F=-0.02, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_10 / close)`: S=-0.01, F=0.00, T=6.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.52, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.66 (strong), ret=+4.8%
  - 2020: S=-1.49 (negative), ret=-8.8%
  - 2021: S=2.04 (strong), ret=+13.7%
  - 2022: S=1.00 (moderate), ret=+8.6%
  - 2023: S=-0.55 (negative), ret=-2.5%

## Risk & Drawdown
- Max drawdown: 14.55% over 571 days (recovered)
- Annualized: return +3.2%, volatility 6.2% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.17, excess kurtosis +7.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.33, max 3.07, latest -0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.62%; worst month: -7.90%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.47
- Sideways: S=0.35
- Bear: S=-0.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(parkinson_volatility_10, 5))` S=0.39, F=0.11, INFERIOR
Direction gap: -0.12 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * parkinson_volatility_10)`: S=-0.07, F=-0.02, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * parkinson_volatility_10 / close)`: S=-0.01, F=0.00, T=6.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(parkinson_volatility_10, 5))`: S=0.39, F=0.11, T=40.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(parkinson_volatility_10, 5))` | TOP3000 | 0.52 | 0.15 | 14.5% | 60% | mixed |
| `rank(parkinson_volatility_10)` | TOP200 | 0.12 | 0.05 | 76.7% | 60% | bear-only |
| `rank(parkinson_volatility_10)` | TOP500 | 0.07 | 0.02 | 75.2% | 60% | bear-only |

## Correlation Notes
Top correlates:
- historical_volatility_10: 0.745 (strongly positively correlated)
- parkinson_volatility_20: 0.552 (moderately positively correlated)
- historical_volatility_20: 0.427 (moderately positively correlated)
- implied_volatility_put_30: 0.413 (moderately positively correlated)
- implied_volatility_mean_30: 0.397 (weakly positively correlated)

Redundancy cluster #98: 2 similar fields, mean |rho| 0.745 (representative: historical_volatility_10). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
