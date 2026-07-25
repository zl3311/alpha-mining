---
field: fnd6_newa2v1300_recch
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.94
best_fitness: 0.59
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.2138
ann_vol: 0.1494
hit_rate: 0.5182
rolling_sharpe_min: -0.62
rolling_sharpe_max: 2.5
top_merge_partner: pv13_revere_key_sector_total
negated_best_sharpe: 0.38
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.56
---
# fnd6_newa2v1300_recch (fundamental6)

*Accounts Receivable - Decrease (Increase)*

## Signal Profile
- `rank(fnd6_newa2v1300_recch)`: S=0.07, F=0.01, T=2.6%, INFERIOR (TOP200)
- `rank(fnd6_newa2v1300_recch / close)`: S=0.08, F=0.01, T=2.3%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newa2v1300_recch, 5))`: S=0.94, F=0.59, T=35.8%, INFERIOR (TOP1000)
- `-rank(fnd6_newa2v1300_recch)`: S=0.09, F=0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_recch, 5))`: S=-0.61, F=-0.35, T=34.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_recch, 22)`: S=0.20, F=0.08, T=26.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_recch, 10)`: S=0.04, F=0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_recch, 22))`: S=0.47, F=0.24, T=16.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_recch)`: S=0.05, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_recch / close)`: S=0.38, F=0.15, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.93, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+6.7%
  - 2020: S=0.58 (moderate), ret=+9.0%
  - 2021: S=1.00 (moderate), ret=+16.9%
  - 2022: S=0.25 (weak), ret=+3.8%
  - 2023: S=2.50 (strong), ret=+32.0%

## Risk & Drawdown
- Max drawdown: 21.38% over 385 days (recovered)
- Annualized: return +14.0%, volatility 14.9% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.03, excess kurtosis +5.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.62, max 2.50, latest 2.50

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +10.67%; worst month: -12.28%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.47
- Sideways: S=1.11
- Bear: S=1.22

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_recch / close)` S=0.38, F=0.15, INFERIOR
Direction gap: -0.56 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_recch)`: S=0.05, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_recch / close)`: S=0.38, F=0.15, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_recch, 5))`: S=-0.61, F=-0.35, T=34.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa2v1300_recch, 5))` | TOP1000 | 0.93 | 0.59 | 21.4% | 100% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_recch, 5))` | TOP3000 | 0.93 | 0.50 | 24.2% | 60% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_recch, 5))` | TOP500 | 0.69 | 0.43 | 33.1% | 100% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_recch, 5))` | TOP200 | 0.54 | 0.35 | 34.3% | 80% | all-weather |

## Correlation Notes
Top correlates:
- fnd6_mfma2_recch: 0.384 (weakly positively correlated)
- fnd6_newa1v1300_aociother: 0.126 (weakly positively correlated)
- news_mins_20_pct_up: -0.122 (weakly negatively correlated)
- news_mins_20_chg: -0.122 (weakly negatively correlated)
- fnd6_optrfr: 0.121 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_revere_key_sector_total | pv13 | -0.03 | 1.26 | +0.33 | -0.95 | yes |
| fn_income_taxes_paid_q | fundamental2 | -0.07 | 1.36 | +0.42 | +0.87 | yes |
| systematic_risk_last_360_days | model51 | -0.01 | 1.35 | +0.34 | -0.80 | yes |
| fnd2_q_flintasamt1expyfour | fundamental2 | -0.01 | 1.32 | +0.39 | -0.20 | yes |
| rp_css_technical | news18 | +0.01 | 1.50 | +0.31 | -0.85 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
