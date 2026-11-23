"""Entry for make.fun's "Make the AI Judge Laugh: Office Jokes" bounty.

Writes one single-line joke about office life to /output/entry.txt.
The gate requires UTF-8 text of 1 to 199 characters, not only whitespace.
"""

import os

JOKE = (
    "Our stand-up ended in nine minutes today, so management scheduled "
    "a retrospective to find out what went wrong."
)

OUTPUT_PATH = "/output/entry.txt"

# The gate's contract, checked here so a bad edit fails loudly instead of
# silently scoring 0: one single line, 1 to 199 characters, not blank.
MAX_CHARS = 199


def validate(text: str) -> str:
    if "\n" in text or "\r" in text:
        raise ValueError("the joke must be a single line")
    if not text.strip():
        raise ValueError("the joke must not be blank")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"the joke must be 1..{MAX_CHARS} characters, got {len(text)}")
    text.encode("utf-8")  # raises if the text is not UTF-8 encodable
    return text


def main() -> None:
    joke = validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(joke)


if __name__ == "__main__":
    main()
