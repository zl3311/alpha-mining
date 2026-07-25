---
field: fnd6_mfma1_csho
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.7
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1337
ann_vol: 0.0662
hit_rate: 0.4947
rolling_sharpe_min: -0.773
rolling_sharpe_max: 2.596
redundancy_cluster: 31
negated_best_sharpe: 0.22
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.48
---
# fnd6_mfma1_csho (fundamental6)

*Common Shares Outstanding*

## Signal Profile
- `rank(fnd6_mfma1_csho)`: S=0.23, F=0.08, T=1.4%, INFERIOR (TOP1000)
- `rank(fnd6_mfma1_csho / close)`: S=0.57, F=0.31, T=1.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_mfma1_csho, 5))`: S=0.15, F=0.03, T=35.4%, INFERIOR (TOP3000)
- `-rank(fnd6_mfma1_csho)`: S=-0.23, F=-0.08, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_csho, 5))`: S=0.22, F=0.08, T=34.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mfma1_csho, 63)`: S=0.70, F=0.59, T=18.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfma1_csho, 10)`: S=0.13, F=0.04, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfma1_csho, 22))`: S=-0.05, F=-0.01, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_csho)`: S=-0.01, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_csho / close)`: S=-0.39, F=-0.20, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.57, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+2.8%
  - 2020: S=0.60 (moderate), ret=+4.6%
  - 2021: S=-0.53 (negative), ret=-4.5%
  - 2022: S=2.37 (strong), ret=+14.5%
  - 2023: S=0.23 (weak), ret=+1.1%

## Risk & Drawdown
- Max drawdown: 13.37% over 344 days (recovered)
- Annualized: return +3.8%, volatility 6.6% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.51, excess kurtosis +2.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.77, max 2.60, latest 0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +5.28%; worst month: -3.20%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.82
- Sideways: S=-0.41
- Bear: S=0.02

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mfma1_csho, 5))` S=0.22, F=0.08, INFERIOR
Direction gap: -0.48 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_mfma1_csho)`: S=-0.01, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_csho / close)`: S=-0.39, F=-0.20, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_csho, 5))`: S=0.22, F=0.08, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfma1_csho / close)` | TOP500 | 0.57 | 0.31 | 13.4% | 80% | mixed |
| `rank(fnd6_mfma1_csho / close)` | TOP200 | 0.40 | 0.20 | 23.4% | 80% | bull-only |
| `rank(fnd6_mfma1_csho / close)` | TOP1000 | 0.37 | 0.16 | 12.2% | 80% | all-weather |
| `rank(fnd6_mfma1_csho)` | TOP1000 | 0.23 | 0.08 | 14.7% | 60% | bull-only |
| `rank(fnd6_mfma1_csho)` | TOP3000 | 0.24 | 0.07 | 10.1% | 80% | bull-only |
| `rank(fnd6_mfma1_csho)` | TOP500 | 0.17 | 0.06 | 25.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_mfma1_csho, 5))` | TOP3000 | 0.08 | 0.03 | 26.3% | 40% | bear-only |
| `rank(fnd6_mfma1_csho / close)` | TOP3000 | 0.08 | 0.02 | 27.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_csho: 0.999 (strongly positively correlated)
- fnd6_cshpri: 0.992 (strongly positively correlated)
- fnd6_newa1v1300_cshfd: 0.992 (strongly positively correlated)
- fnd6_newa1v1300_cshi: 0.982 (strongly positively correlated)
- fnd6_newqv1300_csh12q: 0.979 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
