---
field: fnd6_intan
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.97
best_fitness: 0.85
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1336
ann_vol: 0.0789
hit_rate: 0.4955
rolling_sharpe_min: -1.273
rolling_sharpe_max: 2.371
redundancy_cluster: 1
negated_best_sharpe: 0.63
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: -0.34
---
# fnd6_intan (fundamental6)

*Intangible Assets - Total*

## Signal Profile
- `rank(fnd6_intan)`: S=0.37, F=0.21, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_intan / close)`: S=0.54, F=0.32, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_intan, 5))`: S=0.26, F=0.08, T=34.7%, INFERIOR (TOP1000)
- `-rank(fnd6_intan)`: S=-0.14, F=-0.05, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_intan, 5))`: S=0.63, F=0.26, T=35.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_intan, 63)`: S=0.97, F=0.85, T=18.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_intan, 10)`: S=0.02, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_intan, 22))`: S=0.31, F=0.12, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_intan)`: S=-0.37, F=-0.21, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_intan / close)`: S=-0.54, F=-0.32, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.54, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.29 (weak), ret=+1.1%
  - 2020: S=-0.47 (negative), ret=-3.5%
  - 2021: S=1.19 (moderate), ret=+13.2%
  - 2022: S=1.19 (moderate), ret=+11.3%
  - 2023: S=-0.31 (negative), ret=-1.3%

## Risk & Drawdown
- Max drawdown: 13.36% over 332 days (recovered)
- Annualized: return +4.2%, volatility 7.9% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.20, excess kurtosis +2.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.27, max 2.37, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.44%; worst month: -4.05%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.03
- Sideways: S=0.45
- Bear: S=-2.75

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_intan, 5))` S=0.63, F=0.26, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_intan)`: S=-0.37, F=-0.21, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_intan / close)`: S=-0.54, F=-0.32, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_intan, 5))`: S=0.63, F=0.26, T=35.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_intan / close)` | TOP3000 | 0.54 | 0.32 | 13.4% | 60% | bull-only |
| `rank(fnd6_intan)` | TOP3000 | 0.36 | 0.21 | 28.7% | 60% | bull-only |
| `rank(fnd6_intan / close)` | TOP1000 | 0.32 | 0.16 | 15.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_intan, 5))` | TOP1000 | 0.25 | 0.08 | 18.6% | 40% | mixed |
| `rank(fnd6_intan)` | TOP1000 | 0.13 | 0.05 | 31.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_intano: 0.988 (strongly positively correlated)
- fnd6_newqv1300_intanq: 0.988 (strongly positively correlated)
- fnd6_am: 0.976 (strongly positively correlated)
- goodwill: 0.969 (strongly positively correlated)
- fnd6_newqv1300_gdwlq: 0.969 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
