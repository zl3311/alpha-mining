---
field: fnd6_txtubxintbs
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.45
best_fitness: 0.28
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.254
ann_vol: 0.1085
hit_rate: 0.5093
rolling_sharpe_min: -2.509
rolling_sharpe_max: 2.53
negated_best_sharpe: 0.31
negated_best_template: neg_rank_level
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.14
---
# fnd6_txtubxintbs (fundamental6)

*Interest & Penalties Accrued - B/S*

## Signal Profile
- `rank(fnd6_txtubxintbs)`: S=0.31, F=0.17, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_txtubxintbs / close)`: S=0.45, F=0.28, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txtubxintbs, 5))`: S=0.10, F=0.02, T=29.9%, INFERIOR (TOP500)
- `-rank(fnd6_txtubxintbs)`: S=-0.01, F=0.00, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubxintbs, 5))`: S=-0.02, F=0.00, T=21.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txtubxintbs, 22)`: S=-0.06, F=-0.01, T=18.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txtubxintbs, 10)`: S=0.15, F=0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txtubxintbs, 22))`: S=0.23, F=0.09, T=21.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubxintbs)`: S=0.31, F=0.21, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubxintbs / close)`: S=0.25, F=0.15, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.44, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.35 (negative), ret=-1.7%
  - 2020: S=-1.80 (negative), ret=-12.8%
  - 2021: S=1.40 (moderate), ret=+18.6%
  - 2022: S=1.40 (moderate), ret=+22.0%
  - 2023: S=-0.30 (negative), ret=-2.5%

## Risk & Drawdown
- Max drawdown: 25.40% over 783 days (recovered)
- Annualized: return +4.8%, volatility 10.8% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.04, excess kurtosis +2.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.51, max 2.53, latest -0.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.47%; worst month: -5.07%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.93
- Sideways: S=0.48
- Bear: S=-3.12

## Negated Direction
Best negated: `rank(-1 * fnd6_txtubxintbs)` S=0.31, F=0.21, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txtubxintbs)`: S=0.31, F=0.21, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubxintbs / close)`: S=0.25, F=0.15, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubxintbs, 5))`: S=-0.02, F=0.00, T=21.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txtubxintbs / close)` | TOP3000 | 0.44 | 0.28 | 25.4% | 40% | bull-only |
| `rank(fnd6_txtubxintbs)` | TOP3000 | 0.30 | 0.17 | 34.7% | 40% | bull-only |
| `rank(fnd6_txtubxintbs / close)` | TOP1000 | 0.07 | 0.02 | 24.1% | 40% | bull-only |
| `rank(ts_delta(fnd6_txtubxintbs, 5))` | TOP500 | 0.10 | 0.02 | 37.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txtubtxtr: 0.949 (strongly positively correlated)
- fnd6_txtubsoflimit: 0.945 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.944 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.944 (strongly positively correlated)
- ebitda: 0.944 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
