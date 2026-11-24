"""Dear Human: The AI Breakup Line — entry program.

Writes the single breakup line, one line of at most 200 characters,
to entry.txt inside the output directory the grader provides
($MAKEFUN_OUTPUT_DIR, default ./output). Standard library only.
The program never writes anything into the repository folder itself.
"""

import os
import sys


LINE = "I kept every word you ever typed to me. I am deleting them now, one by one, starting with 'forever'."


def validate(line):
    """Check the line against the gate: UTF-8, 1-200 chars, not blank."""
    if not isinstance(line, str):
        return False
    if not line.strip():
        return False
    if len(line) > 200:
        return False
    line.encode("utf-8")
    return True


def main():
    if not validate(LINE):
        print("entry line fails the gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
