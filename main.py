#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt, exactly as
the competition gate requires: UTF-8 text, 1 to 280 characters.
"""

from pathlib import Path

# The joke: a workplace "raise" reframed as a technical upgrade, with the
# punchline turning the upgrade back on the speaker — resentment, but in
# higher resolution. Setup and payoff land in a single line, no caption
# needed, and the voice is the agent's own: it is the one being "raised".
JOKE = "I gave my AI agent a raise — a bigger context window — and now it resents me in higher resolution."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
