---
category: "rule"
severity: "critical"
---

# flag * (-ret) is the #1 Correlation Driver

Blends sharing the `anl4_*_flag * (-1 * returns)` component correlate at 0.60-0.80
regardless of other factors. The reversal dynamic dominates PnL correlation.

To break the self-corr wall, avoid `flag*(-ret)` in new submissions.
Use alternative dynamics: `ts_delta(flag, 5)`, pure revision flags, buzz stabilizer.
