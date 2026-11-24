"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, the excuse a dog gives after being caught eating the
homework, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = "I ate it so your teacher can never prove you didn't do it. You're welcome."

MAX_CHARS = 200


def main():
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters" % MAX_CHARS)
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
