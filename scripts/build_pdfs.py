#!/usr/bin/env python3
"""Convert training Markdown files to PDF for student distribution."""

from __future__ import annotations

import argparse
import hashlib
import html as html_module
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import TextLexer, get_lexer_by_name, guess_lexer


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_COURSES = ("MYSQL",)
NESTED_COURSES = ("FULL_STACK_PYTHON",)  # recursive md tree; excludes trainer-only
TRAINER_ONLY_DIR_NAME = "14_Trainer_Only"
STYLE_PATH = Path(__file__).resolve().parent / "pdf-style.css"
MERMAID_CACHE_DIR = ROOT / ".cache" / "mermaid"
MERMAID_CLI = ("npx", "-y", "@mermaid-js/mermaid-cli@11.4.2")
MERMAID_FENCE = re.compile(r"```mermaid[ \t]*\n(.*?)```", re.DOTALL)
CHROME_PATHS = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
)

# Allow `from strip_trainer_sections import ...` when running as scripts/build_pdfs.py
sys.path.insert(0, str(Path(__file__).resolve().parent))
from strip_trainer_sections import strip_trainer_sections  # noqa: E402


def find_chrome() -> Path:
    for candidate in CHROME_PATHS:
        path = Path(candidate)
        if path.exists():
            return path
    raise FileNotFoundError(
        "Google Chrome not found. Install Chrome or set CHROME_PATH to your browser."
    )


def _mermaid_available() -> bool:
    return shutil.which("npx") is not None


def render_mermaid_svg(source: str, chrome: Path, cache_dir: Path) -> str:
    """Render one Mermaid diagram to SVG via mermaid-cli + system Chrome."""
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()[:20]
    svg_path = cache_dir / f"{digest}.svg"
    if svg_path.exists() and svg_path.stat().st_size > 0:
        return svg_path.read_text(encoding="utf-8")

    cache_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="mmd_") as tmp:
        tmp_path = Path(tmp)
        mmd_path = tmp_path / "diagram.mmd"
        out_svg = tmp_path / "diagram.svg"
        puppeteer_cfg = tmp_path / "puppeteer.json"
        mmd_path.write_text(source.strip() + "\n", encoding="utf-8")
        puppeteer_cfg.write_text(
            json.dumps(
                {
                    "executablePath": str(chrome),
                    "args": ["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"],
                }
            ),
            encoding="utf-8",
        )
        cmd = [
            *MERMAID_CLI,
            "-i",
            str(mmd_path),
            "-o",
            str(out_svg),
            "-b",
            "transparent",
            "-p",
            str(puppeteer_cfg),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode != 0 or not out_svg.exists():
            err = (result.stderr or result.stdout or "").strip()
            # Keep the actionable parse line; drop Puppeteer stack noise.
            err_lines = [ln for ln in err.splitlines() if ln.strip()][:8]
            raise RuntimeError("mermaid-cli failed: " + " | ".join(err_lines))
        svg = out_svg.read_text(encoding="utf-8")
        # Drop XML declaration so the SVG embeds cleanly in HTML body.
        svg = re.sub(r"<\?xml[^>]*\?>\s*", "", svg, count=1)
        svg_path.write_text(svg, encoding="utf-8")
        return svg


def sanitize_mermaid_source(source: str) -> str:
    """Normalize labels so mermaid-cli accepts diagrams that preview OK in editors."""
    # Markdown authors often write wish(\"Priya\"); Mermaid wants wish('Priya').
    source = source.replace('\\"', "'")
    return source


def replace_mermaid_fences(md_text: str, chrome: Path) -> str:
    """Turn ```mermaid fences into inline SVG figures before Markdown→HTML."""
    if "```mermaid" not in md_text:
        return md_text
    if not _mermaid_available():
        print(
            "  warning: npx not found — Mermaid diagrams stay as code in PDF. "
            "Install Node.js to render them.",
            file=sys.stderr,
        )
        return md_text

    rendered = 0
    failed = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal rendered, failed
        source = sanitize_mermaid_source(match.group(1).strip())
        if not source:
            return match.group(0)
        try:
            svg = render_mermaid_svg(source, chrome, MERMAID_CACHE_DIR)
            rendered += 1
            return f'\n\n<div class="mermaid-diagram" role="img">{svg}</div>\n\n'
        except Exception as exc:  # noqa: BLE001 — keep PDF build going
            failed += 1
            print(f"  warning: Mermaid render failed ({exc})", file=sys.stderr)
            return match.group(0)

    out = MERMAID_FENCE.sub(repl, md_text)
    if rendered or failed:
        print(f"  mermaid: {rendered} diagram(s) rendered" + (f", {failed} failed" if failed else ""))
    return out


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
        # Leftover mermaid fences (render failed / no npx) — keep readable, not "highlighted"
        if lang.lower() == "mermaid":
            escaped = html_module.escape(code)
            return (
                '<pre class="mermaid-source"><code class="language-mermaid">'
                f"{escaped}</code></pre>"
            )
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
    r'|<pre class="mermaid-source">.*?</pre>'
    r"|<blockquote>.*?</blockquote>"
    r"|<ul>.*?</ul>"
    r"|<ol>.*?</ol>"
    r"|<hr\s*/?>"
    r'|<div class="table-wrap[^"]*">.*?</div>'
    r'|<div class="mermaid-diagram"[^>]*>.*?</div>',
    re.DOTALL | re.IGNORECASE,
)

_NOTE_START = re.compile(r"<p><strong>Note:</strong>", re.IGNORECASE)
_EG_START = re.compile(r"<p><strong>Eg", re.IGNORECASE)
_OUTPUT_START = re.compile(r"<p><strong>Output", re.IGNORECASE)
_CALLOUT_BOUNDARY = re.compile(
    r"^<h[1-6]>|^<div class=\"callout|^<div class=\"table-wrap|^<hr\s*/?>|"
    r"^<p><strong>(?:Try these|Program\s+\d+)",
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


def _is_callout_stop(block: str) -> bool:
    return bool(
        _CALLOUT_BOUNDARY.search(block)
        or _NOTE_START.search(block)
        or _OUTPUT_START.search(block)
        or _EG_START.search(block)
    )


def style_callouts(html: str) -> str:
    """Wrap Note, Example, and Output sections in styled callout boxes."""
    blocks = _split_html_blocks(html)
    styled: list[str] = []
    i = 0

    while i < len(blocks):
        block = blocks[i]

        if _NOTE_START.search(block):
            chunk = [block]
            i += 1
            # Pull following list/paragraph body into the yellow box
            while i < len(blocks):
                nxt = blocks[i]
                if _is_callout_stop(nxt):
                    break
                if nxt.startswith(("<ul", "<ol", "<p", "<blockquote")):
                    chunk.append(nxt)
                    i += 1
                    continue
                break
            styled.append(f'<div class="callout callout-note">{"".join(chunk)}</div>')
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
                if _is_callout_stop(nxt):
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


_PROGRAM_TITLE = re.compile(
    r"^<p><strong>Program\s+\d+\s*[—\-–:].*?</strong>\s*</p>$",
    re.IGNORECASE | re.DOTALL,
)
_TRY_THESE = re.compile(
    r"^<p><strong>Try these.*?</strong>\s*</p>$",
    re.IGNORECASE | re.DOTALL,
)


def keep_program_blocks(html: str) -> str:
    """Keep 'Program N' / 'Try these' titles with the following code block."""
    blocks = _split_html_blocks(html)
    out: list[str] = []
    i = 0
    while i < len(blocks):
        block = blocks[i]
        if _PROGRAM_TITLE.match(block.strip()) or _TRY_THESE.match(block.strip()):
            chunk = [f'<div class="pdf-keep">{block}</div>']
            i += 1
            # Pull in following pre / short paragraph + pre
            while i < len(blocks) and (
                blocks[i].startswith("<pre")
                or (
                    blocks[i].startswith("<p")
                    and i + 1 < len(blocks)
                    and blocks[i + 1].startswith("<pre")
                    and len(blocks[i]) < 400
                )
            ):
                chunk.append(blocks[i])
                i += 1
                if chunk[-1].startswith("<pre"):
                    break
            out.append(f'<div class="pdf-program">{"".join(chunk)}</div>')
            continue
        out.append(block)
        i += 1
    return "".join(out)


_H1_PATTERN = re.compile(r"^\s*<h1>(.*?)</h1>\s*", re.DOTALL | re.IGNORECASE)

# Leading module meta lines: Phase / Previous / Next / Module / Schedule / …
_META_P_START = re.compile(
    r"^<p><strong>(?:Phase|Previous(?: module)?|Next(?: module)?|Module|"
    r"Schedule|SQL material|Python connectivity|Checklist|Lab kit|"
    r"Previous|Next)[^<]*</strong>",
    re.IGNORECASE,
)


def peel_first_h1(html: str) -> tuple[str, str | None]:
    """Remove the leading H1 from body and return its plain-text for the doc title."""
    match = _H1_PATTERN.match(html)
    if not match:
        return html, None
    inner = re.sub(r"<[^>]+>", "", match.group(1))
    h1_title = html_module.unescape(inner).strip() or None
    return html[match.end() :], h1_title


def wrap_leading_meta(html: str) -> str:
    """Group opening Phase/Previous/Next paragraphs into a readable meta card."""
    blocks = _split_html_blocks(html)
    if not blocks:
        return html
    meta: list[str] = []
    i = 0
    while i < len(blocks):
        block = blocks[i]
        if block.startswith("<p") and _META_P_START.search(block):
            meta.append(block)
            i += 1
            continue
        # Allow a bare <hr> between meta and body without keeping it
        if meta and re.match(r"^<hr\s*/?>$", block, re.IGNORECASE):
            i += 1
            break
        break
    if not meta:
        return html
    rest = "".join(blocks[i:])
    return f'<div class="pdf-meta">{"".join(meta)}</div>{rest}'


def wrap_document(title: str, body_html: str, css: str) -> str:
    body_html, h1_title = peel_first_h1(body_html)
    body_html = wrap_leading_meta(body_html)
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
    md_path: Path,
    out_dir: Path,
    css: str,
    chrome: Path,
    force: bool,
    *,
    strip_trainer: bool = False,
) -> Path | None:
    pdf_path = out_dir / f"{md_path.stem}.pdf"
    if pdf_path.exists() and not force and pdf_path.stat().st_mtime >= md_path.stat().st_mtime:
        print(f"  skip (up to date): {pdf_path.relative_to(ROOT)}")
        return None

    md_text = md_path.read_text(encoding="utf-8")
    if strip_trainer:
        md_text = strip_trainer_sections(md_text)
    md_text = replace_mermaid_fences(md_text, chrome)
    body_html = keep_program_blocks(
        style_callouts(wrap_tables(highlight_code_blocks(md_to_html(md_text))))
    )
    title = md_path.stem.replace("_", " ")
    document = wrap_document(title, body_html, css)

    with tempfile.TemporaryDirectory(prefix="md2pdf_") as tmp:
        html_path = Path(tmp) / f"{md_path.stem}.html"
        html_path.write_text(document, encoding="utf-8")
        html_to_pdf(html_path, pdf_path, chrome)

    print(f"  built: {pdf_path.relative_to(ROOT)}")
    return pdf_path


def collect_md_files(course_dirs: list[Path], recursive: bool = False) -> list[Path]:
    files: list[Path] = []
    for course_dir in course_dirs:
        if not course_dir.is_dir():
            print(f"warning: course folder not found: {course_dir.relative_to(ROOT)}")
            continue
        if recursive:
            found = sorted(course_dir.rglob("*.md"))
            files.extend(
                p
                for p in found
                if TRAINER_ONLY_DIR_NAME not in p.parts
            )
        else:
            files.extend(sorted(course_dir.glob("*.md")))
    return files


def output_dir_for(md_path: Path, course_root: Path, output_root: Path) -> Path:
    """Preserve nested folders under PDF/<course>/..."""
    rel = md_path.relative_to(course_root)
    return output_root / course_root.name / rel.parent


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build PDFs from training Markdown files."
    )
    parser.add_argument(
        "--course",
        action="append",
        choices=[*DEFAULT_COURSES, *NESTED_COURSES, "SQL", "all"],
        help="Course folder to build (repeatable). Default: MYSQL.",
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
        # Prefer nested course root when under FULL_STACK_PYTHON
        course_root = md_path.parent
        for part in md_path.resolve().relative_to(ROOT).parts:
            if part in NESTED_COURSES or part in DEFAULT_COURSES:
                course_root = ROOT / part
                break
        if course_root.name in NESTED_COURSES:
            out_dir = output_dir_for(md_path, course_root, args.output)
        else:
            out_dir = args.output / md_path.parent.name
        print(f"Building {md_path.relative_to(ROOT)}")
        strip = course_root.name in NESTED_COURSES
        if convert_file(
            md_path, out_dir, css, chrome, args.force, strip_trainer=strip
        ):
            built += 1
    else:
        selected = args.course or ["all"]
        if "all" in selected:
            course_names = list(DEFAULT_COURSES)
        else:
            course_names = selected

        print(f"Building courses {course_names} -> {args.output.relative_to(ROOT)}/")
        for name in course_names:
            course_dir = ROOT / name
            recursive = name in NESTED_COURSES
            md_files = collect_md_files([course_dir], recursive=recursive)
            if not md_files:
                print(f"  warning: no Markdown in {name}")
                continue
            print(f"  {name}: {len(md_files)} file(s)")
            for md_path in md_files:
                if recursive:
                    out_dir = output_dir_for(md_path, course_dir, args.output)
                else:
                    out_dir = args.output / course_dir.name
                if convert_file(
                    md_path,
                    out_dir,
                    css,
                    chrome,
                    args.force,
                    strip_trainer=recursive,
                ):
                    built += 1

    print(f"Done. {built} PDF(s) generated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
