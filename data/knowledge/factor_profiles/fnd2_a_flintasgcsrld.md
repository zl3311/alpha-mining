---
field: fnd2_a_flintasgcsrld
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.69
best_fitness: 0.65
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0729
ann_vol: 0.0673
hit_rate: 0.4988
rolling_sharpe_min: -0.832
rolling_sharpe_max: 2.187
redundancy_cluster: 1
negated_best_sharpe: 0.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.39
---
# fnd2_a_flintasgcsrld (fundamental2)

*Finite Lived Intangible Assets Gross, Customer Related*

## Signal Profile
- `rank(fnd2_a_flintasgcsrld)`: S=0.39, F=0.19, T=0.7%, INFERIOR (TOP3000)
- `rank(fnd2_a_flintasgcsrld / close)`: S=0.75, F=0.47, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_flintasgcsrld, 5))`: S=0.41, F=0.18, T=32.4%, INFERIOR (TOP1000)
- `-rank(fnd2_a_flintasgcsrld)`: S=-0.13, F=-0.04, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasgcsrld, 5))`: S=0.30, F=0.10, T=33.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_flintasgcsrld, 22)`: S=0.69, F=0.65, T=13.5%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_flintasgcsrld, 10)`: S=0.06, F=0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_flintasgcsrld, 22))`: S=-0.27, F=-0.11, T=15.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasgcsrld)`: S=-0.39, F=-0.19, T=0.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasgcsrld / close)`: S=-0.75, F=-0.47, T=1.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.74, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.30 (weak), ret=+1.5%
  - 2020: S=0.69 (moderate), ret=+6.5%
  - 2021: S=0.86 (moderate), ret=+6.1%
  - 2022: S=1.43 (moderate), ret=+8.3%
  - 2023: S=0.46 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 7.29% over 278 days (recovered)
- Annualized: return +5.0%, volatility 6.7% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.78, excess kurtosis +4.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.83, max 2.19, latest 0.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +5.12%; worst month: -3.66%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.85
- Sideways: S=-0.17
- Bear: S=-0.81

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_flintasgcsrld, 5))` S=0.30, F=0.10, INFERIOR
Direction gap: -0.39 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_flintasgcsrld)`: S=-0.39, F=-0.19, T=0.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasgcsrld / close)`: S=-0.75, F=-0.47, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasgcsrld, 5))`: S=0.30, F=0.10, T=33.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_flintasgcsrld / close)` | TOP3000 | 0.74 | 0.47 | 7.3% | 100% | bull-only |
| `rank(fnd2_a_flintasgcsrld)` | TOP3000 | 0.39 | 0.19 | 17.1% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_flintasgcsrld, 5))` | TOP1000 | 0.41 | 0.18 | 30.3% | 60% | mixed |
| `rank(ts_delta(fnd2_a_flintasgcsrld, 5))` | TOP500 | 0.32 | 0.12 | 46.8% | 80% | weak |
| `rank(fnd2_a_flintasgcsrld / close)` | TOP1000 | 0.23 | 0.10 | 10.9% | 40% | bull-only |
| `rank(fnd2_a_flintasgcsrld)` | TOP1000 | 0.11 | 0.04 | 18.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_flintasacmamtzcsrld: 0.960 (strongly positively correlated)
- fn_finite_lived_intangible_assets_gross_a: 0.933 (strongly positively correlated)
- fnd2_a_flintasamt1expnext12m: 0.908 (strongly positively correlated)
- fnd2_a_flintasamt1expytwo: 0.906 (strongly positively correlated)
- fnd2_a_flintasamt1expythree: 0.906 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
