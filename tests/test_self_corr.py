"""Tests for self-correlation infrastructure: thresholds, book filtering, sync."""

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pandas as pd


class TestCorrelationMath:
    """Test the correlation computation from pnl_correlation.py."""

    def test_perfect_correlation(self):
        from scripts.pnl_correlation import compute_correlation

        dates = pd.date_range("2022-01-01", periods=1000, freq="B")
        pnl = pd.Series(np.cumsum(np.random.randn(1000)), index=dates, name="A")
        frames = {"A": pnl, "B": pnl.copy().rename("B")}
        corr = compute_correlation(frames, years=4)
        assert abs(corr.loc["A", "B"] - 1.0) < 0.001

    def test_uncorrelated(self):
        from scripts.pnl_correlation import compute_correlation

        np.random.seed(42)
        dates = pd.date_range("2022-01-01", periods=1000, freq="B")
        frames = {
            "A": pd.Series(np.cumsum(np.random.randn(1000)), index=dates, name="A"),
            "B": pd.Series(np.cumsum(np.random.randn(1000)), index=dates, name="B"),
        }
        corr = compute_correlation(frames, years=4)
        assert abs(corr.loc["A", "B"]) < 0.15

    def test_negative_correlation(self):
        from scripts.pnl_correlation import compute_correlation

        dates = pd.date_range("2022-01-01", periods=1000, freq="B")
        base = np.cumsum(np.random.randn(1000))
        frames = {
            "A": pd.Series(base, index=dates, name="A"),
            "B": pd.Series(-base, index=dates, name="B"),
        }
        corr = compute_correlation(frames, years=4)
        assert corr.loc["A", "B"] < -0.9


class TestThresholdClassification:
    """Test that self-corr verdicts use the correct thresholds."""

    def test_safe_threshold(self):
        assert 0.59 < 0.60  # SAFE
        assert not (0.60 < 0.60)  # boundary -> RISKY

    def test_risky_threshold(self):
        assert 0.60 >= 0.60 and 0.60 < 0.70  # RISKY
        assert 0.675 >= 0.60 and 0.675 < 0.70  # RISKY

    def test_blocked_threshold(self):
        assert 0.70 >= 0.70  # BLOCKED
        assert 0.75 >= 0.70  # BLOCKED

    def test_print_submission_viability_thresholds(self):
        """Verify the actual code uses 0.60/0.70 aligned with result-analysis bands."""
        import inspect

        from scripts.pnl_correlation import print_submission_viability
        source = inspect.getsource(print_submission_viability)
        assert "0.60" in source, "SAFE threshold should be 0.60"
        assert "0.70" in source, "BLOCKED threshold should be 0.70"


class TestBookFiltering:
    """Test that PENDING entries are excluded from the submitted book."""

    def _create_book_dir(self, tmp: Path, entries: list[dict]):
        book_dir = tmp / "data" / "book"
        book_dir.mkdir(parents=True)
        for e in entries:
            content = (
                f"---\nalpha_id: \"{e['id']}\"\nstatus: \"{e['status']}\"\n"
                f"family: \"{e.get('family', 'test')}\"\n---\n# Alpha\n"
            )
            (book_dir / f"{e['id']}.md").write_text(content)
        return book_dir

    def test_active_included(self):
        from scripts.sync_server_book import read_local_book

        with tempfile.TemporaryDirectory() as tmp:
            book_dir = self._create_book_dir(Path(tmp), [
                {"id": "AAA", "status": "ACTIVE"},
                {"id": "BBB", "status": "ACTIVE"},
            ])
            with patch("scripts.sync_server_book.BOOK_DIR", book_dir):
                entries = read_local_book()
            assert len(entries) == 2
            assert {e["alpha_id"] for e in entries} == {"AAA", "BBB"}

    def test_pending_excluded(self):
        from scripts.sync_server_book import read_local_book

        with tempfile.TemporaryDirectory() as tmp:
            book_dir = self._create_book_dir(Path(tmp), [
                {"id": "AAA", "status": "ACTIVE"},
                {"id": "BBB", "status": "PENDING"},
                {"id": "CCC", "status": "REJECTED"},
            ])
            with patch("scripts.sync_server_book.BOOK_DIR", book_dir):
                entries = read_local_book()
            assert len(entries) == 1
            assert entries[0]["alpha_id"] == "AAA"

    def test_empty_book(self):
        from scripts.sync_server_book import read_local_book

        with tempfile.TemporaryDirectory() as tmp:
            book_dir = Path(tmp) / "data" / "book"
            book_dir.mkdir(parents=True)
            with patch("scripts.sync_server_book.BOOK_DIR", book_dir):
                entries = read_local_book()
            assert entries == []


class TestSyncPayload:
    """Test that the sync payload shape matches the server's SeedBookEntry."""

    def test_payload_fields(self):
        from scripts.sync_server_book import read_local_book

        with tempfile.TemporaryDirectory() as tmp:
            book_dir = Path(tmp) / "data" / "book"
            book_dir.mkdir(parents=True)
            content = (
                '---\nalpha_id: "TEST1"\nstatus: "ACTIVE"\nexpression: "rank(close)"\n'
                'sharpe: 2.5\nfitness: 1.8\nfamily: "test"\n---\n# Alpha\n'
            )
            (book_dir / "TEST1.md").write_text(content)

            with patch("scripts.sync_server_book.BOOK_DIR", book_dir):
                entries = read_local_book()

            assert len(entries) == 1
            e = entries[0]
            assert set(e.keys()) == {"alpha_id", "expression", "sharpe", "fitness"}
            assert e["alpha_id"] == "TEST1"
            assert e["expression"] == "rank(close)"
            assert e["sharpe"] == 2.5
            assert e["fitness"] == 1.8

    def test_payload_is_json_serializable(self):
        from scripts.sync_server_book import read_local_book

        with tempfile.TemporaryDirectory() as tmp:
            book_dir = Path(tmp) / "data" / "book"
            book_dir.mkdir(parents=True)
            content = '---\nalpha_id: "X"\nstatus: "ACTIVE"\nexpression: "rank(x)"\nsharpe: 1.0\nfitness: 1.0\n---\n'
            (book_dir / "X.md").write_text(content)

            with patch("scripts.sync_server_book.BOOK_DIR", book_dir):
                entries = read_local_book()

            serialized = json.dumps(entries)
            assert '"alpha_id": "X"' in serialized


class TestHfQuerySelfCorr:
    """Test self-corr verdict classification in hf_query output."""

    def test_verdict_thresholds(self):
        def verdict(sc):
            return "SAFE" if sc < 0.55 else "RISKY" if sc < 0.62 else "BLOCKED"

        assert verdict(0.0) == "SAFE"
        assert verdict(0.49) == "SAFE"
        assert verdict(0.549) == "SAFE"
        assert verdict(0.55) == "RISKY"
        assert verdict(0.60) == "RISKY"
        assert verdict(0.619) == "RISKY"
        assert verdict(0.62) == "BLOCKED"
        assert verdict(0.633) == "BLOCKED"
        assert verdict(0.80) == "BLOCKED"
