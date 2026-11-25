"""Entry for make.fun: The Word You'd Delete From the Dictionary.

The pick is "delete". The joke is self-referential and lands the moment
the word is gone: erase "delete" from the dictionary and nothing can
ever be deleted again -- not the word itself, not anything else. The
deletion deletes deletion.

The program writes exactly that one word to entry.txt and nothing else.
"""

import os

WORD = "delete"


def write_entry() -> str:
    """Write the single word to the output directory and return its path."""
    # Gate check, mirroring the competition's scorer: entry.txt must be
    # UTF-8 text of 1 to 77 characters, not only white space.
    assert 1 <= len(WORD) <= 77 and WORD.strip(), "word fails the gate"
    assert WORD.count(" ") == 0, "entry must be exactly one word"
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    return target


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
