---
category: "rule"
severity: "critical"
---

# EXCELLENT Grade vs Self-Corr Tradeoff

Adding a 4th factor to reach EXCELLENT simultaneously increases self-corr above 0.7.
3-factor MARKET blends cap at GOOD grade (F < 1.85, self-corr ~0.49).
4-factor blends reach EXCELLENT (F=2.06) but self-corr = 0.75.
Above 0.7, submission can still pass if the candidate Sharpe >= 1.10x the max
correlated peer Sharpe (Sharpe premium escape). Otherwise the book is saturated
for EXCELLENT-grade uncorrelated signals on free tier.
