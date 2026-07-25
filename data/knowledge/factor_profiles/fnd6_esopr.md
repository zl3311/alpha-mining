---
field: fnd6_esopr
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.53
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.7522
ann_vol: 0.3343
hit_rate: 0.5109
rolling_sharpe_min: -2.386
rolling_sharpe_max: 3.525
redundancy_cluster: 96
negated_best_sharpe: 0.09
negated_best_template: neg_rank
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.44
---
# fnd6_esopr (fundamental6)

*Preferred ESOP Obligation - Redeemable*

## Signal Profile
- `rank(fnd6_esopr)`: S=0.53, F=0.63, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_esopr / close)`: S=0.53, F=0.63, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_esopr, 5))`: S=0.48, F=0.31, T=3.2%, INFERIOR (TOP500)
- `-rank(fnd6_esopr)`: S=0.09, F=0.03, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_esopr, 5))`: S=-0.09, F=-0.03, T=2.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_esopr, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_esopr, 10)`: S=-0.21, F=-0.20, T=0.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_esopr, 22))`: S=-0.10, F=-0.03, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_esopr)`: S=-0.10, F=-0.03, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_esopr / close)`: S=-0.10, F=-0.03, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 3F/23P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.54, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.27 (moderate), ret=+41.0%
  - 2020: S=2.29 (strong), ret=+92.3%
  - 2021: S=0.18 (weak), ret=+8.0%
  - 2022: S=-2.25 (negative), ret=-57.2%
  - 2023: S=0.85 (moderate), ret=+4.9%

## Risk & Drawdown
- Max drawdown: 75.22% over 1170 days (not yet recovered, ongoing at window end)
- Annualized: return +18.2%, volatility 33.4% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.46, excess kurtosis +10.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.39, max 3.52, latest 1.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +26.30%; worst month: -20.36%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.47
- Sideways: S=0.23
- Bear: S=1.77

## Negated Direction
Best negated: `-rank(fnd6_esopr)` S=0.09, F=0.03, INFERIOR
Direction gap: -0.44 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_esopr)`: S=-0.10, F=-0.03, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_esopr / close)`: S=-0.10, F=-0.03, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_esopr, 5))`: S=-0.09, F=-0.03, T=2.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_esopr / close)` | TOP3000 | 0.54 | 0.63 | 75.2% | 80% | mixed |
| `rank(fnd6_esopr)` | TOP3000 | 0.54 | 0.63 | 75.4% | 80% | mixed |
| `rank(ts_delta(fnd6_esopr, 5))` | TOP500 | 0.45 | 0.31 | 32.6% | 60% | bull-only |
| `rank(fnd6_esopr / close)` | TOP500 | 0.45 | 0.31 | 32.3% | 60% | bull-only |
| `rank(fnd6_esopr)` | TOP500 | 0.45 | 0.31 | 32.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_esopr, 5))` | TOP3000 | 0.19 | 0.09 | 46.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_esoprq: 0.996 (strongly positively correlated)
- anl4_afv4_cfps_high: -0.287 (weakly negatively correlated)
- anl4_afv4_cfps_mean: -0.283 (weakly negatively correlated)
- fn_accum_depr_depletion_and_amortization_ppne_q: -0.282 (weakly negatively correlated)
- anl4_afv4_cfps_median: -0.282 (weakly negatively correlated)

Redundancy cluster #96: 2 similar fields, mean |rho| 0.996 (representative: fnd6_newqv1300_esoprq). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
