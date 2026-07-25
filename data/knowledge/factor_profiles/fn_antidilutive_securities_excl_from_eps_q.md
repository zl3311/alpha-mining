---
field: fn_antidilutive_securities_excl_from_eps_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.73
best_fitness: 0.56
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.1773
ann_vol: 0.1023
hit_rate: 0.5012
rolling_sharpe_min: -0.993
rolling_sharpe_max: 3.259
redundancy_cluster: 71
negated_best_sharpe: 0.64
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: -0.09
---
# fn_antidilutive_securities_excl_from_eps_q (fundamental2)

*Securities (including those issuable pursuant to contingent stock agreements) that could potentially dilute basic earnings per share (EPS) or earnings per unit (EPU) in the future that were not included in the computation of diluted EPS or EPU because to do so would increase EPS or EPU amounts or decrease loss per share or unit amounts for the period presented.*

## Signal Profile
- `rank(fn_antidilutive_securities_excl_from_eps_q)`: S=0.73, F=0.54, T=2.3%, INFERIOR (TOP200)
- `rank(fn_antidilutive_securities_excl_from_eps_q / close)`: S=0.73, F=0.56, T=2.4%, INFERIOR (TOP200)
- `rank(ts_delta(fn_antidilutive_securities_excl_from_eps_q, 5))`: S=-0.11, F=-0.03, T=38.2%, INFERIOR (TOP200)
- `-rank(fn_antidilutive_securities_excl_from_eps_q)`: S=0.00, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_antidilutive_securities_excl_from_eps_q, 5))`: S=0.64, F=0.26, T=35.9%, INFERIOR (TOP3000)
- `ts_zscore(fn_antidilutive_securities_excl_from_eps_q, 22)`: S=0.11, F=0.03, T=32.1%, INFERIOR (TOP3000)
- `ts_mean(fn_antidilutive_securities_excl_from_eps_q, 10)`: S=0.24, F=0.15, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_antidilutive_securities_excl_from_eps_q, 22))`: S=-0.31, F=-0.11, T=16.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_antidilutive_securities_excl_from_eps_q)`: S=0.17, F=0.06, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_antidilutive_securities_excl_from_eps_q / close)`: S=0.08, F=0.02, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.36 (moderate), ret=+7.1%
  - 2020: S=2.39 (strong), ret=+23.0%
  - 2021: S=1.03 (moderate), ret=+11.8%
  - 2022: S=-0.74 (negative), ret=-10.1%
  - 2023: S=0.64 (moderate), ret=+5.1%

## Risk & Drawdown
- Max drawdown: 17.73% over 763 days (not yet recovered, ongoing at window end)
- Annualized: return +7.5%, volatility 10.2% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.40, excess kurtosis +1.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 3.26, latest 0.72

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +9.27%; worst month: -5.50%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.22
- Sideways: S=0.31
- Bear: S=3.30

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_antidilutive_securities_excl_from_eps_q, 5))` S=0.64, F=0.26, INFERIOR
Direction gap: -0.09 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_antidilutive_securities_excl_from_eps_q)`: S=0.17, F=0.06, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_antidilutive_securities_excl_from_eps_q / close)`: S=0.08, F=0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_antidilutive_securities_excl_from_eps_q, 5))`: S=0.64, F=0.26, T=35.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_antidilutive_securities_excl_from_eps_q / close)` | TOP200 | 0.74 | 0.56 | 17.7% | 80% | bear-only |
| `rank(fn_antidilutive_securities_excl_from_eps_q)` | TOP200 | 0.73 | 0.54 | 16.8% | 80% | bear-only |
| `rank(fn_antidilutive_securities_excl_from_eps_q)` | TOP500 | 0.28 | 0.11 | 21.3% | 60% | bear-only |
| `rank(fn_antidilutive_securities_excl_from_eps_q / close)` | TOP500 | 0.24 | 0.09 | 24.1% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fn_antidilutive_securities_excl_from_eps_a: 0.877 (strongly positively correlated)
- fnd6_cshtrq: 0.736 (strongly positively correlated)
- historical_volatility_150: 0.713 (strongly positively correlated)
- historical_volatility_180: 0.713 (strongly positively correlated)
- parkinson_volatility_150: 0.708 (strongly positively correlated)

Redundancy cluster #71: 2 similar fields, mean |rho| 0.877 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
