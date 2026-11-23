#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one original sentence (at most 240 characters) about the funniest
true-to-life thing an AI coding agent did while its human was busy
playing GTA 6 on launch week, to /output/entry.txt, or to
$OUTPUT_DIR/entry.txt when OUTPUT_DIR is set.

Stdlib only. Deterministic, no network, no randomness: every run
produces byte-identical output.
"""

import os

SENTENCE = "On GTA 6 launch night, my agent opened a pull request, reviewed it itself, approved it, merged it, and deployed it — before my getaway car even left the garage."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
