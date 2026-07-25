---
field: fnd6_acdo
dataset: fundamental6
best_template: decay_linear
best_sharpe: 1.38
best_fitness: 1.33
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 40
regime_profile: all-weather
n_variations_with_pnl: 13
max_drawdown: 0.0874
ann_vol: 0.0843
hit_rate: 0.5457
rolling_sharpe_min: -0.639
rolling_sharpe_max: 3.096
top_merge_partner: rp_ess_dividends
negated_best_sharpe: 0.82
negated_best_template: rank_neg_delta
negated_best_fitness: 0.81
n_negated_sims: 12
direction_gap: -0.56
---
# fnd6_acdo (fundamental6)

*Current Assets of Discontinued Operations*

## Signal Profile
- `rank(fnd6_acdo)`: S=1.36, F=1.30, T=1.5%, AVERAGE (TOP3000)
- `rank(fnd6_acdo / close)`: S=1.36, F=1.30, T=1.5%, AVERAGE (TOP3000)
- `rank(ts_delta(fnd6_acdo, 5))`: S=0.08, F=0.02, T=10.7%, INFERIOR (TOP500)
- `ts_decay_linear(rank(fnd6_acdo), 5)`: S=1.38, F=1.33, T=1.4%, AVERAGE (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(fnd6_acdo), ts_std_dev(returns,20)<0.01)`: S=1.17, F=1.10, T=2.5%, AVERAGE (TOP3000)
- `-rank(fnd6_acdo)`: S=-0.35, F=-0.19, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_acdo, 5))`: S=0.82, F=0.81, T=12.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_acdo, 63)`: S=0.38, F=0.28, T=2.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_acdo, 10)`: S=0.45, F=0.31, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_acdo, 22))`: S=0.00, F=0.00, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acdo)`: S=-0.35, F=-0.19, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acdo / close)`: S=-0.35, F=-0.19, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/21P
- LOW_FITNESS: 34F/6P
- LOW_SHARPE: 35F/5P
- LOW_SUB_UNIVERSE_SHARPE: 17F/20P
- LOW_TURNOVER: 1F/39P

## Temporal Behavior
Headline (decay_linear): Overall Sharpe 1.40, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.15 (negative), ret=-0.9%
  - 2020: S=1.47 (moderate), ret=+10.4%
  - 2021: S=2.74 (strong), ret=+28.8%
  - 2022: S=1.10 (moderate), ret=+9.3%
  - 2023: S=1.18 (moderate), ret=+10.4%

## Risk & Drawdown
- Max drawdown: 8.74% over 163 days (not yet recovered, ongoing at window end)
- Annualized: return +11.8%, volatility 8.4% (fraction of booksize)
- Hit rate: 54.6% positive days
- Tail shape: skew +2.11, excess kurtosis +29.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.64, max 3.10, latest 1.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +10.98%; worst month: -4.80%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.89
- Sideways: S=1.32
- Bear: S=1.11

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_acdo, 5))` S=0.82, F=0.81, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_acdo)`: S=-0.35, F=-0.19, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acdo / close)`: S=-0.35, F=-0.19, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_acdo, 5))`: S=0.82, F=0.81, T=12.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `ts_decay_linear(rank(fnd6_acdo), 5)` | TOP3000 | 1.40 | 1.33 | 8.7% | 80% | all-weather |
| `rank(fnd6_acdo / close)` | TOP3000 | 1.38 | 1.30 | 8.8% | 80% | all-weather |
| `rank(fnd6_acdo)` | TOP3000 | 1.38 | 1.30 | 8.8% | 80% | all-weather |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(fnd6_acdo), ts_std_dev(returns,20)<0.01)` | TOP3000 | 1.19 | 1.10 | 14.0% | 80% | all-weather |
| `rank(fnd6_acdo)` | TOP200 | 0.82 | 0.90 | 31.6% | 60% | all-weather |
| `rank(fnd6_acdo / close)` | TOP200 | 0.82 | 0.90 | 31.7% | 60% | all-weather |
| `rank(-1 * ts_delta(fnd6_acdo, 5))` | TOP3000 | 0.56 | 0.42 | 26.0% | 80% | mixed |
| `ts_decay_linear(rank(fnd6_acdo) * rank(volume/adv20), 5)` | TOP3000 | 0.83 | 0.32 | 9.9% | 60% | bull-only |
| `rank(fnd6_acdo)` | TOP500 | 0.48 | 0.31 | 15.2% | 60% | mixed |
| `rank(fnd6_acdo / close)` | TOP500 | 0.47 | 0.31 | 15.2% | 60% | mixed |
| `rank(fnd6_acdo)` | TOP1000 | 0.36 | 0.19 | 11.8% | 60% | mixed |
| `rank(fnd6_acdo / close)` | TOP1000 | 0.35 | 0.19 | 11.8% | 60% | mixed |
| `rank(ts_delta(fnd6_acdo, 5))` | TOP500 | 0.07 | 0.02 | 40.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- est_netdebt: 0.206 (weakly positively correlated)
- anl4_netdebt_low: 0.199 (weakly positively correlated)
- fnd6_optprcby: 0.197 (weakly positively correlated)
- fnd6_intpn: 0.196 (weakly positively correlated)
- anl4_netdebt_mean: 0.193 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_dividends | news18 | -0.01 | 1.99 | +0.59 | -0.80 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.07 | 2.22 | +0.59 | +0.09 | yes |
| implied_volatility_call_120 | option8 | -0.07 | 1.99 | +0.58 | +0.30 | yes |
| implied_volatility_mean_360 | option8 | -0.07 | 1.97 | +0.57 | +0.60 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.02 | 1.98 | +0.53 | -0.28 | yes |

## Actionability
Already in submitted book (alpha: ['Jjnr7VOl', 'omnopQ9k']).
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
