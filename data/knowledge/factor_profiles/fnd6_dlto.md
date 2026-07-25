---
field: fnd6_dlto
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.34
best_fitness: 1.17
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.0819
ann_vol: 0.0715
hit_rate: 0.5045
rolling_sharpe_min: -1.515
rolling_sharpe_max: 3.049
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 12
negated_best_sharpe: 0.17
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -1.17
---
# fnd6_dlto (fundamental6)

*Debt - Long-Term - Other*

## Signal Profile
- `rank(fnd6_dlto)`: S=1.03, F=0.87, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_dlto / close)`: S=1.34, F=1.17, T=2.1%, AVERAGE (TOP3000)
- `rank(ts_delta(fnd6_dlto, 5))`: S=0.12, F=0.03, T=40.3%, INFERIOR (TOP1000)
- `-rank(fnd6_dlto)`: S=-0.39, F=-0.21, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dlto, 5))`: S=0.17, F=0.07, T=27.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dlto, 63)`: S=0.55, F=0.38, T=19.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dlto, 10)`: S=0.11, F=0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dlto, 22))`: S=0.30, F=0.12, T=19.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dlto)`: S=-0.05, F=-0.01, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dlto / close)`: S=-0.20, F=-0.08, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.34, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.05 (negative), ret=-0.2%
  - 2020: S=1.15 (moderate), ret=+11.1%
  - 2021: S=2.07 (strong), ret=+17.9%
  - 2022: S=2.02 (strong), ret=+12.5%
  - 2023: S=1.15 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 8.19% over 499 days (recovered)
- Annualized: return +9.6%, volatility 7.1% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.75, excess kurtosis +4.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.51, max 3.05, latest 1.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.17%; worst month: -2.84%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.91
- Sideways: S=0.40
- Bear: S=0.43

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dlto, 5))` S=0.17, F=0.07, INFERIOR
Direction gap: -1.17 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dlto)`: S=-0.05, F=-0.01, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dlto / close)`: S=-0.20, F=-0.08, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dlto, 5))`: S=0.17, F=0.07, T=27.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dlto / close)` | TOP3000 | 1.34 | 1.17 | 8.2% | 80% | mixed |
| `rank(fnd6_dlto)` | TOP3000 | 1.02 | 0.87 | 13.7% | 80% | bull-only |
| `rank(fnd6_dlto / close)` | TOP1000 | 0.65 | 0.43 | 8.0% | 60% | bull-only |
| `rank(fnd6_dlto)` | TOP1000 | 0.38 | 0.21 | 20.4% | 40% | bull-only |
| `rank(fnd6_dlto / close)` | TOP500 | 0.33 | 0.16 | 13.7% | 40% | bull-only |
| `rank(fnd6_dlto / close)` | TOP200 | 0.20 | 0.08 | 16.4% | 60% | bull-only |
| `rank(fnd6_dlto)` | TOP500 | 0.15 | 0.05 | 28.2% | 40% | bull-only |
| `rank(ts_delta(fnd6_dlto, 5))` | TOP1000 | 0.12 | 0.03 | 62.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_dltt: 0.929 (strongly positively correlated)
- fnd6_cptmfmq_dlttq: 0.926 (strongly positively correlated)
- fnd6_cptnewqv1300_dlttq: 0.926 (strongly positively correlated)
- debt_lt: 0.926 (strongly positively correlated)
- fnd6_newqv1300_xintq: 0.915 (strongly positively correlated)

Redundancy cluster #12: 12 similar fields, mean |rho| 0.749 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.38 | 2.17 | +0.84 | -0.41 | yes |
| rp_ess_dividends | news18 | +0.03 | 1.91 | +0.51 | -0.87 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | -0.02 | 1.99 | +0.54 | -0.58 | yes |
| anl4_qf_az_wol_spfc | analyst4 | -0.02 | 1.99 | +0.54 | -0.58 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.07 | 2.18 | +0.55 | +0.05 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, trade_when
