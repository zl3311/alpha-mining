"""Unit tests for hardened BRAIN /check self-corr polling in pnl_correlation.py.

Covers PENDING-aware wait, 502/timeout retry, wall-clock TIMEOUT, and printer
labels that must not coerce PENDING/ERROR to FAIL.
"""

from __future__ import annotations

import io
from contextlib import redirect_stdout
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest


def _check_payload(result: str, value=None, limit=0.7) -> dict:
    chk = {"name": "SELF_CORRELATION", "result": result, "limit": limit}
    if value is not None:
        chk["value"] = value
    return {"is": {"checks": [
        {"name": "LOW_SHARPE", "result": "PASS", "value": 2.0},
        chk,
    ]}}


def _mock_response(status: int = 200, json_data=None, text: str | None = None,
                   headers: dict | None = None) -> MagicMock:
    r = MagicMock(spec=httpx.Response)
    r.status_code = status
    r.headers = headers or {}
    if json_data is not None:
        body = __import__("json").dumps(json_data)
        r.text = body
        r.json = MagicMock(return_value=json_data)
        r.content = body.encode()
    else:
        r.text = text if text is not None else ""
        r.content = (r.text or "").encode()
        r.json = MagicMock(side_effect=ValueError("no json"))
    return r


@pytest.mark.asyncio
async def test_pending_then_pass():
    """Checks present with SELF_CORRELATION=PENDING must continue until PASS."""
    from scripts.pnl_correlation import fetch_brain_check

    client = AsyncMock()
    client.get = AsyncMock(side_effect=[
        _mock_response(200, _check_payload("PENDING")),
        _mock_response(200, _check_payload("PASS", value=0.42)),
    ])

    with patch("scripts.pnl_correlation.asyncio.sleep", new_callable=AsyncMock):
        data = await fetch_brain_check(client, "abc123", max_wait_seconds=60)

    assert data is not None
    assert data["_check_status"] == "PASS"
    sc = next(c for c in data["is"]["checks"] if c["name"] == "SELF_CORRELATION")
    assert sc["result"] == "PASS"
    assert sc["value"] == 0.42
    assert client.get.await_count == 2


@pytest.mark.asyncio
async def test_http_502_then_pass():
    """HTTP 502 must retry, not abort."""
    from scripts.pnl_correlation import fetch_brain_check

    client = AsyncMock()
    client.get = AsyncMock(side_effect=[
        _mock_response(502, text="bad gateway"),
        _mock_response(200, _check_payload("PASS", value=0.55)),
    ])

    with patch("scripts.pnl_correlation.asyncio.sleep", new_callable=AsyncMock):
        data = await fetch_brain_check(client, "abc123", max_wait_seconds=60)

    assert data is not None
    assert data["_check_status"] == "PASS"
    assert client.get.await_count == 2


@pytest.mark.asyncio
async def test_connect_timeout_then_pass():
    """Transport timeout must retry, then succeed."""
    from scripts.pnl_correlation import fetch_brain_check

    client = AsyncMock()
    client.get = AsyncMock(side_effect=[
        httpx.ConnectTimeout("timed out"),
        _mock_response(200, _check_payload("FAIL", value=0.71)),
    ])

    with patch("scripts.pnl_correlation.asyncio.sleep", new_callable=AsyncMock):
        data = await fetch_brain_check(client, "abc123", max_wait_seconds=60)

    assert data is not None
    assert data["_check_status"] == "FAIL"
    assert client.get.await_count == 2


@pytest.mark.asyncio
async def test_empty_body_long_poll_then_pass():
    """Empty 200 + Retry-After is long-poll, not failure."""
    from scripts.pnl_correlation import fetch_brain_check

    client = AsyncMock()
    client.get = AsyncMock(side_effect=[
        _mock_response(200, text="", headers={"Retry-After": "1"}),
        _mock_response(200, _check_payload("PASS", value=0.3)),
    ])

    with patch("scripts.pnl_correlation.asyncio.sleep", new_callable=AsyncMock):
        data = await fetch_brain_check(client, "abc123", max_wait_seconds=60)

    assert data is not None
    assert data["_check_status"] == "PASS"


@pytest.mark.asyncio
async def test_sustained_pending_times_out():
    """Sustained PENDING past max_wait returns None (TIMEOUT for caller)."""
    from scripts.pnl_correlation import fetch_brain_check

    client = AsyncMock()
    client.get = AsyncMock(return_value=_mock_response(200, _check_payload("PENDING")))

    # Force deadline to expire immediately after first iteration by patching time
    times = iter([100.0, 100.1, 200.0])  # start, mid-loop check, past deadline

    with (
        patch("scripts.pnl_correlation.time.monotonic", side_effect=lambda: next(times, 200.0)),
        patch("scripts.pnl_correlation.asyncio.sleep", new_callable=AsyncMock),
    ):
        data = await fetch_brain_check(client, "abc123", max_wait_seconds=10)

    assert data is None


@pytest.mark.asyncio
async def test_already_submitted_only():
    """Submitted alphas: ALREADY_SUBMITTED without SELF_CORRELATION is terminal."""
    from scripts.pnl_correlation import fetch_brain_check

    payload = {"is": {"checks": [{"name": "ALREADY_SUBMITTED", "result": "FAIL"}]}}
    client = AsyncMock()
    client.get = AsyncMock(return_value=_mock_response(200, payload))

    data = await fetch_brain_check(client, "sub123", max_wait_seconds=60)
    assert data is not None
    assert data["_check_status"] == "ALREADY_SUBMITTED"


def test_printer_does_not_label_pending_as_fail():
    from scripts.pnl_correlation import print_brain_check_results

    results = {
        "a1": {
            "is": {"checks": [{"name": "SELF_CORRELATION", "result": "PENDING", "limit": 0.7}]},
            "_check_status": "PENDING",
        },
        "a2": {
            "is": {"checks": [{"name": "SELF_CORRELATION", "result": "ERROR", "limit": 0.7}]},
            "_check_status": "ERROR",
        },
        "a3": {
            "is": {"checks": []},
            "_check_status": "TIMEOUT",
            "_corr_records": [{"id": "peer1", "correlation": 0.61, "sharpe": 2.0}],
        },
    }
    buf = io.StringIO()
    with redirect_stdout(buf):
        print_brain_check_results(results, {"a1": "a1", "a2": "a2", "a3": "a3"}, {})
    out = buf.getvalue()
    assert "PENDING" in out
    assert "ERROR" in out
    assert "TIMEOUT" in out
    # Must not coerce PENDING → FAIL in the Result column
    # (FAIL may appear elsewhere only if we had a FAIL row; we don't)
    assert " FAIL " not in out or out.count("FAIL") == 0
    assert any("PENDING" in ln for ln in out.splitlines())


def test_extract_and_terminal_helpers():
    from scripts.pnl_correlation import (
        _self_corr_is_terminal,
        extract_self_corr_check,
        is_already_submitted_check,
    )

    pending = _check_payload("PENDING")
    assert not _self_corr_is_terminal(extract_self_corr_check(pending))
    passed = _check_payload("PASS", 0.5)
    assert _self_corr_is_terminal(extract_self_corr_check(passed))
    submitted = {"is": {"checks": [{"name": "ALREADY_SUBMITTED", "result": "FAIL"}]}}
    assert is_already_submitted_check(submitted)
    assert not is_already_submitted_check(passed)
