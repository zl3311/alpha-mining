---
field: fnd6_tfvce
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.99
best_fitness: 0.91
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.1044
ann_vol: 0.1078
hit_rate: 0.5206
rolling_sharpe_min: -0.089
rolling_sharpe_max: 2.052
top_merge_partner: anl4_tot_gw_ft
negated_best_sharpe: 0.14
negated_best_template: neg_rank_level
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.85
---
# fnd6_tfvce (fundamental6)

*Total Fair Value Changes including Earnings*

## Signal Profile
- `rank(fnd6_tfvce)`: S=0.98, F=0.90, T=3.0%, INFERIOR (TOP1000)
- `rank(fnd6_tfvce / close)`: S=0.99, F=0.91, T=3.1%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_tfvce, 5))`: S=0.40, F=0.23, T=13.5%, INFERIOR (TOP3000)
- `-rank(fnd6_tfvce)`: S=-0.98, F=-0.90, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_tfvce, 5))`: S=-0.15, F=-0.06, T=6.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_tfvce, 22)`: S=-0.38, F=-0.15, T=4.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_tfvce, 10)`: S=0.73, F=0.61, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_tfvce, 22))`: S=-0.25, F=-0.16, T=9.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tfvce)`: S=0.14, F=0.08, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tfvce / close)`: S=0.04, F=0.01, T=4.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 30F/2P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.99, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.68 (moderate), ret=+5.1%
  - 2020: S=0.86 (moderate), ret=+10.5%
  - 2021: S=1.04 (moderate), ret=+13.2%
  - 2022: S=1.06 (moderate), ret=+8.3%
  - 2023: S=1.34 (moderate), ret=+15.3%

## Risk & Drawdown
- Max drawdown: 10.44% over 134 days (recovered)
- Annualized: return +10.7%, volatility 10.8% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.53, excess kurtosis +14.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.09, max 2.05, latest 1.32

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +10.91%; worst month: -5.76%
Positive months: 68%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.10
- Sideways: S=1.74
- Bear: S=1.45

## Negated Direction
Best negated: `rank(-1 * fnd6_tfvce)` S=0.14, F=0.08, INFERIOR
Direction gap: -0.85 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_tfvce)`: S=0.14, F=0.08, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tfvce / close)`: S=0.04, F=0.01, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_tfvce, 5))`: S=-0.15, F=-0.06, T=6.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_tfvce / close)` | TOP1000 | 0.99 | 0.91 | 10.4% | 100% | mixed |
| `rank(fnd6_tfvce)` | TOP1000 | 0.98 | 0.90 | 10.4% | 100% | mixed |
| `rank(fnd6_tfvce / close)` | TOP500 | 0.48 | 0.33 | 23.3% | 60% | mixed |
| `rank(fnd6_tfvce)` | TOP500 | 0.47 | 0.33 | 22.8% | 60% | mixed |
| `rank(ts_delta(fnd6_tfvce, 5))` | TOP3000 | 0.39 | 0.23 | 40.9% | 60% | mixed |
| `rank(ts_delta(fnd6_tfvce, 5))` | TOP500 | 0.16 | 0.07 | 40.6% | 80% | bull-only |
| `rank(ts_delta(fnd6_tfvce, 5))` | TOP1000 | 0.13 | 0.04 | 45.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_gwllimrml: 0.212 (weakly positively correlated)
- fnd6_pstkrv: -0.160 (weakly negatively correlated)
- fnd6_pstkl: -0.159 (weakly negatively correlated)
- fn_comp_not_rec_stock_options_a: 0.144 (weakly positively correlated)
- fnd6_optlifeq: -0.132 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_tot_gw_ft | analyst4 | -0.06 | 1.45 | +0.42 | -0.43 | yes |
| rp_css_ptg | news18 | -0.07 | 1.46 | +0.46 | +0.20 | yes |
| systematic_risk_last_360_days | model51 | +0.03 | 1.40 | +0.39 | -0.72 | yes |
| implied_volatility_call_10 | option8 | -0.04 | 1.46 | +0.43 | -0.26 | yes |
| news_open_vol | news12 | -0.09 | 1.40 | +0.41 | -0.47 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
