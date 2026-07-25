---
pattern: "orthogonal-theme-diversification"
discovered: "20260615 (factor PnL merge/theme analysis, PR #47)"
applicable_to: "book construction, RECOMBINE/EXPLORE signal generation"
confidence: "high"
---

# Pattern: Diversify Off the Analyst x Fundamental Axis Into Orthogonal Themes

## The finding (evidence)

Field-level PnL merge analysis over 1,557 factor profiles (8,369 ok curves)
shows the single strongest standalone diversification axis is **analyst-revision
flags x fundamental value/debt**: `analyst4 x fundamental6` is 85 of the top 200
cross-family merges, with `anl4_epsr_flag` (57x) and `anl4_rd_exp_flag` (53x) as
the dominant decorrelating connectors (rho ~ -0.37, div+ ~ +0.9).

Our ACTIVE book (18 alphas) is built almost entirely on this axis (families:
`*_revision`, `fundamental`, `fundamental_sentiment`, `analyst_revision`). That is
why per-alpha fitness is high (F = 2-3) — but it is also why marginal book PnL has
stalled and we sit at the 0.7 self-corr wall:

- Redundancy clustering (|rho| >= 0.7) shows analyst-revision and fundamental
  value/debt are two giant internally-correlated mega-clusters (cluster #1: 232
  fundamental value/debt fields, mean |rho| 0.81; cluster #13: 127 analyst/value
  fields, mean |rho| 0.82).
- Every analyst x fundamental blend decorrelates *within* the alpha but draws from
  the same two clusters + the same `flag*(-ret)` driver (the #1 self-corr driver),
  so each new such alpha is highly correlated *across* the book.

## The lesson

We have been combining the right *pair type* but the wrong *breadth*. Maximizing
per-alpha Sharpe and maximizing marginal book PnL are different objectives; the
book is saturated on one axis.

## The pattern (what to do)

Blend a strong core theme with an **orthogonal, under-represented theme** that
brings new raw fields (lower self-corr vs book) and different temporal/regime
exposure. The merge/theme analysis ranks these:

- **Orthogonal decorrelating themes** the book under-uses: put-call ratio
  (`pcr_oi_10`, `pcr_vol_20`; option9), deferred-tax (`fnd2_dfdtxasoprlcarryfwd`;
  fundamental2), composite model scores (model16), social buzz
  (`scl12_buzz*(-ret)`; socialmedia12), news flow (`news_open_vol`, `rp_ess_*`).
- **Temporal gap**: among 481 strong fields, "best year" piles into 2021/2022 and
  the regime mix is 179 bull-only / 162 all-weather / only 4 bear-only. Favor
  all-weather connectors and negative-`temporal_corr` pairs (e.g. IV-skew x news
  flow, rho -0.60) to smooth the equity curve.

See `data/knowledge/opportunities/factor-merge-candidates.md` (pairs/triples) and
`data/knowledge/opportunities/theme-blend-candidates.md` (cluster x cluster) for
ranked, ready-to-sim targets.

## When to use

- RECOMBINE / EXPLORE sessions when choosing what to blend.
- Reject a candidate blend if both legs are from the analyst-revision or
  fundamental-value mega-clusters (redundant; high self-corr risk).
- Prefer a leg whose raw field does not already appear in `data/book/`.

## Caveat

Combined Sharpe in the analysis is an equal-weight screening estimate; a real
BRAIN blend re-ranks and re-neutralizes. Every candidate still needs a simulation
plus a self-corr check before submission.
