#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


def get_size(line: str) -> int:
    a, b, c = (int(d) for d in line.split("x"))
    sides = [a * b, a * c, b * c]
    return sum(sides) * 2 + min(sides)


with open(INPUT_FILE_NAME, "r") as input_file:
    print(sum(get_size(line.strip()) for line in input_file))
