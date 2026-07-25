"""
PnL-based time series correlation and spectrum analysis.

Aggregates per-field daily returns from 3 template variants using Sharpe-weighted
averaging, then performs:
  1. Pairwise Pearson correlation (full-sample)
  2. Rolling 60-day correlation (regime detection)
  3. Lead-lag cross-correlation (predictive relationships)
  4. Spectral coherence (frequency-band co-movement)

Usage:
    uv run python3 scripts/factor_pnl_analysis.py
    uv run python3 scripts/factor_pnl_analysis.py --top-pairs 50
    uv run python3 scripts/factor_pnl_analysis.py --output local/test_scripts/pnl_analysis.json
"""

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SWEEP_CSV = ROOT / "local" / "sweep_analysis" / "sweep_data.csv"
PNL_CSV = ROOT / "local" / "sweep_analysis" / "pnl_returns.csv"


def load_field_mapping() -> dict[str, list[dict]]:
    """Map fields to their alpha_ids with PnL, grouped by template.

    Returns {field: [{alpha_id, template, universe, sharpe}, ...]}
    """
    with open(SWEEP_CSV) as f:
        sweep = list(csv.DictReader(f))

    pnl_ids = set(pd.read_csv(PNL_CSV, nrows=0).columns[1:])

    field_map = defaultdict(list)
    for r in sweep:
        aid = r["alpha_id"]
        if not aid or aid not in pnl_ids:
            continue
        try:
            sharpe = float(r["sharpe"])
        except (ValueError, TypeError):
            continue
        field_map[r["field"]].append({
            "alpha_id": aid,
            "template": r["template"],
            "universe": r["universe"],
            "sharpe": sharpe,
            "dataset": r["dataset"],
        })

    return field_map


def build_aggregated_returns(field_map: dict, pnl_df: pd.DataFrame) -> pd.DataFrame:
    """Build Sharpe-weighted aggregated return series per field.

    For each field, select the best alpha per template (by Sharpe),
    then Sharpe-weight the daily returns across available templates.
    """
    field_returns = {}

    for field, alphas in field_map.items():
        # Pick best alpha per template (highest abs Sharpe for PnL quality)
        best_per_template = {}
        for a in alphas:
            t = a["template"]
            if t not in best_per_template or abs(a["sharpe"]) > abs(best_per_template[t]["sharpe"]):
                best_per_template[t] = a

        # Get returns for each template's best alpha
        template_returns = {}
        template_sharpes = {}
        for t, a in best_per_template.items():
            aid = a["alpha_id"]
            if aid not in pnl_df.columns:
                continue
            pnl = pnl_df[aid].dropna()
            if len(pnl) < 100:
                continue
            # pnl_returns.csv already contains daily PnL increments (not cumulative)
            ret = pnl
            template_returns[t] = ret
            template_sharpes[t] = max(a["sharpe"], 0.01)  # floor at 0.01 to avoid negative weights

        if not template_returns:
            continue

        # Sharpe-weighted aggregation
        total_sharpe = sum(template_sharpes.values())
        weights = {t: s / total_sharpe for t, s in template_sharpes.items()}

        # Align all series to common index
        common_idx = None
        for ret in template_returns.values():
            if common_idx is None:
                common_idx = ret.index
            else:
                common_idx = common_idx.intersection(ret.index)

        if common_idx is None or len(common_idx) < 100:
            continue

        agg = pd.Series(0.0, index=common_idx)
        for t, ret in template_returns.items():
            agg += weights[t] * ret.reindex(common_idx).fillna(0)

        field_returns[field] = agg

    return pd.DataFrame(field_returns)


def pairwise_correlation(returns_df: pd.DataFrame) -> np.ndarray:
    """Compute full pairwise Pearson correlation matrix."""
    return returns_df.corr().values


def rolling_correlation(returns_df: pd.DataFrame, window: int = 60,
                        pairs: list[tuple[str, str]] = None) -> dict:
    """Compute rolling correlation for specified pairs.

    Returns {(field_a, field_b): {mean, std, min, max, regime_changes}}
    """
    results = {}
    if pairs is None:
        return results

    for a, b in pairs:
        if a not in returns_df.columns or b not in returns_df.columns:
            continue
        rolling_corr = returns_df[a].rolling(window).corr(returns_df[b])
        rolling_corr = rolling_corr.dropna()
        if len(rolling_corr) < window:
            continue

        # Detect regime changes (correlation sign flips)
        signs = np.sign(rolling_corr.values)
        sign_changes = np.sum(np.abs(np.diff(signs)) > 0)

        results[(a, b)] = {
            "mean": float(rolling_corr.mean()),
            "std": float(rolling_corr.std()),
            "min": float(rolling_corr.min()),
            "max": float(rolling_corr.max()),
            "sign_changes": int(sign_changes),
            "stability": "stable" if rolling_corr.std() < 0.15 else "regime_dependent",
        }

    return results


def lead_lag_analysis(returns_df: pd.DataFrame, max_lag: int = 5,
                      top_n: int = 50) -> list[dict]:
    """Compute lead-lag cross-correlation for all field pairs.

    Returns top pairs where the peak correlation is at a non-zero lag.
    """
    fields = returns_df.columns.tolist()
    n = len(fields)
    lead_lag_pairs = []

    # For efficiency, compute on a subset (top fields by variance)
    variances = returns_df.var()
    top_fields = variances.nlargest(min(200, n)).index.tolist()

    for i, a in enumerate(top_fields):
        for j, b in enumerate(top_fields):
            if i >= j:
                continue
            sa = returns_df[a].values
            sb = returns_df[b].values

            # Standardize
            sa = (sa - sa.mean()) / (sa.std() + 1e-10)
            sb = (sb - sb.mean()) / (sb.std() + 1e-10)

            # Cross-correlation at different lags
            best_lag = 0
            best_corr = 0
            zero_corr = np.corrcoef(sa, sb)[0, 1]

            for lag in range(-max_lag, max_lag + 1):
                if lag == 0:
                    continue
                if lag > 0:
                    corr = np.corrcoef(sa[:-lag], sb[lag:])[0, 1]
                else:
                    corr = np.corrcoef(sa[-lag:], sb[:lag])[0, 1]

                if abs(corr) > abs(best_corr):
                    best_corr = corr
                    best_lag = lag

            # Only report if lagged correlation exceeds zero-lag
            if abs(best_corr) > abs(zero_corr) + 0.02 and abs(best_corr) > 0.1:
                lead_lag_pairs.append({
                    "field_a": a,
                    "field_b": b,
                    "zero_lag_corr": float(zero_corr),
                    "best_lag": int(best_lag),
                    "best_lag_corr": float(best_corr),
                    "lead_improvement": float(abs(best_corr) - abs(zero_corr)),
                })

    lead_lag_pairs.sort(key=lambda x: -x["lead_improvement"])
    return lead_lag_pairs[:top_n]


def spectral_coherence(returns_df: pd.DataFrame, top_n: int = 50) -> dict:
    """Compute spectral coherence between field pairs at different frequency bands.

    Bands: low (>60 days), medium (5-60 days), high (<5 days)

    Requires the optional `analysis` extra: `uv sync --extra analysis`.
    """
    try:
        from scipy import signal as scipy_signal
    except ImportError as e:
        raise ImportError(
            "spectral_coherence needs scipy, which is an optional dependency. "
            "Install it with: uv sync --extra analysis"
        ) from e

    fields = returns_df.columns.tolist()
    n = len(fields)
    n_samples = len(returns_df)
    fs = 1.0  # 1 sample per day

    # Frequency band boundaries (in cycles/day)
    low_freq = (0, 1.0 / 60)       # > 60 days
    med_freq = (1.0 / 60, 1.0 / 5)  # 5-60 days
    high_freq = (1.0 / 5, 0.5)      # < 5 days (up to Nyquist)

    # For efficiency, use top fields by variance
    variances = returns_df.var()
    top_fields = variances.nlargest(min(100, n)).index.tolist()

    band_coherence = {"low": [], "medium": [], "high": []}

    for i, a in enumerate(top_fields):
        for j, b in enumerate(top_fields):
            if i >= j:
                continue

            # Compute coherence using Welch's method
            f, Cxy = scipy_signal.coherence(
                returns_df[a].values, returns_df[b].values,
                fs=fs, nperseg=min(256, n_samples // 4)
            )

            # Average coherence per band
            low_mask = (f >= low_freq[0]) & (f < low_freq[1])
            med_mask = (f >= med_freq[0]) & (f < med_freq[1])
            high_mask = (f >= high_freq[0]) & (f <= high_freq[1])

            low_coh = float(Cxy[low_mask].mean()) if low_mask.any() else 0
            med_coh = float(Cxy[med_mask].mean()) if med_mask.any() else 0
            high_coh = float(Cxy[high_mask].mean()) if high_mask.any() else 0

            if low_coh > 0.3 or med_coh > 0.3 or high_coh > 0.3:
                entry = {"field_a": a, "field_b": b,
                         "low": low_coh, "medium": med_coh, "high": high_coh}
                if low_coh > 0.3:
                    band_coherence["low"].append(entry)
                if med_coh > 0.3:
                    band_coherence["medium"].append(entry)
                if high_coh > 0.3:
                    band_coherence["high"].append(entry)

    for band in band_coherence:
        band_coherence[band].sort(key=lambda x: -x[band])
        band_coherence[band] = band_coherence[band][:top_n]

    return band_coherence


def hierarchical_clusters(corr_matrix: np.ndarray, fields: list[str],
                          threshold: float = 0.5) -> list[list[str]]:
    """Simple agglomerative clustering based on correlation threshold."""
    n = len(fields)
    visited = set()
    clusters = []

    for i in range(n):
        if i in visited:
            continue
        cluster = [i]
        visited.add(i)
        queue = [i]
        while queue:
            node = queue.pop(0)
            for j in range(n):
                if j in visited:
                    continue
                if corr_matrix[node, j] >= threshold:
                    visited.add(j)
                    cluster.append(j)
                    queue.append(j)
        clusters.append([fields[idx] for idx in cluster])

    clusters.sort(key=len, reverse=True)
    return clusters


def main():
    parser = argparse.ArgumentParser(description="PnL time series correlation analysis")
    parser.add_argument("--top-pairs", type=int, default=30,
                        help="Number of top pairs to show in each analysis (default 30)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output JSON path")
    parser.add_argument("--cluster-threshold", type=float, default=0.5,
                        help="Correlation threshold for clustering (default 0.5)")
    args = parser.parse_args()

    # Step 1: Load and map data
    print("Step 1: Loading field-to-alpha mapping...")
    field_map = load_field_mapping()
    print(f"  {len(field_map)} fields with PnL-available alphas")

    template_counts = defaultdict(int)
    for f, alphas in field_map.items():
        n_templates = len(set(a["template"] for a in alphas))
        template_counts[n_templates] += 1
    print(f"  Template coverage: {dict(sorted(template_counts.items()))} templates")

    # Step 2: Aggregate returns
    print("\nStep 2: Building Sharpe-weighted aggregated returns...")
    print("  Loading PnL matrix (this may take a moment)...")
    pnl_df = pd.read_csv(PNL_CSV, index_col=0, parse_dates=True)
    print(f"  PnL matrix: {pnl_df.shape[0]} days x {pnl_df.shape[1]} alphas")

    returns_df = build_aggregated_returns(field_map, pnl_df)
    print(f"  Aggregated returns: {returns_df.shape[0]} days x {returns_df.shape[1]} fields")

    # Step 3a: Pairwise correlation
    print(f"\n{'='*80}")
    print("3a. PAIRWISE PEARSON CORRELATION")
    print(f"{'='*80}")
    corr_matrix = pairwise_correlation(returns_df)
    fields = returns_df.columns.tolist()
    n = len(fields)
    print(f"  Correlation matrix: {n} x {n}")

    # Find most correlated pairs
    high_corr_pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            c = corr_matrix[i, j]
            if abs(c) > 0.5:
                high_corr_pairs.append((fields[i], fields[j], c))
    high_corr_pairs.sort(key=lambda x: -abs(x[2]))

    print(f"  Pairs with |corr| > 0.5: {len(high_corr_pairs)}")
    print(f"\n  Top {args.top_pairs} correlated pairs (PnL returns):")
    print(f"  {'Field A':35s} {'Field B':35s} {'Corr':>7s}")
    print(f"  {'-'*80}")
    for a, b, c in high_corr_pairs[:args.top_pairs]:
        print(f"  {a:35s} {b:35s} {c:>7.3f}")

    # Most independent fields
    avg_abs_corr = np.nanmean(np.abs(corr_matrix), axis=1)
    independent_idx = np.argsort(avg_abs_corr)
    print("\n  Most INDEPENDENT fields (lowest avg |return correlation|):")
    print(f"  {'Field':40s} {'AvgAbsCorr':>10s}")
    for idx in independent_idx[:15]:
        print(f"  {fields[idx]:40s} {avg_abs_corr[idx]:>10.4f}")

    # Clustering
    clusters = hierarchical_clusters(corr_matrix, fields, threshold=args.cluster_threshold)
    non_trivial = [c for c in clusters if len(c) > 1]
    singletons = [c for c in clusters if len(c) == 1]
    print(f"\n  Clusters (threshold={args.cluster_threshold}):")
    print(f"    Non-trivial: {len(non_trivial)}, Singletons: {len(singletons)}")
    for i, cluster in enumerate(non_trivial[:10], 1):
        print(f"    Cluster {i} ({len(cluster)} fields): {', '.join(cluster[:5])}"
              + (f" +{len(cluster)-5} more" if len(cluster) > 5 else ""))

    # Step 3b: Rolling correlation
    print(f"\n{'='*80}")
    print("3b. ROLLING CORRELATION (60-day window)")
    print(f"{'='*80}")
    # Pick top correlated pairs for rolling analysis
    rolling_pairs = [(a, b) for a, b, c in high_corr_pairs[:50]]
    rolling_results = rolling_correlation(returns_df, window=60, pairs=rolling_pairs)

    stable_pairs = [(k, v) for k, v in rolling_results.items() if v["stability"] == "stable"]
    regime_pairs = [(k, v) for k, v in rolling_results.items() if v["stability"] == "regime_dependent"]
    print(f"  Analyzed {len(rolling_results)} pairs")
    print(f"  Stable correlations: {len(stable_pairs)}")
    print(f"  Regime-dependent: {len(regime_pairs)}")

    if regime_pairs:
        regime_pairs.sort(key=lambda x: -x[1]["std"])
        print("\n  Top regime-dependent pairs (highest correlation volatility):")
        print(f"  {'Pair':60s} {'Mean':>6s} {'Std':>6s} {'Min':>6s} {'Max':>6s} {'Flips':>5s}")
        for (a, b), v in regime_pairs[:15]:
            pair_str = f"{a} / {b}"[:60]
            print(f"  {pair_str:60s} {v['mean']:>6.3f} {v['std']:>6.3f} "
                  f"{v['min']:>6.3f} {v['max']:>6.3f} {v['sign_changes']:>5d}")

    # Step 3c: Lead-lag
    print(f"\n{'='*80}")
    print("3c. LEAD-LAG CROSS-CORRELATION")
    print(f"{'='*80}")
    lead_lag_results = lead_lag_analysis(returns_df, max_lag=5, top_n=args.top_pairs)
    print(f"  Pairs with lead-lag improvement: {len(lead_lag_results)}")
    if lead_lag_results:
        print("\n  Top lead-lag relationships:")
        print(f"  {'Leader':30s} {'Follower':30s} {'Lag':>4s} {'LagCorr':>8s} {'ZeroCorr':>9s} {'Improve':>8s}")
        for r in lead_lag_results[:args.top_pairs]:
            leader = r["field_a"] if r["best_lag"] > 0 else r["field_b"]
            follower = r["field_b"] if r["best_lag"] > 0 else r["field_a"]
            print(f"  {leader:30s} {follower:30s} {abs(r['best_lag']):>4d} "
                  f"{r['best_lag_corr']:>8.3f} {r['zero_lag_corr']:>9.3f} "
                  f"{r['lead_improvement']:>8.3f}")

    # Step 3d: Spectral coherence
    print(f"\n{'='*80}")
    print("3d. SPECTRAL COHERENCE (frequency bands)")
    print(f"{'='*80}")
    spectral_results = spectral_coherence(returns_df, top_n=args.top_pairs)

    for band, label in [("low", ">60 days"), ("medium", "5-60 days"), ("high", "<5 days")]:
        pairs = spectral_results.get(band, [])
        print(f"\n  {band.upper()} frequency ({label}): {len(pairs)} coherent pairs")
        if pairs:
            print(f"  {'Field A':30s} {'Field B':30s} {'Coh':>6s}")
            for p in pairs[:10]:
                print(f"  {p['field_a']:30s} {p['field_b']:30s} {p[band]:>6.3f}")

    # Identify fields coherent at different bands
    low_only = set()
    high_only = set()
    for p in spectral_results.get("low", []):
        pair = (p["field_a"], p["field_b"])
        if pair not in [(pp["field_a"], pp["field_b"]) for pp in spectral_results.get("high", [])]:
            low_only.add(pair)
    for p in spectral_results.get("high", []):
        pair = (p["field_a"], p["field_b"])
        if pair not in [(pp["field_a"], pp["field_b"]) for pp in spectral_results.get("low", [])]:
            high_only.add(pair)

    print(f"\n  Low-freq ONLY (same macro, different timing): {len(low_only)} pairs")
    print(f"  High-freq ONLY (same data source, redundant): {len(high_only)} pairs")

    # Spectrum analysis
    print(f"\n{'='*80}")
    print("EIGENVALUE SPECTRUM")
    print(f"{'='*80}")
    # Clean correlation matrix (handle NaN)
    corr_clean = np.nan_to_num(corr_matrix, nan=0.0)
    np.fill_diagonal(corr_clean, 1.0)
    eigenvalues = np.linalg.eigvalsh(corr_clean)
    eigenvalues = np.sort(eigenvalues)[::-1]
    total_var = eigenvalues.sum()
    cumulative = np.cumsum(eigenvalues) / total_var

    print(f"  Dimension: {n} fields")
    print("  Top eigenvalues:")
    for i in range(min(15, len(eigenvalues))):
        if eigenvalues[i] < 0.01:
            break
        pct = eigenvalues[i] / total_var * 100
        print(f"    PC{i+1:>2d}: {eigenvalues[i]:>8.2f} ({pct:>5.1f}%, cumul {cumulative[i]*100:>5.1f}%)")

    for target in [0.5, 0.75, 0.9, 0.95]:
        nc = int(np.searchsorted(cumulative, target) + 1)
        print(f"  Components for {target*100:.0f}% variance: {nc} / {n}")

    # Save output
    if args.output:
        output = {
            "summary": {
                "n_fields": n,
                "n_days": int(returns_df.shape[0]),
                "high_corr_pairs": len(high_corr_pairs),
                "n_clusters": len(non_trivial),
                "n_singletons": len(singletons),
                "lead_lag_pairs": len(lead_lag_results),
                "eigenvalue_50pct": int(np.searchsorted(cumulative, 0.5) + 1),
                "eigenvalue_90pct": int(np.searchsorted(cumulative, 0.9) + 1),
            },
            "top_correlated_pairs": [
                {"field_a": a, "field_b": b, "correlation": float(c)}
                for a, b, c in high_corr_pairs[:100]
            ],
            "independent_fields": [
                {"field": fields[idx], "avg_abs_corr": float(avg_abs_corr[idx])}
                for idx in independent_idx[:30]
            ],
            "clusters": [c for c in non_trivial[:20]],
            "rolling_regime_pairs": [
                {"pair": f"{k[0]} / {k[1]}", **v}
                for k, v in sorted(regime_pairs, key=lambda x: -x[1]["std"])[:30]
            ] if regime_pairs else [],
            "lead_lag": lead_lag_results,
            "spectral_coherence": {
                band: pairs[:20] for band, pairs in spectral_results.items()
            },
            "eigenvalues": eigenvalues[:30].tolist(),
        }
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(output, f, indent=2, default=str)
        print(f"\nOutput saved to {out_path}")


if __name__ == "__main__":
    main()
