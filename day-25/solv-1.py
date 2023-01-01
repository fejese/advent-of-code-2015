#!/usr/bin/env python3

import re

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    row, col = [int(num) for num in re.findall(r"\d+", input_file.read().strip())]


def get_no(row: int, col: int) -> int:
    return (row + col - 2) * (row + col - 1) // 2 + col


print(get_no(row, col))

num = 20151125
count = get_no(row, col)
print(row, col, count)
for i in range(count - 1):
    num *= 252533
    num %= 33554393
    # print(f"{i}/{count}: {num}")

print(num)
