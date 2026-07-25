---
id: 20260613-001
date: 2026-06-13
strategy: EXPLOIT
trigger: manual alpha-mining session
status: completed
branch: session/20260611-001-event-detection
---

# Manual Mining Session 20260613-001

Started from the current dirty local workspace. Sync to latest `main` was skipped
to avoid overwriting or disrupting existing uncommitted session/book/server
changes.

## Phase 0 Context

STRATEGY: EXPLOIT

TARGET: New company guidance/share-count cluster, anchored on
`rank(ts_rank(basic_shares_max_guidance_qtr, 22))` and related shares-outstanding
guidance fields.

BUDGET: 12 simulations for round 1; iterate only if results improve beyond the
existing GOOD standalone cluster.

CONSTRAINTS: Use SUBINDUSTRY/default decay first; avoid event-family drift, IV270,
PV reversal, volume-weighted fundamentals, and `flag * (-ret)`; keep variants
structurally informative rather than duplicating all eight identical fields.

RATIONALE: No active non-submit opportunity is open. Recent EXPLORE and RECOMBINE
work produced pending event/leverage candidates, while the fresh 24h discoveries
include a uniform company guidance/share-count cluster that is distinct from the
saturated event, analyst, IV, and PV families.

## Phase 1 Candidate Slate

Batch tag: `guidance_share_exploit_r1`

1. `rank(ts_rank(basic_shares_max_guidance_qtr, 22))`
   - Mechanism: Management share-count guidance has predictive disclosure content.

2. `ts_decay_linear(rank(ts_rank(basic_shares_max_guidance_qtr, 22)), 3)`
   - Mechanism: Light smoothing may lift fitness while preserving the guidance signal.

3. `rank(ts_rank(basic_shares_max_guidance_qtr, 10))`
   - Mechanism: Shorter guidance rank window tests whether the effect is event-like.

4. `rank(ts_rank(basic_shares_max_guidance_qtr, 44))`
   - Mechanism: Longer guidance rank window tests persistence of management outlook.

5. `zscore(ts_rank(basic_shares_max_guidance_qtr, 22))`
   - Mechanism: Cross-sectional zscore tests whether magnitude matters beyond ranks.

6. `rank(abs(ts_delta(basic_shares_max_guidance_qtr, 5)))`
   - Mechanism: Absolute changes in share-count guidance may capture issuance/buyback events.

7. `rank(ts_corr(basic_shares_max_guidance_qtr, returns, 20))`
   - Mechanism: Guidance-return co-movement may identify names where disclosure is being priced.

8. `rank((max_shares_outstanding_guidance - min_shares_outstanding_guidance) / sharesout)`
   - Mechanism: Wider guided share-count range may proxy capital-structure uncertainty.

9. `rank(ts_rank(basic_shares_max_guidance_qtr, 22)) + zscore(-1 * equity / assets)`
   - Mechanism: Combine guidance disclosure with the leverage premium.

10. `rank(ts_rank(basic_shares_max_guidance_qtr, 22)) * rank(-1 * equity / assets)`
    - Mechanism: Nonlinear confirmation: guidance signal pays most in high-leverage names.

11. `rank(ts_rank(basic_shares_max_guidance_qtr, 22)) + zscore(ts_sum(anl4_netprofit_flag, 22))`
    - Mechanism: Management guidance plus analyst net profit revisions.

12. `trade_when(ts_std_dev(returns, 30) > 0.025, rank(ts_rank(basic_shares_max_guidance_qtr, 22)), ts_std_dev(returns, 30) < 0.012)`
    - Mechanism: Guidance signal may concentrate in higher-volatility regimes.

Submitted 12 jobs to the HF queue with tags `20260613-001` and
`guidance_share_exploit_r1`, priority 5, decay 6, SUBINDUSTRY, USA TOP3000.

## Phase 2 Results

Batch completed with 12/12 simulations done, 0 failures, and 3 gate-passers.

| Alpha | Grade | S | F | Turnover | BRAIN Checks | Self-Corr | Verdict |
|-------|-------|---|---|----------|--------------|-----------|---------|
| RRro3NXj | EXCELLENT | 1.72 | 2.21 | 8.2% | ALL PASS | 0.9996 FAIL | BLOCKED |
| XgKxr5Pz | AVERAGE | 1.56 | 1.29 | 1.7% | ALL PASS | 0.7455 FAIL vs `xAn1LqXm` | BLOCKED |
| Vk8L99GJ | AVERAGE | 1.40 | 1.14 | 2.0% | ALL PASS | 0.7633 FAIL vs `xAn1LqXm` | BLOCKED |

### Key Finding

The company guidance/share-count standalone effect did not reproduce the fresh
24h GOOD cluster in this tagged batch: the direct variants fell to INFERIOR.
The only EXCELLENT candidate was dominated by `zscore(ts_sum(anl4_netprofit_flag,
22))`, creating near-duplicate self-correlation with the existing netprofit
revision family. Leverage blends improved the guidance signal enough to gate-pass
but remained blocked by high correlation against `xAn1LqXm`.

No candidate from this round should be queued for manual submission.

## Phase 3 Autonomous Iteration

User requested autonomous continuation until an EXCELLENT+ alpha passed all
tests. Instead of submitting more random variants, the next pass mined the
preexisting HF result database and current knowledgebase for high-grade
candidates with incomplete or stale validation.

### Rechecked and Blocked

- Event-family timeout candidates `mLX0gm5x`, `RRrlmbp1`, and `vRmpvZMw` all
  passed computable checks but failed self-correlation against pending event
  candidates, with correlations from 0.9590 to 0.9977.
- IV90/IV180 sentiment variants were blocked by either `CONCENTRATED_WEIGHT` or
  self-correlation around 0.94 against `omY3pZq2`.
- Company guidance/share-count variants from this session were blocked by
  self-correlation against `xAn1LqXm` or netprofit-revision peers.
- Older low stored-corr rows from the HF database were revalidated against the
  current 17 ACTIVE book entries; most were stale and now blocked by quality,
  guidance, or revision peers.

### Found Candidate

| Alpha | Grade | S | F | Turnover | BRAIN Checks | Self-Corr | Verdict |
|-------|-------|---|---|----------|--------------|-----------|---------|
| zqOrkbbG | EXCELLENT | 1.82 | 2.01 | 11.76% | ALL PASS | 0.6202 PASS vs `xARzmVEW` | QUEUED |

Expression:

`ts_decay_linear(rank(fn_accrued_liab_q / close) + rank(anl4_cfi_flag) + rank(anl4_bvps_flag) + rank(ts_mean(scl12_buzz, 5)), 5)`

`zqOrkbbG` is the first EXCELLENT+ candidate found in this continuation that
passes all computable BRAIN checks and authoritative BRAIN self-correlation. It
has been recorded as `data/book/zqOrkbbG.md` with `status: PENDING` and queued
for manual submission at `data/knowledge/opportunities/submit-zqorkbbg.md`.
