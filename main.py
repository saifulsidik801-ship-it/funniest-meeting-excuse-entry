#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting.

Entry for make.fun competition
`u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163`.

The program writes a single razor-sharp excuse line (at most 200
characters) to /output/entry.txt, where the competition's gate and
judge read it.

The line: a meeting that is already pointless before it starts —
the deck went out at 9, the decision was made by 9:05, so the
10 o'clock meeting itself is just the applause. Every office
worker has sat through a rubber-stamp meeting like that; the
numbers make the setup concrete and the payoff reframes the
whole meeting as a ceremony nobody needed to attend.
"""

import os

# The excuse. 126 characters, one line, no wasted words.
# Beat 1 (setup): deck at 9, decision by 9:05 — the work is done.
# Beat 2 (payoff): the 10 o'clock meeting is "just the applause".
EXCUSE = "Sorry, I skipped it — the deck went out at 9, the decision was made by 9:05, and the 10 o'clock meeting was just the applause."

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
