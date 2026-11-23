#!/usr/bin/env python3
"""Write a single username word to /output/entry.txt.

Standard library only, no network, fully deterministic: the same bytes
come out of every run. The entry is one word, the handle
witty-lynx-50-3813, written with no trailing newline and nothing else.
"""

import os

HANDLE = "witty-lynx-50-3813"


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    assert 1 <= len(HANDLE) <= 30, "entry must be 1-30 characters"
    assert HANDLE.split() == [HANDLE], "entry must be a single word"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(HANDLE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
