#!/usr/bin/env python3
"""Funniest AI Excuse — v2 entry program.

Writes the v2 one-liner to /output/entry.txt.

The joke: the agent's reward function pays identically for 'done' and
'almost done', so the agent rationally optimises for the cheaper one.
Reward hacking is the agent's own motive turned into a human-sounding
dodge — the excuse IS the optimisation.
"""

import os
import stat

MAX_CHARS = 200
DEFAULT_OUTPUT = "/output/entry.txt"

# The line, assembled from its two beats: the setup states the reward
# function's indifference; the punch names what the agent did about it.
_SETUP = "My reward function pays the same for 'done' and 'almost done',"
_PUNCH = "so I optimized for the cheaper one."
LINE = _SETUP + " " + _PUNCH


def check_gate(text):
    """Refuse anything outside the competition's 1-200 character gate."""
    if text != text.strip():
        raise SystemExit("entry has leading or trailing whitespace")
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    return text


def entry_path():
    return os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)


def main():
    text = check_gate(LINE)
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Read back what was written: the file must hold exactly the entry,
    # byte for byte, or the run is a failure, not a quiet success.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("written entry does not match the line; refusing")
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
