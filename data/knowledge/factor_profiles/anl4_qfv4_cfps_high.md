---
field: anl4_qfv4_cfps_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.72
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.082
ann_vol: 0.0653
hit_rate: 0.5198
rolling_sharpe_min: -1.063
rolling_sharpe_max: 2.302
top_merge_partner: parkinson_volatility_90
negated_best_sharpe: 0.41
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.31
---
# anl4_qfv4_cfps_high (analyst4)

*Cash Flow Per Share - The highest estimation for the quarter*

## Signal Profile
- `rank(anl4_qfv4_cfps_high)`: S=0.31, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(anl4_qfv4_cfps_high / close)`: S=0.72, F=0.49, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qfv4_cfps_high, 5))`: S=0.80, F=0.30, T=36.4%, INFERIOR (TOP3000)
- `-rank(anl4_qfv4_cfps_high)`: S=-0.02, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_cfps_high, 5))`: S=-0.31, F=-0.12, T=35.0%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_qfv4_cfps_high, 63)`: S=0.17, F=0.04, T=16.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfv4_cfps_high, 10)`: S=-0.08, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfv4_cfps_high, 22))`: S=0.03, F=0.00, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_cfps_high)`: S=0.34, F=0.17, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_cfps_high / close)`: S=0.41, F=0.25, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.83, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.12 (strong), ret=+12.6%
  - 2020: S=0.79 (moderate), ret=+5.3%
  - 2021: S=0.08 (weak), ret=+0.6%
  - 2022: S=-0.05 (negative), ret=-0.3%
  - 2023: S=1.36 (moderate), ret=+8.5%

## Risk & Drawdown
- Max drawdown: 8.20% over 470 days (recovered)
- Annualized: return +5.4%, volatility 6.5% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew -0.03, excess kurtosis +1.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.06, max 2.30, latest 1.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +4.30%; worst month: -4.05%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.96
- Sideways: S=1.39
- Bear: S=0.11

## Negated Direction
Best negated: `rank(-1 * anl4_qfv4_cfps_high / close)` S=0.41, F=0.25, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_qfv4_cfps_high)`: S=0.34, F=0.17, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_cfps_high / close)`: S=0.41, F=0.25, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_cfps_high, 5))`: S=-0.31, F=-0.12, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_qfv4_cfps_high, 5))` | TOP3000 | 0.83 | 0.30 | 8.2% | 80% | mixed |

## Correlation Notes
Top correlates:
- est_cashflow_ps: 0.809 (strongly positively correlated)
- cashflow_per_share_maximum: 0.739 (strongly positively correlated)
- anl4_qf_az_wol_spfc: 0.673 (moderately positively correlated)
- anl4_qfd1_az_wol_spfc: 0.673 (moderately positively correlated)
- cashflow_per_share_median_value: 0.671 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| parkinson_volatility_90 | option8 | -0.05 | 1.25 | +0.36 | -0.88 | yes |
| fnd2_dfdtxastxdfdexprssaccrs | fundamental2 | -0.02 | 1.22 | +0.34 | -0.96 | yes |
| fnd6_optprcca | fundamental6 | -0.05 | 1.18 | +0.34 | -0.97 | yes |
| fn_debt_instrument_face_amount_a | fundamental2 | -0.03 | 1.18 | +0.35 | -0.79 | yes |
| single_sector_pureplay_company_count | pv13 | -0.05 | 1.22 | +0.36 | -0.70 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
