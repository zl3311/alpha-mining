---
field: fnd6_dltp
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.02
best_fitness: 0.7
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0635
ann_vol: 0.0588
hit_rate: 0.5061
rolling_sharpe_min: -0.761
rolling_sharpe_max: 2.678
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.92
negated_best_template: rank_neg_delta
negated_best_fitness: 0.59
n_negated_sims: 10
direction_gap: -0.1
---
# fnd6_dltp (fundamental6)

*Long-Term Debt - Tied to Prime*

## Signal Profile
- `rank(fnd6_dltp)`: S=0.84, F=0.53, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_dltp / close)`: S=1.02, F=0.70, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dltp, 5))`: S=0.23, F=0.07, T=41.0%, INFERIOR (TOP3000)
- `-rank(fnd6_dltp)`: S=-0.15, F=-0.04, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dltp, 5))`: S=0.92, F=0.59, T=35.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_dltp, 22)`: S=0.08, F=0.02, T=15.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dltp, 10)`: S=-0.08, F=-0.02, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dltp, 22))`: S=-0.24, F=-0.10, T=19.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dltp)`: S=-0.15, F=-0.04, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dltp / close)`: S=-0.24, F=-0.08, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.01, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.68 (moderate), ret=+2.3%
  - 2020: S=0.74 (moderate), ret=+6.0%
  - 2021: S=1.61 (strong), ret=+10.3%
  - 2022: S=1.85 (strong), ret=+10.8%
  - 2023: S=-0.05 (negative), ret=-0.2%

## Risk & Drawdown
- Max drawdown: 6.35% over 154 days (recovered)
- Annualized: return +6.0%, volatility 5.9% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.49, excess kurtosis +3.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.76, max 2.68, latest -0.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.39%; worst month: -2.24%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.48
- Sideways: S=1.11
- Bear: S=-0.52

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dltp, 5))` S=0.92, F=0.59, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_dltp)`: S=-0.15, F=-0.04, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dltp / close)`: S=-0.24, F=-0.08, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dltp, 5))`: S=0.92, F=0.59, T=35.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dltp / close)` | TOP3000 | 1.01 | 0.70 | 6.3% | 80% | bull-only |
| `rank(fnd6_dltp)` | TOP3000 | 0.84 | 0.53 | 8.4% | 60% | bull-only |
| `rank(fnd6_dltp / close)` | TOP1000 | 0.24 | 0.08 | 10.1% | 80% | bull-only |
| `rank(ts_delta(fnd6_dltp, 5))` | TOP3000 | 0.23 | 0.07 | 19.3% | 60% | weak |
| `rank(fnd6_dltp)` | TOP1000 | 0.16 | 0.04 | 13.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dltr: 0.885 (strongly positively correlated)
- fnd6_dlto: 0.884 (strongly positively correlated)
- fnd6_dxd4: 0.858 (strongly positively correlated)
- fnd6_dltis: 0.852 (strongly positively correlated)
- sales_ps: 0.851 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.41 | 1.73 | +0.71 | -0.36 | yes |
| anl4_epsr_flag | analyst4 | -0.34 | 1.82 | +0.65 | -0.70 | yes |
| news_open_vol | news12 | -0.26 | 1.57 | +0.56 | -0.51 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.25 | 1.55 | +0.53 | -0.58 | yes |
| rp_ess_revenue | news18 | -0.33 | 1.52 | +0.50 | -0.52 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
