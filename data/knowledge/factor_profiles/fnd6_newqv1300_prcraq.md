---
field: fnd6_newqv1300_prcraq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.1
best_fitness: 0.7
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0775
ann_vol: 0.0457
hit_rate: 0.5134
rolling_sharpe_min: -0.852
rolling_sharpe_max: 3.11
top_merge_partner: pv13_ompetitorgraphrank_hub_rank
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.51
---
# fnd6_newqv1300_prcraq (fundamental6)

*Repurchase Price - Average per share*

## Signal Profile
- `rank(fnd6_newqv1300_prcraq)`: S=0.24, F=0.09, T=6.1%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_prcraq / close)`: S=1.10, F=0.70, T=7.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_prcraq, 5))`: S=-0.27, F=-0.04, T=40.0%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_prcraq)`: S=-0.20, F=-0.06, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_prcraq, 5))`: S=0.59, F=0.21, T=41.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_prcraq, 63)`: S=0.29, F=0.07, T=20.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_prcraq, 10)`: S=0.42, F=0.21, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_prcraq, 22))`: S=-0.48, F=-0.15, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_prcraq)`: S=0.14, F=0.04, T=8.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_prcraq / close)`: S=-0.35, F=-0.16, T=10.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.07, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.02 (moderate), ret=+3.8%
  - 2020: S=0.26 (weak), ret=+1.5%
  - 2021: S=1.09 (moderate), ret=+5.2%
  - 2022: S=2.44 (strong), ret=+10.5%
  - 2023: S=0.88 (moderate), ret=+3.1%

## Risk & Drawdown
- Max drawdown: 7.75% over 546 days (recovered)
- Annualized: return +4.9%, volatility 4.6% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.69, excess kurtosis +3.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.85, max 3.11, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.25%; worst month: -3.56%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.63
- Sideways: S=0.16
- Bear: S=-0.72

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_prcraq, 5))` S=0.59, F=0.21, INFERIOR
Direction gap: -0.51 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_prcraq)`: S=0.14, F=0.04, T=8.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_prcraq / close)`: S=-0.35, F=-0.16, T=10.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_prcraq, 5))`: S=0.59, F=0.21, T=41.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_prcraq / close)` | TOP3000 | 1.07 | 0.70 | 7.8% | 100% | bull-only |
| `rank(fnd6_newqv1300_prcraq / close)` | TOP1000 | 0.73 | 0.42 | 7.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_prcraq / close)` | TOP500 | 0.53 | 0.28 | 11.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_prcraq / close)` | TOP200 | 0.35 | 0.16 | 13.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_prcraq)` | TOP3000 | 0.23 | 0.09 | 19.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_prcraq)` | TOP1000 | 0.20 | 0.06 | 19.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_revtq: 0.620 (moderately positively correlated)
- revenue: 0.620 (moderately positively correlated)
- fnd6_mfma2_revt: 0.618 (moderately positively correlated)
- fnd6_newa2v1300_sale: 0.618 (moderately positively correlated)
- fnd6_newa2v1300_revt: 0.618 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.17 | 1.71 | +0.55 | -0.49 | yes |
| anl4_epsr_flag | analyst4 | -0.26 | 1.69 | +0.52 | -0.31 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.09 | 1.65 | +0.48 | -0.47 | yes |
| anl4_rd_exp_flag | analyst4 | -0.23 | 1.50 | +0.43 | -0.81 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.15 | 1.53 | +0.45 | -0.56 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
