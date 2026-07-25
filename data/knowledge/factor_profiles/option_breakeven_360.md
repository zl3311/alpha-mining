---
field: option_breakeven_360
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.11
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4816
ann_vol: 0.119
hit_rate: 0.532
rolling_sharpe_min: -3.176
rolling_sharpe_max: 2.551
negated_best_sharpe: 1.11
negated_best_template: rank_neg_delta
negated_best_fitness: 0.43
n_negated_sims: 4
direction_gap: 0.78
---
# option_breakeven_360 (option9)

*Open-interest-weighted average breakeven price of all call and put options expiring in 360 days, representing the price at which option buyers collectively break even*

## Signal Profile
- `rank(option_breakeven_360)`: S=0.14, F=0.05, T=3.3%, INFERIOR (TOP3000)
- `rank(option_breakeven_360 / close)`: S=0.29, F=0.15, T=9.6%, INFERIOR (TOP3000)
- `rank(ts_delta(option_breakeven_360, 5))`: S=-0.57, F=-0.23, T=37.0%, INFERIOR (TOP200)
- `-rank(option_breakeven_360)`: S=0.00, F=0.00, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_360, 5))`: S=1.11, F=0.43, T=39.4%, INFERIOR (TOP3000)
- `-ts_zscore(option_breakeven_360, 63)`: S=0.21, F=0.07, T=15.7%, INFERIOR (TOP3000)
- `ts_mean(option_breakeven_360, 10)`: S=0.33, F=0.17, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(option_breakeven_360, 22))`: S=-0.54, F=-0.22, T=24.1%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_360)`: S=-0.14, F=-0.05, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_360 / close)`: S=-0.18, F=-0.07, T=10.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.14, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.60 (moderate), ret=+4.5%
  - 2020: S=-1.70 (negative), ret=-20.2%
  - 2021: S=0.46 (weak), ret=+5.9%
  - 2022: S=1.35 (moderate), ret=+18.1%
  - 2023: S=-0.03 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 48.16% over 1337 days (recovered)
- Annualized: return +1.6%, volatility 11.9% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.28, excess kurtosis +0.48

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.18, max 2.55, latest -0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.41%; worst month: -10.12%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.61
- Sideways: S=1.10
- Bear: S=-2.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(option_breakeven_360, 5))` S=1.11, F=0.43, INFERIOR
Direction gap: +0.78 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * option_breakeven_360)`: S=-0.14, F=-0.05, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * option_breakeven_360 / close)`: S=-0.18, F=-0.07, T=10.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(option_breakeven_360, 5))`: S=1.11, F=0.43, T=39.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(option_breakeven_360)` | TOP3000 | 0.14 | 0.05 | 48.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- option_breakeven_270: 0.999 (strongly positively correlated)
- option_breakeven_720: 0.999 (strongly positively correlated)
- option_breakeven_1080: 0.999 (strongly positively correlated)
- call_breakeven_270: 0.999 (strongly positively correlated)
- call_breakeven_360: 0.999 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
