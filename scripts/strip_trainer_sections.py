#!/usr/bin/env python3
"""Optional cleaner for leftover trainer-ops phrasing (not used in the default share path).

One material policy: Practice **Model answer** blocks stay in teaching notes and PDFs.
Default share = module PDF after teaching. Optional pack script only excludes
14_Trainer_Only/, solution/, and *_KEY.md — it does not call this stripper.

This module remains available if you ever need to strip trainer-only H2/H3 sections
or Model answers for a special batch (pass a folder path).
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

# Entire H2 sections that are delivery/ops for trainers
TRAINER_H2 = re.compile(
    r"^##[ \t]+(?:\d+\.\s*)?(?:"
    r"Trainer Demo Plan"
    r"|Trainer Tips(?: for Freshers and Career Switchers)?"
    r"|Trainer Tips \(Course-Wide\).*?"
    r"|Trainer Checklist.*?"
    r"|How Trainers Use This Folder"
    r"|How trainers use this"
    r"|Trainer grading tip"
    r"|Trainer note"
    r"|Teaching tip"
    r"|Trainer delivery reminder"
    r"|What trainers use beyond the shared pack"
    r"|Graded tests"
    r"|Session plan \(trainer\).*?"
    r"|Day plan \(trainer\).*?"
    r").*?\n"
    r"(?:.*?\n)*?"
    r"(?=^## |\Z)",
    re.MULTILINE | re.IGNORECASE,
)

TRAINER_H3 = re.compile(
    r"^###[ \t]+(?:"
    r".*trainer only.*"
    r"|.*trainer copy only.*"
    r"|.*trainer walkthrough.*"
    r"|.*Trainer Demo.*"
    r"|.*trainer observes.*"
    r"|Trainer checklist.*"
    r").*?\n"
    r"(?:.*?\n)*?"
    r"(?=^#{1,3} |\Z)",
    re.MULTILINE | re.IGNORECASE,
)

LINE_DROPS = re.compile(
    r"^.*(?:14_Trainer_Only|do \*\*not\*\* share with learners|"
    r"keep answer keys in|Never share answer keys|"
    r"pack_student_share|teaching copy).*$",
    re.MULTILINE | re.IGNORECASE,
)

MODEL_ANSWER_BLOCK = re.compile(
    r"^[ \t]*\*\*(?:Answer|Model answer|Answers|Model scenario answer):\*\*[^\n]*\n"
    r"(?:(?![ \t]*(?:\d+\.|#{1,3} |\Z|\*\*Model answer:\*\*|\*\*Answer:\*\*)).*\n)*"
    r"(?:[ \t]*```[\w+-]*\n[\s\S]*?[ \t]*```\n)?",
    re.MULTILINE | re.IGNORECASE,
)

INLINE_ANSWER = re.compile(
    r"\s*[—\-–]?\s*\*\*(?:Answers?|Model):\*\*\s*[^\n]*",
    re.IGNORECASE,
)
INLINE_ANSWER_COMPACT = re.compile(
    r"\s*\*\*Answer:\s*[^\n*]*\*\*",
    re.IGNORECASE,
)

HINT_SHEET = re.compile(
    r"\(hint sheet — not full answers\)",
    re.IGNORECASE,
)

TITLE_TRAINER_READY = re.compile(
    r"\(Trainer-Ready\)",
    re.IGNORECASE,
)

BLOCK_TRAINER_NOTE = re.compile(
    r"^>?\s*\*\*Trainer note:\*\*.*$",
    re.MULTILINE | re.IGNORECASE,
)

INLINE_PHRASES = [
    (re.compile(r"Trainer walks learners through project:\s*", re.I), "Walk through your project checklist:\n\n"),
    (re.compile(r"\*\*Demo:\*\* Trainer ", re.I), "**Demo check:** You should be able to "),
    (re.compile(r"\*\*Demo criteria:\*\* Trainer ", re.I), "**Success check:** You can "),
    (re.compile(r"\(trainer provides[^)]*\)", re.I), "(provided in class or write your own)"),
    (re.compile(r"\(trainer hint provided\)", re.I), "(see DRF SearchFilter docs or ask in class)"),
    (re.compile(r"without trainer typing the solution first", re.I), "independently"),
    (re.compile(r"only after trainer pair-programming", re.I), "only with help"),
    (re.compile(r"Passes checks only with trainer", re.I), "Passes checks only with help"),
    (re.compile(r"Completes only with trainer/pair help", re.I), "Completes only with help"),
    (re.compile(r"with trainer approval", re.I), "with mentor approval"),
    (re.compile(r"Trainer adds post live in admin; learners refresh", re.I), "Add a post in admin; refresh"),
    (re.compile(r"Optional: trainer deploys one batch repo to Render for class URL", re.I), "Optional: deploy one repo to Render for a live class URL"),
    (re.compile(r"\*\*Trainer note:\*\*[^\n]*", re.I), ""),
]

DURATION_WITH_PHASE = re.compile(
    r"^\*\*Duration:\*\*[^\n]*?\|\s*\*\*Phase:\*\*\s*([^\n]+)\n",
    re.MULTILINE,
)
DURATION_LINE = re.compile(
    r"^\*\*Duration:\*\*[^\n]*\n(?:\n)?",
    re.MULTILINE,
)


def strip_trainer_sections(md_text: str, *, keep_model_answers: bool = False) -> str:
    """Clean trainer-ops wording. By default also removes Practice Model answers.

    For one-material sharing, do not call this on student-facing PDFs/packs.
    Pass keep_model_answers=True to only remove trainer H2/H3/ops lines.
    """
    cleaned = TRAINER_H2.sub("", md_text)
    cleaned = TRAINER_H3.sub("", cleaned)
    cleaned = LINE_DROPS.sub("", cleaned)
    if not keep_model_answers:
        cleaned = MODEL_ANSWER_BLOCK.sub("", cleaned)
        cleaned = INLINE_ANSWER.sub("", cleaned)
        cleaned = INLINE_ANSWER_COMPACT.sub("", cleaned)
    cleaned = BLOCK_TRAINER_NOTE.sub("", cleaned)
    cleaned = HINT_SHEET.sub("", cleaned)
    cleaned = TITLE_TRAINER_READY.sub("", cleaned)
    cleaned = DURATION_WITH_PHASE.sub(r"**Phase:** \1\n", cleaned)
    cleaned = DURATION_LINE.sub("", cleaned)
    for pattern, repl in INLINE_PHRASES:
        cleaned = pattern.sub(repl, cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    cleaned = re.sub(r"\n---\s*\n(?=\n*---|\n*\Z)", "\n", cleaned)
    return cleaned.strip() + "\n"


def process_tree(root: Path, *, keep_model_answers: bool = False) -> int:
    count = 0
    for path in sorted(root.rglob("*.md")):
        if "14_Trainer_Only" in path.parts:
            continue
        original = path.read_text(encoding="utf-8")
        updated = strip_trainer_sections(
            original, keep_model_answers=keep_model_answers
        )
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        type=Path,
        help="Folder of markdown files to clean in place",
    )
    parser.add_argument(
        "--keep-model-answers",
        action="store_true",
        help="Do not remove Practice **Model answer:** blocks",
    )
    args = parser.parse_args()
    if not args.root.is_dir():
        print(f"error: not a directory: {args.root}")
        return 1
    n = process_tree(args.root, keep_model_answers=args.keep_model_answers)
    print(f"Stripped trainer sections from {n} file(s) under {args.root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
