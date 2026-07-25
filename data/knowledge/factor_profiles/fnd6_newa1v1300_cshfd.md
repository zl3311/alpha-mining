---
field: fnd6_newa1v1300_cshfd
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.54
best_fitness: 0.29
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.1294
ann_vol: 0.0652
hit_rate: 0.4988
rolling_sharpe_min: -0.895
rolling_sharpe_max: 2.634
redundancy_cluster: 31
negated_best_sharpe: 0.13
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.41
---
# fnd6_newa1v1300_cshfd (fundamental6)

*Common Shares Used to Calc Earnings Per Share - Fully Diluted*

## Signal Profile
- `rank(fnd6_newa1v1300_cshfd)`: S=0.21, F=0.07, T=1.4%, INFERIOR (TOP1000)
- `rank(fnd6_newa1v1300_cshfd / close)`: S=0.54, F=0.29, T=1.8%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newa1v1300_cshfd, 5))`: S=0.49, F=0.24, T=33.5%, INFERIOR (TOP500)
- `-rank(fnd6_newa1v1300_cshfd)`: S=-0.21, F=-0.07, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_cshfd, 5))`: S=0.13, F=0.02, T=35.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_cshfd, 22)`: S=0.10, F=0.03, T=25.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_cshfd, 10)`: S=0.18, F=0.06, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_cshfd, 22))`: S=-1.06, F=-0.86, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_cshfd)`: S=-0.19, F=-0.06, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_cshfd / close)`: S=-0.07, F=-0.01, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.54, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.38 (weak), ret=+1.6%
  - 2020: S=0.62 (moderate), ret=+4.7%
  - 2021: S=-0.54 (negative), ret=-4.4%
  - 2022: S=2.37 (strong), ret=+14.4%
  - 2023: S=0.19 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 12.94% over 342 days (recovered)
- Annualized: return +3.5%, volatility 6.5% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.49, excess kurtosis +2.08

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.90, max 2.63, latest 0.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +5.21%; worst month: -3.73%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.87
- Sideways: S=-0.50
- Bear: S=-0.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_cshfd, 5))` S=0.13, F=0.02, INFERIOR
Direction gap: -0.41 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_cshfd)`: S=-0.19, F=-0.06, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_cshfd / close)`: S=-0.07, F=-0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_cshfd, 5))`: S=0.13, F=0.02, T=35.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_cshfd / close)` | TOP500 | 0.54 | 0.29 | 12.9% | 80% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_cshfd, 5))` | TOP500 | 0.48 | 0.24 | 37.3% | 60% | mixed |
| `rank(fnd6_newa1v1300_cshfd / close)` | TOP200 | 0.35 | 0.17 | 22.1% | 80% | bull-only |
| `rank(fnd6_newa1v1300_cshfd / close)` | TOP1000 | 0.37 | 0.16 | 11.2% | 80% | all-weather |
| `rank(ts_delta(fnd6_newa1v1300_cshfd, 5))` | TOP200 | 0.33 | 0.16 | 54.1% | 80% | weak |
| `rank(fnd6_newa1v1300_cshfd)` | TOP1000 | 0.21 | 0.07 | 14.5% | 60% | bull-only |
| `rank(fnd6_newa1v1300_cshfd)` | TOP3000 | 0.20 | 0.06 | 10.5% | 80% | bull-only |
| `rank(fnd6_newa1v1300_cshfd)` | TOP500 | 0.16 | 0.05 | 24.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_cshfd, 5))` | TOP1000 | 0.16 | 0.04 | 32.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_cshpri: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_csho: 0.992 (strongly positively correlated)
- fnd6_mfma1_csho: 0.992 (strongly positively correlated)
- fnd6_newqv1300_csh12q: 0.981 (strongly positively correlated)
- fnd6_newa1v1300_cshi: 0.976 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
