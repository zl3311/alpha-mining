---
pattern: "event-magnitude-novel-fields"
discovered: "20260708-001"
applicable_to: "fundamental6 event-detection; decorrelated EXCELLENT alpha generation"
confidence: "high (13-field screen, 4 fields produced GOOD+ event-magnitude)"
---

# Pattern: Event-Magnitude (abs(ts_delta)) Transfers Beyond itci

## The finding

The `event-magnitude-abs-ts-delta` pattern claimed "only itci produces strong signal."
This session disproved that constraint: `abs(ts_delta(FIELD / close, 3))` produces
GOOD+ signal on several other fundamental6 fields when combined with the leverage
premium + a stabilizer, and reaches EXCELLENT on ppegtq with a 4-factor blend.

## Template

```
ts_decay_linear(rank(abs(ts_delta(FIELD / close, D))) + rank(-1 * equity / assets) + STABILIZER, 5)
```

## Novel-event-field screen (session 20260708-001, d=3 or 5, + leverage + drlt)

| Field | Best expr | S | F | Grade | Self-corr vs book |
|-------|-----------|---|---|-------|-------------------|
| fnd6_itci (control) | d=3 + leverage + drlt | 2.62 | 2.73 | SPECTACULAR | blocked (itci family) |
| fnd6_newqv1300_ppegtq | d=3 + leverage + drlt | 1.72 | 1.74 | GOOD | **PASS 0.660** vs 0m8GV1Pp |
| fnd6_cshtr | d=3 + leverage + drlt | 1.89 | 1.58 | GOOD | FAIL 0.793 |
| fnd6_drc | d=5 + leverage + drlt | 1.83 | 1.52 | GOOD | FAIL 0.753 |
| fnd6_dd1q | d=3 + leverage + drlt | 1.65 | 1.51 | GOOD | **PASS 0.680** |
| sales_estimate_count_quarterly | d=3 + leverage + drlt | 1.77 | 1.42 | AVERAGE | n/a |

## EXCELLENT breakthrough: 4-factor with ivaco stabilizer

The 3-factor novel-event blends cap at GOOD (F~1.5-1.74). Replacing drlt with
`fnd6_ivaco / close` OR adding ivaco as a 4th stabilizer boosts Sharpe/fitness:

```
ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_ppegtq / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close), 5)
```

- wpl5eP5v: **EXCELLENT S=2.09 F=2.20**, self-corr **PASS 0.6676**, all 8 checks PASS.

## Self-corr structure

The leverage + drlt base is shared with the itci event-magnitude family (0m8GV1Pp,
le0gY6Ze, etc.), giving a corr floor ~0.55-0.66. The event FIELD determines whether
corr stays under 0.7:
- ppegtq, dd1q event signals → corr 0.66-0.68 (PASS)
- drc, cshtr event signals → corr 0.75-0.79 (FAIL)

ivaco as a stabilizer adds Sharpe but is shared with several book entries; alone
(ppegtq+leverage+ivaco, 3-factor) it pushes corr to FAIL. Combined with drlt in the
4-factor wpl5eP5v it stays PASS (0.6676) — the drlt component holds the itci-family
corr down while ivaco lifts fitness.

## When to use

- Need a decorrelated EXCELLENT event-magnitude alpha: start from ppegtq or dd1q.
- Do NOT use drc/cshtr event-magnitude (self-corr FAIL vs itci family).
- Boost fitness to EXCELLENT by adding `fnd6_ivaco / close` as a 4th factor alongside
  drlt — but verify self-corr (headroom is thin, ~0.03-0.04).

## What doesn't work

- Dual-event blends (ppegtq event + dd1q event) → AVERAGE (events cancel, no boost).
- Longer delta windows (d=5, d=10) on ppegtq → lower fitness (1.45-1.72 vs 1.74 at d=3).
- decay=10 wrap → marginal (no fitness gain).
- Adding dlto as 4th factor → self-corr FAIL (dlto shared with many book entries).
