#!/usr/bin/env python3

from typing import List

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


CHARS: str = "".join([chr(ascii) for ascii in range(ord("a"), ord("z") + 1)])
SEQS: List[str] = [
    f"{chr(ascii)}{chr(ascii + 1)}{chr(ascii + 2)}"
    for ascii in range(ord("a"), ord("z") - 1)
]
SEQS: List[str] = [CHARS[i : i + 3] for i in range(len(CHARS) - 2)]
BLACKLISTED: List[str] = ["i", "o", "l"]
DOUBLES: List[str] = [f"{c}{c}" for c in CHARS]


def increment(chars: List[str]) -> None:
    for i in range(len(chars) - 1, -1, -1):
        if chars[i] == "z":
            chars[i] = "a"
        else:
            chars[i] = chr(ord(chars[i]) + 1)
            break

    reset_pos = None
    for x in "iol":
        try:
            new_reset_pos = chars.index(x)
            reset_pos = (
                min(reset_pos, new_reset_pos)
                if reset_pos is not None
                else new_reset_pos
            )
        except ValueError:
            pass

    if reset_pos:
        chars[reset_pos] = chr(ord(chars[reset_pos]) + 1)
        for pos in range(reset_pos + 1, len(chars)):
            chars[pos] = "a"


def is_valid(chars: List[str]) -> bool:
    pwd = "".join(chars)

    if any(ch in chars for ch in BLACKLISTED):
        # print(f"{pwd}: invalid (Pattern #2 does not match)")
        return False

    if not any(seq in pwd for seq in SEQS):
        # print(f"{pwd}: invalid (Pattern #1 does not match)")
        return False

    if sum(d in pwd for d in DOUBLES) < 2:
        # print(f"{pwd}: invalid (Pattern #3 does not match)")
        return False

    # print(f"{pwd}: valid!")
    return True


def solve(pwd: str) -> str:
    chars = [ch for ch in pwd]
    while not is_valid(chars):
        increment(chars)
    return "".join(chars)


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        first = solve(line.strip())
        print("first:", first)
        bump = [c for c in first]
        increment(bump)
        bump = "".join(bump)
        second = solve(bump)
        print("second:", second)
