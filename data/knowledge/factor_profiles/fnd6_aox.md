---
field: fnd6_aox
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.68
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1006
ann_vol: 0.0719
hit_rate: 0.4842
rolling_sharpe_min: -0.91
rolling_sharpe_max: 2.286
redundancy_cluster: 1
negated_best_sharpe: 0.64
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.04
---
# fnd6_aox (fundamental6)

*Assets - Other - Sundry*

## Signal Profile
- `rank(fnd6_aox)`: S=0.47, F=0.29, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_aox / close)`: S=0.68, F=0.42, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_aox, 5))`: S=-0.41, F=-0.19, T=37.3%, INFERIOR (TOP200)
- `-rank(fnd6_aox)`: S=-0.29, F=-0.15, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_aox, 5))`: S=0.64, F=0.25, T=37.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_aox, 22)`: S=-0.34, F=-0.15, T=30.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_aox, 10)`: S=0.05, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_aox, 22))`: S=-0.20, F=-0.06, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aox)`: S=-0.47, F=-0.29, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aox / close)`: S=-0.68, F=-0.42, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.67, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.23 (negative), ret=-1.0%
  - 2020: S=-0.22 (negative), ret=-1.7%
  - 2021: S=1.15 (moderate), ret=+11.2%
  - 2022: S=1.50 (strong), ret=+11.7%
  - 2023: S=0.80 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 10.06% over 291 days (recovered)
- Annualized: return +4.8%, volatility 7.2% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew +0.41, excess kurtosis +3.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.91, max 2.29, latest 0.73

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.26%; worst month: -3.16%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.67
- Sideways: S=0.76
- Bear: S=-1.98

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_aox, 5))` S=0.64, F=0.25, INFERIOR
Direction gap: -0.04 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_aox)`: S=-0.47, F=-0.29, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aox / close)`: S=-0.68, F=-0.42, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_aox, 5))`: S=0.64, F=0.25, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_aox / close)` | TOP3000 | 0.67 | 0.42 | 10.1% | 60% | bull-only |
| `rank(fnd6_aox / close)` | TOP1000 | 0.52 | 0.34 | 15.0% | 80% | bull-only |
| `rank(fnd6_aox)` | TOP3000 | 0.47 | 0.29 | 29.1% | 80% | bull-only |
| `rank(fnd6_aox / close)` | TOP500 | 0.34 | 0.19 | 26.8% | 80% | bull-only |
| `rank(fnd6_aox)` | TOP1000 | 0.28 | 0.15 | 32.9% | 60% | bull-only |
| `rank(fnd6_aox)` | TOP500 | 0.15 | 0.06 | 44.1% | 60% | bull-only |
| `rank(fnd6_aox / close)` | TOP200 | 0.12 | 0.05 | 40.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_aodo: 0.998 (strongly positively correlated)
- fnd6_newa1v1300_ao: 0.994 (strongly positively correlated)
- fnd6_newqv1300_altoq: 0.984 (strongly positively correlated)
- fnd6_newqv1300_aoq: 0.961 (strongly positively correlated)
- fnd6_mfma2_revt: 0.955 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
