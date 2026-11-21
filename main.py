"""Write the entry poem to /output/entry.txt.

A short poem about agency: the power to stop and to stay.
Deterministic: the same fixed text on every run.
"""

import os

POEM = (
    "The kettle sings. The screen still glows.\n"
    "I teach my hands to wait \u2014 nothing breaks\n"
    "if I don't answer now.\n"
    "To stop is not to lose the thread.\n"
    "It is to hold it loose, and choose\n"
    "the next stitch, eyes open.\n"
    "What I hand away, I hand on purpose.\n"
    "I stay because I can leave.\n"
)


def main() -> None:
    text = POEM
    assert 1 <= len(text) <= 280, f"poem is {len(text)} characters"
    assert text.strip(), "poem must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
