#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — entry program for
make.fun competition u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a.

Writes one line (at most 200 characters), a joke about crypto and
trading life, to /output/entry.txt.
"""

import os

JOKE = (
    "I bought the dip, then the dip bought a shovel. Now my portfolio "
    "is a hole with Wi-Fi, and the group chat still says hold."
)


def main():
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text == text.strip() and "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
