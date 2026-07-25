---
field: fnd6_newa1v1300_csho
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.71
best_fitness: 0.61
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.134
ann_vol: 0.0663
hit_rate: 0.498
rolling_sharpe_min: -0.799
rolling_sharpe_max: 2.593
redundancy_cluster: 31
negated_best_sharpe: 0.21
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.5
---
# fnd6_newa1v1300_csho (fundamental6)

*Common Shares Outstanding*

## Signal Profile
- `rank(fnd6_newa1v1300_csho)`: S=0.25, F=0.09, T=1.4%, INFERIOR (TOP1000)
- `rank(fnd6_newa1v1300_csho / close)`: S=0.58, F=0.32, T=1.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newa1v1300_csho, 5))`: S=0.17, F=0.04, T=35.4%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_csho)`: S=-0.25, F=-0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_csho, 5))`: S=0.21, F=0.08, T=34.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_csho, 63)`: S=0.71, F=0.61, T=18.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_csho, 10)`: S=0.16, F=0.05, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_csho, 22))`: S=-0.08, F=-0.02, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_csho)`: S=0.00, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_csho / close)`: S=-0.38, F=-0.19, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.64 (moderate), ret=+2.8%
  - 2020: S=0.62 (moderate), ret=+4.7%
  - 2021: S=-0.52 (negative), ret=-4.4%
  - 2022: S=2.37 (strong), ret=+14.5%
  - 2023: S=0.25 (weak), ret=+1.2%

## Risk & Drawdown
- Max drawdown: 13.40% over 344 days (recovered)
- Annualized: return +3.8%, volatility 6.6% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.52, excess kurtosis +2.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.80, max 2.59, latest 0.35

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +5.27%; worst month: -3.19%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.81
- Sideways: S=-0.42
- Bear: S=0.05

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_csho, 5))` S=0.21, F=0.08, INFERIOR
Direction gap: -0.50 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_csho)`: S=0.00, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_csho / close)`: S=-0.38, F=-0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_csho, 5))`: S=0.21, F=0.08, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_csho / close)` | TOP500 | 0.58 | 0.32 | 13.4% | 80% | mixed |
| `rank(fnd6_newa1v1300_csho / close)` | TOP200 | 0.39 | 0.19 | 23.6% | 80% | bull-only |
| `rank(fnd6_newa1v1300_csho / close)` | TOP1000 | 0.38 | 0.17 | 12.1% | 80% | all-weather |
| `rank(fnd6_newa1v1300_csho)` | TOP1000 | 0.25 | 0.09 | 14.4% | 60% | bull-only |
| `rank(fnd6_newa1v1300_csho)` | TOP3000 | 0.24 | 0.07 | 9.9% | 80% | bull-only |
| `rank(fnd6_newa1v1300_csho)` | TOP500 | 0.18 | 0.06 | 24.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_csho, 5))` | TOP3000 | 0.11 | 0.04 | 25.3% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_mfma1_csho: 0.999 (strongly positively correlated)
- fnd6_cshpri: 0.992 (strongly positively correlated)
- fnd6_newa1v1300_cshfd: 0.992 (strongly positively correlated)
- fnd6_newa1v1300_cshi: 0.982 (strongly positively correlated)
- fnd6_newqv1300_csh12q: 0.978 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
