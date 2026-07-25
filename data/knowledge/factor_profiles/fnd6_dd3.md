---
field: fnd6_dd3
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.1
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0636
ann_vol: 0.0611
hit_rate: 0.5263
rolling_sharpe_min: -0.418
rolling_sharpe_max: 2.953
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.39
n_negated_sims: 10
direction_gap: -0.52
---
# fnd6_dd3 (fundamental6)

*Debt Due in 3rd Year*

## Signal Profile
- `rank(fnd6_dd3)`: S=0.78, F=0.52, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_dd3 / close)`: S=1.10, F=0.80, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dd3, 5))`: S=-0.04, F=-0.01, T=42.5%, INFERIOR (TOP3000)
- `-rank(fnd6_dd3)`: S=-0.26, F=-0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd3, 5))`: S=0.58, F=0.39, T=24.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dd3, 63)`: S=0.54, F=0.38, T=16.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dd3, 10)`: S=0.31, F=0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dd3, 22))`: S=-0.52, F=-0.28, T=19.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd3)`: S=0.15, F=0.06, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd3 / close)`: S=0.05, F=0.01, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.09, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.08 (moderate), ret=+3.3%
  - 2020: S=0.39 (weak), ret=+2.3%
  - 2021: S=1.36 (moderate), ret=+10.7%
  - 2022: S=1.77 (strong), ret=+13.6%
  - 2023: S=0.71 (moderate), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 6.36% over 157 days (recovered)
- Annualized: return +6.7%, volatility 6.1% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew -0.02, excess kurtosis +2.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.42, max 2.95, latest 0.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.63%; worst month: -2.24%
Positive months: 66%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.77
- Sideways: S=1.57
- Bear: S=-1.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dd3, 5))` S=0.58, F=0.39, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dd3)`: S=0.15, F=0.06, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd3 / close)`: S=0.05, F=0.01, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd3, 5))`: S=0.58, F=0.39, T=24.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dd3 / close)` | TOP3000 | 1.09 | 0.80 | 6.4% | 100% | bull-only |
| `rank(fnd6_dd3)` | TOP3000 | 0.77 | 0.52 | 12.8% | 80% | bull-only |
| `rank(fnd6_dd3 / close)` | TOP1000 | 0.36 | 0.18 | 10.0% | 40% | bull-only |
| `rank(fnd6_dd3)` | TOP1000 | 0.24 | 0.11 | 17.8% | 40% | bull-only |
| `rank(fnd6_dd3 / close)` | TOP500 | 0.12 | 0.04 | 15.3% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dxd3: 0.983 (strongly positively correlated)
- fnd6_dd2: 0.941 (strongly positively correlated)
- fnd6_dd4: 0.933 (strongly positively correlated)
- fnd6_dxd2: 0.914 (strongly positively correlated)
- fnd6_dd5: 0.912 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.46 | 1.86 | +0.77 | -0.84 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.26 | 2.24 | +0.62 | -0.70 | yes |
| anl4_epsr_flag | analyst4 | -0.25 | 1.79 | +0.61 | -0.65 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.31 | 1.67 | +0.58 | -0.85 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.26 | 2.62 | +0.60 | -0.54 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
