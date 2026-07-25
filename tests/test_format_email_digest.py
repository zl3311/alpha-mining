"""Tests for scripts/format_email_digest.py.

Covers all three public functions with corner-case combinations:
- parse_meta_file: valid, no frontmatter, malformed YAML, missing closing fence,
  empty body, empty file
- format_subject: with/without candidates, non-numeric fitness, non-dict entries,
  missing fields, zero-fitness candidates
- format_html: markdown table rendering, fenced code blocks, inline code, empty
  body, zero vs non-zero candidates, non-dict candidate entries, missing candidate
  fields, fitness edge values (None, string, non-numeric), verdict color logic
  (all verdict × self_corr_result combos), budget_cap None fallback, CSS presence,
  PR URL embedding
"""

import importlib.util
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "format_email_digest.py"
_spec = importlib.util.spec_from_file_location("format_email_digest", _SCRIPT)
fmt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fmt)


# ---------------------------------------------------------------------------
# parse_meta_file
# ---------------------------------------------------------------------------

class TestParseMetaFile:
    def test_valid_frontmatter(self, tmp_path):
        p = tmp_path / "meta.md"
        p.write_text('---\nid: "S1"\nstrategy: EXPLORE\n---\n# Body here')
        meta, body = fmt.parse_meta_file(p)
        assert meta["id"] == "S1"
        assert meta["strategy"] == "EXPLORE"
        assert body == "# Body here"

    def test_no_frontmatter(self, tmp_path):
        p = tmp_path / "meta.md"
        p.write_text("# Just a heading\nno frontmatter")
        meta, body = fmt.parse_meta_file(p)
        assert meta == {}
        assert "Just a heading" in body

    def test_malformed_yaml(self, tmp_path):
        p = tmp_path / "meta.md"
        p.write_text("---\nbad: : : yaml\n  - broken\n---\nbody text")
        meta, body = fmt.parse_meta_file(p)
        assert meta == {}
        assert body == "body text"

    def test_missing_closing_fence(self, tmp_path):
        """Only one --- means split produces < 3 parts."""
        p = tmp_path / "meta.md"
        p.write_text("---\nid: X\nno closing fence")
        meta, body = fmt.parse_meta_file(p)
        assert meta == {}

    def test_empty_body(self, tmp_path):
        p = tmp_path / "meta.md"
        p.write_text('---\nid: "S1"\n---\n')
        meta, body = fmt.parse_meta_file(p)
        assert meta["id"] == "S1"
        assert body == ""

    def test_empty_file(self, tmp_path):
        p = tmp_path / "meta.md"
        p.write_text("")
        meta, body = fmt.parse_meta_file(p)
        assert meta == {}
        assert body == ""

    def test_yaml_returns_none(self, tmp_path):
        """YAML block that parses to None (e.g. just a comment)."""
        p = tmp_path / "meta.md"
        p.write_text("---\n# just a comment\n---\nbody")
        meta, body = fmt.parse_meta_file(p)
        assert meta == {}
        assert body == "body"

    def test_body_with_extra_dashes(self, tmp_path):
        """Body containing --- should not confuse the parser (split limit=2)."""
        p = tmp_path / "meta.md"
        p.write_text('---\nid: "S1"\n---\nline1\n---\nline2')
        meta, body = fmt.parse_meta_file(p)
        assert meta["id"] == "S1"
        assert "---" in body


# ---------------------------------------------------------------------------
# format_subject
# ---------------------------------------------------------------------------

class TestFormatSubject:
    def test_with_candidates(self):
        meta = {
            "id": "20260620-001",
            "strategy": "EXPLORE",
            "candidates": [{"fitness": 3.99}, {"fitness": 2.50}],
        }
        subj = fmt.format_subject(meta)
        assert "[Alpha Mining]" in subj
        assert "20260620-001" in subj
        assert "EXPLORE" in subj
        assert "2 candidates" in subj
        assert "F=3.99" in subj

    def test_no_candidates(self):
        meta = {"id": "S1", "strategy": "EXPLOIT"}
        subj = fmt.format_subject(meta)
        assert "0 candidates" in subj
        assert "F=" not in subj

    def test_empty_candidates_list(self):
        meta = {"id": "S1", "strategy": "?", "candidates": []}
        subj = fmt.format_subject(meta)
        assert "0 candidates" in subj
        assert "F=" not in subj

    def test_candidates_none(self):
        meta = {"id": "S1", "strategy": "?", "candidates": None}
        subj = fmt.format_subject(meta)
        assert "0 candidates" in subj

    def test_non_dict_candidate_skipped(self):
        meta = {"id": "S1", "strategy": "?", "candidates": ["bad", 42, None]}
        subj = fmt.format_subject(meta)
        assert "3 candidates" in subj
        assert "F=" not in subj

    def test_non_numeric_fitness(self):
        meta = {
            "id": "S1",
            "strategy": "?",
            "candidates": [{"fitness": "not_a_number"}],
        }
        subj = fmt.format_subject(meta)
        assert "1 candidates" in subj
        assert "F=" not in subj

    def test_fitness_none(self):
        meta = {
            "id": "S1",
            "strategy": "?",
            "candidates": [{"fitness": None}],
        }
        subj = fmt.format_subject(meta)
        assert "F=" not in subj

    def test_fitness_zero(self):
        meta = {
            "id": "S1",
            "strategy": "?",
            "candidates": [{"fitness": 0}],
        }
        subj = fmt.format_subject(meta)
        assert "F=" not in subj

    def test_missing_id_and_strategy(self):
        subj = fmt.format_subject({})
        assert "unknown" in subj
        assert "?" in subj

    def test_mixed_valid_invalid_fitness(self):
        meta = {
            "id": "S1",
            "strategy": "?",
            "candidates": [
                {"fitness": "bad"},
                {"fitness": 1.5},
                {"fitness": None},
                {"fitness": 3.0},
                "not_a_dict",
            ],
        }
        subj = fmt.format_subject(meta)
        assert "F=3.00" in subj


# ---------------------------------------------------------------------------
# format_html — markdown rendering
# ---------------------------------------------------------------------------

class TestFormatHtmlMarkdown:
    """Verify markdown extensions produce correct HTML elements."""

    PR = "https://github.com/test/pr/1"

    def test_table_renders_as_html(self):
        body = "| A | B |\n|---|---|\n| 1 | 2 |"
        html = fmt.format_html({"id": "S1"}, body, self.PR)
        assert "<table>" in html
        assert "<th>A</th>" in html
        assert "<td>1</td>" in html

    def test_fenced_code_renders(self):
        body = "```\nrank(close/open)\n```"
        html = fmt.format_html({"id": "S1"}, body, self.PR)
        assert "<pre>" in html
        assert "<code>" in html
        assert "rank(close/open)" in html

    def test_inline_code_renders(self):
        body = "Use `ts_delay(x, 5)` here."
        html = fmt.format_html({"id": "S1"}, body, self.PR)
        assert "<code>ts_delay(x, 5)</code>" in html

    def test_bold_renders(self):
        body = "This is **important**."
        html = fmt.format_html({"id": "S1"}, body, self.PR)
        assert "<strong>important</strong>" in html

    def test_multiple_tables_in_body(self):
        body = (
            "## T1\n\n| X |\n|---|\n| 1 |\n\n"
            "## T2\n\n| Y |\n|---|\n| 2 |\n"
        )
        html = fmt.format_html({"id": "S1"}, body, self.PR)
        assert html.count("<table>") >= 2

    def test_table_with_bold_cells(self):
        body = "| A |\n|---|\n| **bold** |"
        html = fmt.format_html({"id": "S1"}, body, self.PR)
        assert "<strong>bold</strong>" in html
        assert "<table>" in html

    def test_empty_body(self):
        html = fmt.format_html({"id": "S1"}, "", self.PR)
        assert "<em>No details available.</em>" in html

    def test_none_body_equivalent(self):
        html = fmt.format_html({"id": "S1"}, None, self.PR)
        assert "<em>No details available.</em>" in html


# ---------------------------------------------------------------------------
# format_html — candidate table
# ---------------------------------------------------------------------------

class TestFormatHtmlCandidates:
    PR = "https://github.com/test/pr/1"

    def test_zero_candidates_no_table_header(self):
        html = fmt.format_html({"id": "S1"}, "body", self.PR)
        assert "No submission candidates" in html
        assert "<th>Alpha</th>" not in html

    def test_candidates_present_shows_table(self):
        meta = {
            "id": "S1",
            "candidates": [
                {
                    "id": "ABC",
                    "grade": "EXCELLENT",
                    "fitness": 2.5,
                    "self_corr_value": 0.6,
                    "self_corr_result": "PASS",
                    "verdict": "SUBMITTABLE",
                }
            ],
        }
        html = fmt.format_html(meta, "body", self.PR)
        assert "<th>Alpha</th>" in html
        assert "ABC" in html
        assert "No submission candidates" not in html

    def test_non_dict_candidates_skipped(self):
        meta = {"id": "S1", "candidates": ["garbage", 42, {"id": "OK"}]}
        html = fmt.format_html(meta, "body", self.PR)
        assert "OK" in html
        assert "garbage" not in html.split("<table>")[-1]

    def test_missing_candidate_fields_default(self):
        meta = {"id": "S1", "candidates": [{}]}
        html = fmt.format_html(meta, "body", self.PR)
        assert "<th>Alpha</th>" in html
        assert "?" in html

    def test_fitness_string(self):
        meta = {"id": "S1", "candidates": [{"fitness": "2.75"}]}
        html = fmt.format_html(meta, "body", self.PR)
        assert "2.75" in html

    def test_fitness_none(self):
        meta = {"id": "S1", "candidates": [{"fitness": None}]}
        html = fmt.format_html(meta, "body", self.PR)
        assert "None" in html

    def test_fitness_non_numeric(self):
        meta = {"id": "S1", "candidates": [{"fitness": "N/A"}]}
        html = fmt.format_html(meta, "body", self.PR)
        assert "N/A" in html

    def test_alpha_link(self):
        meta = {"id": "S1", "candidates": [{"id": "XYZ123"}]}
        html = fmt.format_html(meta, "body", self.PR)
        assert "https://platform.worldquantbrain.com/alpha/XYZ123" in html


# ---------------------------------------------------------------------------
# format_html — verdict color logic
# ---------------------------------------------------------------------------

class TestFormatHtmlVerdictColors:
    """Brute-force verdict × self_corr_result color combos."""

    PR = "https://github.com/test/pr/1"
    GREEN = "#2e7d32"
    ORANGE = "#f57c00"

    @pytest.mark.parametrize(
        "verdict,sc_result,expected_color",
        [
            ("SUBMITTABLE", "PASS", "#2e7d32"),
            ("SUBMITTABLE", "PASS_PREMIUM", "#2e7d32"),
            ("SUBMITTABLE", "FAIL", "#f57c00"),
            ("SAFE", "PASS", "#2e7d32"),
            ("SAFE", "FAIL", "#f57c00"),
            ("RISKY", "PASS", "#2e7d32"),
            ("RISKY", "FAIL", "#f57c00"),
            ("BLOCKED", "PASS", "#f57c00"),
            ("BLOCKED", "FAIL", "#f57c00"),
            ("WINNER", "PASS", "#f57c00"),
            ("BACKUP", "PASS", "#f57c00"),
            ("?", "?", "#f57c00"),
        ],
    )
    def test_verdict_color(self, verdict, sc_result, expected_color):
        meta = {
            "id": "S1",
            "candidates": [
                {"verdict": verdict, "self_corr_result": sc_result}
            ],
        }
        html = fmt.format_html(meta, "body", self.PR)
        assert f'color:{expected_color}' in html


# ---------------------------------------------------------------------------
# format_html — header / structural elements
# ---------------------------------------------------------------------------

class TestFormatHtmlStructure:
    PR = "https://github.com/test/pr/1"

    def test_css_style_block_present(self):
        html = fmt.format_html({"id": "S1"}, "body", self.PR)
        assert "<style>" in html
        assert "border-collapse" in html

    def test_pr_url_in_output(self):
        html = fmt.format_html({"id": "S1"}, "body", self.PR)
        assert self.PR in html
        assert "View full PR on GitHub" in html

    def test_session_id_in_header(self):
        html = fmt.format_html({"id": "MY-SESSION"}, "body", self.PR)
        assert "MY-SESSION" in html

    def test_budget_cap_none_fallback(self):
        meta = {"id": "S1", "budget_used": 50, "budget_cap": None}
        html = fmt.format_html(meta, "body", self.PR)
        assert "50/100" in html

    def test_budget_cap_zero_fallback(self):
        meta = {"id": "S1", "budget_used": 50, "budget_cap": 0}
        html = fmt.format_html(meta, "body", self.PR)
        assert "50/100" in html

    def test_all_meta_defaults(self):
        html = fmt.format_html({}, "body", self.PR)
        assert "unknown" in html
        assert "?/100" in html

    def test_doctype_present(self):
        html = fmt.format_html({"id": "S1"}, "body", self.PR)
        assert html.startswith("<!DOCTYPE html>")

    def test_viewport_meta(self):
        html = fmt.format_html({"id": "S1"}, "body", self.PR)
        assert 'name="viewport"' in html


# ---------------------------------------------------------------------------
# main() integration via CLI
# ---------------------------------------------------------------------------

class TestMainCLI:
    def test_writes_output_files(self, tmp_path):
        meta = tmp_path / "meta.md"
        meta.write_text(
            '---\nid: "CLI-1"\nstrategy: EXPLORE\ncandidates:\n'
            '  - id: A1\n    fitness: 2.0\n---\n'
            "| Col |\n|-----|\n| val |"
        )
        out = tmp_path / "out"
        import subprocess
        import sys

        result = subprocess.run(
            [
                sys.executable,
                str(_SCRIPT),
                "--meta-file", str(meta),
                "--pr-url", "https://github.com/test",
                "--output-dir", str(out),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        subj = (out / "email_subject.txt").read_text()
        body = (out / "email_body.html").read_text()
        assert "CLI-1" in subj
        assert "<table>" in body
        assert "<th>Col</th>" in body

    def test_missing_meta_file_exits_1(self, tmp_path):
        import subprocess
        import sys

        result = subprocess.run(
            [
                sys.executable,
                str(_SCRIPT),
                "--meta-file", str(tmp_path / "nope.md"),
                "--pr-url", "https://github.com/test",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 1

    def test_missing_id_exits_1(self, tmp_path):
        meta = tmp_path / "meta.md"
        meta.write_text("---\nstrategy: X\n---\nbody")
        import subprocess
        import sys

        result = subprocess.run(
            [
                sys.executable,
                str(_SCRIPT),
                "--meta-file", str(meta),
                "--pr-url", "https://github.com/test",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 1
