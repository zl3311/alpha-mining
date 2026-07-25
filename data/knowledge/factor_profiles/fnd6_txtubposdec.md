---
field: fnd6_txtubposdec
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 1.14
best_fitness: 1.43
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.25
ann_vol: 0.1883
hit_rate: 0.5142
rolling_sharpe_min: -1.08
rolling_sharpe_max: 2.565
top_merge_partner: fn_assets_fair_val_l3_a
negated_best_sharpe: 0.07
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -1.07
---
# fnd6_txtubposdec (fundamental6)

*Decrease - Current Tax Positions*

## Signal Profile
- `rank(fnd6_txtubposdec)`: S=0.82, F=0.91, T=4.5%, INFERIOR (TOP500)
- `rank(fnd6_txtubposdec / close)`: S=0.82, F=0.91, T=4.5%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_txtubposdec, 5))`: S=0.63, F=0.43, T=7.5%, INFERIOR (TOP500)
- `-rank(fnd6_txtubposdec)`: S=0.04, F=0.01, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubposdec, 5))`: S=0.07, F=0.02, T=5.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txtubposdec, 63)`: S=1.14, F=1.43, T=2.0%, AVERAGE (TOP3000)
- `ts_mean(fnd6_txtubposdec, 10)`: S=0.18, F=0.08, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txtubposdec, 22))`: S=-0.35, F=-0.24, T=9.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubposdec)`: S=-0.06, F=-0.02, T=7.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubposdec / close)`: S=-0.06, F=-0.02, T=7.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 30F/2P
- LOW_FITNESS: 30F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.82, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.41 (strong), ret=+30.5%
  - 2020: S=0.49 (weak), ret=+9.8%
  - 2021: S=1.50 (moderate), ret=+39.7%
  - 2022: S=0.03 (weak), ret=+0.4%
  - 2023: S=-0.36 (negative), ret=-4.5%

## Risk & Drawdown
- Max drawdown: 25.00% over 771 days (not yet recovered, ongoing at window end)
- Annualized: return +15.5%, volatility 18.8% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.66, excess kurtosis +4.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.08, max 2.56, latest -0.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +21.56%; worst month: -10.36%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.09
- Sideways: S=1.36
- Bear: S=1.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txtubposdec, 5))` S=0.07, F=0.02, INFERIOR
Direction gap: -1.07 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_txtubposdec)`: S=-0.06, F=-0.02, T=7.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubposdec / close)`: S=-0.06, F=-0.02, T=7.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubposdec, 5))`: S=0.07, F=0.02, T=5.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txtubposdec)` | TOP500 | 0.82 | 0.91 | 25.0% | 80% | mixed |
| `rank(fnd6_txtubposdec / close)` | TOP500 | 0.82 | 0.91 | 25.0% | 80% | mixed |
| `rank(ts_delta(fnd6_txtubposdec, 5))` | TOP500 | 0.62 | 0.43 | 13.5% | 100% | bull-only |
| `rank(ts_delta(fnd6_txtubposdec, 5))` | TOP1000 | 0.21 | 0.09 | 25.5% | 60% | bull-only |
| `rank(fnd6_txtubposdec / close)` | TOP3000 | 0.24 | 0.08 | 11.3% | 40% | mixed |
| `rank(fnd6_txtubposdec)` | TOP3000 | 0.24 | 0.08 | 11.5% | 40% | mixed |

## Correlation Notes
Top correlates:
- systematic_risk_last_90_days: 0.264 (weakly positively correlated)
- beta_last_90_days_spy: 0.263 (weakly positively correlated)
- anl4_cff_value: 0.258 (weakly positively correlated)
- financing_cashflow_reported_value: 0.258 (weakly positively correlated)
- cashflow_fin: 0.254 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_assets_fair_val_l3_a | fundamental2 | -0.11 | 1.39 | +0.37 | -0.76 | yes |
| fnd2_propplteqflublgland | fundamental2 | -0.09 | 1.21 | +0.39 | -0.50 | yes |
| max_tangible_book_value_per_share_guidance | analyst4 | -0.12 | 1.24 | +0.41 | -0.26 | yes |
| min_tangible_book_value_per_share_guidance | analyst4 | -0.12 | 1.24 | +0.41 | -0.26 | yes |
| fnd2_a_unrgtxbnfitxpenlintacd | fundamental2 | -0.01 | 1.17 | +0.34 | -0.60 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
