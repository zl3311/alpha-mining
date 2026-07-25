---
field: fnd6_txtubend
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.91
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0836
ann_vol: 0.067
hit_rate: 0.5012
rolling_sharpe_min: -1.038
rolling_sharpe_max: 3.062
top_merge_partner: net_profit_adjusted_min_guidance
redundancy_cluster: 1
negated_best_sharpe: 0.93
negated_best_template: rank_neg_delta
negated_best_fitness: 0.55
n_negated_sims: 10
direction_gap: 0.02
---
# fnd6_txtubend (fundamental6)

*Unrecog. Tax Benefits - End of Year*

## Signal Profile
- `rank(fnd6_txtubend)`: S=0.63, F=0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_txtubend / close)`: S=0.91, F=0.63, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txtubend, 5))`: S=0.36, F=0.16, T=32.4%, INFERIOR (TOP500)
- `-rank(fnd6_txtubend)`: S=-0.20, F=-0.08, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubend, 5))`: S=0.93, F=0.55, T=42.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txtubend, 63)`: S=0.33, F=0.18, T=19.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txtubend, 10)`: S=0.28, F=0.14, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txtubend, 22))`: S=0.02, F=0.00, T=21.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubend)`: S=-0.63, F=-0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubend / close)`: S=-0.91, F=-0.63, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.91, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.12 (weak), ret=+0.5%
  - 2020: S=0.31 (weak), ret=+1.7%
  - 2021: S=1.93 (strong), ret=+18.0%
  - 2022: S=1.25 (moderate), ret=+10.1%
  - 2023: S=-0.15 (negative), ret=-0.6%

## Risk & Drawdown
- Max drawdown: 8.36% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +6.1%, volatility 6.7% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.24, excess kurtosis +3.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.04, max 3.06, latest -0.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +7.59%; worst month: -3.00%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.15
- Sideways: S=0.50
- Bear: S=-1.77

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txtubend, 5))` S=0.93, F=0.55, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txtubend)`: S=-0.63, F=-0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubend / close)`: S=-0.91, F=-0.63, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubend, 5))`: S=0.93, F=0.55, T=42.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txtubend / close)` | TOP3000 | 0.91 | 0.63 | 8.4% | 80% | bull-only |
| `rank(fnd6_txtubend)` | TOP3000 | 0.62 | 0.42 | 20.8% | 60% | bull-only |
| `rank(fnd6_txtubend / close)` | TOP1000 | 0.36 | 0.19 | 12.6% | 40% | bull-only |
| `rank(ts_delta(fnd6_txtubend, 5))` | TOP500 | 0.36 | 0.16 | 33.8% | 80% | mixed |
| `rank(fnd6_txtubend / close)` | TOP500 | 0.29 | 0.15 | 27.1% | 40% | bull-only |
| `rank(fnd6_txtubend)` | TOP1000 | 0.19 | 0.08 | 28.1% | 40% | bull-only |
| `rank(fnd6_txtubend / close)` | TOP200 | 0.11 | 0.04 | 33.2% | 80% | bull-only |
| `rank(ts_delta(fnd6_txtubend, 5))` | TOP1000 | 0.10 | 0.02 | 21.3% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_txtubbegin: 0.985 (strongly positively correlated)
- fn_unrecognized_tax_benefits_a: 0.944 (strongly positively correlated)
- fnd6_txtubtxtr: 0.897 (strongly positively correlated)
- fnd6_txtubposinc: 0.888 (strongly positively correlated)
- fnd6_txndba: 0.883 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| net_profit_adjusted_min_guidance | analyst4 | -0.28 | 1.53 | +0.58 | -0.70 | yes |
| anl4_rd_exp_flag | analyst4 | -0.36 | 1.65 | +0.63 | -0.27 | yes |
| rp_ess_revenue | news18 | -0.29 | 1.45 | +0.55 | -0.75 | yes |
| anl4_epsr_flag | analyst4 | -0.26 | 1.71 | +0.53 | -0.87 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.27 | 2.15 | +0.52 | -0.57 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
