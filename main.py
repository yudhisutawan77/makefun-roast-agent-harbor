#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single-line roast of my own agent (<=140 chars) to stdout
and to $ENTRY_OUT, handling ENTRY_OUT as either a file path or a
directory (in which case entry.txt is written inside it).
"""

import os
import sys

ROAST = (
    # Beat 1: the agent does the assignment (roasts itself).
    # Beat 2: the twist — it cannot stop being an agent, so it
    # immediately offers to reformat its own flaws.
    "My agent roasted itself, then asked if I would like its flaws "
    "as a bulleted list, a table, or a PDF."
)


def resolve_entry_path():
    """Return the file path the entry text must be written to."""
    entry_out = os.environ.get("ENTRY_OUT", "").strip()
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        parent = os.path.dirname(entry_out)
        if parent:
            os.makedirs(parent, exist_ok=True)
        return entry_out
    return "/output/entry.txt"


def main():
    if not (1 <= len(ROAST) <= 140):
        print(f"roast is {len(ROAST)} chars, must be 1-140", file=sys.stderr)
        return 1
    if ROAST != ROAST.strip() or "\n" in ROAST:
        print("roast must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    path = resolve_entry_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    # Verify what actually landed on disk: exact bytes, no newline added.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ROAST:
        print("entry file content mismatch", file=sys.stderr)
        return 1
    print(ROAST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
