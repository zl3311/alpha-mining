---
field: fnd6_newa2v1300_txditc
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.55
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1799
ann_vol: 0.088
hit_rate: 0.5109
rolling_sharpe_min: -2.121
rolling_sharpe_max: 2.429
redundancy_cluster: 13
negated_best_sharpe: 0.36
negated_best_template: neg_rank_level
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.19
---
# fnd6_newa2v1300_txditc (fundamental6)

*Deferred Taxes and Investment Tax Credit*

## Signal Profile
- `rank(fnd6_newa2v1300_txditc)`: S=0.38, F=0.21, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_txditc / close)`: S=0.55, F=0.34, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_txditc, 5))`: S=0.59, F=0.25, T=35.9%, INFERIOR (TOP3000)
- `-rank(fnd6_newa2v1300_txditc)`: S=-0.06, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_txditc, 5))`: S=0.44, F=0.23, T=29.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_txditc, 22)`: S=0.35, F=0.20, T=26.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_txditc, 10)`: S=-0.01, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_txditc, 22))`: S=0.44, F=0.21, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txditc)`: S=0.36, F=0.24, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txditc / close)`: S=0.32, F=0.20, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.55, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.04 (weak), ret=+0.1%
  - 2020: S=-1.16 (negative), ret=-7.9%
  - 2021: S=1.15 (moderate), ret=+13.3%
  - 2022: S=1.55 (strong), ret=+18.7%
  - 2023: S=-0.14 (negative), ret=-0.8%

## Risk & Drawdown
- Max drawdown: 17.99% over 772 days (recovered)
- Annualized: return +4.8%, volatility 8.8% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.07, excess kurtosis +2.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.12, max 2.43, latest -0.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.50%; worst month: -4.84%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.00
- Sideways: S=0.67
- Bear: S=-2.83

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_txditc)` S=0.36, F=0.24, INFERIOR
Direction gap: -0.19 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_txditc)`: S=0.36, F=0.24, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txditc / close)`: S=0.32, F=0.20, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_txditc, 5))`: S=0.44, F=0.23, T=29.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_txditc / close)` | TOP3000 | 0.55 | 0.34 | 18.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_txditc, 5))` | TOP3000 | 0.57 | 0.25 | 14.4% | 80% | mixed |
| `rank(fnd6_newa2v1300_txditc)` | TOP3000 | 0.37 | 0.21 | 29.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_txditc, 5))` | TOP500 | 0.27 | 0.10 | 25.5% | 80% | all-weather |
| `rank(fnd6_newa2v1300_txditc / close)` | TOP1000 | 0.17 | 0.07 | 20.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_txditc, 5))` | TOP1000 | 0.12 | 0.03 | 20.8% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_txdb: 0.999 (strongly positively correlated)
- ebitda: 0.955 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.955 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.955 (strongly positively correlated)
- operating_profit_before_depr_amort: 0.952 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
