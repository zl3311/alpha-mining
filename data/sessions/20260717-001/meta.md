---
id: "20260717-001"
date: "2026-07-17"
strategy: "EXPLORE"
research_question: "Can fresh fundamental2 event-magnitude anchors (goodwill, annual/L3 fair value, FX-on-cash, M&A, debt carrying, nopio) plus novel operator trees and densifier tweaks produce a decorrelated EXCELLENT+ alpha?"
budget_used: 52
budget_cap: null
trigger: "manual (user-initiated, no budget constraint, find minimal submittable EXCELLENT+; do not submit, present + draft PR; local BRAIN client — HF offline)"
gate_passers: 15
submissions: 1
submittable_candidates: 1
submitted: ["N1rY5ZJg"]
submitted_date: "2026-07-17"
status: "productive"
tags:
  - "session_20260717-001"
  - "EXPLORE"
  - "event_magnitude"
  - "local_brain"
candidates:
  - id: "N1rY5ZJg"
    grade: "EXCELLENT"
    sharpe: 2.23
    fitness: 2.20
    self_corr_value: 0.6638
    self_corr_result: "PASS (AUTHORITATIVE)"
    verdict: "SUBMITTED"
    status: "ACTIVE (submitted 2026-07-17 by human)"
  - id: "mLbEAk05"
    grade: "GOOD"
    sharpe: 1.78
    fitness: 1.58
    self_corr_value: 0.6646
    self_corr_result: "PASS"
    verdict: "REDUNDANT (same anchor, lower grade)"
  - id: "MPQJ8QR6"
    grade: "GOOD"
    sharpe: 1.96
    fitness: 1.88
    self_corr_value: 0.6919
    self_corr_result: "PASS"
    verdict: "REDUNDANT (same anchor, below EXCELLENT F)"
  - id: "LL106da6"
    grade: "EXCELLENT"
    sharpe: 2.25
    fitness: 2.16
    self_corr_value: 0.7941
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "XgndlqrX"
    grade: "GOOD"
    sharpe: 2.05
    fitness: 2.00
    self_corr_value: 0.7248
    self_corr_result: "FAIL"
    verdict: "BLOCKED (OC alone raises corr)"
best_alpha: "N1rY5ZJg"
best_grade: "EXCELLENT"
best_sharpe: 2.23
best_fitness: 2.20
best_self_corr: 0.6638
best_self_corr_peer: "rKlo39p1"
best_self_corr_method: "AUTHORITATIVE BRAIN /alphas/N1rY5ZJg/check"
---

# Session 20260717-001: EXPLORE — Fresh fnd2 Anchors + Sales Densifier

## Outcome

**Found:** [N1rY5ZJg](https://platform.worldquantbrain.com/alpha/N1rY5ZJg) —
EXCELLENT, S=2.23, F=2.20, T=7.8%, **all 8 BRAIN checks PASS**, including
authoritative `SELF_CORRELATION: PASS value=0.6638` vs `rKlo39p1`.
Initially presented as PENDING (agent does not submit). **Update 2026-07-17:**
human submitted; BRAIN confirms **ACTIVE**, peer self-corr 0.6638 vs
`rKlo39p1` (ALREADY_SUBMITTED on `/check`). Book + submit queue updated.

## Context Assessment (Phase 0)

- Book: 47 ACTIVE + 10 PENDING across 54 families.
- No open HYPOTHESIS opportunities → DEFAULT EXPLORE.
- HF server offline; all sims via local `BrainClient`.
- Event-magnitude family saturated on itci/txw/tlcf/ppegt/L2-fair-val; pursued
  unused annual/L3/goodwill/nopio/debt-carry anchors.

## Discovery Path (3 completed rounds, 52 sims)

1. **Round 1 (18)**: novel trees + event-magnitude backstop on fresh anchors.
   SPECTACULAR `LL106da6` (nopio) and several EXCELLENT/GOOD gate-passers.
2. **Self-corr filter**: nopio/debt/fairval with `buzz*(-ret)` FAIL (~0.76–0.81);
   `mLbEAk05` (liab_fair_val_a + ffo, no buzz*-ret) PASS 0.665 but only GOOD.
3. **Round 2–3**: fitness push. OC alone → `XgndlqrX` F=2.00 but FAIL 0.725.
   **OC + `sales_estimate_count_quarterly` → `N1rY5ZJg` EXCELLENT + PASS 0.664.**

## Key Findings

1. `fn_liab_fair_val_a` (annual) is a viable fresh sibling of ACTIVE
   `fn_liab_fair_val_l2_q` / `fn_assets_fair_val_l2_q`.
2. `open/close` boosts fitness but often raises self-corr above 0.70; pairing
   with `sales_estimate_count_quarterly` restores PASS while clearing EXCELLENT.
3. `fnd6_nopio` reaches SPECTACULAR/EXCELLENT easily but sits deep inside the
   event-magnitude self-corr cluster (~0.79–0.82) with standard buzz*-ret legs.

## Next Steps

- Human may submit `N1rY5ZJg` via platform URL.
- Reuse sales-count densifier pattern on other GOOD PASS bases short of F>2.0.
- Avoid further plain nopio event-magnitude + buzz*-ret variants without a
  stronger decorrelation edit.
