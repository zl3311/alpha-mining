---
field: fnd6_newa2v1300_reuna
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.8
best_fitness: 0.58
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.2429
ann_vol: 0.2059
hit_rate: 0.5053
rolling_sharpe_min: -0.669
rolling_sharpe_max: 3.491
redundancy_cluster: 58
negated_best_sharpe: 0.46
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: -0.34
---
# fnd6_newa2v1300_reuna (fundamental6)

*Retained Earnings - Unadjusted*

## Signal Profile
- `rank(fnd6_newa2v1300_reuna)`: S=0.04, F=0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_reuna / close)`: S=0.20, F=0.09, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_reuna, 5))`: S=0.80, F=0.58, T=31.0%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_reuna)`: S=-0.02, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_reuna, 5))`: S=-0.88, F=-0.67, T=31.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_reuna, 63)`: S=0.01, F=0.00, T=20.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_reuna, 10)`: S=0.01, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_reuna, 22))`: S=0.54, F=0.31, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_reuna)`: S=0.43, F=0.29, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_reuna / close)`: S=0.46, F=0.33, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.80, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=2.65 (strong), ret=+33.4%
  - 2020: S=0.81 (moderate), ret=+13.4%
  - 2021: S=0.68 (moderate), ret=+15.5%
  - 2022: S=0.23 (weak), ret=+6.7%
  - 2023: S=0.70 (moderate), ret=+11.2%

## Risk & Drawdown
- Max drawdown: 24.29% over 331 days (recovered)
- Annualized: return +16.4%, volatility 20.6% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew -1.01, excess kurtosis +18.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.67, max 3.49, latest 0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +14.15%; worst month: -9.96%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.56
- Sideways: S=1.39
- Bear: S=0.60

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_reuna / close)` S=0.46, F=0.33, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_reuna)`: S=0.43, F=0.29, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_reuna / close)`: S=0.46, F=0.33, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_reuna, 5))`: S=-0.88, F=-0.67, T=31.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa2v1300_reuna, 5))` | TOP200 | 0.80 | 0.58 | 24.3% | 100% | all-weather |
| `rank(ts_delta(fnd6_newa2v1300_reuna, 5))` | TOP1000 | 0.33 | 0.11 | 28.3% | 80% | mixed |
| `rank(fnd6_newa2v1300_reuna / close)` | TOP3000 | 0.19 | 0.09 | 36.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_reuna, 5))` | TOP3000 | 0.20 | 0.05 | 33.4% | 60% | bull-only |
| `rank(fnd6_newa2v1300_reuna / close)` | TOP1000 | 0.07 | 0.03 | 33.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_re: 0.944 (strongly positively correlated)
- fnd6_newa1v1300_ibc: 0.568 (moderately positively correlated)
- fnd6_newa1v1300_epsfx: 0.544 (moderately positively correlated)
- fnd6_newa1v1300_epsfi: 0.543 (moderately positively correlated)
- fnd6_citotal: 0.534 (moderately positively correlated)

Redundancy cluster #58: 2 similar fields, mean |rho| 0.944 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
