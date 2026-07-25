---
field: fnd6_aldo
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.96
best_fitness: 1.38
best_universe: TOP200
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.4801
ann_vol: 0.2713
hit_rate: 0.5296
rolling_sharpe_min: -1.024
rolling_sharpe_max: 3.715
top_merge_partner: fnd2_ebitfr
negated_best_sharpe: 0.56
negated_best_template: rank_neg_delta
negated_best_fitness: 0.42
n_negated_sims: 10
direction_gap: -0.4
---
# fnd6_aldo (fundamental6)

*Long-term Assets of Discontinued Operations*

## Signal Profile
- `rank(fnd6_aldo)`: S=0.96, F=1.38, T=1.4%, AVERAGE (TOP200)
- `rank(fnd6_aldo / close)`: S=0.96, F=1.38, T=1.4%, AVERAGE (TOP200)
- `rank(ts_delta(fnd6_aldo, 5))`: S=0.35, F=0.21, T=11.0%, INFERIOR (TOP3000)
- `-rank(fnd6_aldo)`: S=0.04, F=0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_aldo, 5))`: S=0.56, F=0.42, T=8.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_aldo, 22)`: S=0.52, F=0.19, T=0.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_aldo, 10)`: S=-0.05, F=-0.01, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_aldo, 22))`: S=-0.34, F=-0.21, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aldo)`: S=0.04, F=0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aldo / close)`: S=0.04, F=0.01, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 30F/2P
- LOW_FITNESS: 30F/2P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/12P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.98, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.63 (moderate), ret=+10.6%
  - 2020: S=0.09 (weak), ret=+2.9%
  - 2021: S=0.25 (weak), ret=+7.4%
  - 2022: S=2.22 (strong), ret=+59.8%
  - 2023: S=2.05 (strong), ret=+49.0%

## Risk & Drawdown
- Max drawdown: 48.01% over 344 days (recovered)
- Annualized: return +26.5%, volatility 27.1% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +0.18, excess kurtosis +3.05

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.02, max 3.71, latest 2.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +23.58%; worst month: -23.72%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.90
- Sideways: S=1.26
- Bear: S=0.84

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_aldo, 5))` S=0.56, F=0.42, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_aldo)`: S=0.04, F=0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aldo / close)`: S=0.04, F=0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_aldo, 5))`: S=0.56, F=0.42, T=8.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_aldo)` | TOP200 | 0.98 | 1.38 | 48.0% | 100% | all-weather |
| `rank(fnd6_aldo / close)` | TOP200 | 0.98 | 1.38 | 48.0% | 100% | all-weather |
| `rank(fnd6_aldo / close)` | TOP3000 | 0.54 | 0.31 | 22.7% | 80% | mixed |
| `rank(fnd6_aldo)` | TOP3000 | 0.54 | 0.31 | 22.7% | 80% | mixed |
| `rank(ts_delta(fnd6_aldo, 5))` | TOP3000 | 0.34 | 0.21 | 20.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_aldo, 5))` | TOP200 | 0.29 | 0.17 | 30.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_aldo, 5))` | TOP500 | 0.18 | 0.08 | 36.9% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_beta: 0.316 (weakly positively correlated)
- anl4_afv4_cfps_number: 0.287 (weakly positively correlated)
- anl4_qf_az_div_number: 0.274 (weakly positively correlated)
- anl4_qfd1_az_div_number: 0.274 (weakly positively correlated)
- fnd2_propplteqmuflmblgland: 0.268 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd2_ebitfr | fundamental2 | -0.10 | 1.37 | +0.40 | -0.37 | yes |
| fn_assets_fair_val_l3_a | fundamental2 | -0.08 | 1.45 | +0.43 | +0.36 | yes |
| fnd2_unrgtxbnfinregfprtxps | fundamental2 | -0.09 | 1.36 | +0.39 | -0.36 | yes |
| pv13_revere_company_total | pv13 | -0.03 | 1.44 | +0.39 | -0.21 | yes |
| news_mins_5_pct_up | news12 | -0.05 | 1.30 | +0.32 | -0.50 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
