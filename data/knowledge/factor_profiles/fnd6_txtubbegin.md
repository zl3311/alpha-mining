---
field: fnd6_txtubbegin
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.95
best_fitness: 0.7
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0906
ann_vol: 0.0706
hit_rate: 0.5053
rolling_sharpe_min: -0.75
rolling_sharpe_max: 3.1
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.18
negated_best_template: neg_rank_level
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.77
---
# fnd6_txtubbegin (fundamental6)

*Unrecog. Tax Benefits - Beg of Year*

## Signal Profile
- `rank(fnd6_txtubbegin)`: S=0.66, F=0.46, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_txtubbegin / close)`: S=0.95, F=0.70, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txtubbegin, 5))`: S=0.42, F=0.20, T=32.9%, INFERIOR (TOP500)
- `-rank(fnd6_txtubbegin)`: S=-0.17, F=-0.07, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubbegin, 5))`: S=0.19, F=0.07, T=23.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txtubbegin, 63)`: S=0.16, F=0.06, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txtubbegin, 10)`: S=0.19, F=0.08, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txtubbegin, 22))`: S=0.21, F=0.07, T=21.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubbegin)`: S=0.18, F=0.08, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubbegin / close)`: S=0.09, F=0.03, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.95, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.06 (weak), ret=+0.2%
  - 2020: S=0.06 (weak), ret=+0.3%
  - 2021: S=1.98 (strong), ret=+19.2%
  - 2022: S=1.50 (strong), ret=+13.5%
  - 2023: S=-0.10 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 9.06% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +6.7%, volatility 7.1% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.22, excess kurtosis +2.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.75, max 3.10, latest -0.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +7.85%; worst month: -3.14%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.26
- Sideways: S=0.43
- Bear: S=-1.78

## Negated Direction
Best negated: `rank(-1 * fnd6_txtubbegin)` S=0.18, F=0.08, INFERIOR
Direction gap: -0.77 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_txtubbegin)`: S=0.18, F=0.08, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubbegin / close)`: S=0.09, F=0.03, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubbegin, 5))`: S=0.19, F=0.07, T=23.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txtubbegin / close)` | TOP3000 | 0.95 | 0.70 | 9.1% | 80% | bull-only |
| `rank(fnd6_txtubbegin)` | TOP3000 | 0.65 | 0.46 | 21.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_txtubbegin, 5))` | TOP500 | 0.41 | 0.20 | 37.8% | 60% | mixed |
| `rank(ts_delta(fnd6_txtubbegin, 5))` | TOP1000 | 0.40 | 0.15 | 49.6% | 80% | mixed |
| `rank(fnd6_txtubbegin / close)` | TOP1000 | 0.29 | 0.14 | 14.9% | 40% | bull-only |
| `rank(fnd6_txtubbegin / close)` | TOP500 | 0.23 | 0.11 | 25.3% | 40% | bull-only |
| `rank(fnd6_txtubbegin)` | TOP1000 | 0.16 | 0.07 | 29.1% | 40% | bull-only |
| `rank(ts_delta(fnd6_txtubbegin, 5))` | TOP3000 | 0.18 | 0.05 | 56.1% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_txtubend: 0.985 (strongly positively correlated)
- fn_unrecognized_tax_benefits_a: 0.927 (strongly positively correlated)
- fnd6_txtubtxtr: 0.923 (strongly positively correlated)
- fnd6_intan: 0.891 (strongly positively correlated)
- fnd6_txtubpospinc: 0.884 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.40 | 1.74 | +0.72 | -0.40 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.29 | 1.58 | +0.63 | -0.77 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.29 | 2.21 | +0.58 | -0.57 | yes |
| rp_ess_revenue | news18 | -0.29 | 1.49 | +0.55 | -0.79 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.22 | 1.53 | +0.54 | -0.91 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
