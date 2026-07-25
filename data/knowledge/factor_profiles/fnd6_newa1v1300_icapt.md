---
field: fnd6_newa1v1300_icapt
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.72
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0857
ann_vol: 0.082
hit_rate: 0.4794
rolling_sharpe_min: -0.967
rolling_sharpe_max: 2.434
redundancy_cluster: 1
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.14
---
# fnd6_newa1v1300_icapt (fundamental6)

*Invested Capital - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_icapt)`: S=0.61, F=0.45, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_icapt / close)`: S=0.72, F=0.50, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_icapt, 5))`: S=-0.37, F=-0.17, T=34.4%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_icapt)`: S=-0.24, F=-0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_icapt, 5))`: S=0.58, F=0.29, T=33.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_icapt, 63)`: S=0.49, F=0.27, T=19.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_icapt, 10)`: S=0.11, F=0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_icapt, 22))`: S=-0.16, F=-0.05, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_icapt)`: S=-0.02, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_icapt / close)`: S=-0.27, F=-0.13, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.72, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.00 (weak), ret=+0.0%
  - 2020: S=0.28 (weak), ret=+2.7%
  - 2021: S=1.33 (moderate), ret=+13.9%
  - 2022: S=1.03 (moderate), ret=+7.7%
  - 2023: S=0.75 (moderate), ret=+4.6%

## Risk & Drawdown
- Max drawdown: 8.57% over 577 days (not yet recovered, ongoing at window end)
- Annualized: return +5.9%, volatility 8.2% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.68, excess kurtosis +3.73

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.97, max 2.43, latest 0.87

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.81%; worst month: -3.42%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.40
- Sideways: S=0.25
- Bear: S=-0.90

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_icapt, 5))` S=0.58, F=0.29, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_icapt)`: S=-0.02, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_icapt / close)`: S=-0.27, F=-0.13, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_icapt, 5))`: S=0.58, F=0.29, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_icapt / close)` | TOP3000 | 0.72 | 0.50 | 8.6% | 100% | bull-only |
| `rank(fnd6_newa1v1300_icapt)` | TOP3000 | 0.61 | 0.45 | 31.0% | 80% | bull-only |
| `rank(fnd6_newa1v1300_icapt / close)` | TOP1000 | 0.46 | 0.29 | 13.4% | 60% | bull-only |
| `rank(fnd6_newa1v1300_icapt / close)` | TOP500 | 0.26 | 0.13 | 25.9% | 60% | bull-only |
| `rank(fnd6_newa1v1300_icapt)` | TOP1000 | 0.23 | 0.12 | 35.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_at: 0.995 (strongly positively correlated)
- fnd6_newa1v1300_lse: 0.995 (strongly positively correlated)
- fnd6_mfma1_at: 0.994 (strongly positively correlated)
- fnd6_cptmfmq_atq: 0.985 (strongly positively correlated)
- fnd6_cptnewqv1300_atq: 0.985 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
