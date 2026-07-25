---
category: "review"
review_date: "2026-06-14"
scope: "open_draft_prs"
prs_reviewed:
  - 21
  - 30
  - 35
  - 37
  - 38
  - 43
  - 44
outcome: "distilled_and_close_drafts"
---

# Draft PR Distillation — 2026-06-14

This review consolidates the open draft mining PRs into the current V2 knowledge
state. The drafts were useful audit artifacts, but several contain duplicate,
stale, or superseded candidates. The durable record should be the current
`data/book/`, `data/knowledge/`, and session artifacts, not seven long-lived
draft PRs.

## Reviewed Draft PRs

| PR | Topic | Decision |
|----|-------|----------|
| #21 | IV spread plus fundamental hybrids | Superseded by later IV-pattern records and current book state. Preserve the `zscore(ts_mean(IV_spread, 22)) + rank(fundamental)` lesson, not every candidate. |
| #30 | IV hybrid exploitation with `npWYoqQz` | `npWYoqQz` is already ACTIVE and remains the durable representative. Do not carry duplicate safe IV hybrids forward without fresh self-corr checks. |
| #35 | Sentiment × IV multiplicative | `omY3pZq2` is ACTIVE and captures the useful discovery. IV270 variants are now constrained by the IV270 self-corr dead zone and Sharpe-premium rule. |
| #37 | Cumulative analyst revision template | Keep the `zscore(ts_sum(anl4_*_flag, 22))` pattern. Specific GOOD-grade candidates are lower priority after stronger EXCELLENT/SPECTACULAR book growth. |
| #38 | Novel template exploration | Preserve dead-zone lessons: signal-to-noise and high-turnover fast templates are not submit-friendly on BRAIN; several novel tree families failed comprehensively. |
| #43 | Event magnitude and leverage arc | Keep the event-magnitude pattern, leverage-premium pattern, and queued candidates from the current local records. This PR is replaced by the consolidated review PR. |
| #44 | Accrual analyst buzz candidate | Keep `zqOrkbbG` as a queued EXCELLENT candidate unless a future recheck fails. This PR is replaced by the consolidated review PR. |

## Promoted Knowledge

### Patterns To Keep

- **IV zscore smoothing**: `zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, d))` remains a proven options-skew structure. The current durable representative is `vRm07LP3`, with hybrid extensions represented by `npWYoqQz` and related active book entries.
- **Sentiment × IV multiplicative**: `rank(ts_mean(scl12_buzz, 5)) * zscore(ts_mean(IV_call - IV_put, d))` found SPECTACULAR candidates. `omY3pZq2` is the durable ACTIVE representative; additional IV270 variants require Sharpe-premium self-corr validation.
- **Cumulative analyst revision**: `zscore(ts_sum(anl4_*_flag, 22))` is the correct transform for sparse analyst flags. Rank compression underperforms on zero-dominated flags.
- **Event magnitude**: `rank(abs(ts_delta(fnd6_itci / close, 3)))` is a real structural discovery. It works because inventory changes have discrete event dynamics; most other fields do not.
- **Leverage premium**: `rank(-1 * equity / assets)` and `zscore(-1 * equity / assets)` remain useful intra-industry enhancers. MARKET neutralization usually damages this signal.

### Dead Zones / Constraints To Keep

- **Sparse fundamental2 `ts_zscore`** can show spectacular aggregate metrics but fails `CONCENTRATED_WEIGHT`. Session `20260614-001` added the explicit dead-zone record.
- **Fast signal-to-noise templates** can achieve high Sharpe but turnover/fitness tradeoffs make them poor BRAIN submission candidates.
- **Directional gating and rank momentum** were repeatedly noisy or high-turnover in the cloud exploration drafts.
- **IV270 spread variants** are conditionally blocked after `npWYoqQz` and `omY3pZq2`; future variants must pass the 0.70 self-corr gate or the 1.10x Sharpe-premium escape.
- **Cloud-agent compliance** matters: PRs #35 and #38 bypassed parts of the mining skill chain or used ad-hoc polling. Future automation should read the full mining-session chain and use `scripts/hf_poll.py`.

## Candidate Disposition

### Current Active / Submitted

- `xAn2kvOp` — submitted on 2026-06-14 and marked ACTIVE locally. This is the latest session's concrete outcome.
- `npWYoqQz`, `omY3pZq2`, `6Xzm6PQP`, `0mzQQvX8`, and other current ACTIVE book entries supersede many older draft candidates.

### Still Queued / Worth Human Review

- `d5Q3ZmWv` — SPECTACULAR event + leverage + sentiment-reversal candidate. High priority, but shares the event family and passes via Sharpe premium.
- `0m8GV1Pp` — SPECTACULAR event-magnitude base candidate. Still useful as the canonical pattern representative.
- `xAn1LqXm` — EXCELLENT leverage × netprofit revision regime candidate.
- `zqOrkbbG` — EXCELLENT accrual + analyst + buzz candidate from PR #44.

### Do Not Carry Forward Blindly

- Duplicate IV hybrids from #21/#30/#35 should not be submitted without fresh BRAIN self-corr checks against the current ACTIVE book.
- GOOD/AVERAGE cloud candidates from #37/#38 should not displace current EXCELLENT+ opportunities unless the book needs low-correlation filler.
- Draft PR book entries that are not represented in the current `data/book/` should be treated as historical discoveries, not immediate submission queue items.

## Closure Plan

After this distilled review PR is opened, close draft PRs #21, #30, #35, #37,
#38, #43, and #44 with comments pointing to this review. They are audit artifacts
and should not remain open as competing sources of truth.
