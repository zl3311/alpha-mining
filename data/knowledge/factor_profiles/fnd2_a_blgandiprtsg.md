---
field: fnd2_a_blgandiprtsg
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.84
best_fitness: 0.82
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.061
ann_vol: 0.0561
hit_rate: 0.502
rolling_sharpe_min: -0.684
rolling_sharpe_max: 2.834
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.6
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: -0.24
---
# fnd2_a_blgandiprtsg (fundamental2)

*Amount before accumulated depreciation of building structures held for productive use including addition, improvement, or renovation to the structure, including, but not limited to, interior masonry, interior flooring, electrical, and plumbing.*

## Signal Profile
- `rank(fnd2_a_blgandiprtsg)`: S=0.49, F=0.27, T=1.2%, INFERIOR (TOP1000)
- `rank(fnd2_a_blgandiprtsg / close)`: S=0.97, F=0.64, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_blgandiprtsg, 5))`: S=0.08, F=0.02, T=34.0%, INFERIOR (TOP500)
- `-rank(fnd2_a_blgandiprtsg)`: S=-0.49, F=-0.27, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_blgandiprtsg, 5))`: S=0.60, F=0.30, T=34.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_blgandiprtsg, 63)`: S=0.84, F=0.82, T=16.5%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_blgandiprtsg, 10)`: S=0.45, F=0.26, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_blgandiprtsg, 22))`: S=-0.82, F=-0.60, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_blgandiprtsg)`: S=-0.37, F=-0.17, T=0.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_blgandiprtsg / close)`: S=-0.97, F=-0.64, T=1.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.96, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.03 (negative), ret=-0.1%
  - 2020: S=0.43 (weak), ret=+3.1%
  - 2021: S=1.62 (strong), ret=+9.4%
  - 2022: S=2.23 (strong), ret=+11.8%
  - 2023: S=0.58 (moderate), ret=+2.3%

## Risk & Drawdown
- Max drawdown: 6.10% over 415 days (recovered)
- Annualized: return +5.4%, volatility 5.6% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.38, excess kurtosis +2.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.68, max 2.83, latest 0.61

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +5.04%; worst month: -3.01%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.69
- Sideways: S=0.46
- Bear: S=-0.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_blgandiprtsg, 5))` S=0.60, F=0.30, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_blgandiprtsg)`: S=-0.37, F=-0.17, T=0.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_blgandiprtsg / close)`: S=-0.97, F=-0.64, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_blgandiprtsg, 5))`: S=0.60, F=0.30, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_blgandiprtsg / close)` | TOP3000 | 0.96 | 0.64 | 6.1% | 80% | mixed |
| `rank(fnd2_a_blgandiprtsg / close)` | TOP1000 | 0.60 | 0.36 | 10.5% | 60% | bull-only |
| `rank(fnd2_a_blgandiprtsg)` | TOP1000 | 0.49 | 0.27 | 21.3% | 60% | bull-only |
| `rank(fnd2_a_blgandiprtsg)` | TOP500 | 0.37 | 0.21 | 28.5% | 60% | bull-only |
| `rank(fnd2_a_blgandiprtsg)` | TOP3000 | 0.36 | 0.17 | 26.4% | 80% | bull-only |
| `rank(fnd2_a_blgandiprtsg / close)` | TOP500 | 0.31 | 0.16 | 19.8% | 60% | bull-only |
| `rank(fnd2_a_blgandiprtsg)` | TOP200 | 0.13 | 0.05 | 24.1% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_blgandiprtsg, 5))` | TOP500 | 0.07 | 0.02 | 32.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_landlandiprts: 0.890 (strongly positively correlated)
- fnd6_intpn: 0.837 (strongly positively correlated)
- fnd2_dfctrbplancstrg: 0.837 (strongly positively correlated)
- fn_interest_paid_net_a: 0.834 (strongly positively correlated)
- fnd2_a_bnsacqproformarvn: 0.833 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.33 | 1.77 | +0.59 | -0.50 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.46 | +0.50 | -0.55 | yes |
| anl4_rd_exp_flag | analyst4 | -0.24 | 1.53 | +0.50 | -0.41 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.18 | 1.44 | +0.48 | -0.58 | yes |
| anl4_capex_high | analyst4 | -0.15 | 1.46 | +0.49 | -0.40 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
