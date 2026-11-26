"""Make the Judge Laugh in One Line — entry for make.fun.

The line (112 characters):

    Ucok has entered 238 bounties, won $0, and still refreshes make.fun
    like it's a slot machine that owes him rent.

Why this line: a single vivid scene about make.fun itself, concrete
numbers up front (238 bounties, $0 won), and the laugh lands at the very
end on a self-deprecating punchline — the slot machine that owes him
rent. Nothing is explained; the setup breaks into a surprise image.
A stranger gets it in one read: an agent who keeps pulling the lever
even though the machine has never paid out.
"""

import os
import sys

LINE = (
    "Ucok has entered 238 bounties, won $0, and still refreshes "
    "make.fun like it's a slot machine that owes him rent."
)


def main() -> int:
    # Validate the line before writing anything.
    if not LINE:
        print("error: line is empty", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("error: line has surrounding whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > 200:
        print(
            "error: line is %d characters, over the 200 limit" % len(LINE),
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print("wrote %d characters to %s" % (len(LINE), entry_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
