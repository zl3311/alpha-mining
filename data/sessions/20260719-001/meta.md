---
id: "20260719-001"
date: "2026-07-19"
strategy: "EXPLORE"
research_question: "Can existing recent EXCELLENT+ gate-passers on fresh anchors (or newly mined dual-stabilizer / novel-structure variants) clear all BRAIN gates including authoritative self-corr, yielding a minimal submittable EXCELLENT+ alpha?"
budget_used: 0
budget_cap: null
trigger: "manual (user-initiated, no budget constraint, find minimal submittable EXCELLENT+; do not submit, present + draft PR)"
gate_passers: 1
submissions: 1
submitted: ["N1rlJ7mq"]
submitted_date: "2026-07-19"
submittable_candidates: 1
status: "productive"
best_alpha: "N1rlJ7mq"
best_grade: "EXCELLENT"
best_sharpe: 2.32
best_fitness: 2.07
best_self_corr: 0.6903
best_self_corr_peer: "1YJagrVk"
best_self_corr_method: "AUTHORITATIVE BRAIN /alphas/N1rlJ7mq/check (PASS 0.6903; confirmed on 2 independent polls)"
rounds: 1
simulations: 0
tags:
  - "session_20260719-001"
  - "EXPLORE"
  - "event_magnitude"
  - "validation_of_existing"
candidates:
  - id: "N1rlJ7mq"
    grade: "EXCELLENT"
    sharpe: 2.32
    fitness: 2.07
    self_corr_value: 0.6903
    self_corr_result: "PASS"
    verdict: "SUBMITTED"
    status: "ACTIVE (submitted 2026-07-19 by human)"
  - id: "xAd6K9Np"
    grade: "EXCELLENT"
    sharpe: 1.91
    fitness: 2.02
    self_corr_value: 0.6826
    self_corr_result: "PASS (but ALREADY_SUBMITTED on BRAIN; missing from local book)"
    verdict: "REDUNDANT (already submitted)"
  - id: "d50Jdpg2"
    grade: "SPECTACULAR"
    sharpe: 2.15
    fitness: 3.06
    self_corr_value: 0.8494
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "9qrEVpMV"
    grade: "SPECTACULAR"
    sharpe: 2.33
    fitness: 2.96
    self_corr_value: 0.9386
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "LL15dWke"
    grade: "SPECTACULAR"
    sharpe: 2.68
    fitness: 2.71
    self_corr_value: 0.9821
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "oml0kV52"
    grade: "SPECTACULAR"
    sharpe: 2.55
    fitness: 2.55
    self_corr_value: 0.796
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "WjGL7GPj"
    grade: "EXCELLENT"
    sharpe: 2.06
    fitness: 2.47
    self_corr_value: 0.8854
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "GrLjgZrx"
    grade: "EXCELLENT"
    sharpe: 2.16
    fitness: 2.21
    self_corr_value: 0.9255
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "oml00Kx2"
    grade: "EXCELLENT"
    sharpe: 1.98
    fitness: 2.09
    self_corr_value: 0.8754
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "pwKXqJEb"
    grade: "EXCELLENT"
    sharpe: 2.31
    fitness: 2.08
    self_corr_value: 0.6809
    self_corr_result: "PENDING"
    verdict: "BLOCKED (LOW_SUB_UNIVERSE_SHARPE FAIL)"
---

# Session 20260719-001: EXPLORE — Validate Recent Gate-Passers; Discover pstkrv Dual-Stabilizer Submittable

## Outcome

**Found:** [N1rlJ7mq](https://platform.worldquantbrain.com/alpha/N1rlJ7mq) —
EXCELLENT, S=2.32, F=2.07, T=11.09%, **all 8 BRAIN checks PASS**, including
SELF_CORRELATION **PASS 0.6903** (authoritative `/check`, confirmed twice).

**Update 2026-07-19:** submitted by the human and confirmed **ACTIVE** on
BRAIN (`status: ACTIVE`, all computable checks PASS). Book entry and submit
queue updated accordingly.

Zero new simulations this session: the candidate already existed as a recent
HF-queue gate-passer; the work was validation (BRAIN checks + authoritative
self-corr) across a batch of SPECTACULAR/EXCELLENT candidates, most of which
failed self-corr hard (0.80–0.98).

## Context Assessment (Phase 0)

- Book near saturation; no open HYPOTHESIS opportunities.
- HF healthy; new-24h and 7d gate-passers dense with event-magnitude variants.
- `xAd6K9Np` (accrued_liab_curr) was ALL PASS + self-corr PASS but already
  SUBMITTED on BRAIN and missing from local `data/book/` — book-sync gap noted.
- Decision tree → DEFAULT EXPLORE; executed as validation-first EXPLORE
  (satisfice on first SAFE EXCELLENT+).

## Discovery Path

1. Screened new-24h / 7d EXCELLENT+ gate-passers with brain_check.
2. Ran authoritative `--brain-check` self-corr on 8 ALL-PASS UNSUBMITTED
   alphas; 7 FAIL, **1 PASS** (`N1rlJ7mq`).
3. Stopped (satisficing) — no further sim budget burned.

## Key Findings

1. **`fnd6_pstkrv` (Preferred Stock — Redemption Value)** is a viable
   event-magnitude anchor despite INFERIOR standalone profile (cluster #81).
2. Dual-stabilizer + FCF + buzz form clears LOW_SUB_UNIVERSE; IV-spread
   siblings on the same anchor do not.
3. Most recent SPECTACULAR event-magnitude / guidance / debt alphas are
   self-corr BLOCKED (0.80–0.98) — grade alone is not a submission signal.
4. Local book is missing at least one ACTIVE submission (`xAd6K9Np`).

## Next Steps

- `N1rlJ7mq` submitted 2026-07-19 and confirmed ACTIVE. No further action needed.
- Sync `xAd6K9Np` (and any other missing ACTIVE alphas) into `data/book/`.
- Future EXPLORE: other cluster-#80s preferred-stock / capital-structure
  anchors; avoid more IV-hybrid clones of debt/guidance families.
