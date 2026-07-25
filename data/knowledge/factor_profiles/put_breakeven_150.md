---
field: put_breakeven_150
dataset: option9
best_template: rank_neg_delta
best_sharpe: 1.3
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.541
ann_vol: 0.1377
hit_rate: 0.5344
rolling_sharpe_min: -3.27
rolling_sharpe_max: 2.44
negated_best_sharpe: 1.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.62
n_negated_sims: 4
direction_gap: 0.66
---
# put_breakeven_150 (option9)

*Open-interest-weighted mean breakeven price at which buyers of put options break even for options expiring in 150 days*

## Signal Profile
- `rank(put_breakeven_150)`: S=0.09, F=0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(put_breakeven_150 / close)`: S=0.28, F=0.13, T=10.4%, INFERIOR (TOP3000)
- `rank(ts_delta(put_breakeven_150, 5))`: S=-1.06, F=-0.50, T=34.2%, INFERIOR (TOP1000)
- `-rank(put_breakeven_150)`: S=0.06, F=0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_150, 5))`: S=1.30, F=0.62, T=37.4%, INFERIOR (TOP3000)
- `-ts_zscore(put_breakeven_150, 63)`: S=0.64, F=0.44, T=13.5%, INFERIOR (TOP3000)
- `ts_mean(put_breakeven_150, 10)`: S=0.24, F=0.11, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(put_breakeven_150, 22))`: S=-0.80, F=-0.44, T=22.3%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_150)`: S=-0.09, F=-0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_150 / close)`: S=-0.53, F=-0.32, T=12.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 14F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.09, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+4.3%
  - 2020: S=-1.95 (negative), ret=-24.9%
  - 2021: S=0.51 (moderate), ret=+7.7%
  - 2022: S=1.28 (moderate), ret=+21.6%
  - 2023: S=-0.17 (negative), ret=-2.3%

## Risk & Drawdown
- Max drawdown: 54.10% over 1498 days (recovered)
- Annualized: return +1.3%, volatility 13.8% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -0.24, excess kurtosis +0.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.27, max 2.44, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.37%; worst month: -11.39%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.64
- Sideways: S=1.03
- Bear: S=-2.56

## Negated Direction
Best negated: `rank(-1 * ts_delta(put_breakeven_150, 5))` S=1.30, F=0.62, INFERIOR
Direction gap: +0.66 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * put_breakeven_150)`: S=-0.09, F=-0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * put_breakeven_150 / close)`: S=-0.53, F=-0.32, T=12.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(put_breakeven_150, 5))`: S=1.30, F=0.62, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(put_breakeven_150)` | TOP3000 | 0.09 | 0.03 | 54.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- put_breakeven_180: 1.000 (strongly positively correlated)
- put_breakeven_120: 1.000 (strongly positively correlated)
- put_breakeven_90: 1.000 (strongly positively correlated)
- put_breakeven_270: 1.000 (strongly positively correlated)
- put_breakeven_60: 1.000 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
