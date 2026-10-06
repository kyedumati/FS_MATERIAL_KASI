#!/usr/bin/env python3
"""Check FRONTEND/HTML_CSS lessons: nothing is used before it is taught, and links work.

For each lesson, every example file, lab file, and code block in the lesson may only
use HTML tags and CSS properties taught in that lesson or earlier.

Usage:
    python3 scripts/check_frontend_lessons.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE = ROOT / "FRONTEND" / "HTML_CSS"

# What each lesson teaches. Later lessons may use everything from earlier ones.
LESSONS = [
    {
        "md": "Lesson_01_How_the_Web_Works_and_Your_First_Page.md",
        "dirs": ["examples/lesson01", "labs/L01_welcome_page"],
        "tags": {"html", "head", "meta", "title", "body", "h1", "p"},
        "props": set(),
    },
    {
        "md": "Lesson_02_Content_and_Your_First_CSS.md",
        "dirs": ["examples/lesson02", "labs/L02_leave_policy"],
        "tags": {"h2", "h3", "h4", "h5", "h6", "br", "ul", "ol", "li", "a", "strong", "em", "link", "style"},
        "props": {"font-family", "line-height", "color", "background-color", "font-weight", "outline"},
    },
    {
        "md": "Lesson_03_Page_Structure_and_the_Box_Model.md",
        "dirs": ["examples/lesson03", "labs/L03_employee_profile"],
        "tags": {"header", "nav", "main", "section", "aside", "footer", "div", "span", "dl", "dt", "dd"},
        "props": {"margin", "margin-top", "margin-right", "margin-bottom", "margin-left", "margin-inline",
                  "padding", "padding-top", "padding-right", "padding-bottom", "padding-left",
                  "border", "border-top", "border-right", "border-bottom", "border-left", "border-radius",
                  "width", "max-width", "height", "box-sizing", "display", "list-style",
                  "font-size", "text-align"},
    },
    {
        "md": "Lesson_04_Images_Navigation_and_Flexbox.md",
        "dirs": ["examples/lesson04", "labs/L04_employee_directory"],
        "tags": {"img", "article", "figure", "figcaption"},
        "props": {"flex-direction", "justify-content", "align-items", "flex-wrap", "gap", "flex",
                  "text-decoration", "object-fit", "min-width"},
    },
    {
        "md": "Lesson_05_Grid_and_Positioning.md",
        "dirs": ["examples/lesson05", "labs/L05_hr_dashboard"],
        "tags": set(),
        "props": {"grid-template-columns", "grid-column", "grid-template-areas", "grid-area",
                  "position", "top", "right", "bottom", "left", "z-index", "align-self"},
    },
    {
        "md": "Lesson_06_Forms.md",
        "dirs": ["examples/lesson06", "labs/L06_apply_leave"],
        "tags": {"form", "label", "input", "select", "option", "textarea", "button", "fieldset", "legend"},
        "props": {"font", "accent-color", "cursor", "outline-offset"},
    },
    {
        "md": "Lesson_07_Tables.md",
        "dirs": ["examples/lesson07", "labs/L07_attendance_report"],
        "tags": {"table", "caption", "thead", "tbody", "tfoot", "tr", "th", "td"},
        "props": {"border-collapse", "font-variant-numeric", "white-space", "overflow-x", "caption-side"},
    },
    {
        "md": "Lesson_08_Responsive_Design.md",
        "dirs": ["examples/lesson08", "labs/L08_responsive_portal"],
        "tags": {"picture", "source"},
        "props": set(),
    },
    {
        "md": "Lesson_09_Polish_Accessibility_and_Final_Project.md",
        "dirs": ["examples/lesson09", "labs/L09_final_project"],
        "tags": {"details", "summary"},
        "props": {"transition", "transform", "border-color", "border-bottom-color"},
    },
]


# Deliberate bugs in lab "broken" files that the check must not report.
INTENTIONAL = {
    "labs/L05_hr_dashboard/broken/css/dashboard.css": {"grid-template-column"},
}


def strip_comments(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return re.sub(r"/\*.*?\*/", "", text, flags=re.S)


def tags_in(html: str) -> set[str]:
    return {t.lower() for t in re.findall(r"</?([a-zA-Z][a-zA-Z0-9]*)\b", strip_comments(html))}


def props_in(css: str) -> set[str]:
    css = strip_comments(css)
    bodies = re.findall(r"\{([^{}]*)\}", css)
    found = set()
    for body in bodies:
        for prop in re.findall(r"(?:^|;|\{)\s*([a-z-]+)\s*:", ";" + body):
            if not prop.startswith("--"):
                found.add(prop)
    return found


def style_blocks(html: str) -> str:
    return "\n".join(re.findall(r"<style>(.*?)</style>", html, flags=re.S))


def code_blocks(md: str, lang: str) -> str:
    return "\n".join(re.findall(rf"```{lang}\n(.*?)```", md, flags=re.S))


def main() -> int:
    problems = 0
    tags: set[str] = set()
    props: set[str] = set()
    for lesson in LESSONS:
        tags |= lesson["tags"]
        props |= lesson["props"]
        md_path = COURSE / lesson["md"]
        if not md_path.exists():
            continue
        for d in lesson["dirs"]:
            for f in sorted((COURSE / d).rglob("*")):
                if f.suffix == ".html":
                    text = f.read_text()
                    for kind, found, allowed in (("tag", tags_in(text), tags),
                                                 ("property", props_in(style_blocks(text)), props)):
                        extra = found - allowed
                        if extra:
                            print(f"{f.relative_to(COURSE)}: untaught {kind}(s) {sorted(extra)}")
                            problems += 1
                elif f.suffix == ".css":
                    extra = props_in(f.read_text()) - props - INTENTIONAL.get(str(f.relative_to(COURSE)), set())
                    if extra:
                        print(f"{f.relative_to(COURSE)}: untaught property(s) {sorted(extra)}")
                        problems += 1
        md = md_path.read_text()
        extra = tags_in(code_blocks(md, "html")) - tags
        if extra:
            print(f"{lesson['md']} code: untaught tag(s) {sorted(extra)}")
            problems += 1
        extra = props_in(code_blocks(md, "css") + style_blocks(code_blocks(md, "html"))) - props
        if extra:
            print(f"{lesson['md']} code: untaught property(s) {sorted(extra)}")
            problems += 1

    for md in sorted(COURSE.rglob("*.md")):
        for m in re.finditer(r"\]\(([^)#\s]+)(#[^)]*)?\)", md.read_text()):
            target = m.group(1)
            if target.startswith(("http", "mailto")):
                continue
            if not (md.parent / target).exists():
                print(f"{md.relative_to(COURSE)}: broken link {target}")
                problems += 1

    print(f"{problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
