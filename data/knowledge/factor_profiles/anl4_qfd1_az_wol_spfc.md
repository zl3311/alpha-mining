---
field: anl4_qfd1_az_wol_spfc
dataset: analyst4
best_template: rank_delta
best_sharpe: 1.44
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.1074
ann_vol: 0.0671
hit_rate: 0.5466
rolling_sharpe_min: -0.406
rolling_sharpe_max: 3.445
top_merge_partner: implied_volatility_call_90
redundancy_cluster: 9
negated_best_sharpe: 0.38
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -1.06
---
# anl4_qfd1_az_wol_spfc (analyst4)

*Cash Flow Per Share - The lowest estimation*

## Signal Profile
- `rank(anl4_qfd1_az_wol_spfc)`: S=0.29, F=0.12, T=0.9%, INFERIOR (TOP3000)
- `rank(anl4_qfd1_az_wol_spfc / close)`: S=0.78, F=0.55, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qfd1_az_wol_spfc, 5))`: S=1.44, F=0.74, T=36.5%, INFERIOR (TOP3000)
- `-rank(anl4_qfd1_az_wol_spfc)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfd1_az_wol_spfc, 5))`: S=-0.51, F=-0.25, T=34.7%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfd1_az_wol_spfc, 22)`: S=0.22, F=0.06, T=30.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfd1_az_wol_spfc, 10)`: S=-0.05, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfd1_az_wol_spfc, 22))`: S=0.17, F=0.04, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_wol_spfc)`: S=0.36, F=0.18, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_wol_spfc / close)`: S=0.38, F=0.23, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.45, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.66 (strong), ret=+9.9%
  - 2020: S=2.90 (strong), ret=+20.5%
  - 2021: S=0.50 (weak), ret=+3.5%
  - 2022: S=0.22 (weak), ret=+1.5%
  - 2023: S=2.05 (strong), ret=+12.2%

## Risk & Drawdown
- Max drawdown: 10.74% over 417 days (recovered)
- Annualized: return +9.7%, volatility 6.7% (fraction of booksize)
- Hit rate: 54.7% positive days
- Tail shape: skew -0.13, excess kurtosis +1.10

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.41, max 3.44, latest 2.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +10.95%; worst month: -3.23%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.88
- Sideways: S=1.99
- Bear: S=1.46

## Negated Direction
Best negated: `rank(-1 * anl4_qfd1_az_wol_spfc / close)` S=0.38, F=0.23, INFERIOR
Direction gap: -1.06 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_qfd1_az_wol_spfc)`: S=0.36, F=0.18, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_wol_spfc / close)`: S=0.38, F=0.23, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfd1_az_wol_spfc, 5))`: S=-0.51, F=-0.25, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_qfd1_az_wol_spfc, 5))` | TOP3000 | 1.45 | 0.74 | 10.7% | 100% | all-weather |
| `rank(anl4_qfd1_az_wol_spfc / close)` | TOP3000 | 0.78 | 0.55 | 11.7% | 80% | mixed |
| `rank(ts_delta(anl4_qfd1_az_wol_spfc, 5))` | TOP200 | 0.63 | 0.35 | 32.9% | 80% | mixed |
| `rank(ts_delta(anl4_qfd1_az_wol_spfc, 5))` | TOP1000 | 0.63 | 0.24 | 13.2% | 60% | mixed |
| `rank(anl4_qfd1_az_wol_spfc / close)` | TOP1000 | 0.35 | 0.18 | 18.1% | 40% | bull-only |
| `rank(anl4_qfd1_az_wol_spfc)` | TOP3000 | 0.28 | 0.12 | 26.4% | 60% | bull-only |
| `rank(ts_delta(anl4_qfd1_az_wol_spfc, 5))` | TOP500 | 0.30 | 0.08 | 25.3% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_qf_az_wol_spfc: 1.000 (strongly positively correlated)
- est_cashflow_ps: 0.807 (strongly positively correlated)
- cashflow_per_share_minimum: 0.739 (strongly positively correlated)
- anl4_qfv4_cfps_high: 0.673 (moderately positively correlated)
- cashflow_per_share_median_value: 0.649 (moderately positively correlated)

Redundancy cluster #9: 4 similar fields, mean |rho| 0.783 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_call_90 | option8 | +0.00 | 2.04 | +0.57 | -0.54 | yes |
| fnd6_dlto | fundamental_debt | -0.02 | 1.99 | +0.54 | -0.58 | yes |
| implied_volatility_put_180 | option8 | +0.02 | 2.00 | +0.55 | -0.37 | yes |
| implied_volatility_mean_720 | option8 | +0.00 | 2.05 | +0.55 | -0.33 | yes |
| implied_volatility_mean_180 | option8 | +0.00 | 2.09 | +0.56 | -0.24 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
