---
field: anl4_cfo_flag
dataset: analyst4
best_template: rank_level
best_sharpe: 1.12
best_fitness: 0.85
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0726
ann_vol: 0.0654
hit_rate: 0.5328
rolling_sharpe_min: -0.177
rolling_sharpe_max: 1.952
top_merge_partner: fnd6_lcox
redundancy_cluster: 18
negated_best_sharpe: 0.43
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: -0.69
---
# anl4_cfo_flag (analyst4)

*Cash Flow From Operations - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_cfo_flag)`: S=1.12, F=0.85, T=2.6%, INFERIOR (TOP3000)
- `rank(anl4_cfo_flag / close)`: S=0.21, F=0.09, T=3.3%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cfo_flag, 5))`: S=0.29, F=0.14, T=29.9%, INFERIOR (TOP500)
- `-rank(anl4_cfo_flag)`: S=-0.86, F=-0.64, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfo_flag, 5))`: S=0.43, F=0.26, T=34.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_cfo_flag, 22)`: S=0.56, F=0.64, T=15.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_cfo_flag, 10)`: S=0.65, F=0.57, T=4.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cfo_flag, 22))`: S=0.09, F=0.03, T=18.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_flag)`: S=-1.12, F=-0.85, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_flag / close)`: S=0.00, F=0.00, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.12, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.45 (moderate), ret=+6.4%
  - 2020: S=1.40 (moderate), ret=+7.5%
  - 2021: S=0.93 (moderate), ret=+7.5%
  - 2022: S=0.96 (moderate), ret=+7.7%
  - 2023: S=1.24 (moderate), ret=+6.7%

## Risk & Drawdown
- Max drawdown: 7.26% over 168 days (recovered)
- Annualized: return +7.3%, volatility 6.5% (fraction of booksize)
- Hit rate: 53.3% positive days
- Tail shape: skew -0.41, excess kurtosis +4.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.18, max 1.95, latest 1.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +4.28%; worst month: -2.40%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.72
- Sideways: S=1.56
- Bear: S=1.32

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cfo_flag, 5))` S=0.43, F=0.26, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_cfo_flag)`: S=-1.12, F=-0.85, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_flag / close)`: S=0.00, F=0.00, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfo_flag, 5))`: S=0.43, F=0.26, T=34.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cfo_flag)` | TOP3000 | 1.12 | 0.85 | 7.3% | 100% | all-weather |
| `rank(anl4_cfo_flag)` | TOP1000 | 0.88 | 0.64 | 11.3% | 80% | mixed |
| `rank(anl4_cfo_flag)` | TOP500 | 0.80 | 0.57 | 10.0% | 80% | mixed |
| `rank(anl4_cfo_flag)` | TOP200 | 0.47 | 0.31 | 16.1% | 80% | weak |
| `rank(ts_delta(anl4_cfo_flag, 5))` | TOP500 | 0.29 | 0.14 | 78.5% | 40% | weak |
| `rank(anl4_cfo_flag / close)` | TOP200 | 0.22 | 0.09 | 23.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_cfi_flag: 0.904 (strongly positively correlated)
- anl4_cff_flag: 0.903 (strongly positively correlated)
- anl4_totassets_flag: 0.847 (strongly positively correlated)
- anl4_capex_flag: 0.839 (strongly positively correlated)
- anl4_fcf_flag: 0.777 (strongly positively correlated)

Redundancy cluster #18: 7 similar fields, mean |rho| 0.818 (representative: anl4_totassets_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_lcox | fundamental6 | -0.11 | 1.62 | +0.51 | -0.90 | yes |
| fn_repayments_of_debt_a | fundamental2 | -0.10 | 1.68 | +0.49 | -0.99 | yes |
| fnd6_newa1v1300_cogs | fundamental6 | -0.06 | 1.67 | +0.49 | -0.94 | yes |
| fnd6_newqv1300_lcoq | fundamental6 | -0.04 | 1.60 | +0.48 | -0.85 | yes |
| fnd2_a_bnsacqproformarvn | fundamental2 | -0.05 | 1.62 | +0.50 | -0.69 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
