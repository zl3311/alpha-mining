---
field: anl4_ebitda_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.88
best_fitness: 0.7
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: bull-only
n_variations_with_pnl: 12
max_drawdown: 0.1643
ann_vol: 0.0903
hit_rate: 0.5077
rolling_sharpe_min: -1.716
rolling_sharpe_max: 2.95
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: -0.22
negated_best_template: neg_rank
negated_best_fitness: -0.11
n_negated_sims: 4
direction_gap: -1.1
---
# anl4_ebitda_low (analyst4)

*Earnings before interest, taxes, depreciation and amortization - The lowest estimation*

## Signal Profile
- `rank(anl4_ebitda_low)`: S=0.48, F=0.33, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_ebitda_low / close)`: S=0.88, F=0.70, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ebitda_low, 5))`: S=0.52, F=0.12, T=36.6%, INFERIOR (TOP3000)
- `-rank(anl4_ebitda_low)`: S=-0.22, F=-0.11, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_low, 5))`: S=-0.52, F=-0.12, T=36.6%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ebitda_low, 22)`: S=0.56, F=0.18, T=35.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebitda_low, 10)`: S=0.21, F=0.09, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebitda_low, 22))`: S=0.29, F=0.08, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_low)`: S=-0.48, F=-0.33, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_low / close)`: S=-0.88, F=-0.70, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/25P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.88, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.17 (weak), ret=+0.9%
  - 2020: S=-0.94 (negative), ret=-7.4%
  - 2021: S=1.62 (strong), ret=+19.3%
  - 2022: S=1.89 (strong), ret=+21.8%
  - 2023: S=0.78 (moderate), ret=+4.3%

## Risk & Drawdown
- Max drawdown: 16.43% over 530 days (recovered)
- Annualized: return +7.9%, volatility 9.0% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.16, excess kurtosis +2.13

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.72, max 2.95, latest 0.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.15%; worst month: -3.89%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.48
- Sideways: S=0.99
- Bear: S=-2.56

## Negated Direction
Best negated: `-rank(anl4_ebitda_low)` S=-0.22, F=-0.11, INFERIOR
Direction gap: -1.10 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_ebitda_low)`: S=-0.48, F=-0.33, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebitda_low / close)`: S=-0.88, F=-0.70, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebitda_low, 5))`: S=-0.52, F=-0.12, T=36.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ebitda_low / close)` | TOP3000 | 0.88 | 0.70 | 16.4% | 80% | bull-only |
| `rank(anl4_ebitda_low)` | TOP3000 | 0.48 | 0.33 | 39.4% | 80% | bull-only |
| `rank(anl4_ebitda_low / close)` | TOP1000 | 0.43 | 0.26 | 22.8% | 60% | bull-only |
| `rank(ts_delta(anl4_ebitda_low, 5))` | TOP3000 | 0.53 | 0.12 | 8.5% | 60% | weak |
| `rank(anl4_ebitda_low)` | TOP1000 | 0.22 | 0.11 | 43.0% | 60% | bull-only |
| `rank(ts_delta(anl4_ebitda_low, 5))` | TOP1000 | 0.38 | 0.08 | 10.3% | 80% | weak |
| `rank(anl4_ebitda_low / close)` | TOP500 | 0.17 | 0.07 | 37.4% | 60% | bull-only |
| `rank(anl4_ebitda_low / close)` | TOP200 | 0.11 | 0.04 | 35.2% | 60% | bull-only |
| `rank(anl4_ebitda_low)` | TOP500 | 0.12 | 0.04 | 49.1% | 60% | bull-only |
| `rank(ts_delta(anl4_ebitda_low, 5))` | TOP500 | 0.15 | 0.02 | 14.0% | 40% | weak |
| `rank(anl4_ebitda_low)` | TOP200 | 0.05 | 0.02 | 44.8% | 60% | bull-only |
| `rank(ts_delta(anl4_ebitda_low, 5))` | TOP200 | 0.13 | 0.02 | 17.0% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_ebitda_mean: 0.997 (strongly positively correlated)
- anl4_medianepsbfam: 0.996 (strongly positively correlated)
- est_ebitda: 0.991 (strongly positively correlated)
- anl4_ebitda_high: 0.987 (strongly positively correlated)
- anl4_ebit_high: 0.963 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.34 | 1.54 | +0.65 | -0.82 | yes |
| anl4_rd_exp_flag | analyst4 | -0.44 | 1.80 | +0.78 | -0.78 | no |
| fnd6_txtubadjust | fundamental6 | -0.32 | 1.47 | +0.60 | -0.83 | yes |
| news_open_vol | news12 | -0.24 | 1.44 | +0.51 | -0.55 | yes |
| sharesout | pv1 | -0.22 | 1.52 | +0.49 | -0.73 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
