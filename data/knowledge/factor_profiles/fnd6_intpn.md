---
field: fnd6_intpn
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.99
best_fitness: 0.75
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0696
ann_vol: 0.0722
hit_rate: 0.498
rolling_sharpe_min: -0.793
rolling_sharpe_max: 2.33
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.39
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.6
---
# fnd6_intpn (fundamental6)

*Interest Paid - Net*

## Signal Profile
- `rank(fnd6_intpn)`: S=0.66, F=0.46, T=1.7%, INFERIOR (TOP3000)
- `rank(fnd6_intpn / close)`: S=0.99, F=0.75, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_intpn, 5))`: S=-0.02, F=0.00, T=28.1%, INFERIOR (TOP200)
- `-rank(fnd6_intpn)`: S=-0.42, F=-0.26, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_intpn, 5))`: S=0.39, F=0.16, T=37.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_intpn, 63)`: S=0.39, F=0.22, T=19.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_intpn, 10)`: S=0.25, F=0.11, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_intpn, 22))`: S=-0.16, F=-0.05, T=18.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_intpn)`: S=-0.42, F=-0.26, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_intpn / close)`: S=-0.69, F=-0.49, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.99, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.58 (moderate), ret=+2.6%
  - 2020: S=0.70 (moderate), ret=+6.6%
  - 2021: S=1.37 (moderate), ret=+11.0%
  - 2022: S=1.70 (strong), ret=+12.1%
  - 2023: S=0.56 (moderate), ret=+2.7%

## Risk & Drawdown
- Max drawdown: 6.96% over 237 days (recovered)
- Annualized: return +7.1%, volatility 7.2% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.47, excess kurtosis +3.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.79, max 2.33, latest 0.63

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +6.88%; worst month: -3.16%
Positive months: 66%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.72
- Sideways: S=0.81
- Bear: S=-0.72

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_intpn, 5))` S=0.39, F=0.16, INFERIOR
Direction gap: -0.60 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_intpn)`: S=-0.42, F=-0.26, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_intpn / close)`: S=-0.69, F=-0.49, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_intpn, 5))`: S=0.39, F=0.16, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_intpn / close)` | TOP3000 | 0.99 | 0.75 | 7.0% | 100% | bull-only |
| `rank(fnd6_intpn / close)` | TOP1000 | 0.68 | 0.49 | 8.6% | 80% | bull-only |
| `rank(fnd6_intpn)` | TOP3000 | 0.66 | 0.46 | 19.2% | 80% | bull-only |
| `rank(fnd6_intpn)` | TOP1000 | 0.41 | 0.26 | 26.5% | 60% | bull-only |
| `rank(fnd6_intpn / close)` | TOP500 | 0.26 | 0.13 | 22.7% | 60% | bull-only |
| `rank(fnd6_intpn)` | TOP500 | 0.08 | 0.03 | 45.6% | 60% | bull-only |
| `rank(fnd6_intpn / close)` | TOP200 | 0.06 | 0.02 | 39.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_interest_paid_net_a: 0.968 (strongly positively correlated)
- fnd6_newa2v1300_xint: 0.960 (strongly positively correlated)
- fnd6_newqv1300_xintq: 0.948 (strongly positively correlated)
- interest_expense: 0.948 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.939 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.88 | +0.70 | -0.60 | yes |
| anl4_rd_exp_flag | analyst4 | -0.32 | 1.68 | +0.66 | -0.45 | yes |
| rp_ess_revenue | news18 | -0.36 | 1.60 | +0.61 | -0.56 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.21 | 1.53 | +0.54 | -0.62 | yes |
| max_gross_income_guidance | analyst4 | -0.28 | 1.50 | +0.51 | -0.72 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
