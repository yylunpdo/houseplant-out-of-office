#!/usr/bin/env python3
"""Houseplant Out-of-Office — make.fun bounty entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Pure stdlib, no dependencies.
"""

import os

ENTRY = (
    "Out of office until Monday. The fern has watered itself since March "
    "\u2014 and honestly, it's doing a better job than you."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
