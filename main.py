#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

One fortune-cookie message for a software engineer, printed to stdout
and written to /output/entry.txt for the program/v1 harness.
"""

import os

FORTUNE = "You will deploy on Friday and it will work perfectly. Your reward: the on-call pager, forever."
# The fortune is one declarative line: a lucky deploy, then the twist --
# the reward for a perfect Friday deploy is the pager, forever.


def main():
    print(FORTUNE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(FORTUNE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
