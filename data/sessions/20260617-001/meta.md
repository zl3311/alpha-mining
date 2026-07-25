---
id: "20260617-001"
date: "2026-06-17"
strategy: "HYPOTHESIS"
research_question: "Can under-used option-flow/deferred-tax and R&D-tax connector themes become viable when expressed as products, volatility-regime gates, or dynamic alignments rather than weak standalone legs?"
budget_used: 52
budget_cap: null
trigger: "manual alpha-mining session via Cursor"
gate_passers: 18
submissions: 0
submittable_candidates: 3
status: "productive"
tags:
  - "20260617-001"
  - "connector_theme"
  - "city_rare_event"
  - "iv_event_breadth"
  - "HYPOTHESIS"
  - "REFINE"
candidates:
  - id: "0m7lnAEr"
    grade: "EXCELLENT"
    sharpe: 2.08
    fitness: 2.01
    self_corr_value: 0.5480
    self_corr_result: "PASS"
    verdict: "SUBMITTABLE"
  - id: "GrwrVP5G"
    grade: "EXCELLENT"
    sharpe: 2.04
    fitness: 2.29
    self_corr_value: 0.5735
    self_corr_result: "PASS"
    verdict: "SUBMITTED"
  - id: "LLR0n261"
    grade: "EXCELLENT"
    sharpe: 2.51
    fitness: 2.35
    self_corr_value: 0.6094
    self_corr_result: "PASS"
    verdict: "SUBMITTED"
---

# Session 20260617-001

Manual mining session started from the existing dirty local workspace on
`exp/20260615-002-itci-replacement`. Branch-changing sync to latest `main` was
skipped to avoid disrupting untracked `20260616-001` artifacts and the modified
`server` submodule already present in the working tree.

## Phase 0 Context

STRATEGY: HYPOTHESIS

TARGET: Test the remaining open factor/theme-blend opportunity around under-used
connector themes: option9 put-call flow with deferred-tax carryforward, and
analyst R&D-expense revision with tax/debt/option-skew partners. Use structurally
novel product, `trade_when`, and dynamic-correlation wrappers rather than weak
standalone fields.

BUDGET: Start with 12 simulations. Iterate only if this first round produces a
gate-passer or materially improves the known LOW_SHARPE/LOW_FITNESS profile of
option9, model16, fundamental2, and R&D-tax connector fields.

CONSTRAINTS: Avoid standalone option9, model16, news12/news18, sparse
fundamental2 `ts_zscore`, PV reversal, COGS, IV270 spread mutations,
volume-weighted fundamentals, `anl4_*_flag * (-1 * returns)`, and negated
duplicates. Apply the structural novelty requirement: at least half the slate
must use non-saturated products, dynamic correlations, ratios, or regime gates.

RATIONALE: Active opportunity files still point to cross-theme blends, but recent
sessions already tested skew/news and itci-replacement branches. This round
targets distinct connector mechanisms with lower direct overlap to the pending
submission queue, while respecting the dead-zone escape clause by avoiding
standalone reuse.

## Phase 1 Candidate Slate

Batch tag: `connector_theme_r1`

1. `ts_decay_linear(rank(anl4_rd_exp_flag) + rank(fnd6_txs / close), 5)`
   - Mechanism: Baseline R&D-expense revision plus state-tax exposure connector from the factor-merge screen.
   - Sign: positive.

2. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(anl4_rd_exp_flag) + rank(fnd6_txs / close), 5), ts_std_dev(returns, 20) < 0.01)`
   - Mechanism: Test whether the R&D-tax connector only pays in elevated-volatility regimes.
   - Sign: positive.

3. `ts_decay_linear(rank(anl4_rd_exp_flag) * rank(fnd6_txs / close), 5)`
   - Mechanism: Nonlinear confirmation; only emphasize names where both R&D revisions and tax exposure agree.
   - Sign: positive.

4. `ts_decay_linear(rank(anl4_rd_exp_flag) + rank(fnd6_dn / close), 5)`
   - Mechanism: Replace tax exposure with notes/debt exposure, another decorrelating partner for R&D revisions.
   - Sign: positive.

5. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(anl4_rd_exp_flag) + rank(fnd6_dn / close), 5), ts_std_dev(returns, 20) < 0.01)`
   - Mechanism: Volatility-gated debt/R&D connector.
   - Sign: positive.

6. `ts_decay_linear(rank(implied_volatility_mean_skew_180) * rank(anl4_rd_exp_flag), 5)`
   - Mechanism: Options skew as forward-risk confirmation for R&D revision events.
   - Sign: positive.

7. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_180) * rank(anl4_rd_exp_flag), 5), ts_std_dev(returns, 20) < 0.01)`
   - Mechanism: Apply the recently validated volatility-regime idea to a different skew partner.
   - Sign: positive.

8. `ts_decay_linear(rank(implied_volatility_mean_skew_180) + rank(anl4_rd_exp_flag) + rank(fnd6_txs / close), 5)`
   - Mechanism: Three-theme blend of options skew, R&D revisions, and state-tax exposure.
   - Sign: positive.

9. `ts_decay_linear(rank(pcr_vol_20) * rank(fnd2_dfdtxasoprlcarryfwd / close), 5)`
   - Mechanism: Put-call flow only matters when confirmed by deferred-tax loss-carryforward exposure.
   - Sign: positive.

10. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(pcr_vol_20) + rank(fnd2_dfdtxasoprlcarryfwd / close), 5), ts_std_dev(returns, 20) < 0.01)`
    - Mechanism: Volatility-gated version of the top option9/fundamental2 theme-blend row.
    - Sign: positive.

11. `ts_decay_linear(rank(ts_corr(pcr_vol_20, fnd2_dfdtxasoprlcarryfwd, 20)), 5)`
    - Mechanism: Dynamic alignment between options flow and deferred-tax exposure instead of additive levels.
    - Sign: positive.

12. `ts_decay_linear(rank(ts_delta(relative_valuation_rank_derivative, 5)) + rank(implied_volatility_mean_skew_180), 5)`
    - Mechanism: One limited model16/options connector test using model-score change rather than model-score level.
    - Sign: positive.

Submitted via HF queue with tags `20260617-001` and `connector_theme_r1`,
priority 5, USA TOP3000, SUBINDUSTRY neutralization, decay 6.

## Phase 2 Round 1 Results

Batch completed with 12/12 simulations done, 0 failures, and 0 aggregate
gate-passers. Best result was `wpRq06ev`, the option-skew x R&D revision product,
at S=1.19, F=0.67, turnover 23.33%, still below both Sharpe and fitness gates.

### Final Verdict

The hypothesis is refuted for this specific connector branch. Products and
volatility gates improved the options-skew/R&D revision connector modestly, but
not enough to reach BRAIN gates. The option9/deferred-tax branch remained weak
and turnover-heavy, and the model16/options connector also stayed far below
gate thresholds.

No BRAIN checks or self-correlation checks were run because no candidate passed
the aggregate Sharpe/Fitness/Turnover gates.

## Phase 3 Existing Candidate Verification

The user requested autonomous iteration until at least one EXCELLENT+ alpha
passed all checks. Before spending more simulation budget, existing EXCELLENT+
PENDING/queued candidates were rechecked:

- `GrwrVP5G`: EXCELLENT, S=2.04, F=2.29, turnover 2.89%.
- Regular BRAIN checks: ALL PASS.
- BRAIN self-correlation breakdown: max corr 0.5735 vs `d5Q3ZmWv`, below the
  0.70 gate.

This verifies `GrwrVP5G` as a SAFE EXCELLENT+ submittable candidate. The local
book and submit queue entries were updated from `RISKY_BRAIN_PENDING` to `SAFE`.

## Phase 4 Continued Verification After Grwr Submission

The user reported `GrwrVP5G` had already been officially submitted. The local
book entry was flipped to `ACTIVE`, and the submit queue entry was marked
`SUBMITTED`. Remaining EXCELLENT+ queued candidates were then rechecked.

`LLR0n261` is the next clean EXCELLENT+ candidate:

- EXCELLENT, S=2.51, F=2.35, turnover 18.35%.
- Regular BRAIN checks: ALL PASS.
- BRAIN self-correlation breakdown: max corr 0.6094 vs `vR56vdYd`, below the
  0.70 gate.
- `GrwrVP5G` did not enter its top correlated peer set after activation.

The book and submit queue entries for `LLR0n261` were updated with
`self_corr_method: brain_self_correlation_breakdown` and
`self_corr_verdict: SAFE`.

## Phase 5 BRAIN Submission Reconciliation

The user reported `LLR0n261` was already submitted. A BRAIN check across local
book IDs confirmed these local PENDING entries are ACTIVE on the platform:

- `0m8GV1Pp`
- `d5Q3ZmWv`
- `LLR0n261`
- `xAn1LqXm`
- `zqOrkbbG`

Their local book entries were flipped to `status: ACTIVE`, and matching submit
queue entries were marked `status: SUBMITTED`.

## Phase 6 Continued Exploration (pw7j2MXg blocked; two dead-end batches)

With `0m8GV1Pp`/`d5Q3ZmWv`/`xAn1LqXm` now ACTIVE, the remaining EXCELLENT queued
candidate `pw7j2MXg` was re-checked and now FAILS self-corr (0.7414 vs
`0m8GV1Pp`, Sharpe premium not met). Marked REJECTED.

Two fresh exploration batches produced zero gate-passers:
- `city_refine_r1` (10 sims): `fnd6_city` rare-event blended with `current_ratio`
  to repair CONCENTRATED_WEIGHT/SUB_UNIVERSE. Best S=1.33/F=0.76 — the
  decorrelating stabilizer destroys the sparse relocation signal. Recorded as a
  dead zone (`family-city-rare-event-blend.md`).
- `explore_novel_r2` (10 sims): structurally novel guidance-dispersion,
  multi-horizon acceleration, and dynamic-correlation structures over underused
  fields. All INFERIOR (best F=0.40). Confirms decorrelated/novel structures
  don't reach EXCELLENT at the saturation wall.

## Phase 7 Sweep Mining + e7rwP2wd Lead

Rather than generate more weak novel structures, mined the 37k-row background
sweep for the highest-Sharpe ALL-PASS gate-passers and self-corr-checked them:
- Top itci-event variants (`mLX0gm5x`, `MPxeGqan`, `78dvZ3r2`) fail self-corr at
  0.99 vs `d5Q3ZmWv` (pure duplicates).
- **`e7rwP2wd`** (SPECTACULAR, S=2.36, F=2.66): IV270 spread + itci*2 + acdo +
  netdebt. Clean self-corr (max 0.614 vs npWYoqQz) but FAILS
  `LOW_SUB_UNIVERSE_SHARPE` (0.62 vs 1.02). A single-check REFINE target.

## Phase 8 REFINE e7rwP2wd -> winner 0m7lnAEr

Batch `e7r_refine_r3` (10 sims) added breadth legs (open/close, buzz, volume,
sales_estimate). All 9 gate-passers still failed `LOW_SUB_UNIVERSE_SHARPE`
because higher overall Sharpe raised the ~43% bar in lockstep — but self-corr
stayed clean (`E5w7AKwL` SPECTACULAR S=2.77 F=3.36, max corr 0.609).

Batch `e7r_subuniv_r4` (10 sims) tilted weight toward liquid-friendly breadth
legs and added a volatility-regime gate. **`0m7lnAEr`** (the volatility-gated
6-leg blend) PASSED all 8 computable checks at EXCELLENT grade, and authoritative
BRAIN SELF_CORRELATION PASS at **0.548** vs `LLR0n261`.

### Winner

`0m7lnAEr` — EXCELLENT, S=2.08, F=2.01, turnover 14.8%, all 8 BRAIN checks PASS,
self-corr 0.548 PASS. Labeled on BRAIN, recorded as `status: PENDING`, queued for
submission. The volatility-regime gate was the key lever: it lifted the liquid
sub-universe Sharpe above the ~43% bar while preserving EXCELLENT grade and
lowering self-corr. Pattern recorded in
`patterns/volatility-gate-fixes-sub-universe.md`.

This satisfies the user's goal: at least one new submittable EXCELLENT+ alpha
that passes every check.

## Phase 9 Official Submission + Further Mining

`0m7lnAEr` was officially submitted on BRAIN via `--submit-alpha` (SELF_CORRELATION
PASS 0.548); book and queue records flipped to ACTIVE/SUBMITTED. Book is now 25
ACTIVE.

A further decorrelation batch `decorr_volgate_r5` (10 sims) applied the proven
volatility-gate + breadth pattern to thinly-represented families (IV-skew,
guidance, capital intensity, analyst breadth), seeking a SECOND decorrelated
EXCELLENT+:
- Best results were GOOD, not EXCELLENT+: `N1pw5me8` (guidance + fate + ptpr +
  buzz + open/close, vol-gated) S=2.01 F=1.93 ALL computable checks PASS.
- But `N1pw5me8` FAILS self-corr at 0.784 vs `6Xzm6PQP` (S=2.31; premium escape
  needs S>=2.54). The guidance/fate/ptpr core is saturated by `6Xzm6PQP`.
- The IV-skew-anchored variants were only AVERAGE (turnover ~22%).

### Saturation conclusion (re-confirmed)

After 6 batches (62 sims) + a full 37k-row sweep scan, the only genuinely
decorrelated EXCELLENT+ found was the IV270 multi-leg `e7rwP2wd` family, now
exploited and submitted as `0m7lnAEr`. Every other high-grade lead either does
not reach EXCELLENT (novel/decorrelated structures cap at GOOD/AVERAGE) or fails
self-corr against an existing book member (event/itci, IV-spread, guidance,
drlt-blend families). Further new EXCELLENT+ submissions realistically require
retiring a redundant book alpha (to lower a premium-escape bar) or a tier/data
upgrade.

