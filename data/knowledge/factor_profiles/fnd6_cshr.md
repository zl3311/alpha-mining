---
field: fnd6_cshr
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.89
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1463
ann_vol: 0.0638
hit_rate: 0.4972
rolling_sharpe_min: -2.508
rolling_sharpe_max: 2.91
redundancy_cluster: 13
negated_best_sharpe: 0.89
negated_best_template: rank_neg_delta
negated_best_fitness: 0.53
n_negated_sims: 10
direction_gap: 0.37
---
# fnd6_cshr (fundamental6)

*Common/Ordinary Shareholders*

## Signal Profile
- `rank(fnd6_cshr)`: S=0.52, F=0.27, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_cshr / close)`: S=0.50, F=0.22, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cshr, 5))`: S=-0.56, F=-0.35, T=24.8%, INFERIOR (TOP200)
- `-rank(fnd6_cshr)`: S=-0.15, F=-0.05, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cshr, 5))`: S=0.89, F=0.53, T=42.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cshr, 63)`: S=0.39, F=0.24, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cshr, 10)`: S=-0.58, F=-0.52, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cshr, 22))`: S=-0.82, F=-0.55, T=20.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cshr)`: S=-0.52, F=-0.27, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cshr / close)`: S=-0.50, F=-0.22, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.51, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.48 (negative), ret=-1.6%
  - 2020: S=-2.00 (negative), ret=-9.1%
  - 2021: S=1.88 (strong), ret=+13.6%
  - 2022: S=1.40 (moderate), ret=+12.8%
  - 2023: S=0.04 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 14.63% over 781 days (recovered)
- Annualized: return +3.2%, volatility 6.4% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew +0.02, excess kurtosis +1.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.51, max 2.91, latest -0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.73%; worst month: -3.06%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.03
- Sideways: S=0.35
- Bear: S=-2.87

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cshr, 5))` S=0.89, F=0.53, INFERIOR
Direction gap: +0.37 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cshr)`: S=-0.52, F=-0.27, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cshr / close)`: S=-0.50, F=-0.22, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cshr, 5))`: S=0.89, F=0.53, T=42.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cshr)` | TOP3000 | 0.51 | 0.27 | 14.6% | 60% | bull-only |
| `rank(fnd6_cshr / close)` | TOP3000 | 0.48 | 0.22 | 10.3% | 60% | mixed |
| `rank(fnd6_cshr / close)` | TOP1000 | 0.33 | 0.14 | 10.4% | 40% | bull-only |
| `rank(fnd6_cshr)` | TOP1000 | 0.13 | 0.05 | 19.2% | 40% | bull-only |
| `rank(fnd6_cshr / close)` | TOP500 | 0.08 | 0.02 | 14.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_fatb: 0.901 (strongly positively correlated)
- operating_profit_before_interest_tax: 0.896 (strongly positively correlated)
- cash_flow_from_operations: 0.896 (strongly positively correlated)
- anl4_ptp_low: 0.895 (strongly positively correlated)
- pretax_income_total: 0.895 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
