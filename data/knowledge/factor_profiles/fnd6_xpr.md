---
field: fnd6_xpr
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.66
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0889
ann_vol: 0.0677
hit_rate: 0.4842
rolling_sharpe_min: -1.384
rolling_sharpe_max: 2.11
redundancy_cluster: 1
negated_best_sharpe: 0.42
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.24
---
# fnd6_xpr (fundamental6)

*Pension and Retirement Expense*

## Signal Profile
- `rank(fnd6_xpr)`: S=0.36, F=0.18, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_xpr / close)`: S=0.66, F=0.39, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_xpr, 5))`: S=0.54, F=0.27, T=39.3%, INFERIOR (TOP1000)
- `-rank(fnd6_xpr)`: S=0.02, F=0.00, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xpr, 5))`: S=0.42, F=0.25, T=24.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_xpr, 22)`: S=0.06, F=0.01, T=22.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_xpr, 10)`: S=-0.16, F=-0.05, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_xpr, 22))`: S=0.39, F=0.17, T=20.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xpr)`: S=0.08, F=0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xpr / close)`: S=-0.06, F=-0.01, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.66, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.21 (negative), ret=-0.9%
  - 2020: S=0.16 (weak), ret=+1.2%
  - 2021: S=0.96 (moderate), ret=+8.3%
  - 2022: S=1.70 (strong), ret=+12.1%
  - 2023: S=0.29 (weak), ret=+1.1%

## Risk & Drawdown
- Max drawdown: 8.89% over 237 days (recovered)
- Annualized: return +4.5%, volatility 6.8% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew +0.51, excess kurtosis +3.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.38, max 2.11, latest 0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.79%; worst month: -2.95%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.62
- Sideways: S=0.19
- Bear: S=-1.43

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_xpr, 5))` S=0.42, F=0.25, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_xpr)`: S=0.08, F=0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xpr / close)`: S=-0.06, F=-0.01, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xpr, 5))`: S=0.42, F=0.25, T=24.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_xpr / close)` | TOP3000 | 0.66 | 0.39 | 8.9% | 80% | bull-only |
| `rank(ts_delta(fnd6_xpr, 5))` | TOP1000 | 0.54 | 0.27 | 18.7% | 80% | mixed |
| `rank(ts_delta(fnd6_xpr, 5))` | TOP3000 | 0.52 | 0.23 | 30.9% | 80% | mixed |
| `rank(fnd6_xpr)` | TOP3000 | 0.35 | 0.18 | 27.8% | 60% | bull-only |
| `rank(fnd6_xpr / close)` | TOP1000 | 0.20 | 0.08 | 13.1% | 40% | bull-only |
| `rank(fnd6_xpr / close)` | TOP500 | 0.14 | 0.05 | 20.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfma1_dp: 0.940 (strongly positively correlated)
- fnd6_newa1v1300_dp: 0.940 (strongly positively correlated)
- fn_ppne_gross_a: 0.936 (strongly positively correlated)
- fnd6_mfma2_revt: 0.936 (strongly positively correlated)
- fnd6_newa2v1300_sale: 0.936 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
