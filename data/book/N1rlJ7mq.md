---
alpha_id: "N1rlJ7mq"
name: "pstkrv_event_magnitude_dual_stab_fcf_buzz"
status: "ACTIVE"
submitted: "2026-07-19"
grade: "EXCELLENT"
sharpe: 2.32
fitness: 2.07
turnover: 0.1109
returns: 0.0994
drawdown: 0.0378
family: "pstkrv_event_magnitude_dual_stabilizer"
mechanism: "Event-magnitude transform on preferred-stock redemption-value changes, dual-stabilized with investing-activities-other and deferred revenue, plus free-cashflow revision flag and buzz-reversal (no leverage leg)"
fields:
  - "fnd6_pstkrv"
  - "fnd6_ivaco"
  - "fnd6_drlt"
  - "anl4_fcf_flag"
  - "scl12_buzz"
  - "returns"
expression: "ts_decay_linear(rank(abs(ts_delta(fnd6_pstkrv / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_fcf_flag) + rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)"
neutralization: "SUBINDUSTRY"
decay: 6
delay: 1
truncation: 0.08
region: "USA"
universe: "TOP3000"
self_corr_max: 0.6903
self_corr_peer: "1YJagrVk"
self_corr_result: "PASS (AUTHORITATIVE — confirmed via BRAIN /alphas/N1rlJ7mq/check: SELF_CORRELATION {result: PASS, value: 0.6903, limit: 0.7}; below auto-pass threshold, no Sharpe-premium escape needed)"
self_corr_method: "brain_api_check_endpoint (authoritative). Confirmed PASS on two independent polls in session 20260719-001."
session: "20260719-001"
brain_url: "https://platform.worldquantbrain.com/alpha/N1rlJ7mq"
tags:
  - "fnd6_pstkrv"
  - "anl4_fcf_flag"
  - "event_magnitude"
  - "preferred_stock"
  - "dual_stabilizer"
  - "buzz_stabilizer"
  - "session_20260719-001"
---

# N1rlJ7mq — Preferred-Stock-Redemption Event-Magnitude + Dual Stabilizer + FCF-Revision + Buzz

## Expression

`ts_decay_linear(rank(abs(ts_delta(fnd6_pstkrv / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_fcf_flag) + rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)`

## Mechanism

Five-factor blend applying the proven `event-magnitude-abs-ts-delta` +
`event-magnitude-dual-stabilizer` template to a previously unexploited
fundamental6 anchor from redundancy cluster #81:

1. **Preferred-stock redemption event magnitude**
   (`rank(abs(ts_delta(fnd6_pstkrv / close, 3)))`): `fnd6_pstkrv` is Preferred
   Stock — Redemption Value. Standalone templates are INFERIOR (best S=0.63),
   but discrete 3-day swings in redemption value (issuance, call/refinance,
   conversion, or remeasurement) are sparse balance-sheet events the market
   underreacts to by magnitude rather than direction.
2. **Dual stabilizer** (`rank(fnd6_ivaco / close) + rank(fnd6_drlt / close)`):
   both investing-activities-other and deferred-revenue legs together, per
   pattern `event-magnitude-dual-stabilizer.md` — lifts sub-universe Sharpe
   and fitness without materially raising correlation.
3. **Free-cashflow revision flag** (`rank(anl4_fcf_flag)`): analyst4 FCF
   forecast-type flag as a fresh densifier (not previously paired with this
   anchor).
4. **Buzz-reversal stabilizer** (`rank(ts_mean(scl12_buzz, 10) * (-1 * returns))`):
   slightly longer buzz window (10 vs usual 5) as a breadth/turnover smoother.

Notably **omits** the usual `rank(-1 * equity / assets)` leverage leg — the
dual stabilizers + FCF + buzz were sufficient for EXCELLENT grade and
LOW_SUB_UNIVERSE_SHARPE PASS (sub-universe Sharpe 1.87 vs limit 1.0).

## Self-Correlation Profile

- Authoritative BRAIN `/check`: **PASS, value=0.6903**, limit=0.7.
- Closest peer: `1YJagrVk` (conglomerate_revision, S=2.37) at 0.690 — shared
  `ivaco` component; margin under 0.70 is thin (~0.01) but clears Gate 1
  without needing the 1.10× Sharpe-premium escape.
- Sibling IV-spread forms on the same anchor (`A1PXkp1Y`, `np2GnbLd`) fail
  `LOW_SUB_UNIVERSE_SHARPE`; the dual-stabilizer + buzz form is the one that
  clears all gates.

## Post-Submission

Submitted by human 2026-07-19. BRAIN confirms `status: ACTIVE`, all
computable checks PASS (including pre-submission SELF_CORRELATION PASS
0.6903).
