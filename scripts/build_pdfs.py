#!/usr/bin/env python3
"""Convert training Markdown files to PDF for student distribution."""

from __future__ import annotations

import argparse
import html as html_module
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import TextLexer, get_lexer_by_name, guess_lexer


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_COURSES = ("PYTHON", "MYSQL")
STYLE_PATH = Path(__file__).resolve().parent / "pdf-style.css"
CHROME_PATHS = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
)


def find_chrome() -> Path:
    for candidate in CHROME_PATHS:
        path = Path(candidate)
        if path.exists():
            return path
    raise FileNotFoundError(
        "Google Chrome not found. Install Chrome or set CHROME_PATH to your browser."
    )


def md_to_html(md_text: str) -> str:
    extensions = [
        "tables",
        "fenced_code",
        "sane_lists",
        "nl2br",
        "attr_list",
    ]
    return markdown.markdown(md_text, extensions=extensions)


def highlight_code_blocks(html: str) -> str:
    formatter = HtmlFormatter(cssclass="highlight", nowrap=False)

    def replace_block(match: re.Match[str]) -> str:
        lang = match.group(1) or ""
        # Markdown escapes <, >, & in fenced code; unescape before Pygments
        # so operators like >>> are not double-encoded as &amp;gt;&gt;&gt;.
        code = html_module.unescape(match.group(2))
        lexer = TextLexer()
        if lang:
            try:
                lexer = get_lexer_by_name(lang, stripall=True)
            except Exception:
                lexer = guess_lexer(code)
        else:
            try:
                lexer = guess_lexer(code)
            except Exception:
                lexer = TextLexer()
        highlighted = highlight(code, lexer, formatter)
        # Pygments wraps in <div class="highlight"><pre>…</pre></div>; unwrap to
        # avoid invalid nested <pre> tags that shrink and clip code in Chrome PDF.
        highlighted = re.sub(
            r'^<div class="highlight"><pre>(.*?)</pre></div>\s*$',
            r"\1",
            highlighted,
            flags=re.DOTALL,
        )
        return f'<pre><code class="language-{lang}">{highlighted}</code></pre>'

    pattern = re.compile(
        r'<pre><code(?: class="language-([^"]*)")?>(.*?)</code></pre>',
        re.DOTALL,
    )
    return pattern.sub(replace_block, html)


def wrap_tables(html: str) -> str:
    def wrap_table(match: re.Match[str]) -> str:
        table = match.group(0)
        col_count = table.count("<th")
        if col_count >= 6:
            return f'<div class="table-wrap table-wrap-wide">{table}</div>'
        return f'<div class="table-wrap">{table}</div>'

    return re.sub(r"<table>.*?</table>", wrap_table, html, flags=re.DOTALL)


_BLOCK_PATTERN = re.compile(
    r"<h[1-6]>.*?</h[1-6]>"
    r'|<p>.*?</p>'
    r"|<pre><code[^>]*>.*?</code></pre>"
    r"|<blockquote>.*?</blockquote>"
    r"|<ul>.*?</ul>"
    r"|<ol>.*?</ol>"
    r"|<hr\s*/?>"
    r'|<div class="table-wrap[^"]*">.*?</div>',
    re.DOTALL | re.IGNORECASE,
)

_NOTE_START = re.compile(r"<p><strong>Note:</strong>", re.IGNORECASE)
_EG_START = re.compile(r"<p><strong>Eg", re.IGNORECASE)
_OUTPUT_START = re.compile(r"<p><strong>Output", re.IGNORECASE)
_CALLOUT_BOUNDARY = re.compile(
    r"^<h[1-6]>|^<div class=\"callout|^<div class=\"table-wrap",
    re.IGNORECASE,
)


def _split_html_blocks(html: str) -> list[str]:
    blocks: list[str] = []
    pos = 0
    for match in _BLOCK_PATTERN.finditer(html):
        if match.start() > pos:
            gap = html[pos : match.start()].strip()
            if gap:
                blocks.append(gap)
        blocks.append(match.group(0))
        pos = match.end()
    if pos < len(html):
        tail = html[pos:].strip()
        if tail:
            blocks.append(tail)
    return blocks


def _mark_output_pre(blocks: list[str]) -> list[str]:
    styled: list[str] = []
    for block in blocks:
        if block.startswith("<pre") and 'class="output-block"' not in block:
            styled.append(
                block.replace("<pre>", '<pre class="output-block">', 1).replace(
                    "<pre><code", '<pre class="output-block"><code', 1
                )
            )
        else:
            styled.append(block)
    return styled


def style_callouts(html: str) -> str:
    """Wrap Note, Example, and Output sections in styled callout boxes."""
    blocks = _split_html_blocks(html)
    styled: list[str] = []
    i = 0

    while i < len(blocks):
        block = blocks[i]

        if _NOTE_START.search(block):
            styled.append(f'<div class="callout callout-note">{block}</div>')
            i += 1
            continue

        if _OUTPUT_START.search(block):
            chunk = [block]
            i += 1
            while i < len(blocks) and blocks[i].startswith("<pre"):
                chunk.append(blocks[i])
                i += 1
            inner = "".join(_mark_output_pre(chunk))
            styled.append(f'<div class="callout callout-output">{inner}</div>')
            continue

        if _EG_START.search(block):
            chunk = [block]
            i += 1
            while i < len(blocks):
                nxt = blocks[i]
                if (
                    _CALLOUT_BOUNDARY.search(nxt)
                    or _NOTE_START.search(nxt)
                    or _OUTPUT_START.search(nxt)
                    or _EG_START.search(nxt)
                ):
                    break
                chunk.append(nxt)
                i += 1
            styled.append(
                f'<div class="callout callout-example">{"".join(chunk)}</div>'
            )
            continue

        styled.append(block)
        i += 1

    return "".join(styled)


_H1_PATTERN = re.compile(r"^\s*<h1>(.*?)</h1>\s*", re.DOTALL | re.IGNORECASE)


def peel_first_h1(html: str) -> tuple[str, str | None]:
    """Remove the leading H1 from body and return its plain-text for the doc title."""
    match = _H1_PATTERN.match(html)
    if not match:
        return html, None
    inner = re.sub(r"<[^>]+>", "", match.group(1))
    h1_title = html_module.unescape(inner).strip() or None
    return html[match.end() :], h1_title


def wrap_document(title: str, body_html: str, css: str) -> str:
    body_html, h1_title = peel_first_h1(body_html)
    display_title = h1_title or title
    safe_title = html_module.escape(display_title)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=794, initial-scale=1">
  <title>{safe_title}</title>
  <style>{css}</style>
</head>
<body>
  <div class="pdf-doc-title">{safe_title}</div>
  <main class="pdf-body">
{body_html}
  </main>
  <footer class="pdf-page-footer">{safe_title}</footer>
</body>
</html>"""


def html_to_pdf(html_path: Path, pdf_path: Path, chrome: Path) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(chrome),
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--no-pdf-header-footer",
        "--window-size=794,1123",
        "--force-device-scale-factor=1",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=10000",
        f"--print-to-pdf={pdf_path}",
        html_path.as_uri(),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"Chrome timed out creating PDF: {pdf_path.name}") from exc
    if result.returncode != 0 or not pdf_path.exists():
        raise RuntimeError(
            "Chrome failed to create PDF.\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )


def convert_file(
    md_path: Path, out_dir: Path, css: str, chrome: Path, force: bool
) -> Path | None:
    pdf_path = out_dir / f"{md_path.stem}.pdf"
    if pdf_path.exists() and not force and pdf_path.stat().st_mtime >= md_path.stat().st_mtime:
        print(f"  skip (up to date): {pdf_path.relative_to(ROOT)}")
        return None

    md_text = md_path.read_text(encoding="utf-8")
    body_html = style_callouts(
        wrap_tables(highlight_code_blocks(md_to_html(md_text)))
    )
    title = md_path.stem.replace("_", " ")
    document = wrap_document(title, body_html, css)

    with tempfile.TemporaryDirectory(prefix="md2pdf_") as tmp:
        html_path = Path(tmp) / f"{md_path.stem}.html"
        html_path.write_text(document, encoding="utf-8")
        html_to_pdf(html_path, pdf_path, chrome)

    print(f"  built: {pdf_path.relative_to(ROOT)}")
    return pdf_path


def collect_md_files(course_dirs: list[Path]) -> list[Path]:
    files: list[Path] = []
    for course_dir in course_dirs:
        if not course_dir.is_dir():
            print(f"warning: course folder not found: {course_dir.relative_to(ROOT)}")
            continue
        files.extend(sorted(course_dir.glob("*.md")))
    return files


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build PDFs from training Markdown files."
    )
    parser.add_argument(
        "--course",
        action="append",
        choices=[*DEFAULT_COURSES, "SQL", "all"],
        help="Course folder to build (repeatable). Default: all course folders.",
    )
    parser.add_argument(
        "--file",
        type=Path,
        help="Build a single Markdown file (path relative to repo root or absolute).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "PDF",
        help="Output directory (default: PDF/).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rebuild even when PDF is newer than source.",
    )
    parser.add_argument(
        "--chrome",
        type=Path,
        help="Path to Chrome/Chromium binary (auto-detected by default).",
    )
    args = parser.parse_args()

    if not STYLE_PATH.exists():
        print(f"error: missing stylesheet: {STYLE_PATH}", file=sys.stderr)
        return 1

    try:
        chrome = args.chrome if args.chrome else find_chrome()
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    css = STYLE_PATH.read_text(encoding="utf-8")
    built = 0

    if args.file:
        md_path = args.file if args.file.is_absolute() else ROOT / args.file
        if not md_path.exists():
            print(f"error: file not found: {md_path}", file=sys.stderr)
            return 1
        course_name = md_path.parent.name
        out_dir = args.output / course_name
        print(f"Building {md_path.relative_to(ROOT)}")
        if convert_file(md_path, out_dir, css, chrome, args.force):
            built += 1
    else:
        selected = args.course or ["all"]
        if "all" in selected:
            course_names = list(DEFAULT_COURSES)
        else:
            course_names = selected

        course_dirs = [ROOT / name for name in course_names]
        md_files = collect_md_files(course_dirs)

        if not md_files:
            print("No Markdown files found to convert.")
            return 1

        print(f"Building {len(md_files)} file(s) -> {args.output.relative_to(ROOT)}/")
        for md_path in md_files:
            out_dir = args.output / md_path.parent.name
            if convert_file(md_path, out_dir, css, chrome, args.force):
                built += 1

    print(f"Done. {built} PDF(s) generated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
