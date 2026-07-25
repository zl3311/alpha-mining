---
field: fnd6_newa1v1300_aol2
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.12
best_fitness: 0.73
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0715
ann_vol: 0.0473
hit_rate: 0.5263
rolling_sharpe_min: -1.289
rolling_sharpe_max: 3.27
top_merge_partner: fn_def_tax_assets_liab_net_a
redundancy_cluster: 17
negated_best_sharpe: 0.42
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.7
---
# fnd6_newa1v1300_aol2 (fundamental6)

*Assets Level 2 (Observable)*

## Signal Profile
- `rank(fnd6_newa1v1300_aol2)`: S=0.80, F=0.49, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_aol2 / close)`: S=1.12, F=0.73, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_aol2, 5))`: S=0.33, F=0.13, T=36.9%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_aol2)`: S=-0.30, F=-0.12, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aol2, 5))`: S=0.42, F=0.17, T=40.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_aol2, 22)`: S=-0.14, F=-0.05, T=21.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_aol2, 10)`: S=0.61, F=0.39, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_aol2, 22))`: S=-0.02, F=0.00, T=19.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aol2)`: S=-0.80, F=-0.49, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aol2 / close)`: S=-1.12, F=-0.73, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.12, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.03 (negative), ret=-0.1%
  - 2020: S=-0.13 (negative), ret=-0.5%
  - 2021: S=1.01 (moderate), ret=+6.9%
  - 2022: S=2.75 (strong), ret=+13.2%
  - 2023: S=1.72 (strong), ret=+6.4%

## Risk & Drawdown
- Max drawdown: 7.15% over 335 days (recovered)
- Annualized: return +5.3%, volatility 4.7% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew +0.18, excess kurtosis +2.08

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 3.27, latest 1.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.58%; worst month: -1.44%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.88
- Sideways: S=1.17
- Bear: S=-0.93

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_aol2, 5))` S=0.42, F=0.17, INFERIOR
Direction gap: -0.70 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_aol2)`: S=-0.80, F=-0.49, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aol2 / close)`: S=-1.12, F=-0.73, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aol2, 5))`: S=0.42, F=0.17, T=40.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_aol2 / close)` | TOP3000 | 1.12 | 0.73 | 7.1% | 60% | bull-only |
| `rank(fnd6_newa1v1300_aol2)` | TOP3000 | 0.81 | 0.49 | 17.6% | 80% | bull-only |
| `rank(fnd6_newa1v1300_aol2 / close)` | TOP1000 | 0.42 | 0.19 | 15.4% | 40% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_aol2, 5))` | TOP1000 | 0.33 | 0.13 | 34.1% | 60% | mixed |
| `rank(fnd6_newa1v1300_aol2)` | TOP1000 | 0.29 | 0.12 | 22.8% | 40% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_aol2, 5))` | TOP500 | 0.16 | 0.05 | 48.1% | 60% | mixed |
| `rank(fnd6_newa1v1300_aol2 / close)` | TOP500 | 0.06 | 0.02 | 26.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_aol2q: 0.886 (strongly positively correlated)
- fnd6_ivch: 0.744 (strongly positively correlated)
- fnd6_newa1v1300_caps: 0.710 (strongly positively correlated)
- fnd6_tfva: 0.704 (strongly positively correlated)
- fnd6_siv: 0.695 (moderately positively correlated)

Redundancy cluster #17: 12 similar fields, mean |rho| 0.768 (representative: fnd6_newqv1300_aol2q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.28 | 1.68 | +0.56 | -0.04 | yes |
| operating_profit_before_depr_amort_min_guidance_qtr | analyst4 | -0.14 | 1.58 | +0.46 | -0.89 | yes |
| operating_profit_before_depr_amort_max_guidance_qtr | analyst4 | -0.14 | 1.57 | +0.45 | -0.89 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.11 | 1.69 | +0.53 | -0.10 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.17 | 2.12 | +0.49 | +0.06 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
