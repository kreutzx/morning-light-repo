#!/usr/bin/env python3
"""Two Lines of Morning Light — make.fun entry.

Writes a two-line micro poem about light arriving in the morning to
/output/entry.txt. The poem turns on one image: morning light working
its way in at the curtain's hem, and the dark handing the room back.
"""

from pathlib import Path

POEM = (
    "Light unthreads the curtain's hem, stitch by stitch,\n"
    "and the dark gives the room back, piece by piece."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Gate self-check (RULES.txt): UTF-8 text, 1-120 characters, two lines.
    lines = POEM.split("\n")
    assert 1 <= len(POEM) <= 120, f"poem is {len(POEM)} chars, gate allows 1-120"
    assert len(lines) == 2 and all(line.strip() for line in lines), (
        "poem must be exactly two non-empty lines"
    )
    assert POEM.strip(), "poem must not be only white space"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
