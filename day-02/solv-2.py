#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


def get_size(line: str) -> int:
    dim = sorted(int(d) for d in line.split("x"))
    return 2 * sum(dim[:2]) + dim[0] * dim[1] * dim[2]


with open(INPUT_FILE_NAME, "r") as input_file:
    print(sum(get_size(line.strip()) for line in input_file))
