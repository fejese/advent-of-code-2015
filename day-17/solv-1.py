#!/usr/bin/env python3

from typing import List

# INPUT_FILE_NAME: str = "test-input"
# TARGET: int = 25
INPUT_FILE_NAME: str = "input"
TARGET: int = 150

with open(INPUT_FILE_NAME, "r") as input_file:
    buckets = [int(line.strip()) for line in input_file]


def solve(buckets: List[int], target: int, level: int = 0) -> int:
    if not target:
        return 1
    if not buckets or target < min(buckets):
        return 0

    combinations = solve(buckets[1:], target - buckets[0]) + solve(buckets[1:], target)

    return combinations


print(solve(buckets, TARGET))
