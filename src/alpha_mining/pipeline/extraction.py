"""
PDF extraction stage: convert research papers to structured markdown.

Primary: Datalab Marker API (cloud, high accuracy, preserves tables/equations).
Fallback: pymupdf4llm (local, free, no API key needed).

The Marker API is async: submit file, poll for completion, retrieve result.
Adapted from the user's existing doc_parser Streamlit app.
"""

from __future__ import annotations

import logging
import time
from pathlib import Path

import httpx

logger = logging.getLogger(__name__)

MARKER_API_URL = "https://www.datalab.to/api/v1/marker"
_POLL_INTERVAL = 2  # seconds
_MAX_POLL_ATTEMPTS = 300  # 10 minutes max


def extract_pdf(
    pdf_path: str | Path,
    *,
    api_key: str = "",
    mode: str = "balanced",
    use_llm: bool = True,
    force_ocr: bool = False,
) -> str:
    """
    Extract structured markdown from a PDF file.

    Uses Datalab Marker API if api_key is provided, otherwise falls back
    to local pymupdf4llm extraction.

    Args:
        pdf_path: Path to the PDF file.
        api_key: Datalab API key. If empty, uses pymupdf4llm fallback.
        mode: Marker processing mode ("fast", "balanced", "accurate").
        use_llm: Enable LLM-enhanced layout analysis in Marker.
        force_ocr: Force OCR on all pages.

    Returns:
        Extracted text as markdown string.
    """
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    if api_key:
        logger.info("Extracting %s via Marker API (mode=%s, llm=%s)", path.name, mode, use_llm)
        return _extract_via_marker(path, api_key, mode=mode, use_llm=use_llm, force_ocr=force_ocr)

    logger.info("Extracting %s via pymupdf4llm (no DATALAB_API_KEY)", path.name)
    return _extract_via_pymupdf(path)


def extract_pdf_with_images(
    pdf_path: str | Path,
    *,
    api_key: str = "",
    mode: str = "balanced",
    use_llm: bool = True,
) -> tuple[str, dict[str, str]]:
    """
    Extract markdown and images from a PDF via Marker API.

    Returns:
        Tuple of (markdown_text, images_dict) where images_dict maps
        filename -> base64-encoded image data.
    """
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    if not api_key:
        return _extract_via_pymupdf(path), {}

    result = _submit_and_poll_marker(path, api_key, mode=mode, use_llm=use_llm)
    markdown = result.get("markdown", "")
    images = result.get("images", {})
    return markdown, images


def extract_text_file(text_path: str | Path) -> str:
    """Read a plain text or markdown file directly."""
    path = Path(text_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path.read_text(encoding="utf-8")


def extract_and_save(
    pdf_path: str | Path,
    *,
    api_key: str = "",
    output_dir: str | Path = "data/papers",
    mode: str = "balanced",
    use_llm: bool = True,
) -> tuple[str, dict[str, str], Path, list[Path]]:
    """
    Extract a PDF and save markdown + images to disk.

    Directory structure:
        {output_dir}/{stem}/{stem}.md
        {output_dir}/{stem}/images/{filename}

    Args:
        pdf_path: Path to the PDF file.
        api_key: Datalab API key (falls back to pymupdf4llm if empty).
        output_dir: Base directory for saved papers.
        mode: Marker processing mode.
        use_llm: Enable LLM-enhanced layout in Marker.

    Returns:
        Tuple of (markdown_text, images_dict, markdown_path, image_paths).
        images_dict maps filename -> base64 string (raw from Marker).
    """
    import base64

    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    markdown, images = extract_pdf_with_images(
        path, api_key=api_key, mode=mode, use_llm=use_llm
    )

    stem = path.stem
    paper_dir = Path(output_dir) / stem
    paper_dir.mkdir(parents=True, exist_ok=True)

    # Rewrite image references to point to images/ subdirectory
    saved_markdown = markdown
    if images:
        for filename in images:
            saved_markdown = saved_markdown.replace(
                f"]({filename})", f"](images/{filename})"
            )

    md_path = paper_dir / f"{stem}.md"
    md_path.write_text(saved_markdown, encoding="utf-8")
    logger.info("Saved markdown to %s", md_path)

    img_paths: list[Path] = []
    if images:
        img_dir = paper_dir / "images"
        img_dir.mkdir(exist_ok=True)
        for filename, b64_data in images.items():
            raw = b64_data
            if "," in raw:
                raw = raw.split(",", 1)[1]
            try:
                img_bytes = base64.b64decode(raw)
                img_path = img_dir / filename
                img_path.write_bytes(img_bytes)
                img_paths.append(img_path)
            except Exception as e:
                logger.warning("Failed to save image %s: %s", filename, e)

        logger.info("Saved %d images to %s", len(img_paths), img_dir)

    return markdown, images, md_path, img_paths


# ---------------------------------------------------------------------------
# Marker API (Datalab)
# ---------------------------------------------------------------------------


def _extract_via_marker(
    path: Path,
    api_key: str,
    *,
    mode: str = "balanced",
    use_llm: bool = True,
    force_ocr: bool = False,
) -> str:
    """Submit PDF to Marker API, poll, return markdown."""
    result = _submit_and_poll_marker(
        path, api_key, mode=mode, use_llm=use_llm, force_ocr=force_ocr
    )
    markdown = result.get("markdown", "")
    logger.info("Marker extracted %d chars from %s", len(markdown), path.name)
    return markdown


def _submit_and_poll_marker(
    path: Path,
    api_key: str,
    *,
    mode: str = "balanced",
    use_llm: bool = True,
    force_ocr: bool = False,
) -> dict:
    """Full Marker API lifecycle: submit -> poll -> return result JSON."""
    headers = {"X-Api-Key": api_key}

    with open(path, "rb") as f:
        files = {"file": (path.name, f, "application/pdf")}
        data = {
            "mode": mode,
            "use_llm": str(use_llm).lower(),
            "force_ocr": str(force_ocr).lower(),
            "skip_cache": "false",
            "disable_image_extraction": "false",
        }

        with httpx.Client(timeout=60.0) as client:
            r = client.post(MARKER_API_URL, headers=headers, files=files, data=data)

    if r.status_code != 200:
        raise RuntimeError(f"Marker API upload failed (HTTP {r.status_code}): {r.text}")

    initial = r.json()
    request_id = initial.get("request_id")
    if not request_id:
        raise RuntimeError(f"Marker API did not return request_id: {initial}")

    logger.info("Marker job submitted: %s", request_id)
    return _poll_marker_result(request_id, headers)


def _poll_marker_result(request_id: str, headers: dict) -> dict:
    """Poll Marker API until job completes or fails."""
    check_url = f"{MARKER_API_URL}/{request_id}"

    with httpx.Client(timeout=30.0) as client:
        for attempt in range(_MAX_POLL_ATTEMPTS):
            r = client.get(check_url, headers=headers)
            data = r.json()
            status = data.get("status", "unknown")

            if status == "complete":
                logger.info("Marker job %s complete", request_id)
                return data
            elif status == "error":
                raise RuntimeError(f"Marker job {request_id} failed: {data.get('error', 'unknown')}")

            time.sleep(_POLL_INTERVAL)

    raise RuntimeError(f"Marker job {request_id} timed out after {_MAX_POLL_ATTEMPTS * _POLL_INTERVAL}s")


# ---------------------------------------------------------------------------
# pymupdf4llm fallback
# ---------------------------------------------------------------------------


def _extract_via_pymupdf(path: Path) -> str:
    """Local extraction using pymupdf4llm (no API key needed)."""
    try:
        import pymupdf4llm

        md_text = pymupdf4llm.to_markdown(str(path))
        logger.info("pymupdf4llm extracted %d chars from %s", len(md_text), path.name)
        return md_text
    except Exception as e:
        raise RuntimeError(f"pymupdf4llm extraction failed for {path.name}: {e}") from e
