#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
# ITERATIONS: int = 1
INPUT_FILE_NAME: str = "input"
ITERATIONS: int = 40


def _solve(line: str) -> str:
    new_line = ""
    while line:
        ch = line[0]
        cnt = 0
        while line and line[0] == ch:
            line = line[1:]
            cnt += 1
        new_line += f"{cnt}{ch}"
    return new_line


def solve(line: str) -> str:
    for _ in range(ITERATIONS):
        line = _solve(line)
    return line


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        print(len(solve(line.strip())))
