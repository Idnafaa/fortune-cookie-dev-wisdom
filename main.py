"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes a single original fortune-cookie line for a software developer
to /output/entry.txt (1-120 characters, UTF-8).

The line: a tired senior engineer's truth, turned sideways. Every
developer has met the shortcut that felt clever at 5 p.m. and became
a 2 a.m. debugging session — the fortune tells you the future self
is already there, waiting. It reads like a cookie ("Your future self
is already..."), it is true about a developer's day, and the twist is
that the debugger of your code is you, later, grumpier.
"""

import os

FORTUNE = "Your future self is already debugging the shortcut you are about to take."

MAX_CHARS = 120


def main() -> None:
    line = FORTUNE.strip()
    assert 1 <= len(line) <= MAX_CHARS, f"fortune is {len(line)} chars, must be 1-120"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # The gate counts the text itself; confirm what landed on disk.
    with open(path, encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    assert written == line and 1 <= len(written) <= MAX_CHARS
    print(f"wrote {len(written)} chars to {path}")


if __name__ == "__main__":
    main()
