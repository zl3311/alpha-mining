---
field: anl4_cfo_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.83
best_fitness: 0.64
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1799
ann_vol: 0.0905
hit_rate: 0.5053
rolling_sharpe_min: -1.806
rolling_sharpe_max: 2.862
top_merge_partner: fnd6_txtubadjust
redundancy_cluster: 1
negated_best_sharpe: 0.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.58
---
# anl4_cfo_high (analyst4)

*Cash Flow From Operations - The highest value among forecasts*

## Signal Profile
- `rank(anl4_cfo_high)`: S=0.49, F=0.34, T=1.5%, INFERIOR (TOP3000)
- `rank(anl4_cfo_high / close)`: S=0.83, F=0.64, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_cfo_high, 5))`: S=0.58, F=0.16, T=36.9%, INFERIOR (TOP3000)
- `-rank(anl4_cfo_high)`: S=-0.22, F=-0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfo_high, 5))`: S=0.25, F=0.06, T=37.0%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_cfo_high, 63)`: S=-0.07, F=-0.01, T=17.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_cfo_high, 10)`: S=0.11, F=0.04, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cfo_high, 22))`: S=-0.15, F=-0.03, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_high)`: S=-0.09, F=-0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_high / close)`: S=-0.12, F=-0.04, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.82, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.05 (negative), ret=-0.3%
  - 2020: S=-1.48 (negative), ret=-11.3%
  - 2021: S=1.80 (strong), ret=+21.5%
  - 2022: S=1.80 (strong), ret=+20.6%
  - 2023: S=0.99 (moderate), ret=+6.0%

## Risk & Drawdown
- Max drawdown: 17.99% over 565 days (recovered)
- Annualized: return +7.5%, volatility 9.0% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.26, excess kurtosis +1.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.81, max 2.86, latest 0.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +9.57%; worst month: -3.48%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.71
- Sideways: S=0.44
- Bear: S=-2.64

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cfo_high, 5))` S=0.25, F=0.06, INFERIOR
Direction gap: -0.58 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_cfo_high)`: S=-0.09, F=-0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_high / close)`: S=-0.12, F=-0.04, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfo_high, 5))`: S=0.25, F=0.06, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cfo_high / close)` | TOP3000 | 0.82 | 0.64 | 18.0% | 60% | bull-only |
| `rank(anl4_cfo_high)` | TOP3000 | 0.48 | 0.34 | 35.9% | 80% | bull-only |
| `rank(ts_delta(anl4_cfo_high, 5))` | TOP3000 | 0.59 | 0.16 | 5.0% | 80% | mixed |
| `rank(anl4_cfo_high / close)` | TOP1000 | 0.31 | 0.16 | 21.6% | 40% | bull-only |
| `rank(anl4_cfo_high)` | TOP1000 | 0.21 | 0.10 | 37.3% | 60% | bull-only |
| `rank(anl4_cfo_high / close)` | TOP500 | 0.12 | 0.04 | 36.2% | 60% | bull-only |
| `rank(ts_delta(anl4_cfo_high, 5))` | TOP1000 | 0.20 | 0.04 | 12.0% | 40% | mixed |
| `rank(anl4_cfo_high)` | TOP500 | 0.08 | 0.03 | 47.1% | 80% | bull-only |

## Correlation Notes
Top correlates:
- anl4_cfo_median: 0.995 (strongly positively correlated)
- anl4_cfo_mean: 0.995 (strongly positively correlated)
- est_cashflow_op: 0.979 (strongly positively correlated)
- anl4_cfo_low: 0.978 (strongly positively correlated)
- anl4_ebit_high: 0.948 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_txtubadjust | fundamental6 | -0.33 | 1.44 | +0.59 | -0.81 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.47 | +0.58 | -0.85 | yes |
| anl4_rd_exp_flag | analyst4 | -0.44 | 1.76 | +0.73 | -0.76 | no |
| news_open_vol | news12 | -0.25 | 1.40 | +0.47 | -0.57 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.33 | 1.42 | +0.59 | -0.91 | no |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
