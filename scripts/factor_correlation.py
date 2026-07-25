"""
Cross-factor correlation and spectrum analysis.

Aggregates single-factor Sharpe across the 3 basic templates (rank_level, rank_value_norm,
rank_delta) for each field, then uses the factor profile correlation notes + sweep Sharpe
patterns to build a cross-field correlation structure and identify independent clusters.

Usage:
    uv run python3 scripts/factor_correlation.py
    uv run python3 scripts/factor_correlation.py --top 50
    uv run python3 scripts/factor_correlation.py --output local/test_scripts/correlation_analysis.json
"""

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
SWEEP_CSV = ROOT / "local" / "sweep_analysis" / "sweep_data.csv"
PROFILES_DIR = ROOT / "data" / "knowledge" / "factor_profiles"
BOOK_DIR = ROOT / "data" / "book"
FACTORS_DIR = ROOT / "data" / "factors"


def load_sweep_aggregated(universe: str = "TOP3000") -> dict[str, dict]:
    """Load sweep data and aggregate Sharpe by field across 3 basic templates.

    Returns {field: {rank_level: S, rank_value_norm: S, rank_delta: S, dataset: str, avg_sharpe: float}}
    """
    with open(SWEEP_CSV) as f:
        rows = list(csv.DictReader(f))

    fields = defaultdict(lambda: {"rank_level": None, "rank_value_norm": None, "rank_delta": None, "dataset": ""})

    for r in rows:
        field = r["field"]
        if field.startswith("-1"):
            continue
        template = r["template"]
        univ = r["universe"]
        if template not in ("rank_level", "rank_value_norm", "rank_delta"):
            continue
        if univ != universe:
            continue
        try:
            s = float(r["sharpe"])
        except (ValueError, TypeError):
            continue

        entry = fields[field]
        entry["dataset"] = r["dataset"]
        if entry[template] is None or s > entry[template]:
            entry[template] = s

    # Compute aggregate metrics
    result = {}
    for field, data in fields.items():
        sharpes = [v for k, v in data.items() if k in ("rank_level", "rank_value_norm", "rank_delta") and v is not None]
        if len(sharpes) < 2:
            continue
        data["avg_sharpe"] = sum(sharpes) / len(sharpes)
        data["max_sharpe"] = max(sharpes)
        data["min_sharpe"] = min(sharpes)
        data["n_templates"] = len(sharpes)
        result[field] = data

    return result


def parse_profile_correlations(profiles_dir: Path) -> dict[str, list[tuple[str, float]]]:
    """Parse correlation notes from factor profile markdown files.

    Returns {field: [(correlated_field, correlation_value), ...]}
    """
    correlations = {}
    corr_pattern = re.compile(r"^- (.+?):\s*([\d.]+)\s*\(")

    for profile_path in profiles_dir.glob("*.md"):
        field = profile_path.stem
        in_corr_section = False
        field_corrs = []

        with open(profile_path) as f:
            for line in f:
                if "## Correlation Notes" in line:
                    in_corr_section = True
                    continue
                if in_corr_section:
                    if line.startswith("##"):
                        break
                    m = corr_pattern.match(line.strip())
                    if m:
                        corr_field = m.group(1).strip()
                        corr_val = float(m.group(2))
                        field_corrs.append((corr_field, corr_val))

        if field_corrs:
            correlations[field] = field_corrs

    return correlations


def build_correlation_matrix(correlations: dict, fields: set) -> tuple[list[str], np.ndarray]:
    """Build a symmetric correlation matrix from sparse correlation notes.

    Uses the top-5 correlations reported in each profile to construct a sparse
    symmetric matrix, then fills diagonal with 1.0.
    """
    field_list = sorted(fields)
    field_idx = {f: i for i, f in enumerate(field_list)}
    n = len(field_list)
    matrix = np.zeros((n, n))
    np.fill_diagonal(matrix, 1.0)

    for field, corrs in correlations.items():
        if field not in field_idx:
            continue
        i = field_idx[field]
        for corr_field, corr_val in corrs:
            if corr_field in field_idx:
                j = field_idx[corr_field]
                matrix[i, j] = max(matrix[i, j], corr_val)
                matrix[j, i] = max(matrix[j, i], corr_val)

    return field_list, matrix


def compute_sharpe_correlation(sweep_data: dict, universe: str = "TOP3000") -> tuple[list[str], np.ndarray]:
    """Compute cross-field correlation based on Sharpe pattern similarity.

    For each field, the signal vector is [rank_level_S, rank_value_norm_S, rank_delta_S]
    across multiple universes. Fields with similar signal patterns are likely correlated.
    """
    with open(SWEEP_CSV) as f:
        rows = list(csv.DictReader(f))

    TEMPLATES = ["rank_level", "rank_value_norm", "rank_delta"]
    UNIVERSES = ["TOP200", "TOP500", "TOP1000", "TOP3000"]

    # Build feature vector for each field: Sharpe across all (template, universe) combos
    field_vectors = defaultdict(lambda: {})
    for r in rows:
        field = r["field"]
        if field.startswith("-1"):
            continue
        template = r["template"]
        univ = r["universe"]
        if template not in TEMPLATES or univ not in UNIVERSES:
            continue
        try:
            s = float(r["sharpe"])
        except (TypeError, ValueError):
            continue
        key = f"{template}_{univ}"
        if key not in field_vectors[field] or abs(s) > abs(field_vectors[field][key]):
            field_vectors[field][key] = s

    # Filter to fields with enough data points (at least 6/12 combos)
    all_keys = [f"{t}_{u}" for t in TEMPLATES for u in UNIVERSES]
    complete_fields = {}
    for field, vec in field_vectors.items():
        present = [k for k in all_keys if k in vec]
        if len(present) >= 6:
            values = [vec.get(k, np.nan) for k in all_keys]
            complete_fields[field] = values

    field_list = sorted(complete_fields.keys())

    # Build matrix and compute pairwise Pearson correlation
    # Use pandas for NaN-aware correlation (missing template/universe combos are NaN, not 0)
    import pandas as pd
    data_df = pd.DataFrame(complete_fields, index=all_keys).T
    data_df = data_df.loc[field_list]
    corr_matrix = data_df.T.corr().fillna(0).values

    return field_list, corr_matrix


def identify_clusters(field_list: list[str], corr_matrix: np.ndarray,
                      threshold: float = 0.5) -> list[list[str]]:
    """Identify correlation clusters using simple connected-component approach."""
    n = len(field_list)
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
                if abs(corr_matrix[node, j]) >= threshold:
                    visited.add(j)
                    cluster.append(j)
                    queue.append(j)
        clusters.append([field_list[idx] for idx in cluster])

    clusters.sort(key=len, reverse=True)
    return clusters


def load_book_fields() -> set[str]:
    """Load fields used in submitted book alphas."""
    book_fields = set()
    if not BOOK_DIR.exists():
        return book_fields

    for f in BOOK_DIR.glob("*.md"):
        with open(f) as fh:
            for line in fh:
                if line.startswith("---"):
                    continue
                # Look for expression or field references
    return book_fields


def main():
    parser = argparse.ArgumentParser(description="Cross-factor correlation analysis")
    parser.add_argument("--top", type=int, default=100,
                        help="Analyze top N fields by average Sharpe (default 100)")
    parser.add_argument("--threshold", type=float, default=0.5,
                        help="Correlation threshold for clustering (default 0.5)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output JSON path")
    args = parser.parse_args()

    print("Loading sweep data (aggregated by field)...")
    sweep_data = load_sweep_aggregated("TOP3000")
    print(f"  {len(sweep_data)} fields with at least 2 templates at TOP3000")

    # Sort by average Sharpe
    ranked = sorted(sweep_data.items(), key=lambda x: -x[1]["avg_sharpe"])

    print(f"\n{'='*90}")
    print(f"TOP {args.top} FIELDS BY AVERAGE SHARPE (3 templates, TOP3000)")
    print(f"{'='*90}")
    print(f"{'#':>3s} {'Field':40s} {'Dataset':15s} {'RankLvl':>8s} {'ValNorm':>8s} {'Delta':>8s} {'Avg':>6s}")
    print("-" * 90)
    for i, (field, data) in enumerate(ranked[:args.top], 1):
        rl = f"{data['rank_level']:.2f}" if data['rank_level'] is not None else "N/A"
        rv = f"{data['rank_value_norm']:.2f}" if data['rank_value_norm'] is not None else "N/A"
        rd = f"{data['rank_delta']:.2f}" if data['rank_delta'] is not None else "N/A"
        print(f"{i:>3d} {field:40s} {data['dataset']:15s} {rl:>8s} {rv:>8s} {rd:>8s} {data['avg_sharpe']:>6.2f}")

    # Profile-based correlation analysis
    print(f"\n{'='*90}")
    print("CORRELATION ANALYSIS (from factor profile notes)")
    print(f"{'='*90}")

    print("\nParsing factor profile correlation notes...")
    profile_corrs = parse_profile_correlations(PROFILES_DIR)
    print(f"  {len(profile_corrs)} profiles with correlation data")

    # Focus on top fields
    top_fields = set(f for f, _ in ranked[:args.top])
    top_profile_corrs = {f: c for f, c in profile_corrs.items() if f in top_fields}

    if top_profile_corrs:
        print(f"  {len(top_profile_corrs)} of top-{args.top} fields have correlation notes")

        # Build and analyze the correlation matrix
        field_list, corr_matrix = build_correlation_matrix(profile_corrs, top_fields & set(profile_corrs.keys()))
        print(f"  Correlation matrix: {len(field_list)} x {len(field_list)}")

        # Identify clusters
        clusters = identify_clusters(field_list, corr_matrix, threshold=args.threshold)
        non_trivial = [c for c in clusters if len(c) > 1]
        singletons = [c for c in clusters if len(c) == 1]

        print(f"\n  Clusters (threshold={args.threshold}):")
        print(f"    Non-trivial clusters (>1 field): {len(non_trivial)}")
        print(f"    Singletons (independent): {len(singletons)}")

        for i, cluster in enumerate(non_trivial[:15], 1):
            print(f"\n    Cluster {i} ({len(cluster)} fields):")
            for f in cluster[:8]:
                avg_s = sweep_data.get(f, {}).get("avg_sharpe", 0)
                ds = sweep_data.get(f, {}).get("dataset", "?")
                print(f"      {f:40s} ({ds}) avg_S={avg_s:.2f}")
            if len(cluster) > 8:
                print(f"      ... and {len(cluster) - 8} more")

    # Sharpe-pattern correlation (signal similarity)
    print(f"\n{'='*90}")
    print("SHARPE-PATTERN CORRELATION (signal vector similarity)")
    print(f"{'='*90}")

    print("\nComputing cross-field Sharpe pattern correlations...")
    sp_fields, sp_matrix = compute_sharpe_correlation(sweep_data)
    print(f"  {len(sp_fields)} fields with sufficient data")

    # Find highly correlated pairs
    high_corr_pairs = []
    for i in range(len(sp_fields)):
        for j in range(i + 1, len(sp_fields)):
            if abs(sp_matrix[i, j]) >= 0.8:
                high_corr_pairs.append((sp_fields[i], sp_fields[j], sp_matrix[i, j]))

    high_corr_pairs.sort(key=lambda x: -abs(x[2]))
    print(f"  Pairs with |corr| >= 0.8: {len(high_corr_pairs)}")

    print("\n  Top 30 most correlated field pairs (Sharpe pattern similarity):")
    print(f"  {'Field A':40s} {'Field B':40s} {'Corr':>6s}")
    print(f"  {'-'*88}")
    for a, b, c in high_corr_pairs[:30]:
        print(f"  {a:40s} {b:40s} {c:>6.3f}")

    # Find most independent fields (low correlation with everything)
    avg_abs_corr = np.mean(np.abs(sp_matrix), axis=1) - 1.0 / len(sp_fields)
    independent_idx = np.argsort(avg_abs_corr)
    print("\n  Most INDEPENDENT fields (lowest avg |correlation| with all others):")
    print(f"  {'Field':40s} {'Dataset':15s} {'AvgAbsCorr':>10s} {'AvgSharpe':>10s}")
    for idx in independent_idx[:20]:
        field = sp_fields[idx]
        ds = sweep_data.get(field, {}).get("dataset", "?")
        avg_s = sweep_data.get(field, {}).get("avg_sharpe", 0)
        print(f"  {field:40s} {ds:15s} {avg_abs_corr[idx]:>10.4f} {avg_s:>10.2f}")

    # Spectrum analysis: eigenvalue decomposition
    print(f"\n{'='*90}")
    print("SPECTRUM ANALYSIS (eigenvalue decomposition)")
    print(f"{'='*90}")

    eigenvalues = np.linalg.eigvalsh(sp_matrix)
    eigenvalues = np.sort(eigenvalues)[::-1]

    # Variance explained by top components
    total_var = eigenvalues.sum()
    cumulative = np.cumsum(eigenvalues) / total_var

    print(f"\n  Total variance (sum of eigenvalues): {total_var:.1f}")
    print(f"  Number of factors (matrix dimension): {len(eigenvalues)}")
    print("\n  Variance explained by top principal components:")
    print(f"  {'PC':>4s} {'Eigenvalue':>12s} {'% Variance':>12s} {'Cumulative %':>12s}")
    for i in range(min(20, len(eigenvalues))):
        pct = eigenvalues[i] / total_var * 100
        print(f"  {i+1:>4d} {eigenvalues[i]:>12.2f} {pct:>11.1f}% {cumulative[i]*100:>11.1f}%")

    # Effective dimensionality
    for target_pct in [0.5, 0.75, 0.9, 0.95]:
        n_components = np.searchsorted(cumulative, target_pct) + 1
        print(f"\n  Components for {target_pct*100:.0f}% variance: {n_components} / {len(eigenvalues)}")

    # Save output
    if args.output:
        output = {
            "top_fields": [
                {"field": f, "dataset": d["dataset"], "avg_sharpe": d["avg_sharpe"],
                 "rank_level": d["rank_level"], "rank_value_norm": d["rank_value_norm"],
                 "rank_delta": d["rank_delta"]}
                for f, d in ranked[:args.top]
            ],
            "high_correlation_pairs": [
                {"field_a": a, "field_b": b, "correlation": float(c)}
                for a, b, c in high_corr_pairs[:100]
            ],
            "spectrum": {
                "top_eigenvalues": eigenvalues[:20].tolist(),
                "cumulative_variance": cumulative[:20].tolist(),
                "n_for_50pct": int(np.searchsorted(cumulative, 0.5) + 1),
                "n_for_75pct": int(np.searchsorted(cumulative, 0.75) + 1),
                "n_for_90pct": int(np.searchsorted(cumulative, 0.90) + 1),
            },
        }
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(output, f, indent=2)
        print(f"\nOutput saved to {out_path}")


if __name__ == "__main__":
    main()
