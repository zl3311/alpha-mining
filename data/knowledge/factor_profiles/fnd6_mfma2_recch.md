---
field: fnd6_mfma2_recch
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.95
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.2238
ann_vol: 0.1195
hit_rate: 0.5142
rolling_sharpe_min: -1.151
rolling_sharpe_max: 2.958
top_merge_partner: implied_volatility_call_10
negated_best_sharpe: 0.38
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.57
---
# fnd6_mfma2_recch (fundamental6)

*Accounts Receivable - Decrease (Increase)*

## Signal Profile
- `rank(fnd6_mfma2_recch)`: S=0.01, F=0.00, T=2.6%, INFERIOR (TOP200)
- `rank(fnd6_mfma2_recch / close)`: S=0.10, F=0.02, T=2.3%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_mfma2_recch, 5))`: S=0.95, F=0.53, T=35.7%, INFERIOR (TOP3000)
- `-rank(fnd6_mfma2_recch)`: S=0.08, F=0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma2_recch, 5))`: S=-0.55, F=-0.30, T=34.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_mfma2_recch, 22)`: S=0.26, F=0.12, T=25.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfma2_recch, 10)`: S=0.04, F=0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfma2_recch, 22))`: S=0.47, F=0.24, T=16.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_recch)`: S=0.04, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_recch / close)`: S=0.38, F=0.14, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.97, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.02 (negative), ret=-0.3%
  - 2020: S=0.22 (weak), ret=+2.7%
  - 2021: S=2.94 (strong), ret=+37.4%
  - 2022: S=0.48 (weak), ret=+5.6%
  - 2023: S=1.02 (moderate), ret=+11.4%

## Risk & Drawdown
- Max drawdown: 22.38% over 625 days (recovered)
- Annualized: return +11.6%, volatility 11.9% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.53, excess kurtosis +7.98

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 2.96, latest 1.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +15.27%; worst month: -7.95%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.51
- Sideways: S=1.14
- Bear: S=0.19

## Negated Direction
Best negated: `rank(-1 * fnd6_mfma2_recch / close)` S=0.38, F=0.14, INFERIOR
Direction gap: -0.57 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mfma2_recch)`: S=0.04, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_recch / close)`: S=0.38, F=0.14, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma2_recch, 5))`: S=-0.55, F=-0.30, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_mfma2_recch, 5))` | TOP3000 | 0.97 | 0.53 | 22.4% | 80% | mixed |
| `rank(ts_delta(fnd6_mfma2_recch, 5))` | TOP1000 | 0.83 | 0.49 | 21.9% | 80% | mixed |
| `rank(ts_delta(fnd6_mfma2_recch, 5))` | TOP500 | 0.67 | 0.40 | 35.3% | 100% | mixed |
| `rank(ts_delta(fnd6_mfma2_recch, 5))` | TOP200 | 0.51 | 0.32 | 34.4% | 80% | all-weather |
| `rank(fnd6_mfma2_recch / close)` | TOP1000 | 0.10 | 0.02 | 9.0% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_recch: 0.384 (weakly positively correlated)
- fnd6_cimii: -0.203 (weakly negatively correlated)
- fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q: 0.114 (weakly positively correlated)
- fnd6_prcc: 0.112 (weakly positively correlated)
- fnd6_prcl: 0.106 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_call_10 | option8 | +0.00 | 1.41 | +0.38 | -0.80 | yes |
| rp_css_ptg | news18 | -0.08 | 1.45 | +0.45 | +0.59 | yes |
| anl4_afv4_dts_spe | analyst4 | +0.03 | 1.36 | +0.36 | -0.79 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.01 | 1.34 | +0.38 | -0.62 | yes |
| systematic_risk_last_60_days | model51 | +0.00 | 1.30 | +0.33 | -0.99 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
