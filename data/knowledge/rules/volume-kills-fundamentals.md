---
category: "rule"
severity: "high"
---

# Volume Weighting Destroys Fundamental Signals

`rank(F) * rank(volume/adv20)` kills fitness on slow fundamental factors
(itci, acdo, drlt, etc.). Only use volume weighting on PV reversal signals.
