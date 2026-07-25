---
field: fnd6_newa1v1300_at
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.84
best_fitness: 0.66
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0935
ann_vol: 0.0829
hit_rate: 0.4866
rolling_sharpe_min: -0.937
rolling_sharpe_max: 2.422
redundancy_cluster: 1
negated_best_sharpe: 0.83
negated_best_template: rank_neg_delta
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: -0.01
---
# fnd6_newa1v1300_at (fundamental6)

*Assets - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_at)`: S=0.62, F=0.46, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_at / close)`: S=0.76, F=0.54, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_at, 5))`: S=-0.31, F=-0.10, T=34.5%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_at)`: S=-0.30, F=-0.17, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_at, 5))`: S=0.83, F=0.40, T=35.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_at, 63)`: S=0.84, F=0.66, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_at, 10)`: S=0.18, F=0.06, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_at, 22))`: S=-0.05, F=-0.01, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_at)`: S=-0.62, F=-0.46, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_at / close)`: S=-0.76, F=-0.54, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.75, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.10 (negative), ret=-0.5%
  - 2020: S=0.34 (weak), ret=+3.3%
  - 2021: S=1.39 (moderate), ret=+14.4%
  - 2022: S=1.18 (moderate), ret=+9.2%
  - 2023: S=0.68 (moderate), ret=+4.2%

## Risk & Drawdown
- Max drawdown: 9.35% over 237 days (recovered)
- Annualized: return +6.2%, volatility 8.3% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.67, excess kurtosis +3.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.94, max 2.42, latest 0.79

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.28%; worst month: -3.46%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.51
- Sideways: S=0.27
- Bear: S=-0.94

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_at, 5))` S=0.83, F=0.40, INFERIOR
Direction gap: -0.01 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_at)`: S=-0.62, F=-0.46, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_at / close)`: S=-0.76, F=-0.54, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_at, 5))`: S=0.83, F=0.40, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_at / close)` | TOP3000 | 0.75 | 0.54 | 9.3% | 80% | bull-only |
| `rank(fnd6_newa1v1300_at)` | TOP3000 | 0.61 | 0.46 | 31.4% | 80% | bull-only |
| `rank(fnd6_newa1v1300_at / close)` | TOP1000 | 0.50 | 0.32 | 14.4% | 60% | bull-only |
| `rank(fnd6_newa1v1300_at / close)` | TOP500 | 0.34 | 0.20 | 24.2% | 60% | bull-only |
| `rank(fnd6_newa1v1300_at)` | TOP1000 | 0.29 | 0.17 | 34.8% | 60% | bull-only |
| `rank(fnd6_newa1v1300_at)` | TOP500 | 0.10 | 0.04 | 49.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_lse: 1.000 (strongly positively correlated)
- fnd6_mfma1_at: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_icapt: 0.995 (strongly positively correlated)
- fnd6_cptmfmq_atq: 0.990 (strongly positively correlated)
- fnd6_cptnewqv1300_atq: 0.989 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
