---
field: fn_antidilutive_securities_excl_from_eps_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.51
best_fitness: 0.32
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 5
max_drawdown: 0.2684
ann_vol: 0.0977
hit_rate: 0.5036
rolling_sharpe_min: -1.467
rolling_sharpe_max: 3.182
redundancy_cluster: 71
negated_best_sharpe: 0.33
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.18
---
# fn_antidilutive_securities_excl_from_eps_a (fundamental2)

*Securities (including those issuable pursuant to contingent stock agreements) that could potentially dilute basic earnings per share (EPS) or earnings per unit (EPU) in the future that were not included in the computation of diluted EPS or EPU because to do so would increase EPS or EPU amounts or decrease loss per share or unit amounts for the period presented.*

## Signal Profile
- `rank(fn_antidilutive_securities_excl_from_eps_a)`: S=0.50, F=0.30, T=2.0%, INFERIOR (TOP200)
- `rank(fn_antidilutive_securities_excl_from_eps_a / close)`: S=0.51, F=0.32, T=2.2%, INFERIOR (TOP200)
- `rank(ts_delta(fn_antidilutive_securities_excl_from_eps_a, 5))`: S=0.46, F=0.20, T=34.4%, INFERIOR (TOP3000)
- `-rank(fn_antidilutive_securities_excl_from_eps_a)`: S=0.11, F=0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_antidilutive_securities_excl_from_eps_a, 5))`: S=0.33, F=0.13, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(fn_antidilutive_securities_excl_from_eps_a, 63)`: S=0.00, F=0.00, T=16.9%, INFERIOR (TOP3000)
- `ts_mean(fn_antidilutive_securities_excl_from_eps_a, 10)`: S=-0.27, F=-0.17, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_antidilutive_securities_excl_from_eps_a, 22))`: S=-0.03, F=0.00, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_antidilutive_securities_excl_from_eps_a)`: S=0.11, F=0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_antidilutive_securities_excl_from_eps_a / close)`: S=-0.03, F=0.00, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.54, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.15 (moderate), ret=+5.2%
  - 2020: S=2.25 (strong), ret=+19.5%
  - 2021: S=0.34 (weak), ret=+4.1%
  - 2022: S=-1.08 (negative), ret=-13.8%
  - 2023: S=1.42 (moderate), ret=+10.5%

## Risk & Drawdown
- Max drawdown: 26.84% over 935 days (not yet recovered, ongoing at window end)
- Annualized: return +5.2%, volatility 9.8% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.22, excess kurtosis +1.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.47, max 3.18, latest 1.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +9.02%; worst month: -5.12%
Positive months: 46%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.19
- Sideways: S=0.35
- Bear: S=2.76

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_antidilutive_securities_excl_from_eps_a, 5))` S=0.33, F=0.13, INFERIOR
Direction gap: -0.18 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_antidilutive_securities_excl_from_eps_a)`: S=0.11, F=0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_antidilutive_securities_excl_from_eps_a / close)`: S=-0.03, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_antidilutive_securities_excl_from_eps_a, 5))`: S=0.33, F=0.13, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_antidilutive_securities_excl_from_eps_a / close)` | TOP200 | 0.54 | 0.32 | 26.8% | 80% | bear-only |
| `rank(fn_antidilutive_securities_excl_from_eps_a)` | TOP200 | 0.54 | 0.30 | 27.2% | 80% | bear-only |
| `rank(ts_delta(fn_antidilutive_securities_excl_from_eps_a, 5))` | TOP3000 | 0.46 | 0.20 | 20.3% | 80% | all-weather |
| `rank(fn_antidilutive_securities_excl_from_eps_a)` | TOP500 | 0.34 | 0.14 | 22.8% | 60% | bear-only |
| `rank(fn_antidilutive_securities_excl_from_eps_a / close)` | TOP500 | 0.33 | 0.14 | 25.5% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fn_antidilutive_securities_excl_from_eps_q: 0.877 (strongly positively correlated)
- fnd6_cshtrq: 0.777 (strongly positively correlated)
- anl4_epsa_flag: 0.714 (strongly positively correlated)
- news_mov_vol: 0.695 (moderately positively correlated)
- volume: 0.682 (moderately positively correlated)

Redundancy cluster #71: 2 similar fields, mean |rho| 0.877 (representative: fn_antidilutive_securities_excl_from_eps_q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
