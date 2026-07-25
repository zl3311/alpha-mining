---
category: "dead_zone"
entity_type: "dataset"
dataset: "model51"
discovered: "20260716-001"
expressions_tested: 12
best_sharpe: 1.42
best_fitness: 0.71
status: "dead_end"
confidence: "medium"
---

# Dataset: model51 (Idiosyncratic/Systematic Risk, Beta) — High Turnover Kills Fitness

`model51` (16 usable fields: `unsystematic_risk_last_*_days`,
`systematic_risk_last_*_days`, `beta_last_*_days_spy`,
`correlation_last_*_days_spy`) was completely untouched by the book/factors
prior to this session — a genuinely fresh dataset dimension (rolling
regression statistics vs SPY, recomputed daily). Tested as the primary
anchor for `unsystematic_risk_last_360_days` (standalone `rank(ts_delta(F,5))`
S=1.31-1.38 per its factor profile) across 12 sims including the profile's
own "untried" `decay_linear` wrap.

## Evidence (session 20260716-001)

| Expression | S | F | T |
|-----------|---|---|---|
| `ts_decay_linear(ts_zscore(unsystematic_risk_last_360_days,22),8)` | 1.42 | 0.71 | 28.0% |
| `ts_decay_linear(rank(ts_rank(unsystematic_risk_last_360_days,22)),8)` | 1.37 | 0.65 | 28.3% |
| `ts_decay_linear(rank(ts_delta(unsystematic_risk_last_360_days,3)),6)` | 1.33 | 0.45 | 56.5% |
| `ts_decay_linear(rank(ts_delta(unsystematic_risk_last_360_days,5)),5/8/10)` | 0.84-0.97 | 0.26-0.30 | 46-50% |
| Blended with fresh fundamentals (`fnd6_cld2`, `fnd6_fopo`) | 0.81-1.24 | 0.28-0.57 | 29-33% |

All INFERIOR despite decent Sharpe (0.8-1.4) — turnover never dropped below
~28% even with `ts_decay_linear` decay up to 10, roughly 15-25x higher than
the ~2% turnover of a quarterly fundamental ratio.

## Why it fails

`unsystematic_risk_last_360_days` (and by extension the other model51
fields) is `1 - R²` from a ROLLING regression recomputed EVERY trading day
(not a discrete quarterly-update fundamental) — the entire 360-day window
shifts daily, so the value itself has meaningfully different day-to-day
noise even without any real economic change, unlike balance-sheet items that
are flat between quarterly filings. `ts_decay_linear` smooths the RANKED
signal but cannot suppress this inherent day-to-day recomputation noise the
way it suppresses discrete-update noise in fundamental fields.

## Rule

Do not use model51 rolling-regression risk/beta fields as standalone alpha
anchors expecting fundamental-style low turnover — they behave like a dense
daily series (more similar to option8 IV or price/volume) for turnover
purposes, not like a fundamental. If revisited, treat as a beta/vol-regime
GATE (e.g. `trade_when` condition) rather than a rank-based signal leg —
untested.
