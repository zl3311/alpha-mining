---
field: fn_effect_of_exchange_rate_on_cash_and_equiv_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 1.29
best_fitness: 1.31
best_universe: TOP1000
grade: AVERAGE
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 26
regime_profile: all-weather
n_variations_with_pnl: 12
max_drawdown: 0.2432
ann_vol: 0.1868
hit_rate: 0.5239
rolling_sharpe_min: -0.491
rolling_sharpe_max: 2.971
top_merge_partner: fnd6_nopio
negated_best_sharpe: -0.21
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.05
n_negated_sims: 4
direction_gap: -1.5
---
# fn_effect_of_exchange_rate_on_cash_and_equiv_a (fundamental2)

*Amount of increase (decrease) from the effect of exchange rate changes on cash and cash equivalent balances held in foreign currencies.*

## Signal Profile
- `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_a)`: S=0.85, F=0.39, T=1.1%, INFERIOR (TOP1000)
- `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_a / close)`: S=0.88, F=0.43, T=1.3%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_a, 5))`: S=1.29, F=1.31, T=23.5%, AVERAGE (TOP1000)
- `-rank(fn_effect_of_exchange_rate_on_cash_and_equiv_a)`: S=-0.85, F=-0.39, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_a, 5))`: S=-0.26, F=-0.12, T=25.9%, INFERIOR (TOP3000)
- `ts_zscore(fn_effect_of_exchange_rate_on_cash_and_equiv_a, 22)`: S=-0.15, F=-0.07, T=10.4%, INFERIOR (TOP3000)
- `ts_mean(fn_effect_of_exchange_rate_on_cash_and_equiv_a, 10)`: S=0.80, F=0.47, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_effect_of_exchange_rate_on_cash_and_equiv_a, 22))`: S=0.89, F=0.93, T=12.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_effect_of_exchange_rate_on_cash_and_equiv_a)`: S=-0.29, F=-0.07, T=0.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_effect_of_exchange_rate_on_cash_and_equiv_a / close)`: S=-0.21, F=-0.05, T=0.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/16P
- LOW_FITNESS: 22F/4P
- LOW_SHARPE: 23F/3P
- LOW_SUB_UNIVERSE_SHARPE: 8F/15P
- LOW_TURNOVER: 5F/21P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.29, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.70 (moderate), ret=+10.0%
  - 2020: S=2.54 (strong), ret=+49.5%
  - 2021: S=0.48 (weak), ret=+13.2%
  - 2022: S=2.79 (strong), ret=+47.4%
  - 2023: S=-0.33 (negative), ret=-1.8%

## Risk & Drawdown
- Max drawdown: 24.32% over 365 days (recovered)
- Annualized: return +24.1%, volatility 18.7% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew +2.77, excess kurtosis +38.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.49, max 2.97, latest -0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +18.35%; worst month: -12.96%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.02
- Sideways: S=0.12
- Bear: S=2.40

## Negated Direction
Best negated: `rank(-1 * fn_effect_of_exchange_rate_on_cash_and_equiv_a / close)` S=-0.21, F=-0.05, INFERIOR
Direction gap: -1.50 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_effect_of_exchange_rate_on_cash_and_equiv_a)`: S=-0.29, F=-0.07, T=0.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_effect_of_exchange_rate_on_cash_and_equiv_a / close)`: S=-0.21, F=-0.05, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_a, 5))`: S=-0.26, F=-0.12, T=25.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_a, 5))` | TOP1000 | 1.29 | 1.31 | 24.3% | 80% | all-weather |
| `rank(ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_a, 5))` | TOP500 | 1.11 | 1.14 | 20.5% | 80% | all-weather |
| `rank(ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_a, 5))` | TOP200 | 0.83 | 0.85 | 40.5% | 60% | all-weather |
| `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_a / close)` | TOP1000 | 0.87 | 0.43 | 3.2% | 100% | all-weather |
| `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_a)` | TOP1000 | 0.85 | 0.39 | 2.9% | 80% | all-weather |
| `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_a)` | TOP200 | 0.39 | 0.16 | 10.9% | 60% | mixed |
| `rank(ts_delta(fn_effect_of_exchange_rate_on_cash_and_equiv_a, 5))` | TOP3000 | 0.29 | 0.15 | 34.1% | 60% | mixed |
| `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_a / close)` | TOP200 | 0.30 | 0.11 | 11.7% | 60% | weak |
| `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_a / close)` | TOP500 | 0.27 | 0.09 | 7.1% | 80% | mixed |
| `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_a)` | TOP500 | 0.27 | 0.08 | 5.6% | 60% | mixed |
| `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_a)` | TOP3000 | 0.29 | 0.07 | 3.6% | 60% | all-weather |
| `rank(fn_effect_of_exchange_rate_on_cash_and_equiv_a / close)` | TOP3000 | 0.19 | 0.05 | 5.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- fn_effect_of_exchange_rate_on_cash_and_equiv_q: 0.298 (weakly positively correlated)
- fnd2_eixrtreclstatelocalitxes: 0.229 (weakly positively correlated)
- fnd2_a_stkdrgprdvalnewissues: 0.188 (weakly positively correlated)
- fnd2_propplteqmuflmeqmt: 0.159 (weakly positively correlated)
- fnd2_a_ltrmdmrepoplinnext12m: 0.153 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_nopio | fundamental6 | -0.06 | 1.88 | +0.59 | -0.32 | yes |
| news_mins_4_pct_dn | news12 | +0.01 | 1.83 | +0.53 | +0.42 | yes |
| anl4_ptp_flag | analyst_revision | -0.02 | 1.94 | +0.51 | +0.96 | yes |
| anl4_ffo_flag | analyst_revision_momentum | +0.00 | 1.83 | +0.49 | +0.47 | yes |
| rp_css_technical | news18 | -0.03 | 1.78 | +0.48 | +0.90 | yes |

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
