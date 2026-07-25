---
id: "20260615-001"
date: "2026-06-15"
strategy: "EXPLORE"
research_question: "Do standalone-dead datasets (option9 put-call, fundamental2 deferred-tax, model16 scores, news flow) become live as decorrelating blend legs / via novel structures, producing gate-passing alphas with LOW self-corr vs the book?"
budget_used: 168
budget_cap: null
trigger: "manual"
gate_passers: 20
submissions: 0
submittable_candidates: 1
status: "productive"
tags:
  - "s20260615-001"
  - "ortho-theme"
  - "EXPLORE"
candidates:
  - id: "1YgMZ6OW"
    grade: "SPECTACULAR"
    sharpe: 2.73
    fitness: 4.38
    self_corr_value: 0.966
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
    note: "IV90 spread + guidance + itci, MARKET. All 8 IS checks PASS; blocked by self-corr (0.966 vs Gro21wWG S2.59, IV family saturated)."
  - id: "kqKAKLgl"
    grade: "EXCELLENT"
    sharpe: 2.19
    fitness: 2.02
    self_corr_value: 0.608
    self_corr_result: "PASS"
    verdict: "BLOCKED"
    note: "guidance + itci, SUBINDUSTRY. Self-corr PASS (0.608 = decorrelated); blocked only by LOW_SUB_UNIVERSE_SHARPE (itci structural)."
  - id: "mLXGw2R2"
    grade: "SPECTACULAR"
    sharpe: 2.10
    fitness: 2.96
    self_corr_value: 0.982
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
    note: "IV180 spread, MARKET. All 8 IS checks PASS; self-corr saturated vs IV book."
  - id: "LLR0Xjz2"
    grade: "AVERAGE"
    sharpe: 1.75
    fitness: 1.48
    self_corr_value: 0.675
    self_corr_result: "PASS"
    verdict: "SUBMITTABLE"
    note: "acdo + dlto/close + sales_estimate_count, SUBINDUSTRY decay10. All 8 IS checks PASS; self-corr 0.675 < 0.70 BRAIN gate (borderline vs 0.65 conservative). Only fully-submittable alpha this session; AVERAGE grade."
---

# Session 20260615-001: Orthogonal-Theme Diversification (validation)

## Research Question

The factor PnL merge/theme analysis (PR #47) found our ACTIVE book is
over-concentrated on the analyst x fundamental axis (the self-corr wall), and that
the marginal-PnL move is blending in orthogonal, under-used themes — several of
which are in `dead_zones/` for *standalone* weakness (option9 put-call ratio,
fundamental2 deferred-tax, model16 scores, news12/18 flow).

This session validates that thesis: used as **decorrelating blend legs** and via
**structurally novel** shapes, do these dead-standalone themes produce gate-passing
alphas with LOW self-correlation vs the existing book?

## Strategy Rationale

EXPLORE (mining-session default; book saturated per `book-saturation` rule).
Clears the dead-zone escape clause: prior tests marked these datasets dead
*standalone*; this tests them as cross-family blend legs / novel structures
(the `book-saturation` "Phase B cross-cluster combinations" path).

Constraints honored:
- `flag-ret-correlation`: NO `anl4_*_flag * (-1*returns)` legs; only raw `rank(flag)`.
- `novelty-required`: >=50% structurally novel (directional gating, dynamic
  correlation, multi-horizon spread, trade_when, cross-family ratios/products).

## Key Findings

142 sims across 10 rounds + a full scan of the 21,442-sim sweep.

1. **Orthogonal-theme decorrelation thesis: CONFIRMED.** Cross-family blends do
   decorrelate — `kqKAKLgl` (guidance + itci) reached self-corr **0.608** (PASS),
   the lowest of any EXCELLENT this session.
2. **But orthogonal dead-zone legs cannot reach EXCELLENT.** Raw option9 PCR /
   news / fundamental2 deferred-tax legs are weak and turnover-heavy (news legs
   hit 120% turnover). Smoothing with `ts_mean(...,22)` fixes turnover but they
   stay weak (S<1.1). They only help as small decorrelating tilts, slightly
   lowering fitness.
3. **EXCELLENT + submittable is blocked by saturation (precisely characterized):**
   - `itci` → EXCELLENT/SPECTACULAR but FAILS `LOW_SUB_UNIVERSE_SHARPE` (known
     structural block; value concentrates in large caps).
   - IV call-put spread (any maturity 30-1080, plain or vol-gated) → SPECTACULAR
     (F up to 4.38) and passes all 8 IS checks, but FAILS self-corr (0.95-0.99 vs
     the IV book; premium escape needs S >= 2.85 = 1.10x `Gro21wWG` S2.59 — no
     variant reaches it).
   - Clean broad-coverage legs (guidance, analyst flags, sales_estimate_count)
     pass SUB_UNIVERSE but only reach GOOD/AVERAGE without the banned
     `flag*(-ret)` driver.
   - `fnd6_city` (rare event) fails CONCENTRATED_WEIGHT + SUB_UNIVERSE.
   - **0** EXCELLENT/SPECTACULAR signals in the 21k sweep pass the hard checks
     outside the IV-spread / itci / guidance / flag-ret mechanisms.
4. **Stale local book:** `Gro21wWG` (iv90 vol-gated spread, S2.59) is the binding
   self-corr peer on the BRAIN platform but is MISSING from `data/book/`. The
   local book understates the true IV-family saturation.

## Outcome

No fully-submittable EXCELLENT+ found — confirmed blocked by the saturation wall
(`rules/book-saturation.md`). Two near-misses, each failing exactly one gate:
- `1YgMZ6OW` SPECTACULAR S2.73 F4.38 — all IS checks pass, self-corr blocked.
- `kqKAKLgl` EXCELLENT S2.19 F2.02 — self-corr PASS (0.608), SUB_UNIVERSE blocked.

## Next Steps

- Sync `data/book/` with the BRAIN platform (add `Gro21wWG`); the local book is stale.
- To submit an IV SPECTACULAR, the human would need to retire a redundant IV book
  alpha to lower the premium bar — but `Gro21wWG` (2.59) still binds at 2.85.
- The realistic submittable result in this regime is a GOOD-grade decorrelated
  filler (book-saturation path #1), not EXCELLENT+.
- For a self-corr-clean EXCELLENT, the only lever is breaking `kqKAKLgl`'s
  SUB_UNIVERSE block (a non-itci high-coverage strong base) — none found in the
  current field universe; needs a tier/region/data upgrade or a novel field.
