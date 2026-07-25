---
id: "20260615-002"
date: "2026-06-15"
strategy: "HYPOTHESIS"
research_question: "Can broad-coverage, lower-correlation replacements for the itci/event leg turn the latest EXCELLENT near-miss structure into a submittable EXCELLENT+ alpha without LOW_SUB_UNIVERSE or self-correlation failure?"
budget_used: 12
budget_cap: null
trigger: "manual alpha-mining session via Cursor"
gate_passers: 8
submissions: 0
submittable_candidates: 1
status: "productive"
tags:
  - "20260615-002"
  - "itci_replacement"
  - "HYPOTHESIS"
---

# Session 20260615-002

Manual mining session started from the existing dirty local workspace. Branch-changing
sync to latest `main` was skipped to avoid disrupting uncommitted server and data
changes already present in the working tree.

## Phase 0 Context

STRATEGY: HYPOTHESIS

TARGET: Replace the concentrated `fnd6_itci / close`-style leg in recent EXCELLENT
near-misses with broader-coverage fields from the factor-merge and theme-blend
opportunities, while preserving analyst/guidance confirmation and avoiding known
self-correlation drivers.

BUDGET: Start with 12 simulations. Iterate only if results produce at least one
gate-passer or improve the specific failure profile from `kqKAKLgl` (LOW_SUB_UNIVERSE).

CONSTRAINTS: Avoid PV reversal, COGS, sparse fundamental2 `ts_zscore`, model16,
option9 standalone, IV270 spread variants, volume-weighted fundamentals,
`anl4_*_flag * (-1 * returns)`, and negated duplicates. Treat IV-family and
shared-field candidates conservatively because local PnL correlation can
understate BRAIN self-correlation.

RATIONALE: The latest manual EXPLORE session validated that orthogonal blend legs
can reduce self-correlation, but EXCELLENT candidates were blocked by either IV
family self-correlation or `itci`/event sub-universe concentration. The best next
test is a focused hypothesis pass using broader coverage replacements rather than
another broad EXPLORE sweep.

## Phase 1 Candidate Slate

Batch tag: `itci_replacement_r1`

1. `ts_decay_linear(rank(fnd6_acdo) + rank(fnd6_dlto / close) + rank(sales_estimate_count) + rank(max_adjusted_net_income_guidance), 10)`
   - Mechanism: Start from the only submittable recent AVERAGE (`LLR0Xjz2`) and add broad management guidance to lift grade without adding `itci`.
   - Sign: positive, long stronger accrual/debt/guidance/sales-estimate breadth composite.

2. `ts_decay_linear(rank(fnd6_acdo) + rank(fnd6_dlto / close) + rank(sales_estimate_count) + rank(min_adjusted_net_income_guidance), 10)`
   - Mechanism: Same as above, using the lower-bound guidance field that anchors the strong guidance cluster.
   - Sign: positive.

3. `ts_decay_linear(rank(fnd6_acdo) + rank(fnd6_dlto / close) + rank(sales_estimate_count) + rank(anl4_bvps_flag), 10)`
   - Mechanism: Use book-value revision confirmation instead of `itci` to raise analyst/fundamental breadth.
   - Sign: positive.

4. `ts_decay_linear(rank(fnd6_acdo) + rank(fnd6_dlto / close) + rank(sales_estimate_count) + rank(anl4_epsr_flag), 10)`
   - Mechanism: EPS revision confirmation may preserve EXCELLENT fitness with broader coverage than event magnitude.
   - Sign: positive.

5. `ts_decay_linear(rank(fnd6_acdo) + rank(open / close - 1) + rank(anl4_bvps_flag), 5)`
   - Mechanism: Directly test the top factor-merge pair without `itci`; a light intraday dislocation leg diversifies the analyst revision leg.
   - Sign: positive.

6. `ts_decay_linear(rank(fnd6_acdo) + rank(open / close - 1) + rank(anl4_netdebt_flag), 5)`
   - Mechanism: Same cross-family structure with net-debt revision, avoiding the saturated netprofit flag.
   - Sign: positive.

7. `ts_decay_linear(rank(fnd6_acdo) + rank(open / close - 1) + rank(anl4_ptpr_flag), 5)`
   - Mechanism: Pre-tax profit revision is a high-ranking decorrelated pair in the merge screen.
   - Sign: positive.

8. `ts_decay_linear(rank(max_adjusted_net_income_guidance) + rank(fnd6_acdo) + rank(open / close - 1), 5)`
   - Mechanism: Theme-blend candidate: management guidance plus the acdo/intraday dislocation composite.
   - Sign: positive.

9. `ts_decay_linear(rank(sales_estimate_count) + rank(fnd6_acdo) + rank(open / close - 1), 5)`
   - Mechanism: Sales-estimate breadth plus the strongest non-`itci` composite; tests whether breadth can replace sparse event magnitude.
   - Sign: positive.

10. `ts_decay_linear(rank(fnd6_fatl / close) + rank(anl4_epsr_flag) + rank(fnd6_acdo), 5)`
    - Mechanism: Capital intensity plus EPS revision plus discontinued-ops accruals, a broader fundamental substitute for tax-credit/event legs.
    - Sign: positive.

11. `ts_decay_linear(rank(fnd6_fate / close) + rank(anl4_epsr_flag) + rank(fnd6_acdo), 5)`
    - Mechanism: Sister capital-intensity field to test whether fixed-asset exposure has better sub-universe behavior.
    - Sign: positive.

12. `ts_decay_linear(rank(fnd6_dlto / close) + rank(anl4_epsr_flag) + rank(sales_estimate_count), 5)`
    - Mechanism: Debt value, EPS revision, and sales-estimate breadth form a clean high-coverage replacement for `itci`.
    - Sign: positive.

Submitted via HF queue with tags `20260615-002` and `itci_replacement_r1`, priority 5, USA TOP3000, SUBINDUSTRY neutralization, decay 6.

## Phase 2 Round 1 Results

Batch completed with 12/12 simulations done, 0 failures, and 8 gate-passers.

| Alpha | Expression Variant | Grade | S | F | Turnover | BRAIN Checks | Self-Corr | Verdict |
|-------|--------------------|-------|---|---|----------|--------------|-----------|---------|
| LLR0n261 | `acdo + open/close + anl4_netdebt_flag` | EXCELLENT | 2.51 | 2.35 | 18.35% | ALL PASS | 0.6094 PASS vs `vR56vdYd` | QUEUED |
| 88LMONJa | `acdo + open/close + anl4_ptpr_flag` | EXCELLENT | 2.41 | 2.23 | 16.48% | ALL PASS | 0.6415 PASS vs `6Xzm6PQP` | BACKUP / likely redundant |
| npWLn33d | `acdo + open/close + anl4_bvps_flag` | EXCELLENT | 2.37 | 2.19 | 18.76% | ALL PASS | 0.7234 FAIL vs `vR56vdYd` | BLOCKED |
| j2gqnp3O | `sales_estimate_count + acdo + open/close` | GOOD | 2.16 | 1.78 | 13.24% | ALL PASS | 0.7168 FAIL vs `RRN1EM51` | BLOCKED |
| 0m81eZv6 | `LLR0Xjz2 + min_adjusted_net_income_guidance` | GOOD | 1.83 | 1.58 | 2.98% | ALL PASS | 0.6794 PASS vs `6Xzm6PQP` | LOWER-GRADE |
| 78dea5M5 | `LLR0Xjz2 + max_adjusted_net_income_guidance` | GOOD | 1.83 | 1.58 | 2.98% | ALL PASS | 0.6794 PASS vs `6Xzm6PQP` | LOWER-GRADE |
| d5QNnvdv | `max_adjusted_net_income_guidance + acdo + open/close` | GOOD | 2.01 | 1.52 | 25.93% | ALL PASS | 0.8352 FAIL vs `RRN1EM51` | BLOCKED |
| 1Ygro5Kk | `LLR0Xjz2 + anl4_bvps_flag` | AVERAGE | 1.47 | 1.34 | 3.68% | ALL PASS | check timed out | LOWER-GRADE |

### Key Finding

The hypothesis is confirmed: replacing the `itci` event leg with a broad
`fnd6_acdo + open/close` dislocation composite plus selected analyst flags
produced EXCELLENT alphas that pass `LOW_SUB_UNIVERSE_SHARPE` and, for two
variants, BRAIN self-correlation.

`LLR0n261` is the keeper because it has the highest Sharpe and fitness among the
self-corr passers. `88LMONJa` is also current-book submittable, but it shares the
same `acdo + open/close` backbone and should be treated as a backup rather than
a second submission unless `LLR0n261` is rejected or not submitted.

## Phase 3 Candidate Queue

Queued `LLR0n261` as the primary submission candidate and pushed metadata to the
BRAIN platform. Official BRAIN submission remains a manual human action.
