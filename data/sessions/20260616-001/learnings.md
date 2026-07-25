---
id: "20260616-001-learnings"
session: "20260616-001"
category: "discovery"
confidence: "medium"
actionable: true
---

# Learnings: Session 20260616-001

## What Worked

- Volatility-regime gating is the key structure for the option-skew/news-flow
  theme. The only viable candidate used `trade_when(ts_std_dev(returns, 20) >
  0.02, signal, ts_std_dev(returns, 20) < 0.01)`.
- The nonlinear product form beat the additive form after gating:
  `rank(implied_volatility_mean_skew_360) * rank(ts_mean(news_open_vol, 22))`
  reached AVERAGE grade and passed all checks.
- The winning candidate is genuinely decorrelated for the current book:
  BRAIN self-corr 0.4613 PASS for `YPpjReEW`.

## What Didn't Work

- Raw additive `rank(implied_volatility_mean_skew_360) + rank(news_open_vol)`
  has strong Sharpe but turnover is unusable at 129.48%.
- Simple smoothing of `news_open_vol` fixes turnover but leaves fitness below
  gate. The theme needs a regime filter or nonlinear interaction.
- Rank-ratio, multi-horizon skew acceleration, news acceleration, and dynamic
  skew/news correlation were all weak in this sample.
- Adding `scl12_buzz` or `fnd6_cshtr` as stabilizers diluted the signal rather
  than repairing it.
- Additive volatility-gated variants remain sub-universe blocked; the product
  interaction is the only all-pass shape tested here.

## New Rules Discovered

No hard rule was discovered. The evidence is medium-confidence because the
session tested only one option-skew/news theme and produced one AVERAGE-grade
submittable candidate.

## New Dead Zones

Do not treat option-skew/news-flow additive blends as a submission path unless a
regime gate or another structural change is present. The additive versions were
either turnover-heavy, below fitness, or blocked by `LOW_SUB_UNIVERSE_SHARPE`.

## New Patterns

Candidate reusable pattern:

```
trade_when(
  ts_std_dev(returns, 20) > 0.02,
  ts_decay_linear(rank(option_skew_field) * rank(ts_mean(news_flow_field, 22)), 5),
  ts_std_dev(returns, 20) < 0.01
)
```

Use this only for underrepresented option-skew/news-flow themes; it produced a
decorrelated AVERAGE filler, not an EXCELLENT-grade breakthrough.

## Mechanism Insights

The result supports a conditional-attention interpretation. Option skew alone is
too weak and news opening volatility alone is too turnover-heavy, but their joint
extreme during high realized-volatility regimes identifies names where option
market asymmetry and information flow agree. That conditional interaction adds
book diversification but has limited standalone grade.
