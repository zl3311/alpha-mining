"""
Pull PnL curves from BRAIN and compute pairwise correlation matrix.

This is the LOCAL verification path for self-correlation. The cloud agent
uses the server's pre-computed self_corr instead (via hf_query.py).

Modes:
  --vs-book       Local PnL-return correlation (original mode)
  --brain-check   BRAIN's authoritative SELF_CORRELATION check result
  --brain-corr    Full self-correlation breakdown from BRAIN

Usage:
    uv run python3 scripts/pnl_correlation.py --alphas ABC123 --vs-book
    uv run python3 scripts/pnl_correlation.py --from-server --grade EXCELLENT --vs-book
    uv run python3 scripts/pnl_correlation.py --alphas ABC123 DEF456 --save-pnl /tmp/pnl.csv
    uv run python3 scripts/pnl_correlation.py --alphas ABC123 --brain-check
    uv run python3 scripts/pnl_correlation.py --alphas ABC123 --brain-corr
"""

import argparse
import asyncio
import os
import sys
import time
from pathlib import Path

import httpx
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

BRAIN_URL = "https://api.worldquantbrain.com"
SERVER_URL = os.environ.get("HF_SERVER_URL", "").rstrip("/")
API_KEY = os.environ.get("HF_API_KEY", "")
HF_TOKEN = os.environ.get("HF_TOKEN", "")

# Terminal SELF_CORRELATION results from GET /alphas/{id}/check.
# PENDING means still computing; keep polling. ERROR is terminal (distinct from FAIL).
_TERMINAL_SELF_CORR = frozenset({"PASS", "FAIL", "ERROR"})
_DEFAULT_MAX_WAIT_SECONDS = 900  # 15 min — peak-load lag often exceeds 9 min
_TRANSIENT_HTTP = frozenset({502, 503, 504})

if not API_KEY or not HF_TOKEN:
    from alpha_mining.config import get_settings as _gs
    _s = _gs()
    API_KEY = API_KEY or getattr(_s, "hf_api_key", "")
    HF_TOKEN = HF_TOKEN or getattr(_s, "hf_token", "")

SERVER_HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "X-API-Key": API_KEY,
}


async def brain_auth(client: httpx.AsyncClient) -> None:
    from alpha_mining.config import get_settings
    settings = get_settings()
    r = await client.post(
        "/authentication",
        auth=(settings.brain_email, settings.brain_password),
    )
    if r.status_code != 201:
        raise RuntimeError(f"BRAIN auth failed: HTTP {r.status_code} -- {r.text[:200]}")
    print(f"  BRAIN auth OK (cookies: {len(client.cookies)})")


async def fetch_pnl(client: httpx.AsyncClient, alpha_id: str) -> pd.Series | None:
    last_failure = "unknown"
    for attempt in range(8):
        r = await client.get(f"/alphas/{alpha_id}/recordsets/pnl")
        if r.status_code == 401:
            print(f"    {alpha_id}: 401 -- re-authenticating")
            await brain_auth(client)
            last_failure = "auth"
            continue
        if r.status_code == 429:
            raw_retry = r.headers.get("Retry-After", "10")
            try:
                retry_after = int(float(raw_retry))
            except (ValueError, TypeError):
                retry_after = 10
            print(f"    {alpha_id}: 429 rate-limited, waiting {retry_after}s")
            await asyncio.sleep(retry_after)
            last_failure = "rate_limited"
            continue
        if r.status_code != 200:
            print(f"    {alpha_id}: HTTP {r.status_code}")
            return None
        if r.text and len(r.text) > 100:
            break
        # Long-poll: BRAIN returns 200 + empty body + Retry-After when generating PnL
        retry_after_str = r.headers.get("Retry-After", "")
        if retry_after_str:
            wait = max(float(retry_after_str), 0.5)
            await asyncio.sleep(wait)
            last_failure = "long_poll"
            continue
        last_failure = "empty"
        await asyncio.sleep(1)
    else:
        msg = {
            "rate_limited": "RATE LIMITED -- sustained 429s (self-corr may be incomplete)",
            "empty": "empty PnL after retries",
            "auth": "authentication failed after retries",
        }.get(last_failure, f"failed ({last_failure})")
        print(f"    {alpha_id}: {msg}")
        return None
    data = r.json()
    records = data.get("records", [])
    if not records:
        print(f"    {alpha_id}: 0 records in response")
        return None
    schema = [p["name"] for p in data.get("schema", {}).get("properties", [])]
    di = schema.index("date")
    pi = schema.index("pnl")
    return pd.Series(
        {pd.Timestamp(rec[di]): float(rec[pi]) for rec in records},
        name=alpha_id,
    ).sort_index()


def _parse_retry_after(headers, default: int = 5) -> int:
    """Parse Retry-After header safely, handling numeric and HTTP-date forms."""
    raw = headers.get("Retry-After", "")
    if not raw:
        return default
    try:
        return max(1, int(float(raw)))
    except (ValueError, TypeError):
        return default


def extract_self_corr_check(data: dict) -> dict | None:
    """Return the SELF_CORRELATION check dict from a /check payload, or None."""
    checks = data.get("is", {}).get("checks", [])
    if not isinstance(checks, list):
        return None
    for chk in checks:
        name = (chk.get("name") or "").upper().replace("-", "_").replace(" ", "_")
        if name == "SELF_CORRELATION" or "SELFCORRELATION" in name.replace("_", ""):
            return chk
    return None


def is_already_submitted_check(data: dict) -> bool:
    """True when /check only reports ALREADY_SUBMITTED (no SELF_CORRELATION).

    Submitted alphas no longer expose SELF_CORRELATION on /check; the payload
    is typically just ALREADY_SUBMITTED: FAIL. Peer corr still comes from
    /correlations/self.
    """
    checks = data.get("is", {}).get("checks", [])
    if not isinstance(checks, list) or not checks:
        return False
    if extract_self_corr_check(data) is not None:
        return False
    return any(c.get("name") == "ALREADY_SUBMITTED" for c in checks)


def _self_corr_is_terminal(sc_check: dict | None) -> bool:
    """True when SELF_CORRELATION has a terminal result (PASS/FAIL/ERROR)."""
    if not sc_check:
        return False
    result = (sc_check.get("result") or "").upper()
    if result in _TERMINAL_SELF_CORR:
        return True
    # Some payloads omit result but include a numeric value — treat as ready.
    value = sc_check.get("value")
    if result not in ("", "PENDING") and value not in ("", None):
        return True
    return False


def _corr_records_from_payload(corr_data: dict) -> list[dict]:
    """Parse /correlations/self records into sorted peer dicts (schema-aware)."""
    schema = [p["name"] for p in corr_data.get("schema", {}).get("properties", [])]
    col_map = {name: idx for idx, name in enumerate(schema)}
    corr_records = []
    for rec in corr_data.get("records", []):
        corr_val = rec[col_map.get("correlation", 5)]
        if corr_val is None:
            continue
        try:
            corr_val = float(corr_val)
        except (TypeError, ValueError):
            continue
        sharpe_raw = rec[col_map.get("sharpe", 6)] if len(rec) > col_map.get("sharpe", 6) else None
        try:
            sharpe = float(sharpe_raw) if sharpe_raw is not None else None
        except (TypeError, ValueError):
            sharpe = None
        corr_records.append({
            "id": rec[col_map.get("id", 0)],
            "correlation": corr_val,
            "sharpe": sharpe,
        })
    corr_records.sort(key=lambda x: -abs(x["correlation"]))
    return corr_records


async def fetch_brain_check(
    client: httpx.AsyncClient,
    alpha_id: str,
    max_wait_seconds: int = _DEFAULT_MAX_WAIT_SECONDS,
) -> dict | None:
    """Poll GET /alphas/{id}/check until SELF_CORRELATION is terminal or budget expires.

    BRAIN long-polls this endpoint: empty 200 + Retry-After means still computing.
    Under peak load the wait is often ~9 minutes and can exceed 90 minutes; we
    also retry 429/502/503 and transport timeouts instead of aborting.

    Note: POST /alphas/{id}/check returns HTTP 405 (as of 2026-07) — GET only.
    Submitted alphas return ALREADY_SUBMITTED without SELF_CORRELATION.
    """
    deadline = time.monotonic() + max_wait_seconds
    attempt = 0
    while time.monotonic() < deadline:
        attempt += 1
        try:
            r = await client.get(f"/alphas/{alpha_id}/check")
        except (httpx.TimeoutException, httpx.TransportError) as exc:
            wait = min(15, 2 + attempt)
            print(f"    {alpha_id}: transport error ({type(exc).__name__}), retry in {wait}s (#{attempt})")
            await asyncio.sleep(wait)
            continue

        if r.status_code == 401:
            print(f"    {alpha_id}: 401 -- re-authenticating")
            await brain_auth(client)
            continue
        if r.status_code == 429:
            retry_after = _parse_retry_after(r.headers, default=10)
            print(f"    {alpha_id}: 429 rate-limited, waiting {retry_after}s (#{attempt})")
            await asyncio.sleep(retry_after)
            continue
        if r.status_code in _TRANSIENT_HTTP:
            wait = _parse_retry_after(r.headers, default=min(15, 2 + attempt))
            print(f"    {alpha_id}: HTTP {r.status_code}, retry in {wait}s (#{attempt})")
            await asyncio.sleep(wait)
            continue
        if r.status_code != 200:
            wait = min(10, 2 + attempt)
            print(f"    {alpha_id}: HTTP {r.status_code}, retry in {wait}s (#{attempt})")
            await asyncio.sleep(wait)
            continue

        # Long-poll: empty 200 + Retry-After while check is generating
        if not r.text or len(r.text) < 10:
            retry_after = _parse_retry_after(r.headers, default=5)
            print(f"    {alpha_id}: async pending (empty body), retry in {retry_after}s (#{attempt})")
            await asyncio.sleep(retry_after)
            continue

        try:
            data = r.json()
        except Exception:
            wait = _parse_retry_after(r.headers, default=5)
            print(f"    {alpha_id}: invalid JSON, retry in {wait}s (#{attempt})")
            await asyncio.sleep(wait)
            continue

        checks = data.get("is", {}).get("checks", [])
        if not checks:
            retry_after = _parse_retry_after(r.headers, default=5)
            print(f"    {alpha_id}: empty checks, retry in {retry_after}s (#{attempt})")
            await asyncio.sleep(retry_after)
            continue

        if is_already_submitted_check(data):
            data["_check_status"] = "ALREADY_SUBMITTED"
            print(f"    {alpha_id}: /check reports ALREADY_SUBMITTED (no SELF_CORRELATION on submitted alphas)")
            return data

        sc_check = extract_self_corr_check(data)
        if _self_corr_is_terminal(sc_check):
            data["_check_status"] = (sc_check.get("result") or "").upper()
            print(
                f"    {alpha_id}: SELF_CORRELATION "
                f"result={sc_check.get('result')} value={sc_check.get('value')} "
                f"(attempt {attempt})"
            )
            return data

        # Checks present but SELF_CORRELATION still PENDING / missing — keep waiting
        result = (sc_check or {}).get("result", "missing")
        retry_after = _parse_retry_after(r.headers, default=10)
        print(
            f"    {alpha_id}: SELF_CORRELATION pending "
            f"(result={result!r}), retry in {retry_after}s (#{attempt})"
        )
        await asyncio.sleep(retry_after)

    print(f"    {alpha_id}: check polling timed out after {max_wait_seconds}s")
    return None


async def fetch_brain_self_corr(
    client: httpx.AsyncClient,
    alpha_id: str,
    max_wait_seconds: int = _DEFAULT_MAX_WAIT_SECONDS,
) -> dict | None:
    """Poll GET /alphas/{id}/correlations/self until peer records arrive or budget expires."""
    deadline = time.monotonic() + max_wait_seconds
    attempt = 0
    while time.monotonic() < deadline:
        attempt += 1
        try:
            r = await client.get(f"/alphas/{alpha_id}/correlations/self")
        except (httpx.TimeoutException, httpx.TransportError) as exc:
            wait = min(15, 2 + attempt)
            print(f"    {alpha_id}: transport error ({type(exc).__name__}), retry in {wait}s (#{attempt})")
            await asyncio.sleep(wait)
            continue

        if r.status_code == 401:
            print(f"    {alpha_id}: 401 -- re-authenticating")
            await brain_auth(client)
            continue
        if r.status_code == 429:
            retry_after = _parse_retry_after(r.headers, default=10)
            print(f"    {alpha_id}: 429 rate-limited, waiting {retry_after}s (#{attempt})")
            await asyncio.sleep(retry_after)
            continue
        if r.status_code in _TRANSIENT_HTTP:
            wait = _parse_retry_after(r.headers, default=min(15, 2 + attempt))
            print(f"    {alpha_id}: HTTP {r.status_code}, retry in {wait}s (#{attempt})")
            await asyncio.sleep(wait)
            continue
        if r.status_code != 200:
            wait = min(10, 2 + attempt)
            print(f"    {alpha_id}: HTTP {r.status_code}, retry in {wait}s (#{attempt})")
            await asyncio.sleep(wait)
            continue

        if not r.text or len(r.text) < 10:
            retry_after = _parse_retry_after(r.headers, default=5)
            print(f"    {alpha_id}: async pending, retry in {retry_after}s (#{attempt})")
            await asyncio.sleep(retry_after)
            continue

        try:
            data = r.json()
        except Exception:
            wait = _parse_retry_after(r.headers, default=5)
            print(f"    {alpha_id}: invalid JSON, retry in {wait}s (#{attempt})")
            await asyncio.sleep(wait)
            continue

        if not data.get("records"):
            retry_after = _parse_retry_after(r.headers, default=5)
            print(f"    {alpha_id}: no records yet, retry in {retry_after}s (#{attempt})")
            await asyncio.sleep(retry_after)
            continue
        return data

    print(f"    {alpha_id}: correlations/self polling timed out after {max_wait_seconds}s")
    return None


def print_brain_check_results(results: dict[str, dict], labels: dict[str, str], infos: dict) -> None:
    """Print BRAIN SELF_CORRELATION check verdicts (PASS/FAIL/ERROR/PENDING/TIMEOUT)."""
    print(f"\n{'Alpha':>25} {'Grade':>9} {'S':>5} {'F':>5} | "
          f"{'SelfCorr':>8} {'Limit':>6} {'Result':>10} | Top Corr Peer")
    print("-" * 115)

    for alpha_id, data in sorted(results.items(), key=lambda x: -infos.get(x[0], {}).get("fitness", 0)):
        info = infos.get(alpha_id, {})
        label = labels.get(alpha_id, alpha_id)[:25]

        status = data.get("_check_status")
        sc_check = extract_self_corr_check(data)
        corr_records = data.get("_corr_records", [])

        value, limit = 0.0, 0.0
        if sc_check:
            raw_value = sc_check.get("value")
            raw_limit = sc_check.get("limit")
            try:
                value = float(raw_value) if raw_value is not None else 0.0
            except (TypeError, ValueError):
                value = 0.0
            try:
                limit = float(raw_limit) if raw_limit is not None else 0.0
            except (TypeError, ValueError):
                limit = 0.0

        if status == "TIMEOUT":
            verdict_marker = "TIMEOUT"
            if value == 0.0 and corr_records:
                try:
                    value = abs(float(corr_records[0]["correlation"]))
                except (TypeError, ValueError, KeyError):
                    pass
        elif status == "ALREADY_SUBMITTED":
            verdict_marker = "SUBMITTED"
            if corr_records:
                try:
                    value = abs(float(corr_records[0]["correlation"]))
                except (TypeError, ValueError, KeyError):
                    pass
        elif sc_check:
            result = (sc_check.get("result") or "?").upper()
            # Keep PASS/FAIL/PENDING/ERROR distinct — never coerce PENDING→FAIL
            verdict_marker = result if result else "?"
        else:
            verdict_marker = status or "N/A"

        peer_str = ""
        if corr_records:
            top = corr_records[0]
            try:
                peer_id = str(top["id"])[:8]
                sharpe = top.get("sharpe")
                if sharpe is not None:
                    peer_str = f"{float(top['correlation']):.3f} ({peer_id} S={float(sharpe):.2f})"
                else:
                    peer_str = f"{float(top['correlation']):.3f} ({peer_id})"
            except (TypeError, ValueError):
                peer_str = f"{top.get('id', '?')}"
            if status == "TIMEOUT":
                peer_str = f"est {peer_str}"

        print(
            f"{label:>25} {info.get('grade', '?'):>9} "
            f"{info.get('sharpe', 0):>5.2f} {info.get('fitness', 0):>5.2f} | "
            f"{value:>8.4f} {limit:>6.2f} {verdict_marker:>10} | {peer_str}"
        )


def print_brain_corr_breakdown(results: dict[str, dict], labels: dict[str, str]) -> None:
    """Print full self-correlation breakdown from BRAIN."""
    for alpha_id, data in results.items():
        label = labels.get(alpha_id, alpha_id)
        schema = [p["name"] for p in data.get("schema", {}).get("properties", [])]
        records = data.get("records", [])

        print(f"\n{'='*80}")
        print(f"  Self-correlations for: {label} ({alpha_id})")
        print(f"  {len(records)} correlated alpha(s) in book")
        print(f"{'='*80}")

        if not records:
            print("  (no correlations found)")
            continue

        col_map = {name: idx for idx, name in enumerate(schema)}
        id_i = col_map.get("id", 0)
        name_i = col_map.get("name", 1)
        corr_i = col_map.get("correlation", 5)
        sharpe_i = col_map.get("sharpe", 6)
        returns_i = col_map.get("returns", 7)
        turnover_i = col_map.get("turnover", 8)
        fitness_i = col_map.get("fitness", 9)
        margin_i = col_map.get("margin", 10)

        print(f"\n  {'ID':>10} {'Name':>20} {'Corr':>7} {'Sharpe':>7} {'Return':>8} {'TO':>6} {'Fit':>6} {'Margin':>8}")
        print(f"  {'-'*10} {'-'*20} {'-'*7} {'-'*7} {'-'*8} {'-'*6} {'-'*6} {'-'*8}")

        for rec in sorted(records, key=lambda r: -abs(r[corr_i] if isinstance(r[corr_i], (int, float)) else 0)):
            rid = str(rec[id_i])[:10] if len(schema) > id_i else "?"
            name = str(rec[name_i])[:20] if len(schema) > name_i else "?"
            corr = rec[corr_i] if len(schema) > corr_i and isinstance(rec[corr_i], (int, float)) else 0
            sharpe = rec[sharpe_i] if len(schema) > sharpe_i and isinstance(rec[sharpe_i], (int, float)) else 0
            returns = rec[returns_i] if len(schema) > returns_i and isinstance(rec[returns_i], (int, float)) else 0
            turnover = rec[turnover_i] if len(schema) > turnover_i and isinstance(rec[turnover_i], (int, float)) else 0
            fitness = rec[fitness_i] if len(schema) > fitness_i and isinstance(rec[fitness_i], (int, float)) else 0
            margin = rec[margin_i] if len(schema) > margin_i and isinstance(rec[margin_i], (int, float)) else 0
            print(f"  {rid:>10} {name:>20} {corr:>7.4f} {sharpe:>7.2f} "
              f"{returns:>8.4f} {turnover:>6.3f} {fitness:>6.2f} {margin:>8.5f}")


async def get_server_alphas(
    grades: list[str] | None = None,
    min_sharpe: float = 1.25,
    min_fitness: float = 1.0,
) -> list[dict]:
    if not SERVER_URL:
        print(
            "HF_SERVER_URL is not set; cannot read candidates from the queue server. "
            "Copy .env.example to .env and point it at your own deployment (see server/).",
            file=sys.stderr,
        )
        return []

    grade_filter = ""
    if grades:
        grade_list = ",".join(f'"{g}"' for g in grades)
        grade_filter = f"AND r.grade IN ({grade_list})"

    sql = f"""
        SELECT r.alpha_id, j.expression, r.sharpe, r.fitness, r.turnover, r.grade
        FROM jobs j JOIN results r ON r.job_id = j.id
        WHERE r.sharpe >= {min_sharpe} AND r.fitness >= {min_fitness} {grade_filter}
        ORDER BY r.fitness DESC
    """
    async with httpx.AsyncClient(timeout=10.0) as srv:
        r = await srv.get(
            f"{SERVER_URL}/v1/db/query",
            params={"sql": sql},
            headers=SERVER_HEADERS,
        )
        if r.status_code != 200:
            print(f"Server query failed: {r.status_code}")
            return []
        data = r.json()
        return [
            {"alpha_id": row[0], "expression": row[1], "sharpe": row[2],
             "fitness": row[3], "turnover": row[4], "grade": row[5]}
            for row in data.get("rows", [])
            if row[0]
        ]


def compute_correlation(frames: dict[str, pd.Series], years: int = 4) -> pd.DataFrame:
    pnl = pd.DataFrame(frames)
    ret = pnl - pnl.ffill().shift(1)
    cutoff = ret.index.max() - pd.DateOffset(years=years)
    ret = ret[ret.index > cutoff].dropna()
    return ret.corr()


def print_correlation_matrix(corr: pd.DataFrame, labels: dict[str, str]) -> None:
    ids = list(corr.columns)
    short = {aid: labels.get(aid, aid)[:18] for aid in ids}

    header = "".join(f"{short[c]:>20}" for c in ids)
    print(f"\n{'':>20}{header}")
    for i in ids:
        vals = "".join(f"{corr.loc[i, j]:>20.3f}" for j in ids)
        print(f"{short[i]:>20}{vals}")


def print_submission_viability(corr: pd.DataFrame, labels: dict[str, str], submitted: list[str], infos: dict) -> None:
    candidates = [a for a in corr.index if a not in submitted]

    print(f"\n{'Alpha':>25} {'Grade':>9} {'S':>5} {'F':>5} | {'vs_book':>8} {'Verdict':>8} | Top mutual")
    print("-" * 110)

    for cand in sorted(candidates, key=lambda c: -infos.get(c, {}).get("fitness", 0)):
        info = infos.get(cand, {})
        vs_book = max(
            (abs(corr.loc[cand, sub]) for sub in submitted if sub in corr.columns),
            default=0,
        )
        verdict = "SAFE" if vs_book < 0.60 else "RISKY" if vs_book < 0.70 else "BLOCKED"

        mutual = sorted(
            [(abs(corr.loc[cand, o]), labels.get(o, o)[:15])
             for o in candidates if o != cand and o in corr.columns],
            reverse=True,
        )[:2]
        mutual_str = ", ".join(f"{value:.2f}({peer})" for value, peer in mutual)

        label = labels.get(cand, cand)[:25]
        print(
            f"{label:>25} {info.get('grade', '?'):>9} {info.get('sharpe', 0):>5.2f} "
            f"{info.get('fitness', 0):>5.2f} | {vs_book:>8.3f} {verdict:>8} | {mutual_str}"
        )


async def main():
    parser = argparse.ArgumentParser(description="PnL correlation analysis")
    parser.add_argument("--alphas", nargs="+", help="Alpha IDs to correlate")
    parser.add_argument("--from-server", action="store_true", help="Pull gate-passers from the server")
    parser.add_argument("--grade", default=None, help="Comma-separated grades to filter (e.g., GOOD,EXCELLENT)")
    parser.add_argument("--vs-book", action="store_true", help="Include submitted alphas for self-corr check")
    parser.add_argument("--brain-check", action="store_true",
                        help="Use BRAIN's /check endpoint for authoritative SELF_CORRELATION verdict")
    parser.add_argument("--brain-corr", action="store_true",
                        help="Use BRAIN's /correlations/self endpoint for full breakdown")
    parser.add_argument(
        "--max-wait-seconds",
        type=int,
        default=_DEFAULT_MAX_WAIT_SECONDS,
        help=f"Max wall-clock seconds to poll /check or /correlations/self (default: {_DEFAULT_MAX_WAIT_SECONDS})",
    )
    parser.add_argument("--save-pnl", default=None, help="Save PnL returns to CSV")
    parser.add_argument("--years", type=int, default=4, help="Rolling window for correlation (default: 4)")
    args = parser.parse_args()

    alpha_ids = []
    infos = {}
    labels = {}

    # Submitted book -- read from data/book/*.md (V2, canonical source)
    book_dir = Path(__file__).resolve().parent.parent / "data" / "book"

    submitted = []
    submitted_labels = {}

    if book_dir.exists() and any(book_dir.glob("*.md")):
        import yaml
        for md_file in sorted(book_dir.glob("*.md")):
            text = md_file.read_text()
            if text.startswith("---"):
                parts = text.split("---", 2)
                if len(parts) >= 3:
                    try:
                        fm = yaml.safe_load(parts[1]) or {}
                    except yaml.YAMLError:
                        continue
                    aid = fm.get("alpha_id", md_file.stem)
                    status = fm.get("status")
                    if status is None:
                        print(f"  WARNING: {md_file.name} has no status field, skipping")
                        continue
                    if status == "ACTIVE":
                        submitted.append(aid)
                        family = fm.get("family", aid)[:15]
                        submitted_labels[aid] = f"SUB:{family}"
        print(f"  Loaded {len(submitted)} ACTIVE book entries from data/book/")
    else:
        submitted = ["RRN1EM51", "zq5RLWO8"]
        submitted_labels = {"RRN1EM51": "SUB:intraday_rev", "zq5RLWO8": "SUB:return_rev"}
        print("  WARNING: data/book/ is empty, using hardcoded fallback")

    if args.from_server:
        grades = args.grade.split(",") if args.grade else None
        server_alphas = await get_server_alphas(grades=grades)
        print(f"Found {len(server_alphas)} alphas from server")
        for a in server_alphas:
            aid = a["alpha_id"]
            alpha_ids.append(aid)
            infos[aid] = a
            labels[aid] = a["expression"][:25]

    if args.alphas:
        for aid in args.alphas:
            if aid not in alpha_ids:
                alpha_ids.append(aid)
                labels[aid] = aid

    if args.vs_book:
        for aid in submitted:
            if aid not in alpha_ids:
                alpha_ids.append(aid)
            labels[aid] = submitted_labels.get(aid, aid)

    if not alpha_ids:
        parser.print_help()
        return

    client = httpx.AsyncClient(base_url=BRAIN_URL, follow_redirects=True, timeout=90.0)
    await brain_auth(client)
    max_wait = args.max_wait_seconds

    # --- BRAIN check mode: authoritative SELF_CORRELATION verdict ---
    if args.brain_check:
        print(
            f"\n  Fetching BRAIN /check for {len(alpha_ids)} alpha(s) "
            f"(max wait {max_wait}s each)..."
        )
        check_results = {}
        for aid in alpha_ids:
            data = await fetch_brain_check(client, aid, max_wait_seconds=max_wait)
            if data is None:
                # Budget exhausted — still try peer breakdown as an estimate
                data = {"is": {"checks": []}, "_check_status": "TIMEOUT"}
            # Peer budget: remaining time for TIMEOUT cases, else full budget
            peer_wait = max_wait if data.get("_check_status") != "TIMEOUT" else min(120, max_wait)
            corr_data = await fetch_brain_self_corr(client, aid, max_wait_seconds=peer_wait)
            if corr_data:
                data["_corr_records"] = _corr_records_from_payload(corr_data)
            check_results[aid] = data
            await asyncio.sleep(0.5)
        await client.aclose()
        if check_results:
            print_brain_check_results(check_results, labels, infos)
        else:
            print("  No check results retrieved.")
        return

    # --- BRAIN full correlation breakdown mode ---
    if args.brain_corr:
        print(
            f"\n  Fetching BRAIN /correlations/self for {len(alpha_ids)} alpha(s) "
            f"(max wait {max_wait}s each)..."
        )
        corr_results = {}
        for aid in alpha_ids:
            data = await fetch_brain_self_corr(client, aid, max_wait_seconds=max_wait)
            if data:
                corr_results[aid] = data
            await asyncio.sleep(0.5)
        await client.aclose()
        if corr_results:
            print_brain_corr_breakdown(corr_results, labels)
        else:
            print("  No correlation data retrieved.")
        return

    # --- Original local PnL correlation mode ---
    frames = {}
    for aid in alpha_ids:
        pnl = await fetch_pnl(client, aid)
        if pnl is not None:
            frames[aid] = pnl
            print(f"  {labels.get(aid, aid):>30}: {len(pnl)} pts")
        else:
            print(f"  {labels.get(aid, aid):>30}: NO PnL")
        await asyncio.sleep(0.3)

    await client.aclose()

    if len(frames) < 2:
        print(f"\nOnly {len(frames)} alphas with PnL -- need at least 2")
        return

    # Compute correlation
    corr = compute_correlation(frames, years=args.years)
    print_correlation_matrix(corr, labels)

    if args.vs_book:
        print_submission_viability(corr, labels, submitted, infos)

    if args.save_pnl:
        pnl_df = pd.DataFrame(frames)
        ret_df = pnl_df - pnl_df.ffill().shift(1)
        ret_df.to_csv(args.save_pnl)
        print(f"\nPnL returns saved to {args.save_pnl}")


if __name__ == "__main__":
    asyncio.run(main())
