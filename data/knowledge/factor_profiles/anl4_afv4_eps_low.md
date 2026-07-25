---
field: anl4_afv4_eps_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.85
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1
ann_vol: 0.0794
hit_rate: 0.5028
rolling_sharpe_min: -1.059
rolling_sharpe_max: 2.887
top_merge_partner: fnd6_txtubadjust
redundancy_cluster: 1
negated_best_sharpe: 0.83
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.02
---
# anl4_afv4_eps_low (analyst4)

*Earnings per share - The lowest estimation for annual frequency*

## Signal Profile
- `rank(anl4_afv4_eps_low)`: S=0.37, F=0.22, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_afv4_eps_low / close)`: S=0.85, F=0.62, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_afv4_eps_low, 5))`: S=0.37, F=0.12, T=35.5%, INFERIOR (TOP200)
- `-rank(anl4_afv4_eps_low)`: S=-0.22, F=-0.10, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_eps_low, 5))`: S=0.83, F=0.31, T=37.2%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_afv4_eps_low, 63)`: S=0.14, F=0.03, T=17.1%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_eps_low, 10)`: S=-0.12, F=-0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_eps_low, 22))`: S=-0.48, F=-0.18, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_eps_low)`: S=-0.03, F=-0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_eps_low / close)`: S=-0.23, F=-0.11, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.84, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.60 (moderate), ret=+3.0%
  - 2020: S=-0.65 (negative), ret=-5.3%
  - 2021: S=0.89 (moderate), ret=+8.2%
  - 2022: S=2.75 (strong), ret=+26.0%
  - 2023: S=0.17 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 10.00% over 544 days (recovered)
- Annualized: return +6.7%, volatility 7.9% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.25, excess kurtosis +1.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.06, max 2.89, latest 0.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.94%; worst month: -3.67%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.80
- Sideways: S=-0.11
- Bear: S=-1.66

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_afv4_eps_low, 5))` S=0.83, F=0.31, INFERIOR
Direction gap: -0.02 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_afv4_eps_low)`: S=-0.03, F=-0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_eps_low / close)`: S=-0.23, F=-0.11, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_eps_low, 5))`: S=0.83, F=0.31, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_eps_low / close)` | TOP3000 | 0.84 | 0.62 | 10.0% | 80% | bull-only |
| `rank(anl4_afv4_eps_low / close)` | TOP1000 | 0.48 | 0.33 | 17.8% | 60% | bull-only |
| `rank(anl4_afv4_eps_low)` | TOP3000 | 0.37 | 0.22 | 39.0% | 60% | bull-only |
| `rank(ts_delta(anl4_afv4_eps_low, 5))` | TOP200 | 0.37 | 0.12 | 25.9% | 80% | weak |
| `rank(anl4_afv4_eps_low / close)` | TOP500 | 0.21 | 0.11 | 30.1% | 40% | bull-only |
| `rank(anl4_afv4_eps_low)` | TOP1000 | 0.21 | 0.10 | 38.5% | 60% | bull-only |
| `rank(ts_delta(anl4_afv4_eps_low, 5))` | TOP3000 | 0.36 | 0.07 | 8.3% | 80% | weak |

## Correlation Notes
Top correlates:
- anl4_afv4_eps_mean: 0.939 (strongly positively correlated)
- anl4_qf_az_hgih_spe: 0.932 (strongly positively correlated)
- anl4_qfd1_az_hgih_spe: 0.932 (strongly positively correlated)
- earnings_per_share_average: 0.932 (strongly positively correlated)
- anl4_qf_az_eps_mean: 0.932 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_txtubadjust | fundamental6 | -0.32 | 1.45 | +0.60 | -0.81 | yes |
| rp_ess_revenue | news18 | -0.34 | 1.49 | +0.60 | -0.50 | yes |
| anl4_rd_exp_flag | analyst4 | -0.40 | 1.69 | +0.67 | -0.82 | no |
| news_open_vol | news12 | -0.29 | 1.48 | +0.55 | -0.18 | yes |
| sharesout | pv1 | -0.17 | 1.45 | +0.42 | -0.97 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
