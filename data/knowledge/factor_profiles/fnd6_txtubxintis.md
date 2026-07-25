---
field: fnd6_txtubxintis
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.44
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1416
ann_vol: 0.0628
hit_rate: 0.4955
rolling_sharpe_min: -2.464
rolling_sharpe_max: 2.626
negated_best_sharpe: -0.05
negated_best_template: neg_rank_level
negated_best_fitness: -0.01
n_negated_sims: 10
direction_gap: -0.49
---
# fnd6_txtubxintis (fundamental6)

*Interest & Penalties Recognized - I/S*

## Signal Profile
- `rank(fnd6_txtubxintis)`: S=0.36, F=0.16, T=2.1%, INFERIOR (TOP3000)
- `rank(fnd6_txtubxintis / close)`: S=0.44, F=0.21, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txtubxintis, 5))`: S=0.02, F=0.00, T=39.0%, INFERIOR (TOP3000)
- `-rank(fnd6_txtubxintis)`: S=-0.10, F=-0.03, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubxintis, 5))`: S=-0.06, F=-0.01, T=15.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txtubxintis, 63)`: S=0.44, F=0.41, T=14.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txtubxintis, 10)`: S=0.27, F=0.12, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txtubxintis, 22))`: S=0.25, F=0.10, T=23.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubxintis)`: S=-0.05, F=-0.01, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubxintis / close)`: S=-0.17, F=-0.07, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.43, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.14 (weak), ret=+0.5%
  - 2020: S=-1.83 (negative), ret=-7.3%
  - 2021: S=1.41 (moderate), ret=+11.5%
  - 2022: S=1.41 (moderate), ret=+12.2%
  - 2023: S=-0.76 (negative), ret=-3.6%

## Risk & Drawdown
- Max drawdown: 14.16% over 782 days (recovered)
- Annualized: return +2.7%, volatility 6.3% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.06, excess kurtosis +2.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.46, max 2.63, latest -0.87

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.94%; worst month: -2.33%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.34
- Sideways: S=0.77
- Bear: S=-2.62

## Negated Direction
Best negated: `rank(-1 * fnd6_txtubxintis)` S=-0.05, F=-0.01, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txtubxintis)`: S=-0.05, F=-0.01, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubxintis / close)`: S=-0.17, F=-0.07, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubxintis, 5))`: S=-0.06, F=-0.01, T=15.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txtubxintis / close)` | TOP3000 | 0.43 | 0.21 | 14.2% | 60% | bull-only |
| `rank(fnd6_txtubxintis)` | TOP3000 | 0.35 | 0.16 | 17.4% | 60% | bull-only |
| `rank(fnd6_txtubxintis / close)` | TOP200 | 0.15 | 0.07 | 35.0% | 60% | bull-only |
| `rank(fnd6_txtubxintis / close)` | TOP500 | 0.12 | 0.05 | 19.5% | 40% | bull-only |
| `rank(fnd6_txtubxintis / close)` | TOP1000 | 0.14 | 0.05 | 14.9% | 40% | bull-only |
| `rank(fnd6_txtubxintis)` | TOP1000 | 0.09 | 0.03 | 18.1% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txtubxintbs: 0.869 (strongly positively correlated)
- fnd6_txfo: 0.842 (strongly positively correlated)
- fnd6_txtubtxtr: 0.841 (strongly positively correlated)
- fnd6_txtubsettle: 0.838 (strongly positively correlated)
- net_income_total_2: 0.836 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
