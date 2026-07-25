---
field: anl4_afv4_eps_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 1.06
best_fitness: 0.85
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 11
max_drawdown: 0.0988
ann_vol: 0.0759
hit_rate: 0.5053
rolling_sharpe_min: -1.149
rolling_sharpe_max: 3.255
top_merge_partner: rp_ess_revenue
redundancy_cluster: 33
negated_best_sharpe: 0.37
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.69
---
# anl4_afv4_eps_high (analyst4)

*Earnings per share - The highest estimation*

## Signal Profile
- `rank(anl4_afv4_eps_high)`: S=0.47, F=0.30, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_afv4_eps_high / close)`: S=1.06, F=0.85, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_afv4_eps_high, 5))`: S=0.67, F=0.20, T=36.8%, INFERIOR (TOP1000)
- `-rank(anl4_afv4_eps_high)`: S=-0.31, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_eps_high, 5))`: S=0.37, F=0.12, T=35.4%, INFERIOR (TOP3000)
- `ts_zscore(anl4_afv4_eps_high, 22)`: S=0.52, F=0.16, T=35.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_eps_high, 10)`: S=-0.09, F=-0.02, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_eps_high, 22))`: S=0.35, F=0.11, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_eps_high)`: S=-0.40, F=-0.24, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_eps_high / close)`: S=-0.58, F=-0.46, T=3.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.05, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.57 (moderate), ret=+3.6%
  - 2020: S=-0.10 (negative), ret=-1.0%
  - 2021: S=0.84 (moderate), ret=+6.7%
  - 2022: S=3.20 (strong), ret=+22.5%
  - 2023: S=1.44 (moderate), ret=+7.1%

## Risk & Drawdown
- Max drawdown: 9.88% over 457 days (recovered)
- Annualized: return +7.9%, volatility 7.6% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.49, excess kurtosis +2.01

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 3.25, latest 1.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.56%; worst month: -4.18%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=3.25
- Sideways: S=0.09
- Bear: S=-0.31

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_afv4_eps_high, 5))` S=0.37, F=0.12, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_afv4_eps_high)`: S=-0.40, F=-0.24, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_eps_high / close)`: S=-0.58, F=-0.46, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_eps_high, 5))`: S=0.37, F=0.12, T=35.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_eps_high / close)` | TOP3000 | 1.05 | 0.85 | 9.9% | 80% | mixed |
| `rank(anl4_afv4_eps_high / close)` | TOP1000 | 0.65 | 0.50 | 16.9% | 80% | bull-only |
| `rank(anl4_afv4_eps_high / close)` | TOP500 | 0.63 | 0.50 | 18.5% | 80% | bull-only |
| `rank(anl4_afv4_eps_high / close)` | TOP200 | 0.56 | 0.46 | 26.2% | 60% | bull-only |
| `rank(anl4_afv4_eps_high)` | TOP3000 | 0.47 | 0.30 | 36.4% | 80% | bull-only |
| `rank(anl4_afv4_eps_high)` | TOP200 | 0.39 | 0.24 | 26.4% | 60% | bull-only |
| `rank(ts_delta(anl4_afv4_eps_high, 5))` | TOP1000 | 0.67 | 0.20 | 11.2% | 100% | mixed |
| `rank(anl4_afv4_eps_high)` | TOP1000 | 0.31 | 0.16 | 37.7% | 80% | bull-only |
| `rank(ts_delta(anl4_afv4_eps_high, 5))` | TOP3000 | 0.55 | 0.13 | 5.7% | 100% | weak |
| `rank(ts_delta(anl4_afv4_eps_high, 5))` | TOP500 | 0.40 | 0.11 | 8.8% | 80% | weak |
| `rank(anl4_afv4_eps_high)` | TOP500 | 0.22 | 0.10 | 34.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_afv4_median_eps: 0.955 (strongly positively correlated)
- anl4_afv4_eps_mean: 0.948 (strongly positively correlated)
- anl4_afv4_cfps_high: 0.852 (strongly positively correlated)
- anl4_afv4_cfps_mean: 0.849 (strongly positively correlated)
- anl4_afv4_cfps_median: 0.849 (strongly positively correlated)

Redundancy cluster #33: 12 similar fields, mean |rho| 0.787 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.34 | 1.64 | +0.59 | -0.31 | yes |
| anl4_epsr_flag | analyst4 | -0.30 | 1.87 | +0.69 | -0.08 | no |
| fnd6_txtubadjust | fundamental6 | -0.17 | 1.47 | +0.42 | -0.96 | yes |
| news_mins_4_chg | news12 | -0.04 | 1.51 | +0.43 | -0.87 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.29 | 1.63 | +0.48 | -0.36 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
