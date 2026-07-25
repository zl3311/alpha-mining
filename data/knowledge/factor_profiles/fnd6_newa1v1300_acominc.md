---
field: fnd6_newa1v1300_acominc
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.99
best_fitness: 0.65
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.1855
ann_vol: 0.1532
hit_rate: 0.5247
rolling_sharpe_min: -1.102
rolling_sharpe_max: 2.272
top_merge_partner: fn_incremental_shares_attributable_to_share_based_payment_q
negated_best_sharpe: 0.53
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.46
---
# fnd6_newa1v1300_acominc (fundamental6)

*Accumulated Other Comprehensive Income (Loss)*

## Signal Profile
- `rank(fnd6_newa1v1300_acominc)`: S=0.39, F=0.22, T=2.3%, INFERIOR (TOP200)
- `rank(fnd6_newa1v1300_acominc / close)`: S=0.33, F=0.17, T=2.4%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newa1v1300_acominc, 5))`: S=0.99, F=0.65, T=35.3%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_acominc)`: S=0.11, F=0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_acominc, 5))`: S=0.02, F=0.00, T=35.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_acominc, 22)`: S=0.64, F=0.47, T=27.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_acominc, 10)`: S=-0.20, F=-0.08, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_acominc, 22))`: S=0.69, F=0.42, T=16.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_acominc)`: S=0.39, F=0.16, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_acominc / close)`: S=0.53, F=0.24, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.98, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.31 (negative), ret=-3.6%
  - 2020: S=2.19 (strong), ret=+36.5%
  - 2021: S=0.44 (weak), ret=+6.9%
  - 2022: S=0.79 (moderate), ret=+13.4%
  - 2023: S=1.56 (strong), ret=+20.5%

## Risk & Drawdown
- Max drawdown: 18.55% over 405 days (recovered)
- Annualized: return +15.0%, volatility 15.3% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +0.18, excess kurtosis +3.98

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.10, max 2.27, latest 1.51

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +23.71%; worst month: -7.81%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.19
- Sideways: S=0.77
- Bear: S=0.99

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_acominc / close)` S=0.53, F=0.24, INFERIOR
Direction gap: -0.46 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_acominc)`: S=0.39, F=0.16, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_acominc / close)`: S=0.53, F=0.24, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_acominc, 5))`: S=0.02, F=0.00, T=35.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_acominc, 5))` | TOP1000 | 0.98 | 0.65 | 18.6% | 80% | all-weather |
| `rank(fnd6_newa1v1300_acominc)` | TOP200 | 0.41 | 0.22 | 28.2% | 80% | bear-only |
| `rank(ts_delta(fnd6_newa1v1300_acominc, 5))` | TOP500 | 0.40 | 0.20 | 35.2% | 80% | weak |
| `rank(fnd6_newa1v1300_acominc / close)` | TOP200 | 0.35 | 0.17 | 30.1% | 60% | bear-only |
| `rank(fnd6_newa1v1300_acominc)` | TOP500 | 0.17 | 0.05 | 29.4% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_fiao: -0.208 (weakly negatively correlated)
- fnd6_newa1v1300_aociother: 0.204 (weakly positively correlated)
- fnd6_txpd: -0.153 (weakly negatively correlated)
- fnd6_dc: 0.152 (weakly positively correlated)
- fnd6_optrfr: -0.151 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_incremental_shares_attributable_to_share_based_payment_q | fundamental2 | -0.04 | 1.52 | +0.40 | -0.59 | yes |
| systematic_risk_last_360_days | model51 | -0.08 | 1.44 | +0.43 | -0.12 | yes |
| news_low_exc_stddev | news12 | -0.05 | 1.31 | +0.33 | -0.96 | yes |
| fn_income_taxes_paid_q | fundamental2 | -0.07 | 1.39 | +0.41 | +0.50 | yes |
| rp_ess_mna | news18 | -0.05 | 1.31 | +0.33 | -0.78 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
