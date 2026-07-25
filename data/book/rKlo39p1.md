---
alpha_id: "rKlo39p1"
name: "tlcf_event_magnitude_ivaco_drlt_buzz"
tags:
  - "fnd6_tlcf"
  - "event_magnitude"
  - "buzz_stabilizer"
  - "session_20260709-001"
submitted: "2026-07-10"
session: "20260709-001"
grade: "EXCELLENT"
sharpe: 2.13
fitness: 2.22
turnover: 0.1071
expression: "ts_decay_linear(rank(abs(ts_delta(fnd6_tlcf / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
family: "tlcf_event_magnitude_buzz_blend"
neutralization: "SUBINDUSTRY"
decay: 6
self_corr_max: 0.6262
self_corr_peer: "d5Q3ZmWv"
self_corr_result: "PASS"
self_corr_method: "brain_correlations_self_endpoint"
status: "ACTIVE"
brain_url: "https://platform.worldquantbrain.com/alpha/rKlo39p1"
---

# Alpha: rKlo39p1

## Expression

```
ts_decay_linear(rank(abs(ts_delta(fnd6_tlcf / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)
```

## Mechanism

Extends the `event-magnitude-abs-ts-delta` / `event-magnitude-novel-fields` pattern
to `fnd6_tlcf` (Tax Loss Carry Forward), a low-community-usage fundamental6 field
(alphaCount 419, vs typical fundamental6 median ~8000+) not previously used in the
submitted book. The economic mechanism: a sudden change in a firm's tax loss
carryforward balance (`abs(ts_delta(tlcf/close, 3))`) signals a discrete tax event
(loss recognition, utilization, or expiration) that the market under-reacts to in
the short term. This event-magnitude signal is blended with:

- `-1 * equity/assets` (leverage premium — proven decorrelation anchor from the
  `event-magnitude-novel-fields` pattern)
- `fnd6_ivaco/close` (investing-activities-other — proven fitness booster from
  `product-interaction-blend`; captures a distinct capital-allocation dimension)
- `fnd6_drlt/close` (deferred revenue long-term — holds down correlation with the
  broader itci-family event-magnitude cluster, per `event-magnitude-novel-fields`)
- `rank(ts_mean(scl12_buzz, 5) * (-1 * returns))` (buzz-stabilizer, added this
  session as a 5th factor — boosts Sharpe from 1.91→2.13 and fitness from
  1.79→2.22 over the 4-factor base, pushing GOOD→EXCELLENT)

## Self-Correlation Profile

Max correlation 0.6262 vs `d5Q3ZmWv` (event3d_leverage_buzz, S=2.97) — auto-PASS
(no Sharpe premium needed, well under the 0.7 threshold). Full peer breakdown
(BRAIN `/correlations/self`, 5 correlated alphas in book):

| Peer | Family | Corr | Peer Sharpe |
|------|--------|------|--------------|
| d5Q3ZmWv | event3d_leverage_buzz | 0.6262 | 2.97 |
| GrwrVP5G | event_leverage_capital_intensity_product | 0.5487 | 2.04 |
| wpl5eP5v | ppegtq_event_magnitude (ACTIVE) | 0.5299 | 2.09 |
| e7O5EQbJ | coverage_breadth_deferred_revenue_value | 0.4798 | 2.50 |
| 78w5d35x | dd1q_ptpr_itci_intraday_analyst_blend | 0.4676 | 2.34 |

The `-1*equity/assets` + `ivaco` + `drlt` base is shared with the broader
event-magnitude/leverage cluster (hence 4 non-trivial peer correlations in the
0.47-0.63 range), but the `fnd6_tlcf` event field itself is not used anywhere
else in the book, keeping the max correlation comfortably under 0.7.

Note: BRAIN's `/check` endpoint showed `SELF_CORRELATION: PENDING` at time of
verification (did not resolve within the session); the 0.6262 value above is from
the authoritative `/correlations/self` endpoint, which per
`self-corr-threshold.md` auto-passes at <= 0.7 with no Sharpe-premium requirement.
Recommend a final `/check` re-poll immediately before submission to confirm the
`/check` endpoint has caught up and shows `PASS` explicitly.

## Post-Submission

Submitted by the human on 2026-07-10. BRAIN now reports `status: ACTIVE` with
all checks PASS (`SELF_CORRELATION` check no longer listed post-submission,
consistent with the pre-submission `/correlations/self` verification of 0.6262
PASS vs `d5Q3ZmWv`).
