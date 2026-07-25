---
field: fnd6_newa2v1300_txdb
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.57
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1687
ann_vol: 0.0835
hit_rate: 0.5085
rolling_sharpe_min: -2.123
rolling_sharpe_max: 2.395
redundancy_cluster: 13
negated_best_sharpe: 0.36
negated_best_template: neg_rank_level
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.21
---
# fnd6_newa2v1300_txdb (fundamental6)

*Deferred Taxes - Balance Sheet*

## Signal Profile
- `rank(fnd6_newa2v1300_txdb)`: S=0.40, F=0.22, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_txdb / close)`: S=0.57, F=0.35, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_txdb, 5))`: S=0.48, F=0.18, T=35.7%, INFERIOR (TOP3000)
- `-rank(fnd6_newa2v1300_txdb)`: S=-0.06, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_txdb, 5))`: S=0.40, F=0.20, T=29.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_txdb, 22)`: S=0.35, F=0.20, T=26.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_txdb, 10)`: S=-0.02, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_txdb, 22))`: S=0.37, F=0.16, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txdb)`: S=0.36, F=0.23, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txdb / close)`: S=0.32, F=0.19, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.04 (weak), ret=+0.1%
  - 2020: S=-1.10 (negative), ret=-7.0%
  - 2021: S=1.11 (moderate), ret=+12.1%
  - 2022: S=1.54 (strong), ret=+17.7%
  - 2023: S=-0.01 (negative), ret=-0.0%

## Risk & Drawdown
- Max drawdown: 16.87% over 772 days (recovered)
- Annualized: return +4.7%, volatility 8.3% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.04, excess kurtosis +2.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.12, max 2.40, latest -0.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.01%; worst month: -4.66%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.03
- Sideways: S=0.80
- Bear: S=-2.91

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_txdb)` S=0.36, F=0.23, INFERIOR
Direction gap: -0.21 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_txdb)`: S=0.36, F=0.23, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txdb / close)`: S=0.32, F=0.19, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_txdb, 5))`: S=0.40, F=0.20, T=29.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_txdb / close)` | TOP3000 | 0.56 | 0.35 | 16.9% | 60% | bull-only |
| `rank(fnd6_newa2v1300_txdb)` | TOP3000 | 0.39 | 0.22 | 27.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_txdb, 5))` | TOP3000 | 0.46 | 0.18 | 14.9% | 80% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_txdb, 5))` | TOP500 | 0.27 | 0.10 | 25.8% | 80% | all-weather |
| `rank(fnd6_newa2v1300_txdb / close)` | TOP1000 | 0.18 | 0.07 | 20.4% | 60% | bull-only |
| `rank(fnd6_newa2v1300_txdb / close)` | TOP500 | 0.08 | 0.03 | 31.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_txdb, 5))` | TOP1000 | 0.09 | 0.02 | 20.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_txditc: 0.999 (strongly positively correlated)
- ebitda: 0.956 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.956 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.956 (strongly positively correlated)
- operating_profit_before_depr_amort: 0.953 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
