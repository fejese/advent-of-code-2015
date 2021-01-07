#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        floor = 0
        for i, c in enumerate(line):
            if c == "(":
                floor += 1
            if c == ")":
                floor -= 1
            if floor == -1:
                print(i + 1)
                break
