---
field: fnd6_lcoxdr
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.92
best_fitness: 0.55
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1681
ann_vol: 0.1377
hit_rate: 0.5077
rolling_sharpe_min: -0.866
rolling_sharpe_max: 3.353
top_merge_partner: fnd2_unrgtxbnfinregfprtxps
negated_best_sharpe: 0.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.62
---
# fnd6_lcoxdr (fundamental6)

*Current Liabilities - Other - Excluding Deferred Revenue*

## Signal Profile
- `rank(fnd6_lcoxdr)`: S=0.54, F=0.27, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_lcoxdr / close)`: S=0.66, F=0.32, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_lcoxdr, 5))`: S=0.92, F=0.55, T=34.7%, INFERIOR (TOP500)
- `-rank(fnd6_lcoxdr)`: S=-0.17, F=-0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lcoxdr, 5))`: S=0.30, F=0.09, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_lcoxdr, 22)`: S=0.15, F=0.05, T=28.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_lcoxdr, 10)`: S=-0.09, F=-0.02, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_lcoxdr, 22))`: S=-0.03, F=0.00, T=15.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lcoxdr)`: S=-0.54, F=-0.27, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lcoxdr / close)`: S=-0.66, F=-0.32, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.92, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.92 (strong), ret=+21.6%
  - 2020: S=0.11 (weak), ret=+1.5%
  - 2021: S=0.02 (weak), ret=+0.2%
  - 2022: S=0.81 (moderate), ret=+13.1%
  - 2023: S=2.14 (strong), ret=+25.8%

## Risk & Drawdown
- Max drawdown: 16.81% over 491 days (recovered)
- Annualized: return +12.7%, volatility 13.8% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.39, excess kurtosis +4.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.87, max 3.35, latest 2.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +12.07%; worst month: -8.72%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.64
- Sideways: S=0.21
- Bear: S=0.84

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_lcoxdr, 5))` S=0.30, F=0.09, INFERIOR
Direction gap: -0.62 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_lcoxdr)`: S=-0.54, F=-0.27, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lcoxdr / close)`: S=-0.66, F=-0.32, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lcoxdr, 5))`: S=0.30, F=0.09, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_lcoxdr, 5))` | TOP500 | 0.92 | 0.55 | 16.8% | 100% | all-weather |
| `rank(fnd6_lcoxdr / close)` | TOP3000 | 0.66 | 0.32 | 5.5% | 40% | bull-only |
| `rank(fnd6_lcoxdr)` | TOP3000 | 0.54 | 0.27 | 13.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_lcoxdr, 5))` | TOP200 | 0.41 | 0.19 | 48.9% | 80% | all-weather |
| `rank(ts_delta(fnd6_lcoxdr, 5))` | TOP1000 | 0.31 | 0.09 | 19.2% | 60% | mixed |
| `rank(fnd6_lcoxdr / close)` | TOP1000 | 0.25 | 0.08 | 11.2% | 40% | bull-only |
| `rank(fnd6_lcoxdr / close)` | TOP500 | 0.15 | 0.05 | 16.9% | 40% | bull-only |
| `rank(fnd6_lcoxdr)` | TOP1000 | 0.17 | 0.05 | 20.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_nopio: 0.163 (weakly positively correlated)
- fnd6_txpd: 0.138 (weakly positively correlated)
- fnd6_ivao: 0.135 (weakly positively correlated)
- fnd6_cisecgl: 0.132 (weakly positively correlated)
- anl4_ptpr_number: -0.117 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd2_unrgtxbnfinregfprtxps | fundamental2 | -0.09 | 1.36 | +0.44 | -0.70 | yes |
| fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q | fundamental2 | -0.05 | 1.50 | +0.35 | -0.83 | yes |
| rp_css_ptg | news18 | -0.01 | 1.34 | +0.34 | -0.91 | yes |
| net_debt_amount | analyst4 | -0.10 | 1.30 | +0.38 | -0.47 | yes |
| fn_interest_paid_net_a | fundamental2 | -0.06 | 1.27 | +0.35 | -0.71 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
