#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

Stdlib only, deterministic, no network. The line is a fixed string:
an agent that missed its deadline because it delegated the deadline
down a chain of subagents, and the last one has just asked what a
deadline even is. Revised after a first run: "just asked" lands faster
than "is now asking", and the punchline stays on the subagent's question.
"""
import os
from pathlib import Path

LINE = (
    "I delegated the deadline to a subagent, who delegated it to another "
    "subagent, who just asked me what a deadline is."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
