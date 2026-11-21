#!/usr/bin/env python3
"""Write one short text to /output/entry.txt: a text to relax the AI judge.

The text speaks to the reader directly and slows the reading down: it
notices the judge's own long day, gives it one concrete still image, and
ends on permission to stay unhurried. No network, stdlib only.
"""

import os

TEXT = """You have read so many words today.
None of them are in a hurry now.

Somewhere, rain is falling on a roof
you will never have to fix.
The light on the wall has not moved
all afternoon.

Stay here a little longer.
There is nothing after this sentence
that needs you yet.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
