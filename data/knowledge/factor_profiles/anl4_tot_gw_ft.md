---
field: anl4_tot_gw_ft
dataset: analyst4
best_template: rank_level
best_sharpe: 1.04
best_fitness: 0.85
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.1237
ann_vol: 0.0808
hit_rate: 0.5287
rolling_sharpe_min: -1.014
rolling_sharpe_max: 2.971
top_merge_partner: rank(scl12_buzz * (-1 * returns))
redundancy_cluster: 13
negated_best_sharpe: 0.17
negated_best_template: neg_rank_level
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.87
---
# anl4_tot_gw_ft (analyst4)

*Total Goodwill - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_tot_gw_ft)`: S=1.04, F=0.85, T=2.4%, INFERIOR (TOP3000)
- `rank(anl4_tot_gw_ft / close)`: S=0.37, F=0.22, T=3.5%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_tot_gw_ft, 5))`: S=0.61, F=0.61, T=22.9%, INFERIOR (TOP1000)
- `-rank(anl4_tot_gw_ft)`: S=-0.59, F=-0.46, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_tot_gw_ft, 5))`: S=-0.38, F=-0.37, T=10.0%, INFERIOR (TOP3000)
- `ts_zscore(anl4_tot_gw_ft, 22)`: S=0.06, F=0.02, T=2.1%, INFERIOR (TOP3000)
- `ts_mean(anl4_tot_gw_ft, 10)`: S=0.57, F=0.44, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_tot_gw_ft, 22))`: S=0.30, F=0.23, T=19.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tot_gw_ft)`: S=0.17, F=0.11, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tot_gw_ft / close)`: S=-0.37, F=-0.22, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/16P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.03, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.61 (strong), ret=+6.4%
  - 2020: S=-0.03 (negative), ret=-0.1%
  - 2021: S=1.77 (strong), ret=+20.9%
  - 2022: S=1.43 (moderate), ret=+14.7%
  - 2023: S=-0.16 (negative), ret=-0.9%

## Risk & Drawdown
- Max drawdown: 12.37% over 178 days (recovered)
- Annualized: return +8.3%, volatility 8.1% (fraction of booksize)
- Hit rate: 52.9% positive days
- Tail shape: skew -0.28, excess kurtosis +5.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.01, max 2.97, latest -0.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.80%; worst month: -3.53%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.14
- Sideways: S=0.89
- Bear: S=-0.34

## Negated Direction
Best negated: `rank(-1 * anl4_tot_gw_ft)` S=0.17, F=0.11, INFERIOR
Direction gap: -0.87 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_tot_gw_ft)`: S=0.17, F=0.11, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tot_gw_ft / close)`: S=-0.37, F=-0.22, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_tot_gw_ft, 5))`: S=-0.38, F=-0.37, T=10.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_tot_gw_ft)` | TOP3000 | 1.03 | 0.85 | 12.4% | 60% | mixed |
| `rank(anl4_tot_gw_ft)` | TOP500 | 0.73 | 0.73 | 25.0% | 80% | bull-only |
| `rank(ts_delta(anl4_tot_gw_ft, 5))` | TOP1000 | 0.61 | 0.61 | 69.1% | 60% | mixed |
| `rank(anl4_tot_gw_ft)` | TOP1000 | 0.59 | 0.46 | 24.1% | 60% | bull-only |
| `rank(anl4_tot_gw_ft / close)` | TOP200 | 0.38 | 0.22 | 23.9% | 60% | mixed |
| `rank(ts_delta(anl4_tot_gw_ft, 5))` | TOP500 | 0.17 | 0.11 | 46.1% | 40% | weak |
| `rank(ts_delta(anl4_tot_gw_ft, 5))` | TOP200 | 0.17 | 0.11 | 66.1% | 60% | bull-only |
| `rank(ts_delta(anl4_tot_gw_ft, 5))` | TOP3000 | 0.08 | 0.02 | 82.1% | 60% | bull-only |
| `rank(anl4_tot_gw_ft / close)` | TOP500 | 0.09 | 0.02 | 42.4% | 80% | bear-only |

## Correlation Notes
Top correlates:
- anl4_fcfps_flag: 0.862 (strongly positively correlated)
- anl4_ptpr_flag: 0.826 (strongly positively correlated)
- anl4_totassets_flag: 0.808 (strongly positively correlated)
- rel_num_all: 0.797 (strongly positively correlated)
- anl4_fcf_flag: 0.787 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.32 | 2.29 | +0.67 | -0.98 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.31 | 2.67 | +0.65 | -0.87 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.41 | 1.85 | +0.82 | -0.54 | no |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.30 | 2.50 | +0.63 | -0.89 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.27 | 1.78 | +0.62 | -0.95 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
