---
field: fnd6_newa1v1300_ao
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.73
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0998
ann_vol: 0.0718
hit_rate: 0.4891
rolling_sharpe_min: -0.875
rolling_sharpe_max: 2.243
redundancy_cluster: 1
negated_best_sharpe: 0.79
negated_best_template: rank_neg_delta
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: 0.06
---
# fnd6_newa1v1300_ao (fundamental6)

*Assets - Other*

## Signal Profile
- `rank(fnd6_newa1v1300_ao)`: S=0.50, F=0.32, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_ao / close)`: S=0.73, F=0.47, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_ao, 5))`: S=-0.03, F=0.00, T=36.9%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_ao)`: S=-0.30, F=-0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ao, 5))`: S=0.79, F=0.33, T=37.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_ao, 22)`: S=0.09, F=0.02, T=30.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_ao, 10)`: S=0.16, F=0.05, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_ao, 22))`: S=-0.11, F=-0.02, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ao)`: S=-0.50, F=-0.32, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ao / close)`: S=-0.73, F=-0.47, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.73, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.20 (negative), ret=-0.8%
  - 2020: S=-0.15 (negative), ret=-1.2%
  - 2021: S=1.07 (moderate), ret=+10.5%
  - 2022: S=1.69 (strong), ret=+12.8%
  - 2023: S=1.03 (moderate), ret=+4.4%

## Risk & Drawdown
- Max drawdown: 9.98% over 291 days (recovered)
- Annualized: return +5.2%, volatility 7.2% (fraction of booksize)
- Hit rate: 48.9% positive days
- Tail shape: skew +0.42, excess kurtosis +3.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.88, max 2.24, latest 0.98

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.44%; worst month: -3.07%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.65
- Sideways: S=0.85
- Bear: S=-1.78

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_ao, 5))` S=0.79, F=0.33, INFERIOR
Direction gap: +0.06 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_ao)`: S=-0.50, F=-0.32, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ao / close)`: S=-0.73, F=-0.47, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ao, 5))`: S=0.79, F=0.33, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_ao / close)` | TOP3000 | 0.73 | 0.47 | 10.0% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ao / close)` | TOP1000 | 0.53 | 0.35 | 15.9% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ao)` | TOP3000 | 0.49 | 0.32 | 29.5% | 80% | bull-only |
| `rank(fnd6_newa1v1300_ao / close)` | TOP500 | 0.33 | 0.19 | 30.8% | 80% | bull-only |
| `rank(fnd6_newa1v1300_ao)` | TOP1000 | 0.29 | 0.16 | 35.0% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ao)` | TOP500 | 0.10 | 0.04 | 50.1% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ao / close)` | TOP200 | 0.08 | 0.02 | 45.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_aox: 0.994 (strongly positively correlated)
- fnd6_aodo: 0.993 (strongly positively correlated)
- fnd6_newqv1300_altoq: 0.987 (strongly positively correlated)
- fnd6_newqv1300_aoq: 0.963 (strongly positively correlated)
- fnd6_mfma2_revt: 0.954 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
