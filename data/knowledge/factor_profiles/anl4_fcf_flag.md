---
field: anl4_fcf_flag
dataset: analyst4
best_template: decay_linear
best_sharpe: 1.06
best_fitness: 0.75
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 35
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0876
ann_vol: 0.0602
hit_rate: 0.5304
rolling_sharpe_min: -0.33
rolling_sharpe_max: 3.046
top_merge_partner: fn_comp_options_forfeitures_and_expirations_a
redundancy_cluster: 18
negated_best_sharpe: 0.92
negated_best_template: rank_neg_delta
negated_best_fitness: 0.71
n_negated_sims: 10
direction_gap: -0.14
---
# anl4_fcf_flag (analyst4)

*Free cash flow - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_fcf_flag)`: S=1.05, F=0.74, T=2.4%, INFERIOR (TOP3000)
- `rank(anl4_fcf_flag / close)`: S=0.30, F=0.16, T=3.4%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_fcf_flag, 5))`: S=0.29, F=0.14, T=32.5%, INFERIOR (TOP500)
- `ts_decay_linear(rank(anl4_fcf_flag), 5)`: S=1.06, F=0.75, T=2.4%, INFERIOR (TOP3000)
- `-rank(anl4_fcf_flag)`: S=-0.64, F=-0.37, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_flag, 5))`: S=0.92, F=0.71, T=35.0%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_fcf_flag, 63)`: S=-0.02, F=0.00, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcf_flag, 10)`: S=0.53, F=0.39, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcf_flag, 22))`: S=0.00, F=0.00, T=17.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_flag)`: S=-1.05, F=-0.74, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_flag / close)`: S=0.09, F=0.03, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/22P
- LOW_FITNESS: 35F/0P
- LOW_SHARPE: 35F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/21P

## Temporal Behavior
Headline (decay_linear): Overall Sharpe 1.06, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.71 (moderate), ret=+2.5%
  - 2020: S=1.04 (moderate), ret=+5.0%
  - 2021: S=1.74 (strong), ret=+15.0%
  - 2022: S=1.34 (moderate), ret=+9.1%
  - 2023: S=-0.10 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 8.76% over 172 days (recovered)
- Annualized: return +6.4%, volatility 6.0% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.13, excess kurtosis +3.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.33, max 3.05, latest -0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.15%; worst month: -1.75%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.55
- Sideways: S=1.37
- Bear: S=0.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_fcf_flag, 5))` S=0.92, F=0.71, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_fcf_flag)`: S=-1.05, F=-0.74, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcf_flag / close)`: S=0.09, F=0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcf_flag, 5))`: S=0.92, F=0.71, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `ts_decay_linear(rank(anl4_fcf_flag), 5)` | TOP3000 | 1.06 | 0.75 | 8.8% | 80% | mixed |
| `rank(anl4_fcf_flag)` | TOP3000 | 1.05 | 0.74 | 8.8% | 80% | mixed |
| `rank(anl4_fcf_flag)` | TOP500 | 0.75 | 0.51 | 10.2% | 80% | mixed |
| `rank(anl4_fcf_flag)` | TOP1000 | 0.65 | 0.37 | 10.7% | 100% | mixed |
| `rank(anl4_fcf_flag)` | TOP200 | 0.47 | 0.31 | 22.2% | 80% | weak |
| `rank(anl4_fcf_flag / close)` | TOP200 | 0.32 | 0.16 | 27.6% | 60% | mixed |
| `rank(ts_delta(anl4_fcf_flag, 5))` | TOP500 | 0.30 | 0.14 | 64.6% | 80% | weak |
| `rank(anl4_fcf_flag / close)` | TOP500 | 0.11 | 0.03 | 30.6% | 60% | bear-only |
| `rank(ts_delta(anl4_fcf_flag, 5))` | TOP200 | 0.10 | 0.03 | 51.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- anl4_fcfps_flag: 0.841 (strongly positively correlated)
- anl4_cff_flag: 0.817 (strongly positively correlated)
- anl4_totassets_flag: 0.811 (strongly positively correlated)
- anl4_cfi_flag: 0.810 (strongly positively correlated)
- anl4_tot_gw_ft: 0.787 (strongly positively correlated)

Redundancy cluster #18: 7 similar fields, mean |rho| 0.818 (representative: anl4_totassets_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.19 | 1.75 | +0.58 | -0.43 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.23 | 2.18 | +0.56 | -0.62 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.36 | 1.71 | +0.65 | -0.90 | no |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.22 | 2.54 | +0.52 | -0.35 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.21 | 2.36 | +0.49 | -0.33 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
