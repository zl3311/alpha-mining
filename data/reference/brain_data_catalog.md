# BRAIN Data Catalog (USA TOP3000)

**Last updated**: 2026-05-16
**Source**: BRAIN API `data-fields` endpoint, complete paginated download
**Total downloaded**: 4,367 fields across 14 datasets

## Filtering Pipeline

```
4,367 total fields
  → type=MATRIX only                → 2,828  (dropped 1,539 GROUP/VECTOR/SYMBOL)
  → coverage >= 30%                 → 2,635  (dropped 193 low coverage)
  → alphaCount > 0                  → 1,628  (dropped 1,007 never used)
  → cluster by financial category   →    73  independent concept clusters
```

## Dataset Summary

| Dataset | Total | MATRIX | Usable | Clusters | Top Field | Top Alphas |
|---------|-------|--------|--------|----------|-----------|-----------|
| pv1 | 24 | 13 | 13 | 4 | close | 546,513 |
| fundamental6 | 886 | 574 | 574 | 8 | assets | 147,826 |
| fundamental2 | 766 | 766 | 240 | 7 | fn_liab_fair_val | 18,614 |
| analyst4 | 1,324 | 1,105 | 459 | 9 | anl4_adj_netincome | 43,825 |
| model16 | 24 | 24 | 16 | 1 | fscore_quality | 1,536 |
| model51 | 16 | 16 | 16 | 3 | unsys_risk_360d | 10,178 |
| option8 | 64 | 64 | 64 | 4 | iv_call_270 | 12,883 |
| option9 | 74 | 74 | 74 | 5 | pcr_oi_270 | 12,721 |
| news12 | 875 | 75 | 67 | 6 | nws12_afterhsz_sl | 20,057 |
| news18 | 121 | 71 | 61 | 6 | rp_css_business | 3,294 |
| socialmedia12 | 18 | 12 | 12 | 2 | scl12_buzz | 20,785 |
| socialmedia8 | 4 | 4 | 2 | 2 | snt_social_value | 4,976 |
| univ1 | 6 | 0 | 0 | 0 | -- | -- |
| pv13 | 165 | 30 | 30 | 3 | rel_num_part | 6,898 |

---

## 73 Independent Concept Clusters (ranked by total community alpha usage)

Each cluster groups fields that measure the same financial concept. The **representative** is the highest-alphaCount field in the cluster -- use it for probing.

### Tier 1: High-Signal Clusters (total alphas > 100k)

| # | Cluster | Fields | Representative | Alphas | Cov | Explored? |
|---|---------|--------|---------------|--------|-----|-----------|
| 1 | pv1 core (price, volume, returns) | 9 | `close` | 546k | 100% | YES |
| 2 | pv1 market cap | 1 | `cap` | 410k | 100% | YES |
| 3 | analyst4 earnings estimates | 225 | `anl4_adjusted_netincome_ft` | 44k | 87% | NO |
| 4 | fundamental6 assets | 75 | `assets` | 148k | 50% | NO |
| 5 | fundamental6 liabilities | 86 | `liabilities` | 63k | 50% | NO |
| 6 | fundamental6 other balance sheet | 169 | `cash` | 12k | 50% | NO |
| 7 | fundamental6 earnings | 118 | `ebitda` | 20k | 50% | NO |
| 8 | option8 implied vol ratios | 36 | `implied_volatility_call_270` | 13k | 97% | NO |
| 9 | fundamental6 operating income | 50 | `operating_income` | 51k | 50% | NO |
| 10 | analyst4 cash flow estimates | 84 | `anl4_capex_high` | 8k | 62% | NO |
| 11 | fundamental6 cash flow | 27 | `capex` | 28k | 50% | NO |

### Tier 2: Medium-Signal Clusters (total alphas 10k-100k)

| # | Cluster | Fields | Representative | Alphas | Cov | Explored? |
|---|---------|--------|---------------|--------|-----|-----------|
| 12 | fundamental6 equity | 33 | `equity` | 22k | 50% | NO |
| 13 | fundamental6 revenue | 12 | `sales` | 36k | 50% | NO |
| 14 | pv13 relationships | 24 | `rel_num_part` | 7k | 78% | NO |
| 15 | analyst4 operating estimates | 35 | `anl4_ebitda_value` | 15k | 81% | NO |
| 16 | socialmedia12 sentiment | 10 | `scl12_buzz` | 21k | 100% | NO |
| 17 | option9 put-call ratios | 40 | `pcr_oi_270` | 13k | 98% | NO |
| 18 | fundamental2 liabilities detail | 44 | `fn_liab_fair_val_l1_a` | 19k | 36% | NO |
| 19 | fundamental6 enterprise value | 1 | `enterprise_value` | 40k | 50% | NO |
| 20 | analyst4 book value estimates | 33 | `anl4_bvps_flag` | 16k | 82% | NO |
| 21 | analyst4 asset estimates | 29 | `anl4_totassets_flag` | 11k | 81% | NO |
| 22 | option8 historical vol | 12 | `historical_volatility_180` | 4k | 98% | NO |
| 23 | news12 news signals | 31 | `news_tot_ticks` | 2k | 97% | NO |
| 24 | news18 sentiment scores | 32 | `rp_css_business` | 3k | 50% | NO |
| 25 | option8 IV averages | 12 | `implied_volatility_mean_10` | 7k | 97% | NO |
| 26 | model51 idiosyncratic risk | 4 | `unsystematic_risk_last_360_days` | 10k | 94% | NO |
| 27 | analyst4 debt estimates | 14 | `anl4_netdebt_flag` | 13k | 86% | NO |
| 28 | pv1 corporate actions | 2 | `dividend` | 12k | 100% | NO |
| 29 | model51 beta/correlation | 8 | `beta_last_60_days_spy` | 2k | 98% | NO |
| 30 | pv1 split | 1 | `split` | 18k | 100% | NO |

### Tier 3: Lower-Signal Clusters (total alphas < 10k)

| # | Cluster | Representative | Alphas | Cov |
|---|---------|---------------|--------|-----|
| 31 | analyst4 revenue est. | `est_sales` | 2.7k | 75% |
| 32 | news12 valuation | `news_cap` | 6.6k | 83% |
| 33 | fundamental6 ratios | `current_ratio` | 6.9k | 50% |
| 34 | option8 forecast vol | `parkinson_volatility_90` | 1.8k | 98% |
| 35 | pv13 analyst ratings | `pv13_com_rk_au` | 2.3k | 91% |
| 36 | model51 systematic risk | `systematic_risk_last_90_days` | 1.9k | 96% |
| 37-73 | (remaining 37 smaller clusters) | ... | <5k | varies |

---

## Probe Representatives (top 30 for BRAIN probing)

These are the highest-value representative fields from each independent cluster, prioritized for the signal triage probe system. Each gets 3 probes: `rank(field)`, `rank(ts_delta(field,5))`, `rank(-ts_delta(field,5))`.

### Must-probe (high alpha count, untouched, good coverage)

| # | Field | Dataset | Cluster | Alphas | Coverage |
|---|-------|---------|---------|--------|----------|
| 1 | `assets` | fundamental6 | Balance sheet assets | 147,826 | 50% |
| 2 | `operating_income` | fundamental6 | Operating income | 51,233 | 50% |
| 3 | `enterprise_value` | fundamental6 | Valuation | 39,787 | 50% |
| 4 | `sales` | fundamental6 | Revenue | 36,130 | 50% |
| 5 | `anl4_adjusted_netincome_ft` | analyst4 | Earnings estimates | 43,825 | 87% |
| 6 | `anl4_ebit_value` | analyst4 | Operating estimates | 15,220 | 95% |
| 7 | `anl4_bvps_flag` | analyst4 | Book value estimates | 15,619 | 82% |
| 8 | `est_eps` | analyst4 | EPS consensus | 7,207 | 78% |
| 9 | `scl12_buzz` | socialmedia12 | Sentiment volume | 20,785 | 100% |
| 10 | `scl12_sentiment` | socialmedia12 | Sentiment direction | 3,310 | 100% |
| 11 | `implied_volatility_call_270` | option8 | IV long-term | 12,883 | 97% |
| 12 | `implied_volatility_mean_10` | option8 | IV short-term | 7,077 | 97% |
| 13 | `historical_volatility_180` | option8 | Realized vol | 4,458 | 98% |
| 14 | `pcr_oi_270` | option9 | Put-call ratio | 12,721 | 98% |
| 15 | `unsystematic_risk_last_360_days` | model51 | Idiosyncratic risk | 10,178 | 94% |

### Should-probe (medium alpha count, different mechanisms)

| # | Field | Dataset | Cluster | Alphas | Coverage |
|---|-------|---------|---------|--------|----------|
| 16 | `beta_last_60_days_spy` | model51 | Beta | 1,673 | 98% |
| 17 | `eps` | fundamental6 | EPS actual | 16,556 | 50% |
| 18 | `ebitda` | fundamental6 | Earnings | 20,319 | 50% |
| 19 | `capex` | fundamental6 | CapEx | 27,541 | 50% |
| 20 | `equity` | fundamental6 | Equity | 22,496 | 50% |
| 21 | `current_ratio` | fundamental6 | Ratios | 6,905 | 50% |
| 22 | `dividend` | pv1 | Dividends | 11,753 | 100% |
| 23 | `sharesout` | pv1 | Shares outstanding | 30,025 | 100% |
| 24 | `news_tot_ticks` | news12 | Trading activity | 2,162 | 97% |
| 25 | `rp_css_business` | news18 | Ravenpack sentiment | 3,294 | 50% |
| 26 | `rel_num_part` | pv13 | Stock relationships | 6,898 | 78% |
| 27 | `fscore_quality` | model16 | Quality composite | 1,536 | 30% |
| 28 | `analyst_revision_rank_derivative` | model16 | Analyst revision | 418 | 100% |
| 29 | `snt_social_value` | socialmedia8 | Social sentiment | 4,976 | 100% |
| 30 | `anl4_capex_high` | analyst4 | CapEx estimates | 8,228 | 62% |

---

## Cross-Dataset Relationship Map

Expected independence between clusters (based on financial theory):

```
               PV1    Fund6   Analyst4  Option8  Model51  SentMedia  News
PV1(price)      -     LOW     LOW       MED      MED      LOW        LOW
Fund6(value)   LOW     -      HIGH      LOW      LOW      LOW        LOW
Analyst4(est)  LOW    HIGH     -        LOW      LOW      LOW        MED
Option8(IV)    MED    LOW     LOW        -       MED      LOW        LOW
Model51(risk)  MED    LOW     LOW       MED       -       LOW        LOW
SentMedia      LOW    LOW     LOW       LOW      LOW       -         MED
News           LOW    LOW     MED       LOW      LOW      MED         -
```

HIGH = likely correlated (same underlying data), LOW = likely independent (different data source/frequency).

**Best cross-dataset pairs for uncorrelated alphas:**
- Fundamental / Price ratios: `rank(eps/close)`, `rank(bookvalue_ps/close)`
- Options / Realized: `rank(implied_volatility_mean_10 - historical_volatility_180)`
- Sentiment / Reversal: `rank(scl12_sentiment * (-1*returns))`
- Analyst revision / Volume: `rank(ts_delta(est_eps,1) * (volume/adv20))`
- Risk / Return: `rank(-1 * beta_last_60_days_spy)`

---

## Raw Data

- Complete field catalog: `data/reference/brain_fields_raw.json` (4,367 fields)
- Filtered + clustered: `data/reference/brain_fields_filtered.json` (1,628 usable fields)
- Probe representatives: `data/reference/brain_probe_representatives.json` (60 cluster reps)
