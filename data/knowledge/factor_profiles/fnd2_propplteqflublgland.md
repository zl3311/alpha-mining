---
field: fnd2_propplteqflublgland
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.82
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.3267
ann_vol: 0.1768
hit_rate: 0.4947
rolling_sharpe_min: -0.577
rolling_sharpe_max: 2.305
top_merge_partner: fnd6_txtubposdec
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: -0.33
---
# fnd2_propplteqflublgland (fundamental2)

*PPE, Buildings & Land, Useful Life, Maximum*

## Signal Profile
- `rank(fnd2_propplteqflublgland)`: S=0.35, F=0.15, T=1.4%, INFERIOR (TOP200)
- `rank(fnd2_propplteqflublgland / close)`: S=0.45, F=0.28, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_propplteqflublgland, 5))`: S=0.82, F=0.80, T=15.4%, INFERIOR (TOP3000)
- `-rank(fnd2_propplteqflublgland)`: S=0.27, F=0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_propplteqflublgland, 5))`: S=0.49, F=0.37, T=7.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_propplteqflublgland, 22)`: S=0.46, F=0.23, T=0.8%, INFERIOR (TOP3000)
- `ts_mean(fnd2_propplteqflublgland, 10)`: S=-0.13, F=-0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_propplteqflublgland, 22))`: S=0.17, F=0.09, T=9.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_propplteqflublgland)`: S=-0.35, F=-0.15, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_propplteqflublgland / close)`: S=0.36, F=0.18, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.81, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.92 (moderate), ret=+16.1%
  - 2020: S=0.67 (moderate), ret=+11.7%
  - 2021: S=0.31 (weak), ret=+6.0%
  - 2022: S=1.07 (moderate), ret=+13.7%
  - 2023: S=1.23 (moderate), ret=+23.2%

## Risk & Drawdown
- Max drawdown: 32.67% over 499 days (recovered)
- Annualized: return +14.4%, volatility 17.7% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +3.06, excess kurtosis +44.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.58, max 2.31, latest 1.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +23.51%; worst month: -12.12%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.08
- Sideways: S=1.87
- Bear: S=-0.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_propplteqflublgland, 5))` S=0.49, F=0.37, INFERIOR
Direction gap: -0.33 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_propplteqflublgland)`: S=-0.35, F=-0.15, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_propplteqflublgland / close)`: S=0.36, F=0.18, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_propplteqflublgland, 5))`: S=0.49, F=0.37, T=7.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_propplteqflublgland, 5))` | TOP3000 | 0.81 | 0.80 | 32.7% | 100% | bull-only |
| `rank(fnd2_propplteqflublgland / close)` | TOP3000 | 0.45 | 0.28 | 20.8% | 60% | mixed |
| `rank(ts_delta(fnd2_propplteqflublgland, 5))` | TOP1000 | 0.27 | 0.18 | 41.5% | 60% | bull-only |
| `rank(fnd2_propplteqflublgland)` | TOP200 | 0.33 | 0.15 | 9.7% | 60% | bull-only |
| `rank(fnd2_propplteqflublgland / close)` | TOP1000 | 0.17 | 0.06 | 22.3% | 40% | mixed |
| `rank(ts_delta(fnd2_propplteqflublgland, 5))` | TOP500 | 0.13 | 0.06 | 34.9% | 40% | bull-only |
| `rank(fnd2_propplteqflublgland)` | TOP500 | 0.12 | 0.03 | 15.0% | 20% | bull-only |
| `rank(fnd2_propplteqflublgland)` | TOP3000 | 0.12 | 0.02 | 12.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_gwllimrml: 0.276 (weakly positively correlated)
- cap: 0.262 (weakly positively correlated)
- fnd6_cptrank_gvkeymap: -0.258 (weakly negatively correlated)
- call_breakeven_720: 0.253 (weakly positively correlated)
- call_breakeven_360: 0.253 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_txtubposdec | fundamental6 | -0.09 | 1.21 | +0.39 | -0.50 | yes |
| rp_ess_insider | news18 | -0.07 | 1.21 | +0.38 | -0.55 | yes |
| guidance_reporting_currency | analyst4 | -0.04 | 1.17 | +0.34 | -0.79 | yes |
| fnd6_aqc | fundamental6 | +0.00 | 1.14 | +0.33 | -0.84 | yes |
| fnd6_optprcca | fundamental6 | -0.10 | 1.19 | +0.35 | -0.54 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
