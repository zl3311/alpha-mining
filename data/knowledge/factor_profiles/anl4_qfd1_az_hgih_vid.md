---
field: anl4_qfd1_az_hgih_vid
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.56
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.2043
ann_vol: 0.126
hit_rate: 0.4964
rolling_sharpe_min: -0.968
rolling_sharpe_max: 2.004
redundancy_cluster: 99
negated_best_sharpe: 0.56
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: 0.01
---
# anl4_qfd1_az_hgih_vid (analyst4)

*Dividend per share - The highest estimation*

## Signal Profile
- `rank(anl4_qfd1_az_hgih_vid)`: S=-0.07, F=-0.01, T=1.3%, INFERIOR (TOP1000)
- `rank(anl4_qfd1_az_hgih_vid / close)`: S=0.46, F=0.25, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_qfd1_az_hgih_vid, 5))`: S=0.55, F=0.25, T=33.6%, INFERIOR (TOP200)
- `-rank(anl4_qfd1_az_hgih_vid)`: S=0.07, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfd1_az_hgih_vid, 5))`: S=-0.55, F=-0.25, T=33.6%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfd1_az_hgih_vid, 22)`: S=0.48, F=0.18, T=33.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfd1_az_hgih_vid, 10)`: S=0.12, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfd1_az_hgih_vid, 22))`: S=0.15, F=0.03, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_hgih_vid)`: S=0.46, F=0.28, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_hgih_vid / close)`: S=0.56, F=0.40, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.53, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.74 (strong), ret=+16.4%
  - 2020: S=0.84 (moderate), ret=+9.9%
  - 2021: S=0.67 (moderate), ret=+8.1%
  - 2022: S=0.08 (weak), ret=+1.3%
  - 2023: S=-0.25 (negative), ret=-2.7%

## Risk & Drawdown
- Max drawdown: 20.43% over 723 days (not yet recovered, ongoing at window end)
- Annualized: return +6.7%, volatility 12.6% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +1.43, excess kurtosis +16.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.97, max 2.00, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +12.15%; worst month: -9.73%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.10
- Sideways: S=0.90
- Bear: S=-0.66

## Negated Direction
Best negated: `rank(-1 * anl4_qfd1_az_hgih_vid / close)` S=0.56, F=0.40, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_qfd1_az_hgih_vid)`: S=0.46, F=0.28, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_hgih_vid / close)`: S=0.56, F=0.40, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfd1_az_hgih_vid, 5))`: S=-0.55, F=-0.25, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_qfd1_az_hgih_vid, 5))` | TOP200 | 0.53 | 0.25 | 20.4% | 80% | bull-only |
| `rank(anl4_qfd1_az_hgih_vid / close)` | TOP1000 | 0.45 | 0.25 | 10.3% | 60% | bull-only |
| `rank(anl4_qfd1_az_hgih_vid / close)` | TOP3000 | 0.43 | 0.21 | 9.2% | 60% | bull-only |
| `rank(ts_delta(anl4_qfd1_az_hgih_vid, 5))` | TOP500 | 0.37 | 0.11 | 9.8% | 80% | weak |
| `rank(ts_delta(anl4_qfd1_az_hgih_vid, 5))` | TOP3000 | 0.17 | 0.03 | 13.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_qf_az_hgih_vid: 1.000 (strongly positively correlated)
- anl4_qfv4_div_mean: 0.292 (weakly positively correlated)
- est_dividend_ps: 0.282 (weakly positively correlated)
- fnd2_asdm: 0.137 (weakly positively correlated)
- fn_income_from_equity_investments_a: 0.128 (weakly positively correlated)

Redundancy cluster #99: 2 similar fields, mean |rho| 1.0 (representative: anl4_qf_az_hgih_vid). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
