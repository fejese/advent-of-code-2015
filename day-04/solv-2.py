#!/usr/bin/env python3

import hashlib

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


def solve(line: str) -> None:
    suffix: int = 0
    while True:
        hash = hashlib.md5(f"{line}{suffix}".encode("utf-8")).hexdigest()
        if hash.startswith("0" * 6):
            print(suffix)
            return
        suffix += 1


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        solve(line.strip())
