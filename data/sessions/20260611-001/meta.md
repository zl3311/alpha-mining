---
id: "20260611-001"
date: "2026-06-11"
strategy: "EXPLORE"
research_question: "Can structurally novel operator trees — ts_corr dynamic alignment, ts_zscore regime detection, multi-horizon fundamental spreads, abs(ts_delta) event detection, and novel conditional gates — produce decorrelated submittable alphas?"
budget_used: 92
budget_cap: null
trigger: "local_manual"
gate_passers: 30
submissions: 0
submittable_candidates: 6
status: "productive"
tags:
  - "20260611-001"
  - "explore_novel_trees"
  - "abs_ts_delta"
  - "event_detection"
  - "event_leverage_fundamental"
candidates:
  - id: "0m8GV1Pp"
    grade: "SPECTACULAR"
    sharpe: 2.64
    fitness: 2.77
    self_corr_value: 0.5492
    self_corr_result: "PASS"
    verdict: "SUBMITTABLE (best variant)"
  - id: "le0gY6Ze"
    grade: "SPECTACULAR"
    sharpe: 2.62
    fitness: 2.74
    self_corr_value: 0.5466
    self_corr_result: "PASS"
    verdict: "SUPERSEDED by 0m8GV1Pp"
  - id: "88LGM8Ga"
    grade: "SPECTACULAR"
    sharpe: 2.64
    fitness: 2.69
    self_corr_value: 0.6047
    self_corr_result: "PASS"
    verdict: "REDUNDANT (mutual self-corr vs 0m8GV1Pp)"
  - id: "pw7W23p6"
    grade: "SPECTACULAR"
    sharpe: 2.62
    fitness: 2.74
    self_corr_value: null
    self_corr_result: null
    verdict: "REDUNDANT (decay wrap of le0gY6Ze)"
  - id: "A13LA2GX"
    grade: "EXCELLENT"
    sharpe: 2.20
    fitness: 2.50
    self_corr_value: null
    self_corr_result: null
    verdict: "REDUNDANT (fatl variant, lower grade)"
  - id: "j2gV7oP9"
    grade: "EXCELLENT"
    sharpe: 2.25
    fitness: 2.44
    self_corr_value: null
    self_corr_result: null
    verdict: "REDUNDANT (dlto variant, lower grade)"
---

# Session 20260611-001: EXPLORE — abs(ts_delta) Event Detection Discovery

## Research Question

Can structurally novel operator trees produce decorrelated submittable alphas?

## Answer: YES — SPECTACULAR event detection template discovered

**Primary candidate:** 0m8GV1Pp — SPECTACULAR S=2.64 F=2.77, ALL 8 BRAIN checks
PASS, self-corr 0.5492 (SAFE). Expression:
`rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`

## Key Discovery: Event Magnitude Detection

The session's breakthrough is that `abs(ts_delta(field/close, d))` — the absolute
magnitude of a fundamental field change — is a powerful alpha signal. Markets
underreact to the SIZE of inventory events regardless of direction.

This is a structurally novel template not present anywhere in the existing book or
factor catalog. Combined with leverage premium and deferred revenue quality, it
produces the 2nd-highest fitness SPECTACULAR ever found in this project.

## Rounds

### Round 1: Novel operator tree exploration (15 sims, 3 gate-passers)

Tested 6 novel template families:
- ts_corr dynamic alignment: ALL FAILED (0/3)
- ts_zscore time-series normalization: ALL FAILED (0/3)
- Multi-horizon spreads: ALL FAILED (0/3)
- Signal-to-noise ratios: ALL FAILED (0/2)
- **Event magnitude (abs(ts_delta))**: GOOD S=1.99 (1/2 gate-pass) ← KEY FINDING
- Novel conditional gates: 2/2 marginal

### Round 2: Event detection refinement (15 sims, 8 gate-passers)

- **SPECTACULAR S=2.49 F=2.60**: event + leverage (2-factor) — FAILS SUB_UNIVERSE
- **EXCELLENT S=2.28 F=2.07**: event + drlt (2-factor) — FAILS SUB_UNIVERSE
- Window sweep: d=3 (S=2.04) > d=5 (S=1.99) > d=10 (S=1.92) > d=22 (S=1.81)
- itci is the ONLY field that works; drlt/acdo/dlto/fatl/ivaco events all fail
- zscore normalization kills Sharpe on event component

### Round 3: SUB_UNIVERSE fix (25 sims, 11 gate-passers)

- **SPECTACULAR S=2.62 F=2.74 ALL PASS**: event + leverage + drlt (3-factor) ← BREAKTHROUGH
- Adding drlt as 3rd factor fixes LOW_SUB_UNIVERSE_SHARPE
- zscore of event component: GOOD S=1.45-1.66 (kills Sharpe but passes checks)
- MARKET neut: 0/5 gate-passers (kills both event and leverage signals)
- Multiplicative: EXCELLENT S=2.32 but FAILS SUB_UNIVERSE

### Round 4: Novel templates + decay sweep (20 sims, 4 gate-passers)

- ts_rank: AVERAGE only
- Quadratic rank(itci) * rank(itci): GOOD S=1.98 (interesting, very low turnover)
- Event detection on other datasets (guidance, IV, sentiment): ALL FAILED
- ts_corr as blend component: ALL FAILED

### Round 5: Winner refinement (12 sims, 11 gate-passers)

- **0m8GV1Pp**: SPECTACULAR S=2.64 F=2.77, ALL PASS, self-corr 0.55 ← BEST VARIANT
- d=3 window marginally better than d=5
- ivaco as 3rd factor: SPECTACULAR ALL PASS but lower fitness (2.69)
- fatl, dlto as 3rd factor: EXCELLENT ALL PASS (F=2.44-2.50)
- 4-factor with buzz: GOOD S=2.07 (buzz hurts fitness)
- 4-factor with netprofit revision: GOOD S=1.67

## Submission Queue

- **0m8GV1Pp** (SPECTACULAR S=2.64 F=2.77): QUEUED for manual submission
  - https://platform.worldquantbrain.com/alpha/0m8GV1Pp

## Lessons Learned

1. **abs(ts_delta) is a novel, powerful template**: Absolute change magnitude
   captures fundamental events the market underreacts to. This is structurally
   unique in the entire book.

2. **itci is uniquely suited for event detection**: Inventory has discrete event
   dynamics (stable periods punctuated by jumps) that abs(delta) captures. Other
   fundamental fields change too gradually for this template.

3. **3-factor blends fix SUB_UNIVERSE**: The 2-factor event+leverage blend is
   SPECTACULAR but always fails LOW_SUB_UNIVERSE_SHARPE. Adding drlt as a
   stabilizer fixes this while maintaining SPECTACULAR grade.

4. **Shorter windows are better for events**: d=3 > d=5 > d=10 > d=22 for event
   detection. Recent events are more actionable.

5. **Most novel templates are dead ends**: ts_corr, ts_zscore, multi-horizon
   spreads, signal-to-noise ratios all failed comprehensively. The operator tree
   must capture a genuine economic mechanism to work.

6. **zscore KILLS the event signal**: Unlike its success with analyst flags
   (session 20260608-001), zscore normalization destroys the abs(ts_delta) signal.
   rank() preserves the ordinal event magnitude information that drives returns.
