---
alpha_id: "6XwZXn97"
status: "PENDING"
grade: "SPECTACULAR"
sharpe: 2.00
fitness: 3.27
turnover: 0.141
family: "buzz_reversal_accumulated"
dataset: "socialmedia12 + analyst4"
fields:
  - "scl12_buzz"
  - "returns"
  - "anl4_bvps_flag"
expression: "ts_decay_linear(zscore(ts_sum(scl12_buzz * (-1 * returns), 10)) + rank(anl4_bvps_flag), 5)"
neutralization: "SUBINDUSTRY"
decay: 10
universe: "TOP3000"
region: "USA"
self_corr_value: 0.329
self_corr_result: "PASS"
self_corr_peer: "vR56vdYd"
brain_checks: "ALL PASS"
session: "20260628-001"
submitted_date: null
platform_url: "https://platform.worldquantbrain.com/alpha/6XwZXn97"
---

# 6XwZXn97 — Accumulated Buzz Reversal + BVPS Revision

## Expression

```
ts_decay_linear(zscore(ts_sum(scl12_buzz * (-1 * returns), 10)) + rank(anl4_bvps_flag), 5)
```

Settings: SUBINDUSTRY neutralization, decay=10, USA TOP3000

## Mechanism

Two-factor blend capturing attention-driven overselling reversion:

1. **Accumulated buzz reversal** (`zscore(ts_sum(scl12_buzz * (-1 * returns), 10))`):
   Stocks that have been consistently discussed on social media AND experiencing
   negative returns over 10 days are deeply oversold due to herding/panic. The
   zscore normalizes this accumulated attention-loss signal across stocks. When
   social media attention fades, these oversold stocks revert.

2. **BVPS revision** (`rank(anl4_bvps_flag)`): Book value per share analyst
   revision acts as a contrarian quality filter. Stocks with positive fundamental
   revisions during social media panic represent the strongest reversion candidates
   (fundamental disconnect from market narrative).

The combination achieves S=2.00, F=3.27 because:
- The accumulated buzz signal has high predictive power (underlying S=1.63 from
  raw buzz*returns) with low turnover (14.1% vs 50%+ for raw signal)
- BVPS revision adds orthogonal information (rho=-0.34 with buzz signal)
- The two mechanisms are temporally complementary (temporal_rho=-0.76)

## Self-Correlation Profile

Self-corr 0.329 — the LOWEST in the entire submitted book. This signal creates
genuinely different position rankings from all existing families because:
- Fundamental value signals rank stocks by cheapness (same stocks always ranked high)
- Analyst revision ranks stocks by positive revisions (overlaps with value)
- Buzz reversal ranks stocks by ATTENTION + RECENT LOSSES — different cross-section

Top correlated peer: vR56vdYd (analyst_revision family, corr=0.329). The low
correlation with all 31 ACTIVE book entries confirms this is a genuinely new
mechanism family.

## Submission Notes

- **HIGH LONG-TERM VALUE**: SPECTACULAR grade + self-corr < 0.4
- Submitting this alpha consumes minimal correlation headroom for future alphas
- Siblings GrwXq7q5 (22-day window) and xAxVAYwn (22-day + netdebt) likely blocked
  after submission (mutual family correlation expected high)
