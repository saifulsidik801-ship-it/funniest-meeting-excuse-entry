#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting.

Entry for make.fun competition
`u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163`.

The program writes a single razor-sharp excuse line (at most 200
characters) to /output/entry.txt, where the competition's gate and
judge read it.

The line: an office worker's favourite get-out clause, "I have a
hard stop", inverted so the hard stop falls at the *start* of the
meeting. Every office worker knows the jargon, the twist lands in
one breath, and there is no setup to explain.
"""

import os

# The excuse. 55 characters, one line, no wasted words.
EXCUSE = "Sorry, I have a hard stop at the start of this meeting."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    """Write the excuse line to /output/entry.txt."""
    text = EXCUSE.strip()
    if not text:
        raise ValueError("excuse must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} chars, over the 200 limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
