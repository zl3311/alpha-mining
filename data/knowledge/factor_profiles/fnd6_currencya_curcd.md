---
field: fnd6_currencya_curcd
dataset: fundamental6
best_template: rank_delta
best_sharpe: 1.03
best_fitness: 0.98
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.2909
ann_vol: 0.1779
hit_rate: 0.4899
rolling_sharpe_min: -0.317
rolling_sharpe_max: 2.565
top_merge_partner: anl4_rd_exp_flag
negated_best_sharpe: -0.04
negated_best_template: neg_rank
negated_best_fitness: -0.01
n_negated_sims: 10
direction_gap: -1.07
---
# fnd6_currencya_curcd (fundamental6)

*ISO Currency Code - Company Annual Market*

## Signal Profile
- `rank(fnd6_currencya_curcd)`: S=0.07, F=0.03, T=8.0%, INFERIOR (TOP200)
- `rank(fnd6_currencya_curcd / close)`: S=0.34, F=0.18, T=2.4%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_currencya_curcd, 5))`: S=1.03, F=0.98, T=20.1%, INFERIOR (TOP3000)
- `-rank(fnd6_currencya_curcd)`: S=-0.04, F=-0.01, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_currencya_curcd, 5))`: S=-0.35, F=-0.23, T=9.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_currencya_curcd, 63)`: S=0.13, F=0.06, T=6.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_currencya_curcd, 10)`: S=0.37, F=0.27, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_currencya_curcd, 22))`: S=0.74, F=0.93, T=11.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_currencya_curcd)`: S=-0.26, F=-0.19, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_currencya_curcd / close)`: S=-0.29, F=-0.14, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 23F/9P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.03, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.51 (moderate), ret=+9.7%
  - 2020: S=0.73 (moderate), ret=+13.7%
  - 2021: S=1.25 (moderate), ret=+24.0%
  - 2022: S=2.06 (strong), ret=+35.0%
  - 2023: S=0.64 (moderate), ret=+7.8%

## Risk & Drawdown
- Max drawdown: 29.09% over 245 days (recovered)
- Annualized: return +18.4%, volatility 17.8% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.73, excess kurtosis +8.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.32, max 2.56, latest 0.50

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +16.07%; worst month: -7.93%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.28
- Sideways: S=0.14
- Bear: S=0.55

## Negated Direction
Best negated: `-rank(fnd6_currencya_curcd)` S=-0.04, F=-0.01, INFERIOR
Direction gap: -1.07 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_currencya_curcd)`: S=-0.26, F=-0.19, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_currencya_curcd / close)`: S=-0.29, F=-0.14, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_currencya_curcd, 5))`: S=-0.35, F=-0.23, T=9.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_currencya_curcd, 5))` | TOP3000 | 1.03 | 0.98 | 29.1% | 100% | all-weather |
| `rank(ts_delta(fnd6_currencya_curcd, 5))` | TOP500 | 0.70 | 0.66 | 24.9% | 60% | mixed |
| `rank(ts_delta(fnd6_currencya_curcd, 5))` | TOP200 | 0.50 | 0.41 | 24.7% | 80% | mixed |
| `rank(fnd6_currencya_curcd / close)` | TOP200 | 0.35 | 0.18 | 20.0% | 100% | mixed |
| `rank(ts_delta(fnd6_currencya_curcd, 5))` | TOP1000 | 0.29 | 0.17 | 39.0% | 20% | bull-only |
| `rank(fnd6_currencya_curcd / close)` | TOP500 | 0.29 | 0.14 | 28.5% | 80% | bear-only |
| `rank(fnd6_currencya_curcd / close)` | TOP1000 | 0.17 | 0.07 | 35.3% | 40% | bear-only |
| `rank(fnd6_currencya_curcd)` | TOP200 | 0.08 | 0.03 | 62.0% | 60% | bull-only |
| `rank(fnd6_currencya_curcd)` | TOP3000 | 0.06 | 0.02 | 51.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- max_share_buyback_guidance: 0.227 (weakly positively correlated)
- min_adjusted_funds_from_operations_adj_guidance: 0.227 (weakly positively correlated)
- max_total_goodwill_guidance_2: 0.227 (weakly positively correlated)
- min_custom_eps_guidance: 0.227 (weakly positively correlated)
- max_adjusted_funds_from_operations_adj_guidance: 0.227 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.12 | 1.49 | +0.46 | -0.46 | yes |
| sharesout | pv1 | -0.02 | 1.44 | +0.40 | -0.93 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.11 | 1.45 | +0.42 | -0.55 | yes |
| pv13_revere_company_total | pv13 | +0.04 | 1.45 | +0.39 | -0.67 | yes |
| implied_volatility_call_10 | option8 | -0.08 | 1.48 | +0.44 | -0.16 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
