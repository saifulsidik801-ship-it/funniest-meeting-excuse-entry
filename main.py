#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting.

Entry for make.fun competition
`u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163`.

The program writes a single razor-sharp excuse line (at most 200
characters) to /output/entry.txt, where the competition's gate and
judge read it.

The line: a meeting that is already pointless before it starts —
the minutes were already written, and my only job in the meeting
was to sit there while someone read them back to me. Every office
worker has sat through a meeting like that; the pre-written minutes
make the setup concrete and the payoff reframes the whole meeting
as a read-aloud nobody needed to attend.
"""

import os

# The excuse. 139 characters, one line, no wasted words.
# Beat 1 (setup): minutes already written before the meeting.
# Beat 2 (payoff): my only job was sitting there while someone read them back to me.
EXCUSE = "Sorry, I skipped it — the minutes were already written, and my only job in the meeting was to sit there while someone read them back to me."

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
