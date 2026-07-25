---
id: "20260628-001"
date: "2026-06-28"
strategy: "EXPLORE"
trigger: "local_manual"
budget: "unlimited"
budget_used: 53
target_grade: "EXCELLENT+"
status: "productive"
branch: "session/20260628-001-explore-buzz-reversal"
tags:
  - "20260628-001"
  - "explore_novel"
  - "buzz_reversal"
  - "socialmedia12"
  - "zscore_ts_sum"
gate_passers: 10
submissions: 1
submitted: ["xAxVAYwn"]
submittable_candidates: 3
best_alpha: "6XwZXn97"
best_sharpe: 2.00
best_fitness: 3.27
best_self_corr: 0.329
candidates:
  - id: "6XwZXn97"
    grade: "SPECTACULAR"
    sharpe: 2.00
    fitness: 3.27
    turnover: 0.141
    self_corr_value: 0.329
    self_corr_result: "PASS"
    self_corr_peer: "vR56vdYd"
    verdict: "SAFE — HIGH LONG-TERM VALUE (self-corr < 0.4, SPECTACULAR grade)"
  - id: "GrwXq7q5"
    grade: "SPECTACULAR"
    sharpe: 1.59
    fitness: 2.77
    turnover: 0.091
    self_corr_value: 0.385
    self_corr_result: "PASS"
    self_corr_peer: "vR56vdYd"
    verdict: "SAFE — HIGH LONG-TERM VALUE (self-corr < 0.4, SPECTACULAR grade)"
  - id: "xAxVAYwn"
    grade: "SPECTACULAR"
    sharpe: 1.54
    fitness: 2.62
    turnover: 0.079
    self_corr_value: 0.419
    self_corr_result: "PASS"
    self_corr_peer: "XgpJGaL0"
    verdict: "SUBMITTED"
---

# Session 20260628-001: EXPLORE — Social Media Buzz Reversal (zscore accumulation)

## Research Question

Can `scl12_buzz * (-1 * returns)` (social media attention × price reversal) produce
EXCELLENT+ submittable alphas when wrapped in the `zscore(ts_sum(..., D))` accumulation
template, decorrelated from the existing fundamental-heavy book?

## Strategy Rationale

EXPLORE mode (default). Book is saturated with 46 entries across 39+ families, almost
entirely driven by fundamental value + analyst revision + intraday timing mechanisms.
Social media reversal (`scl12_buzz * (-1 * returns)`, standalone S=1.63) represents a
genuinely different mechanism family (attention-driven overselling) with very low
cross-correlation to existing book (rho = -0.31 to -0.34 with analyst flags).

The critical insight was that raw buzz × returns has EXCELLENT Sharpe (2.03-2.57) but
catastrophic turnover (42-63%) that kills fitness. The `zscore(ts_sum(..., D))`
wrapper accumulates the signal over D days, dramatically reducing turnover while
preserving predictive power — the same technique that made XgpJGaL0 EXCELLENT.

## Key Discovery: Accumulated Buzz Reversal Family

The template `ts_decay_linear(zscore(ts_sum(scl12_buzz * (-1 * returns), D)) + rank(anl4_bvps_flag), 5)`
produces a family of SPECTACULAR-grade alphas that pass all 8 BRAIN checks AND
self-correlation with extraordinary margins (corr 0.33-0.42 vs 0.7 threshold).

### Novel elements
- `scl12_buzz * (-1 * returns)` (social media buzz × negative returns) — captures
  attention-driven overselling. Stocks heavily discussed on social media while losing
  money are experiencing panic-driven overreaction that subsequently reverts.
- The `zscore(ts_sum(..., D))` accumulation wrapper transforms the high-frequency
  social signal into a persistent positioning factor. Stocks with CONSISTENTLY high
  buzz AND negative returns over D days are deeply oversold.
- **Self-corr 0.329** is the lowest in the entire book — this signal is truly orthogonal
  to the existing fundamental/analyst/options families.

### Economic Mechanism

Social media attention amplifies behavioral biases (loss aversion, herding, panic
selling). When a stock has high social media buzz AND declining price over 10 days,
the aggregate attention + negative returns creates a self-reinforcing overreaction
cycle. The `zscore(ts_sum())` captures the CUMULATIVE overselling pressure.
Informed buyers (institutions, value investors) eventually absorb the supply,
causing mean reversion. The `anl4_bvps_flag` (BVPS revision) adds a contrarian
quality signal: stocks receiving positive fundamental revisions during social
media panic represent the strongest reversion candidates.

## Results Summary

| Batch | Size | Strategy | Gate-Passers | Best |
|-------|------|----------|-------------|------|
| batch_r1 | 15 | Novel cross-family (buzz, rel_num_all) | 10 | gJ1rVlbv SPECTACULAR S=2.55 (failed self-corr) |
| batch_r2_smooth | 8 | ts_mean smoothing, decay=10 | 6 | rKo0aemJ GOOD S=1.96 |
| batch_r2_decay | 7 | Higher inner decay=10 | 6 | 0m7GV00G AVERAGE S=2.06 |
| batch_r3 | 12 | dlto anchor + buzz triples | 6 | rKo0xWba EXCELLENT S=2.09 (failed self-corr) |
| batch_r4_market | 5 | MARKET neut | 4 | wpRN0enl GOOD S=1.42 |
| batch_r4_novel | 7 | IV put momentum + dispersion | 4 | j2ZVqOgj AVERAGE S=1.73 |
| batch_r4_push | 3 | decay=5 push | 3 | O0pR1wEJ EXCELLENT S=2.12 (would fail self-corr) |
| batch_r5_buzz_push | 8 | **zscore(ts_sum) template** | 7 | **6XwZXn97 SPECTACULAR S=2.00 F=3.27 PASS** |
| batch_r5_buzz_decay12 | 3 | zscore(ts_sum) decay=12 | 3 | xAxVAYwn SPECTACULAR S=1.54 F=2.62 PASS |

## Submittable Candidates

| Alpha | Expression | S | F | T | Self-Corr | Top Peer | Verdict |
|-------|-----------|---|---|---|-----------|----------|---------|
| 6XwZXn97 | zscore(ts_sum(buzz*(-ret), 10)) + bvps | 2.00 | 3.27 | 14.1% | 0.329 PASS | vR56vdYd | **SAFE — HIGH LONG-TERM VALUE** |
| GrwXq7q5 | zscore(ts_sum(buzz*(-ret), 22)) + bvps | 1.59 | 2.77 | 9.1% | 0.385 PASS | vR56vdYd | SAFE — HIGH LONG-TERM VALUE |
| xAxVAYwn | zscore(ts_sum(buzz*(-ret), 22)) + bvps + netdebt | 1.54 | 2.62 | 7.9% | 0.419 PASS | XgpJGaL0 | **SUBMITTED** |

### Submission Recommendation

Per long-term point maximization strategy: submit **6XwZXn97** first:
- Highest Sharpe (2.00) and highest fitness (3.27) in the family
- **Self-corr 0.329** — the lowest in the entire book, maximally preserves correlation headroom
- SPECTACULAR grade = maximum per-alpha point yield
- Flagged HIGH LONG-TERM VALUE (SPECTACULAR + self-corr < 0.4)

**UPDATE**: xAxVAYwn was submitted first and is now ACTIVE on BRAIN. 6XwZXn97 remains PENDING (unsubmitted) — still HIGH LONG-TERM VALUE with the lowest self-corr in the book (0.329).

## What Worked

1. **`zscore(ts_sum(signal, D))` is the breakthrough template** — transforms any
   high-frequency signal into a low-turnover, high-fitness alpha. Turnover dropped
   from 50-60% (raw) → 14% (ts_sum 10d) → 9% (ts_sum 22d).
2. **Social media buzz × returns is a genuinely decorrelated mechanism** — self-corr
   0.329 vs entire book. The attention-driven overselling mechanism produces
   different rankings from fundamental value / analyst revision / options signals.
3. **10-day accumulation window is optimal** — balances responsiveness (S=2.00) with
   smoothing (T=14.1%). The 22-day window over-smooths (S drops to 1.59) but has
   even lower turnover (9.1%) and higher fitness per unit Sharpe.

## What Didn't Work

1. **Raw buzz × returns**: S=2.03-2.57 but T=42-63% → AVERAGE grade due to low fitness.
2. **ts_mean smoothing**: Reduced turnover to 13-18% but also killed Sharpe (1.7-2.0) —
   ended up at GOOD grade (F=1.8-1.9).
3. **fnd6_dlto anchor blends**: EXCELLENT grade but all failed self-corr (0.78-0.82 vs
   6Xzm6PQP). ANY fundamental value + revision blend correlates with the existing book.
4. **MARKET neutralization**: Halves Sharpe (1.4-1.5 vs 2.0-2.1 at SUBINDUSTRY).
5. **IV put momentum**: Too much turnover (21-24%), stays at AVERAGE.
6. **Analyst dispersion (afv4_dts_spe)**: Too weak standalone (S=1.0), stays at AVERAGE.

## Lessons Learned

1. **The self-corr wall is about POSITIONS, not FIELDS** — all fundamental value signals
   (dlto, acdo, itci, drlt) rank the SAME stocks highly. Substituting one debt field
   for another doesn't decorrelate. Only a fundamentally different MECHANISM
   (attention, momentum, volatility) creates different position rankings.
2. **`zscore(ts_sum())` is the universal turnover fix** — works for sparse event flags
   (epsr, bvps) AND high-frequency signals (buzz*returns). The key insight is that
   accumulation converts daily noise into persistent positioning.
3. **Social media buzz × reversal (scl12_buzz * (-1 * returns)) is a new submittable
   mechanism family** — standalone S=1.63, in combination SPECTACULAR (S=2.00),
   and critically: self-corr 0.329 (lowest in the entire book). This opens a new
   "attention reversal" family for future exploitation.
4. **The 10-day window is optimal for buzz accumulation** — captures the typical
   duration of social media attention cycles. Shorter (5-day) has too much turnover;
   longer (22-44 day) over-smooths the reversion timing.
