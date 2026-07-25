---
field: fnd6_txtubpospdec
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.64
best_fitness: 0.36
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1929
ann_vol: 0.1615
hit_rate: 0.498
rolling_sharpe_min: -0.788
rolling_sharpe_max: 1.95
negated_best_sharpe: 0.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.34
---
# fnd6_txtubpospdec (fundamental6)

*Decrease - Prior Tax Positions*

## Signal Profile
- `rank(fnd6_txtubpospdec)`: S=0.54, F=0.28, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_txtubpospdec / close)`: S=0.63, F=0.34, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txtubpospdec, 5))`: S=0.64, F=0.36, T=32.4%, INFERIOR (TOP500)
- `-rank(fnd6_txtubpospdec)`: S=-0.39, F=-0.19, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubpospdec, 5))`: S=0.30, F=0.10, T=40.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txtubpospdec, 22)`: S=-0.36, F=-0.25, T=22.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txtubpospdec, 10)`: S=0.34, F=0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txtubpospdec, 22))`: S=-0.01, F=0.00, T=21.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubpospdec)`: S=-0.54, F=-0.28, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubpospdec / close)`: S=-0.63, F=-0.34, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.05 (moderate), ret=+14.9%
  - 2020: S=-0.05 (negative), ret=-0.9%
  - 2021: S=1.31 (moderate), ret=+19.6%
  - 2022: S=0.60 (moderate), ret=+9.5%
  - 2023: S=0.43 (weak), ret=+7.2%

## Risk & Drawdown
- Max drawdown: 19.29% over 312 days (recovered)
- Annualized: return +10.2%, volatility 16.2% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew -0.01, excess kurtosis +13.77

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.79, max 1.95, latest 0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +14.71%; worst month: -9.66%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.97
- Sideways: S=0.43
- Bear: S=-0.76

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txtubpospdec, 5))` S=0.30, F=0.10, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txtubpospdec)`: S=-0.54, F=-0.28, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubpospdec / close)`: S=-0.63, F=-0.34, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubpospdec, 5))`: S=0.30, F=0.10, T=40.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txtubpospdec, 5))` | TOP500 | 0.63 | 0.36 | 19.3% | 80% | bull-only |
| `rank(fnd6_txtubpospdec / close)` | TOP3000 | 0.63 | 0.34 | 13.1% | 80% | bull-only |
| `rank(fnd6_txtubpospdec)` | TOP3000 | 0.53 | 0.28 | 16.8% | 80% | bull-only |
| `rank(fnd6_txtubpospdec / close)` | TOP500 | 0.46 | 0.26 | 19.8% | 80% | bull-only |
| `rank(fnd6_txtubpospdec / close)` | TOP1000 | 0.47 | 0.26 | 14.6% | 60% | bull-only |
| `rank(fnd6_txtubpospdec)` | TOP1000 | 0.38 | 0.19 | 19.1% | 60% | bull-only |
| `rank(fnd6_txtubpospdec)` | TOP500 | 0.33 | 0.16 | 23.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_txtubpospdec, 5))` | TOP1000 | 0.27 | 0.09 | 42.3% | 60% | bull-only |
| `rank(fnd6_txtubpospdec / close)` | TOP200 | 0.10 | 0.03 | 24.8% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_ds: 0.233 (weakly positively correlated)
- fnd6_newa1v1300_dcom: 0.198 (weakly positively correlated)
- fnd6_txndb: 0.163 (weakly positively correlated)
- fnd6_dvpa: 0.160 (weakly positively correlated)
- implied_volatility_mean_skew_30: 0.157 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
