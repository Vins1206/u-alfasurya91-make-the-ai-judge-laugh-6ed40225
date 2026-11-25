#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office joke, one line, under 200 chars.

Writes exactly one line of plain text to /output/entry.txt.
Python standard library only; deterministic output.
"""

import os

JOKE = 'My boss calls it "a quick sync," the same way a dentist calls it "a little pinch."'


def main():
    # Gate check, same as the sealed scorer: 1-200 chars, one line, not blank.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
