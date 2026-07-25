---
field: fnd6_newa1v1300_ap
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.88
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0869
ann_vol: 0.0729
hit_rate: 0.4923
rolling_sharpe_min: -1.263
rolling_sharpe_max: 2.666
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.62
negated_best_template: rank_neg_delta
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.26
---
# fnd6_newa1v1300_ap (fundamental6)

*Accounts Payable - Trade*

## Signal Profile
- `rank(fnd6_newa1v1300_ap)`: S=0.67, F=0.51, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_ap / close)`: S=0.88, F=0.63, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_ap, 5))`: S=0.40, F=0.19, T=35.1%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_ap)`: S=-0.47, F=-0.32, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ap, 5))`: S=0.62, F=0.32, T=34.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_ap, 22)`: S=0.23, F=0.09, T=29.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_ap, 10)`: S=0.22, F=0.09, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_ap, 22))`: S=-0.01, F=0.00, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ap)`: S=-0.31, F=-0.17, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ap / close)`: S=-0.50, F=-0.31, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.86, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.47 (negative), ret=-2.2%
  - 2020: S=0.31 (weak), ret=+2.7%
  - 2021: S=1.79 (strong), ret=+16.2%
  - 2022: S=1.50 (moderate), ret=+11.1%
  - 2023: S=0.76 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 8.69% over 508 days (recovered)
- Annualized: return +6.3%, volatility 7.3% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew +0.55, excess kurtosis +3.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 2.67, latest 0.85

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.26%; worst month: -3.83%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.14
- Sideways: S=0.05
- Bear: S=-1.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_ap, 5))` S=0.62, F=0.32, INFERIOR
Direction gap: -0.26 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_ap)`: S=-0.31, F=-0.17, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ap / close)`: S=-0.50, F=-0.31, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ap, 5))`: S=0.62, F=0.32, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_ap / close)` | TOP3000 | 0.86 | 0.63 | 8.7% | 80% | bull-only |
| `rank(fnd6_newa1v1300_ap)` | TOP3000 | 0.66 | 0.51 | 26.4% | 80% | bull-only |
| `rank(fnd6_newa1v1300_ap / close)` | TOP1000 | 0.67 | 0.49 | 12.5% | 80% | bull-only |
| `rank(fnd6_newa1v1300_ap)` | TOP1000 | 0.46 | 0.32 | 26.3% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ap / close)` | TOP500 | 0.49 | 0.31 | 21.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_ap, 5))` | TOP200 | 0.40 | 0.19 | 38.5% | 80% | mixed |
| `rank(fnd6_newa1v1300_ap)` | TOP500 | 0.30 | 0.17 | 32.5% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ap / close)` | TOP200 | 0.13 | 0.05 | 28.0% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ap)` | TOP200 | 0.06 | 0.02 | 42.0% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_apq: 0.988 (strongly positively correlated)
- fnd6_newa1v1300_cogs: 0.972 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.972 (strongly positively correlated)
- fnd6_newa1v1300_lct: 0.970 (strongly positively correlated)
- employee: 0.969 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.36 | 1.52 | +0.63 | -0.64 | yes |
| anl4_epsr_flag | analyst4 | -0.35 | 1.79 | +0.61 | -0.54 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.33 | 1.39 | +0.53 | -0.95 | yes |
| min_gross_income_guidance | analyst4 | -0.24 | 1.37 | +0.50 | -0.76 | yes |
| max_gross_income_guidance | analyst4 | -0.24 | 1.39 | +0.50 | -0.76 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
