---
field: forward_price_150
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.32
best_fitness: 0.64
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.5491
ann_vol: 0.1343
hit_rate: 0.5393
rolling_sharpe_min: -3.35
rolling_sharpe_max: 2.414
negated_best_sharpe: 1.32
negated_best_template: rank_neg_delta
negated_best_fitness: 0.64
n_negated_sims: 4
direction_gap: 0.71
---
# forward_price_150 (option9)

*Synthetic forward price at 150 days derived from at-the-money call and put options reflecting the market's forward expectation of the underlying security*

## Signal Profile
- `rank(forward_price_150)`: S=0.07, F=0.02, T=7.3%, INFERIOR (TOP3000)
- `rank(forward_price_150 / close)`: S=0.42, F=0.18, T=17.9%, INFERIOR (TOP3000)
- `rank(ts_delta(forward_price_150, 5))`: S=-1.03, F=-0.49, T=40.0%, INFERIOR (TOP1000)
- `-rank(forward_price_150)`: S=0.07, F=0.02, T=5.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(forward_price_150, 5))`: S=1.32, F=0.64, T=43.6%, INFERIOR (TOP3000)
- `-ts_zscore(forward_price_150, 63)`: S=0.61, F=0.40, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(forward_price_150, 10)`: S=0.27, F=0.13, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(forward_price_150, 22))`: S=-0.85, F=-0.47, T=28.1%, INFERIOR (TOP3000)
- `rank(-1 * forward_price_150)`: S=-0.07, F=-0.02, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * forward_price_150 / close)`: S=-0.29, F=-0.10, T=18.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.07, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.51 (moderate), ret=+4.1%
  - 2020: S=-1.94 (negative), ret=-24.8%
  - 2021: S=0.51 (moderate), ret=+7.3%
  - 2022: S=1.21 (moderate), ret=+19.9%
  - 2023: S=-0.14 (negative), ret=-1.8%

## Risk & Drawdown
- Max drawdown: 54.91% over 1518 days (recovered)
- Annualized: return +1.0%, volatility 13.4% (fraction of booksize)
- Hit rate: 53.9% positive days
- Tail shape: skew -0.28, excess kurtosis +0.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.35, max 2.41, latest -0.35

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.11%; worst month: -11.03%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.51
- Sideways: S=1.01
- Bear: S=-2.46

## Negated Direction
Best negated: `rank(-1 * ts_delta(forward_price_150, 5))` S=1.32, F=0.64, INFERIOR
Direction gap: +0.71 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * forward_price_150)`: S=-0.07, F=-0.02, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * forward_price_150 / close)`: S=-0.29, F=-0.10, T=18.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(forward_price_150, 5))`: S=1.32, F=0.64, T=43.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(forward_price_150)` | TOP3000 | 0.07 | 0.02 | 54.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- forward_price_120: 1.000 (strongly positively correlated)
- forward_price_180: 1.000 (strongly positively correlated)
- forward_price_90: 1.000 (strongly positively correlated)
- forward_price_270: 1.000 (strongly positively correlated)
- forward_price_60: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
