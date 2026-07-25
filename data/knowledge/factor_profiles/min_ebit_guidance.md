---
field: min_ebit_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.9
best_fitness: 0.68
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.156
ann_vol: 0.0787
hit_rate: 0.5239
rolling_sharpe_min: -0.758
rolling_sharpe_max: 3.203
top_merge_partner: fnd2_a_sbcpnargmpmtwopsffesip
redundancy_cluster: 41
negated_best_sharpe: 0.35
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.55
---
# min_ebit_guidance (analyst4)

*Minimum guidance value for Earnings Before Interest and Taxes (EBIT)*

## Signal Profile
- `rank(min_ebit_guidance)`: S=0.90, F=0.68, T=2.2%, INFERIOR (TOP500)
- `rank(min_ebit_guidance / close)`: S=0.24, F=0.10, T=2.3%, INFERIOR (TOP500)
- `rank(ts_delta(min_ebit_guidance, 5))`: S=0.17, F=0.04, T=33.8%, INFERIOR (TOP200)
- `-rank(min_ebit_guidance)`: S=-0.76, F=-0.47, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_ebit_guidance, 5))`: S=0.35, F=0.08, T=36.3%, INFERIOR (TOP3000)
- `ts_zscore(min_ebit_guidance, 22)`: S=0.87, F=0.38, T=43.4%, INFERIOR (TOP3000)
- `ts_mean(min_ebit_guidance, 10)`: S=0.75, F=0.46, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(min_ebit_guidance, 22))`: S=0.08, F=0.01, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * min_ebit_guidance)`: S=-0.90, F=-0.68, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * min_ebit_guidance / close)`: S=-0.24, F=-0.10, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.92, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.67 (moderate), ret=+3.8%
  - 2020: S=0.20 (weak), ret=+1.4%
  - 2021: S=2.52 (strong), ret=+24.8%
  - 2022: S=-0.66 (negative), ret=-6.0%
  - 2023: S=1.77 (strong), ret=+11.5%

## Risk & Drawdown
- Max drawdown: 15.60% over 475 days (recovered)
- Annualized: return +7.2%, volatility 7.9% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew +0.06, excess kurtosis +0.74

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.76, max 3.20, latest 1.85

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +6.26%; worst month: -5.79%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.10
- Sideways: S=1.89
- Bear: S=1.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(min_ebit_guidance, 5))` S=0.35, F=0.08, INFERIOR
Direction gap: -0.55 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * min_ebit_guidance)`: S=-0.90, F=-0.68, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * min_ebit_guidance / close)`: S=-0.24, F=-0.10, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_ebit_guidance, 5))`: S=0.35, F=0.08, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_ebit_guidance)` | TOP500 | 0.92 | 0.68 | 15.6% | 80% | mixed |
| `rank(min_ebit_guidance)` | TOP3000 | 1.03 | 0.64 | 10.6% | 80% | all-weather |
| `rank(min_ebit_guidance)` | TOP1000 | 0.78 | 0.47 | 10.9% | 100% | mixed |
| `rank(min_ebit_guidance)` | TOP200 | 0.47 | 0.30 | 29.9% | 60% | bear-only |
| `rank(min_ebit_guidance / close)` | TOP500 | 0.24 | 0.10 | 31.6% | 60% | bull-only |
| `rank(min_ebit_guidance / close)` | TOP200 | 0.22 | 0.09 | 31.2% | 60% | mixed |
| `rank(min_ebit_guidance / close)` | TOP3000 | 0.16 | 0.06 | 49.8% | 80% | bull-only |
| `rank(ts_delta(min_ebit_guidance, 5))` | TOP200 | 0.18 | 0.04 | 24.2% | 40% | bear-only |

## Correlation Notes
Top correlates:
- operating_profit_max_guidance_qtr: 0.999 (strongly positively correlated)
- anl4_flag_erbfintax: -0.454 (moderately negatively correlated)
- sales_min_guidance_value: 0.348 (weakly positively correlated)
- fnd2_a_sbcpnargmsptawervl: 0.341 (weakly positively correlated)
- correlation_last_360_days_spy: 0.336 (weakly positively correlated)

Redundancy cluster #41: 2 similar fields, mean |rho| 0.999 (representative: operating_profit_max_guidance_qtr). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd2_a_sbcpnargmpmtwopsffesip | fundamental2 | -0.13 | 1.33 | +0.42 | -0.43 | yes |
| fnd2_a_flintasacmamtzcsrld | fundamental2 | -0.06 | 1.37 | +0.40 | -0.53 | yes |
| fn_treasury_stock_shares_a | fundamental2 | -0.07 | 1.29 | +0.37 | -0.83 | yes |
| news_pct_10min | news12 | -0.04 | 1.28 | +0.37 | -0.66 | yes |
| news_open_vol | news12 | -0.00 | 1.30 | +0.38 | -0.54 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
