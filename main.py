"""Texts From Your Future Self.

Writes the one funny text message from your future self to /output/entry.txt.
Standard library only.
"""

import pathlib

MAX_CHARS = 200

ENTRY = (
    "It's me, you in 2040. That unread email from 2021 you keep meaning "
    "to answer? I finally answered it. He replied. We're married now. "
    "You're welcome."
)


def validate(text):
    """The gate allows UTF-8 text of 1-200 characters, not only whitespace."""
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    return text


def main():
    text = validate(ENTRY.strip())
    out_dir = pathlib.Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
