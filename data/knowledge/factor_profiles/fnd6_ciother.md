---
field: fnd6_ciother
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.63
best_fitness: 0.76
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.6218
ann_vol: 0.201
hit_rate: 0.4955
rolling_sharpe_min: -2.343
rolling_sharpe_max: 3.222
top_merge_partner: guidance_reporting_currency
negated_best_sharpe: 0.23
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.4
---
# fnd6_ciother (fundamental6)

*Comp. Inc. - Other Adj.*

## Signal Profile
- `rank(fnd6_ciother)`: S=0.59, F=0.22, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_ciother / close)`: S=0.58, F=0.22, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_ciother, 5))`: S=0.81, F=0.58, T=31.4%, INFERIOR (TOP3000)
- `-rank(fnd6_ciother)`: S=-0.15, F=-0.03, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ciother, 5))`: S=0.23, F=0.10, T=20.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_ciother, 63)`: S=0.63, F=0.76, T=9.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ciother, 10)`: S=-0.08, F=-0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ciother, 22))`: S=0.50, F=0.32, T=20.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ciother)`: S=0.15, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ciother / close)`: S=0.14, F=0.04, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.81, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.45 (strong), ret=+58.4%
  - 2020: S=0.52 (moderate), ret=+9.8%
  - 2021: S=-1.36 (negative), ret=-30.6%
  - 2022: S=2.02 (strong), ret=+33.3%
  - 2023: S=0.59 (moderate), ret=+9.1%

## Risk & Drawdown
- Max drawdown: 62.18% over 1221 days (not yet recovered, ongoing at window end)
- Annualized: return +16.3%, volatility 20.1% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +1.98, excess kurtosis +35.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.34, max 3.22, latest 0.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +29.24%; worst month: -16.94%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.56
- Sideways: S=0.87
- Bear: S=-0.83

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_ciother, 5))` S=0.23, F=0.10, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_ciother)`: S=0.15, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ciother / close)`: S=0.14, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ciother, 5))`: S=0.23, F=0.10, T=20.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_ciother, 5))` | TOP3000 | 0.81 | 0.58 | 62.2% | 80% | bull-only |
| `rank(ts_delta(fnd6_ciother, 5))` | TOP1000 | 0.77 | 0.57 | 19.7% | 60% | all-weather |
| `rank(fnd6_ciother)` | TOP3000 | 0.58 | 0.22 | 3.5% | 60% | mixed |
| `rank(fnd6_ciother / close)` | TOP3000 | 0.57 | 0.22 | 3.6% | 60% | mixed |
| `rank(fnd6_ciother)` | TOP500 | 0.21 | 0.07 | 6.4% | 60% | mixed |
| `rank(fnd6_ciother / close)` | TOP500 | 0.21 | 0.07 | 6.5% | 60% | mixed |
| `rank(ts_delta(fnd6_ciother, 5))` | TOP500 | 0.17 | 0.06 | 23.5% | 40% | mixed |
| `rank(fnd6_ciother / close)` | TOP1000 | 0.11 | 0.03 | 5.7% | 60% | weak |
| `rank(fnd6_ciother)` | TOP1000 | 0.13 | 0.03 | 5.5% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_aociother: 0.203 (weakly positively correlated)
- fnd6_cipen: -0.160 (weakly negatively correlated)
- min_share_count_guidance: 0.159 (weakly positively correlated)
- shares_outstanding_max_guidance: 0.159 (weakly positively correlated)
- min_basic_shares_guidance: 0.159 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| guidance_reporting_currency | analyst4 | -0.01 | 1.16 | +0.33 | -0.65 | yes |
| news_mins_5_chg | news12 | -0.03 | 1.17 | +0.34 | -0.33 | yes |
| fnd2_ebitfr | fundamental2 | +0.02 | 1.18 | +0.30 | -0.57 | yes |
| fnd2_unrgtxbnfinregfprtxps | fundamental2 | +0.04 | 1.19 | +0.27 | -0.90 | yes |
| rp_ess_insider | news18 | +0.03 | 1.15 | +0.31 | -0.19 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
