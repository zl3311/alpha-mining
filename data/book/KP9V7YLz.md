---
alpha_id: "KP9V7YLz"
name: "msaq_event_magnitude_ivaco_drlt_ffo_buzz"
status: "ACTIVE"
submitted: "2026-07-14"
session: "20260714-001"
grade: "EXCELLENT"
sharpe: 2.83
fitness: 2.49
turnover: 0.1563
expression: "ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_msaq / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_ffo_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
family: "msaq_event_magnitude_stabilizer_blend"
mechanism: "Marketable-security-adjustment event magnitude combined with investing-activity, deferred-revenue, FFO-revision, and buzz-reversal stabilizers"
fields:
  - "fnd6_newqv1300_msaq"
  - "fnd6_ivaco"
  - "fnd6_drlt"
  - "anl4_ffo_flag"
  - "scl12_buzz"
  - "returns"
neutralization: "SUBINDUSTRY"
decay: 6
delay: 1
truncation: 0.08
region: "USA"
universe: "TOP3000"
self_corr_max: 0.8015
self_corr_peer: "O0Z6NE0b"
self_corr_result: "PASS (BRAIN authoritative Sharpe-premium override)"
self_corr_method: "BRAIN /alphas/KP9V7YLz/check and /correlations/self"
self_corr_caveat: "Correlation exceeds 0.70, but BRAIN passed the check because Sharpe 2.83 exceeds 1.10x the highest correlated peer Sharpe (O0Z6NE0b: 2.10; required: 2.31)."
tags:
  - "fnd6_newqv1300_msaq"
  - "anl4_ffo_flag"
  - "event_magnitude"
  - "buzz_stabilizer"
  - "session_20260714-001"
brain_url: "https://platform.worldquantbrain.com/alpha/KP9V7YLz"
---

# KP9V7YLz — MSAQ Event-Magnitude + FFO-Revision Stabilizer Blend

## Expression

`ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_msaq / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_ffo_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

## Mechanism

Large changes in accumulated other-comprehensive-income marketable-security
adjustments indicate a valuation or portfolio-reallocation event. The
event-magnitude signal is broadened with capital-allocation and deferred-revenue
quality legs, an FFO analyst-revision densifier, and a high-coverage
buzz-reversal stabilizer.

## Self-Correlation Profile

The candidate's maximum BRAIN self-correlation is 0.8015 against the ACTIVE
MSAQ MARKET-neutral sibling `O0Z6NE0b`. It nevertheless passes because its
Sharpe is 2.83, above BRAIN's required 2.31 premium. This makes it valid but
low long-term value; prioritize lower-correlation EXCELLENT+ candidates first.

## Post-Submission

Submitted directly to BRAIN on 2026-07-14. BRAIN accepted the scoring
submission and confirmed the self-correlation PASS at 0.8015 via the
Sharpe-premium override.
