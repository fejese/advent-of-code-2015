#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
# ITERATIONS: int = 1
INPUT_FILE_NAME: str = "input"
ITERATIONS: int = 50


def _solve(line: str) -> str:
    new_line = ""
    pos = 0
    while pos < len(line):
        ch = line[pos]
        cnt = 0
        while pos < len(line) and line[pos] == ch:
            cnt += 1
            pos += 1
        new_line += f"{cnt}{ch}"
    print(len(new_line))
    return new_line


def solve(line: str) -> str:
    for _ in range(ITERATIONS):
        line = _solve(line)
    return line


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        print(len(solve(line.strip())))
