---
field: fnd2_a_unrgtxbnfitxpenlintacd
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.69
best_fitness: 0.79
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1572
ann_vol: 0.1461
hit_rate: 0.515
rolling_sharpe_min: -0.385
rolling_sharpe_max: 1.776
top_merge_partner: fnd6_aqc
negated_best_sharpe: 0.21
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.48
---
# fnd2_a_unrgtxbnfitxpenlintacd (fundamental2)

*Amount accrued for interest on an underpayment of income taxes and penalties related to a tax position claimed or expected to be claimed in the tax return.*

## Signal Profile
- `rank(fnd2_a_unrgtxbnfitxpenlintacd)`: S=0.15, F=0.05, T=0.7%, INFERIOR (TOP3000)
- `rank(fnd2_a_unrgtxbnfitxpenlintacd / close)`: S=0.43, F=0.23, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_unrgtxbnfitxpenlintacd, 5))`: S=0.83, F=0.53, T=30.1%, INFERIOR (TOP500)
- `-rank(fnd2_a_unrgtxbnfitxpenlintacd)`: S=-0.04, F=-0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_unrgtxbnfitxpenlintacd, 5))`: S=-0.37, F=-0.20, T=22.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_unrgtxbnfitxpenlintacd, 63)`: S=0.69, F=0.79, T=14.0%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_unrgtxbnfitxpenlintacd, 10)`: S=0.12, F=0.04, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_unrgtxbnfitxpenlintacd, 22))`: S=0.11, F=0.03, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_unrgtxbnfitxpenlintacd)`: S=0.15, F=0.07, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_unrgtxbnfitxpenlintacd / close)`: S=0.21, F=0.11, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.83, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.83 (moderate), ret=+12.2%
  - 2020: S=0.62 (moderate), ret=+8.6%
  - 2021: S=0.34 (weak), ret=+5.2%
  - 2022: S=1.27 (moderate), ret=+21.5%
  - 2023: S=1.24 (moderate), ret=+12.1%

## Risk & Drawdown
- Max drawdown: 15.72% over 92 days (recovered)
- Annualized: return +12.2%, volatility 14.6% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.62, excess kurtosis +5.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.39, max 1.78, latest 1.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +13.05%; worst month: -8.07%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.53
- Sideways: S=0.95
- Bear: S=-0.08

## Negated Direction
Best negated: `rank(-1 * fnd2_a_unrgtxbnfitxpenlintacd / close)` S=0.21, F=0.11, INFERIOR
Direction gap: -0.48 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_unrgtxbnfitxpenlintacd)`: S=0.15, F=0.07, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_unrgtxbnfitxpenlintacd / close)`: S=0.21, F=0.11, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_unrgtxbnfitxpenlintacd, 5))`: S=-0.37, F=-0.20, T=22.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_a_unrgtxbnfitxpenlintacd, 5))` | TOP500 | 0.83 | 0.53 | 15.7% | 100% | mixed |
| `rank(fnd2_a_unrgtxbnfitxpenlintacd / close)` | TOP3000 | 0.42 | 0.23 | 15.4% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_unrgtxbnfitxpenlintacd, 5))` | TOP1000 | 0.42 | 0.18 | 28.1% | 80% | mixed |
| `rank(ts_delta(fnd2_a_unrgtxbnfitxpenlintacd, 5))` | TOP200 | 0.20 | 0.07 | 36.2% | 60% | bull-only |
| `rank(fnd2_a_unrgtxbnfitxpenlintacd / close)` | TOP1000 | 0.14 | 0.05 | 22.5% | 60% | bull-only |
| `rank(fnd2_a_unrgtxbnfitxpenlintacd)` | TOP3000 | 0.14 | 0.05 | 29.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_propplteqmuflmeqmt: 0.207 (weakly positively correlated)
- fnd2_a_allfdbflaccrwriteoffs: 0.202 (weakly positively correlated)
- fnd6_pifo: 0.200 (weakly positively correlated)
- fnd6_oprepsx: 0.191 (weakly positively correlated)
- fnd6_txs: 0.191 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_aqc | fundamental6 | -0.03 | 1.18 | +0.35 | -0.70 | yes |
| news_mins_5_chg | news12 | -0.01 | 1.18 | +0.35 | -0.70 | yes |
| fnd6_idit | fundamental6 | -0.06 | 1.40 | +0.33 | -0.72 | yes |
| min_gross_income_guidance | analyst4 | -0.06 | 1.22 | +0.35 | -0.51 | yes |
| fnd6_txtubposdec | fundamental6 | -0.01 | 1.17 | +0.34 | -0.60 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
