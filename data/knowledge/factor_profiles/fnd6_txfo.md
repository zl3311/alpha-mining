---
field: fnd6_txfo
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.54
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1944
ann_vol: 0.0871
hit_rate: 0.5028
rolling_sharpe_min: -2.685
rolling_sharpe_max: 2.48
redundancy_cluster: 13
negated_best_sharpe: 0.31
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.23
---
# fnd6_txfo (fundamental6)

*Income Taxes - Foreign*

## Signal Profile
- `rank(fnd6_txfo)`: S=0.44, F=0.26, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_txfo / close)`: S=0.57, F=0.36, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txfo, 5))`: S=0.59, F=0.32, T=31.6%, INFERIOR (TOP500)
- `-rank(fnd6_txfo)`: S=-0.17, F=-0.07, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txfo, 5))`: S=0.31, F=0.15, T=24.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txfo, 63)`: S=0.54, F=0.42, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txfo, 10)`: S=-0.11, F=-0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txfo, 22))`: S=-0.04, F=-0.01, T=20.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txfo)`: S=0.15, F=0.06, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txfo / close)`: S=0.13, F=0.05, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.21 (weak), ret=+0.9%
  - 2020: S=-1.49 (negative), ret=-8.9%
  - 2021: S=1.19 (moderate), ret=+13.9%
  - 2022: S=1.46 (moderate), ret=+17.5%
  - 2023: S=0.11 (weak), ret=+0.7%

## Risk & Drawdown
- Max drawdown: 19.44% over 757 days (recovered)
- Annualized: return +4.9%, volatility 8.7% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.10, excess kurtosis +2.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.69, max 2.48, latest -0.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.92%; worst month: -4.42%
Positive months: 46%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.03
- Sideways: S=0.95
- Bear: S=-3.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txfo, 5))` S=0.31, F=0.15, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txfo)`: S=0.15, F=0.06, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txfo / close)`: S=0.13, F=0.05, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txfo, 5))`: S=0.31, F=0.15, T=24.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txfo / close)` | TOP3000 | 0.56 | 0.36 | 19.4% | 80% | bull-only |
| `rank(ts_delta(fnd6_txfo, 5))` | TOP500 | 0.58 | 0.32 | 26.2% | 80% | mixed |
| `rank(ts_delta(fnd6_txfo, 5))` | TOP3000 | 0.56 | 0.27 | 19.9% | 60% | all-weather |
| `rank(fnd6_txfo)` | TOP3000 | 0.44 | 0.26 | 29.5% | 80% | bull-only |
| `rank(ts_delta(fnd6_txfo, 5))` | TOP1000 | 0.35 | 0.13 | 21.0% | 60% | mixed |
| `rank(fnd6_txfo / close)` | TOP1000 | 0.21 | 0.09 | 28.3% | 60% | bull-only |
| `rank(fnd6_txfo)` | TOP1000 | 0.17 | 0.07 | 37.2% | 60% | bull-only |
| `rank(fnd6_txfo / close)` | TOP500 | 0.09 | 0.03 | 35.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txc: 0.955 (strongly positively correlated)
- ebitda: 0.938 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.938 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.938 (strongly positively correlated)
- fnd6_txdba: 0.936 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
