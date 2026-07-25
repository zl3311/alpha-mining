---
field: fnd6_invrm
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.95
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.2108
ann_vol: 0.1825
hit_rate: 0.5142
rolling_sharpe_min: -0.841
rolling_sharpe_max: 2.326
top_merge_partner: fn_income_taxes_paid_q
negated_best_sharpe: 0.39
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: -0.56
---
# fnd6_invrm (fundamental6)

*Inventories - Raw Materials*

## Signal Profile
- `rank(fnd6_invrm)`: S=0.66, F=0.56, T=3.2%, INFERIOR (TOP500)
- `rank(fnd6_invrm / close)`: S=0.72, F=0.62, T=3.4%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_invrm, 5))`: S=0.95, F=0.63, T=39.6%, INFERIOR (TOP3000)
- `-rank(fnd6_invrm)`: S=-0.46, F=-0.33, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_invrm, 5))`: S=0.11, F=0.03, T=21.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_invrm, 22)`: S=0.40, F=0.32, T=16.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_invrm, 10)`: S=0.45, F=0.28, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_invrm, 22))`: S=0.41, F=0.23, T=19.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_invrm)`: S=0.15, F=0.06, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_invrm / close)`: S=0.39, F=0.26, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.95, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.98 (strong), ret=+29.6%
  - 2020: S=1.18 (moderate), ret=+27.7%
  - 2021: S=0.36 (weak), ret=+5.8%
  - 2022: S=1.08 (moderate), ret=+20.8%
  - 2023: S=0.11 (weak), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 21.08% over 494 days (recovered)
- Annualized: return +17.4%, volatility 18.2% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.74, excess kurtosis +7.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.84, max 2.33, latest -0.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +16.94%; worst month: -10.03%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.08
- Sideways: S=1.66
- Bear: S=1.26

## Negated Direction
Best negated: `rank(-1 * fnd6_invrm / close)` S=0.39, F=0.26, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_invrm)`: S=0.15, F=0.06, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_invrm / close)`: S=0.39, F=0.26, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_invrm, 5))`: S=0.11, F=0.03, T=21.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_invrm, 5))` | TOP3000 | 0.95 | 0.63 | 21.1% | 100% | mixed |
| `rank(fnd6_invrm / close)` | TOP500 | 0.72 | 0.62 | 14.8% | 60% | bull-only |
| `rank(fnd6_invrm)` | TOP500 | 0.65 | 0.56 | 27.7% | 80% | bull-only |
| `rank(fnd6_invrm / close)` | TOP1000 | 0.53 | 0.39 | 15.9% | 80% | bull-only |
| `rank(fnd6_invrm)` | TOP1000 | 0.45 | 0.33 | 22.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_invrm, 5))` | TOP500 | 0.50 | 0.30 | 20.0% | 80% | mixed |
| `rank(ts_delta(fnd6_invrm, 5))` | TOP1000 | 0.56 | 0.30 | 27.8% | 80% | all-weather |
| `rank(fnd6_invrm / close)` | TOP3000 | 0.47 | 0.28 | 15.4% | 60% | bull-only |
| `rank(fnd6_invrm)` | TOP3000 | 0.32 | 0.17 | 28.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dlcch: 0.186 (weakly positively correlated)
- fnd6_newa1v1300_gdwl: 0.154 (weakly positively correlated)
- pv13_revere_term: 0.136 (weakly positively correlated)
- fnd6_prcc: -0.126 (weakly negatively correlated)
- fnd2_a_sbcpnargmsptawervl: -0.126 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_income_taxes_paid_q | fundamental2 | -0.07 | 1.36 | +0.41 | -0.60 | yes |
| fnd2_unrgtxbnfinregfprtxps | fundamental2 | -0.04 | 1.35 | +0.40 | -0.58 | yes |
| fn_assets_fair_val_l3_a | fundamental2 | +0.00 | 1.40 | +0.38 | -0.59 | yes |
| earnings_certainty_rank_derivative | model16 | -0.02 | 1.35 | +0.39 | +0.69 | yes |
| relative_valuation_rank_derivative | model16 | -0.02 | 1.35 | +0.39 | +0.69 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
