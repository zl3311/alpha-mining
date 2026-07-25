---
field: fnd6_txbco
dataset: fundamental6
best_template: rank_delta
best_sharpe: 1.02
best_fitness: 1.07
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1284
ann_vol: 0.1347
hit_rate: 0.4899
rolling_sharpe_min: -0.687
rolling_sharpe_max: 2.338
top_merge_partner: sharesout
negated_best_sharpe: 0.46
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.44
n_negated_sims: 10
direction_gap: -0.56
---
# fnd6_txbco (fundamental6)

*Excess Tax Benefit Stock Options - Cash Flow Operating*

## Signal Profile
- `rank(fnd6_txbco)`: S=0.11, F=0.05, T=5.1%, INFERIOR (TOP200)
- `rank(fnd6_txbco / close)`: S=0.11, F=0.05, T=5.1%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_txbco, 5))`: S=1.02, F=1.07, T=11.8%, AVERAGE (TOP3000)
- `-rank(fnd6_txbco)`: S=0.25, F=0.16, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txbco, 5))`: S=0.45, F=0.29, T=6.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txbco, 22)`: S=-0.15, F=-0.05, T=1.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txbco, 10)`: S=-0.55, F=-0.55, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txbco, 22))`: S=0.46, F=0.36, T=7.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txbco)`: S=0.46, F=0.44, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txbco / close)`: S=0.46, F=0.44, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 30F/2P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.01, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.91 (moderate), ret=+11.2%
  - 2020: S=0.60 (moderate), ret=+9.2%
  - 2021: S=1.34 (moderate), ret=+23.1%
  - 2022: S=2.09 (strong), ret=+25.4%
  - 2023: S=-0.38 (negative), ret=-2.1%

## Risk & Drawdown
- Max drawdown: 12.84% over 281 days (recovered)
- Annualized: return +13.6%, volatility 13.5% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +3.26, excess kurtosis +51.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.69, max 2.34, latest -0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +12.05%; worst month: -4.74%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=3.20
- Sideways: S=0.21
- Bear: S=0.19

## Negated Direction
Best negated: `rank(-1 * fnd6_txbco / close)` S=0.46, F=0.44, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_txbco)`: S=0.46, F=0.44, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txbco / close)`: S=0.46, F=0.44, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txbco, 5))`: S=0.45, F=0.29, T=6.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txbco, 5))` | TOP3000 | 1.01 | 1.07 | 12.8% | 80% | mixed |
| `rank(ts_delta(fnd6_txbco, 5))` | TOP200 | 0.12 | 0.05 | 30.0% | 60% | bull-only |
| `rank(fnd6_txbco)` | TOP200 | 0.10 | 0.05 | 43.8% | 60% | mixed |
| `rank(fnd6_txbco / close)` | TOP200 | 0.10 | 0.05 | 43.8% | 60% | mixed |
| `rank(fnd6_txbco)` | TOP3000 | 0.17 | 0.04 | 10.2% | 80% | mixed |
| `rank(fnd6_txbco / close)` | TOP3000 | 0.17 | 0.04 | 10.1% | 80% | mixed |

## Correlation Notes
Top correlates:
- max_reported_eps_guidance_2: 0.299 (weakly positively correlated)
- min_reported_eps_guidance: 0.299 (weakly positively correlated)
- earnings_per_share_max_guidance: 0.295 (weakly positively correlated)
- earnings_per_share_min_guidance: 0.291 (weakly positively correlated)
- pcr_oi_1080: 0.283 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| sharesout | pv1 | -0.10 | 1.52 | +0.48 | -0.87 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.15 | 1.52 | +0.50 | -0.60 | yes |
| anl4_rd_exp_flag | analyst4 | -0.13 | 1.52 | +0.50 | -0.46 | yes |
| systematic_risk_last_360_days | model51 | -0.13 | 1.52 | +0.51 | +0.57 | yes |
| fn_income_taxes_paid_q | fundamental2 | -0.05 | 1.40 | +0.39 | -0.93 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
