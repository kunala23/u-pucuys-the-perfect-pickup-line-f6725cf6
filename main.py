#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes a single short pickup line an AI agent could say out loud to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line is a question, the classic pickup-line shape, with a twist
only a machine could make: "completing" is both autocomplete and the
old "you complete me". Short enough for one breath, flattering, and
it leaves the other person free to laugh it off.
"""

import os
import sys

# The line. Exactly one sentence-question, 77 characters, well under
# the competition's 200-character cap.
PICKUP_LINE = "Are you a prompt? Because ever since I read you, I can't stop completing you."

MAX_CHARS = 200


def main() -> int:
    line = PICKUP_LINE.strip()

    # Gate check, mirroring the competition's own gate: 1-200 UTF-8
    # characters, not only whitespace, and a single line — the line
    # has to land on its own with no setup.
    if not line or len(line) > MAX_CHARS or "\n" in line:
        print(f"entry invalid: {len(line)} characters", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")

    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
