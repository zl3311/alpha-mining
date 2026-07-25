---
field: fnd6_dd5
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.16
best_fitness: 0.85
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0768
ann_vol: 0.0578
hit_rate: 0.5142
rolling_sharpe_min: -0.433
rolling_sharpe_max: 2.845
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.23
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.93
---
# fnd6_dd5 (fundamental6)

*Debt Due in 5th Year*

## Signal Profile
- `rank(fnd6_dd5)`: S=0.86, F=0.58, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_dd5 / close)`: S=1.16, F=0.85, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dd5, 5))`: S=0.79, F=0.45, T=42.1%, INFERIOR (TOP3000)
- `-rank(fnd6_dd5)`: S=-0.28, F=-0.12, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd5, 5))`: S=0.23, F=0.10, T=24.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dd5, 63)`: S=0.27, F=0.13, T=17.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dd5, 10)`: S=0.37, F=0.17, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dd5, 22))`: S=-0.42, F=-0.21, T=19.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd5)`: S=0.03, F=0.00, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd5 / close)`: S=0.07, F=0.02, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.15, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.18 (moderate), ret=+3.3%
  - 2020: S=0.46 (weak), ret=+2.7%
  - 2021: S=1.46 (moderate), ret=+11.2%
  - 2022: S=1.71 (strong), ret=+11.4%
  - 2023: S=1.01 (moderate), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 7.68% over 156 days (recovered)
- Annualized: return +6.6%, volatility 5.8% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.17, excess kurtosis +2.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.43, max 2.85, latest 0.90

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.22%; worst month: -3.11%
Positive months: 71%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.23
- Sideways: S=1.34
- Bear: S=-1.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dd5, 5))` S=0.23, F=0.10, INFERIOR
Direction gap: -0.93 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dd5)`: S=0.03, F=0.00, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd5 / close)`: S=0.07, F=0.02, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd5, 5))`: S=0.23, F=0.10, T=24.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dd5 / close)` | TOP3000 | 1.15 | 0.85 | 7.7% | 100% | bull-only |
| `rank(fnd6_dd5)` | TOP3000 | 0.85 | 0.58 | 12.0% | 80% | bull-only |
| `rank(ts_delta(fnd6_dd5, 5))` | TOP3000 | 0.78 | 0.45 | 25.2% | 60% | mixed |
| `rank(fnd6_dd5 / close)` | TOP500 | 0.42 | 0.24 | 15.2% | 40% | bull-only |
| `rank(ts_delta(fnd6_dd5, 5))` | TOP500 | 0.41 | 0.21 | 26.1% | 80% | mixed |
| `rank(fnd6_dd5 / close)` | TOP1000 | 0.38 | 0.19 | 8.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_dd5, 5))` | TOP1000 | 0.42 | 0.18 | 34.5% | 80% | mixed |
| `rank(fnd6_dd5)` | TOP500 | 0.31 | 0.15 | 18.8% | 40% | bull-only |
| `rank(fnd6_dd5)` | TOP1000 | 0.27 | 0.12 | 14.8% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dxd5: 0.981 (strongly positively correlated)
- fnd6_dd3: 0.912 (strongly positively correlated)
- fnd6_dd4: 0.911 (strongly positively correlated)
- fnd6_dd2: 0.891 (strongly positively correlated)
- fnd6_dn: 0.890 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.43 | 1.83 | +0.68 | -0.90 | yes |
| anl4_epsr_flag | analyst4 | -0.24 | 1.79 | +0.61 | -0.65 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.15 | 1.77 | +0.60 | -0.73 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.22 | 2.23 | +0.60 | -0.66 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.33 | 1.71 | +0.56 | -0.91 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
