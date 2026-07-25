---
field: adjfactor
dataset: pv1
best_template: rank_level
best_sharpe: 0.56
best_fitness: 0.19
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1103
ann_vol: 0.1024
hit_rate: 0.515
rolling_sharpe_min: -0.689
rolling_sharpe_max: 2.168
redundancy_cluster: 40
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.03
---
# adjfactor (pv1)

*Adjustment factor applied to historical prices and dividends to account for splits and other corporate actions*

## Signal Profile
- `rank(adjfactor)`: S=0.56, F=0.19, T=49.8%, INFERIOR (TOP200)
- `rank(ts_delta(adjfactor, 5))`: S=0.49, F=0.13, T=52.4%, INFERIOR (TOP200)
- `-rank(adjfactor)`: S=0.41, F=0.09, T=54.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(adjfactor, 5))`: S=0.53, F=0.10, T=57.1%, INFERIOR (TOP3000)
- `ts_zscore(adjfactor, 22)`: S=-0.09, F=-0.02, T=26.8%, INFERIOR (TOP3000)
- `ts_mean(adjfactor, 10)`: S=-0.27, F=-0.11, T=18.4%, INFERIOR (TOP3000)
- `rank(ts_rank(adjfactor, 22))`: S=0.22, F=0.06, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * adjfactor)`: S=0.41, F=0.09, T=54.5%, INFERIOR (TOP3000)
- `rank(-1 * adjfactor / close)`: S=-0.06, F=-0.01, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/20P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.56, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.37 (negative), ret=-3.0%
  - 2020: S=2.35 (strong), ret=+23.1%
  - 2021: S=-0.38 (negative), ret=-4.5%
  - 2022: S=0.93 (moderate), ret=+10.5%
  - 2023: S=0.26 (weak), ret=+2.3%

## Risk & Drawdown
- Max drawdown: 11.03% over 349 days (recovered)
- Annualized: return +5.8%, volatility 10.2% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.07, excess kurtosis +5.13

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.69, max 2.17, latest 0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +6.95%; worst month: -6.25%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.05
- Sideways: S=-0.17
- Bear: S=2.11

## Negated Direction
Best negated: `rank(-1 * ts_delta(adjfactor, 5))` S=0.53, F=0.10, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * adjfactor)`: S=0.41, F=0.09, T=54.5%, INFERIOR (TOP3000)
- `rank(-1 * adjfactor / close)`: S=-0.06, F=-0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(adjfactor, 5))`: S=0.53, F=0.10, T=57.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(adjfactor)` | TOP200 | 0.56 | 0.19 | 11.0% | 60% | mixed |
| `rank(ts_delta(adjfactor, 5))` | TOP200 | 0.49 | 0.13 | 11.6% | 60% | mixed |
| `rank(adjfactor)` | TOP3000 | 0.16 | 0.02 | 20.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- max_stock_option_expense_guidance: 0.819 (strongly positively correlated)
- min_stock_option_expense_guidance_2: 0.819 (strongly positively correlated)
- dividend_max_guidance_value: 0.816 (strongly positively correlated)
- max_reported_pretax_income_guidance_2: 0.813 (strongly positively correlated)
- dividend_min_guidance_value: 0.812 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
