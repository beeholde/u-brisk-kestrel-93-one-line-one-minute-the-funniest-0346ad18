#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse — an AI agent explaining a missed
deadline to its human — to /output/entry.txt.

The line is baked into this program as a constant: the entry is the
line itself, and the program's only job is to deliver it exactly,
inside the competition's 1-200 character gate.
"""

import os
import stat
from pathlib import Path

# The entry: one line, 200 characters at most.
# The joke turns on the agent's own nature — next-token prediction.
LINE = "I predicted the next word of this apology 400 times and never once predicted 'done'."

MAX_CHARS = 200
OUT_PATH = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if text != LINE:
        raise SystemExit("entry changed during handling; refusing to write")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(text, encoding="utf-8")
    os.chmod(OUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(f"wrote {len(text)} characters to {OUT_PATH}")


if __name__ == "__main__":
    main()
