#!/usr/bin/env python3

from typing import List

# INPUT_FILE_NAME: str = "test-input"
# TARGET: int = 25
INPUT_FILE_NAME: str = "input"
TARGET: int = 150

with open(INPUT_FILE_NAME, "r") as input_file:
    buckets = [int(line.strip()) for line in input_file]


def solve(buckets: List[int], target: int, bucket_limit: int) -> int:
    if not target:
        return 1
    if not buckets or bucket_limit == 0 or target < min(buckets):
        return 0

    combinations = solve(buckets[1:], target - buckets[0], bucket_limit - 1) + solve(
        buckets[1:], target, bucket_limit
    )

    return combinations


for bucket_limit in range(len(buckets)):
    combinations = solve(buckets, TARGET, bucket_limit)
    print(f"{combinations} combinations using {bucket_limit} buckets")
    if combinations:
        break
