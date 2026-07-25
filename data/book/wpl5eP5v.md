---
alpha_id: "wpl5eP5v"
name: "ppegtq_event_magnitude_leverage_ivaco_drlt"
tags:
  - "fnd6_newqv1300_ppegtq"
  - "event_magnitude"
  - "leverage_premium"
  - "fnd6_ivaco"
  - "fnd6_drlt"
  - "session_20260708-001"
submitted: "2026-07-08"
session: "20260708-001"
grade: "EXCELLENT"
sharpe: 2.09
fitness: 2.20
turnover: 0.087
expression: "ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_ppegtq / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close), 5)"
family: "ppegtq_event_magnitude_leverage"
fields:
  - "fnd6_newqv1300_ppegtq"
  - "equity"
  - "assets"
  - "fnd6_ivaco"
  - "fnd6_drlt"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
self_corr_max: 0.6676
self_corr_peer: "0m8GV1Pp"
self_corr_result: "PASS"
self_corr_method: "brain_check"
status: "ACTIVE"
brain_url: "https://platform.worldquantbrain.com/alpha/wpl5eP5v"
---

# Alpha: wpl5eP5v

## Expression

```
ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_ppegtq / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close), 5)
```

## Mechanism

Event-magnitude signal on PP&E gross (fnd6_newqv1300_ppegtq / close): `abs(ts_delta(..., 3))`
captures the SIZE of property/plant/equipment changes regardless of direction. Markets
underreact to the magnitude of capex events — large PP&E jumps (capacity expansion
anticipating demand) or drops (asset writedowns/divestiture) both signal repricing.

Blended with the leverage premium (`rank(-1 * equity / assets)` — high-debt firms earn
a subindustry risk premium) and two stabilizer factors: `fnd6_ivaco / close`
(invested capital) boosts Sharpe/fitness, and `fnd6_drlt / close` (long-term
deferred revenue) fixes LOW_SUB_UNIVERSE_SHARPE. This extends the proven itci event-magnitude pattern
(`event-magnitude-abs-ts-delta`) to a novel event field (ppegtq) not previously used
in event-magnitude form in the book.

## Self-Correlation Profile

- BRAIN `/check` SELF_CORRELATION: **PASS**, value 0.6676 vs limit 0.70.
- Top correlated peer: `0m8GV1Pp` (itci event-magnitude + leverage + drlt, SPECTACULAR,
  S=2.64). Correlation driven by the shared leverage + drlt base + event-magnitude
  structure; the ppegtq event signal itself is decorrelated from itci.
- All 8 BRAIN submission checks PASS (7 computable + self-corr).
- Self-corr 0.6676 is in the 0.6-0.7 range (LOW long-term value per
  submission-priority-long-term rule) — barely passing. Acceptable for submission but
  submit after any lower-corr EXCELLENT+ candidates in the queue.

## Post-Submission

Submitted by the user on 2026-07-08. Status flipped to ACTIVE.
