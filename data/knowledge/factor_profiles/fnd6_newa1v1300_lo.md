---
field: fnd6_newa1v1300_lo
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.86
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0978
ann_vol: 0.0702
hit_rate: 0.485
rolling_sharpe_min: -1.416
rolling_sharpe_max: 2.63
redundancy_cluster: 1
negated_best_sharpe: 0.86
negated_best_template: rank_neg_delta
negated_best_fitness: 0.56
n_negated_sims: 10
direction_gap: 0.14
---
# fnd6_newa1v1300_lo (fundamental6)

*Liabilities - Other - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_lo)`: S=0.57, F=0.38, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_lo / close)`: S=0.72, F=0.46, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_lo, 5))`: S=0.50, F=0.17, T=36.6%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_lo)`: S=-0.35, F=-0.21, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_lo, 5))`: S=0.86, F=0.56, T=36.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_lo, 63)`: S=0.32, F=0.15, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_lo, 10)`: S=0.29, F=0.12, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_lo, 22))`: S=0.03, F=0.00, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_lo)`: S=0.22, F=0.12, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_lo / close)`: S=0.18, F=0.08, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.70, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.08 (negative), ret=-0.3%
  - 2020: S=0.14 (weak), ret=+1.1%
  - 2021: S=1.53 (strong), ret=+15.0%
  - 2022: S=0.90 (moderate), ret=+6.4%
  - 2023: S=0.56 (moderate), ret=+2.1%

## Risk & Drawdown
- Max drawdown: 9.78% over 94 days (recovered)
- Annualized: return +5.0%, volatility 7.0% (fraction of booksize)
- Hit rate: 48.5% positive days
- Tail shape: skew +0.52, excess kurtosis +4.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.42, max 2.63, latest 0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.75%; worst month: -4.22%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.93
- Sideways: S=0.44
- Bear: S=-1.92

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_lo, 5))` S=0.86, F=0.56, INFERIOR
Direction gap: +0.14 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_lo)`: S=0.22, F=0.12, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_lo / close)`: S=0.18, F=0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_lo, 5))`: S=0.86, F=0.56, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_lo / close)` | TOP3000 | 0.70 | 0.46 | 9.8% | 80% | bull-only |
| `rank(fnd6_newa1v1300_lo)` | TOP3000 | 0.56 | 0.38 | 26.2% | 80% | bull-only |
| `rank(fnd6_newa1v1300_lo / close)` | TOP1000 | 0.52 | 0.35 | 13.0% | 60% | bull-only |
| `rank(fnd6_newa1v1300_lo)` | TOP1000 | 0.34 | 0.21 | 31.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_lo, 5))` | TOP3000 | 0.50 | 0.17 | 15.6% | 60% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_lo, 5))` | TOP1000 | 0.29 | 0.09 | 28.0% | 80% | mixed |
| `rank(fnd6_newa1v1300_lo / close)` | TOP500 | 0.14 | 0.06 | 30.2% | 40% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_lo, 5))` | TOP500 | 0.16 | 0.04 | 34.4% | 60% | mixed |
| `rank(fnd6_newa1v1300_lo)` | TOP500 | 0.06 | 0.02 | 46.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_loq: 0.987 (strongly positively correlated)
- fnd6_newqv1300_loxdrq: 0.964 (strongly positively correlated)
- fnd6_newa1v1300_ao: 0.949 (strongly positively correlated)
- fnd6_aodo: 0.949 (strongly positively correlated)
- fnd6_aox: 0.949 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
