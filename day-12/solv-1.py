#!/usr/bin/env python3

import json

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


def sum_numbers(data) -> int:
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        return sum(sum_numbers(e) for e in data)
    if isinstance(data, dict):
        return sum(sum_numbers(e) for e in data.values())
    return 0


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        print(sum_numbers(json.loads(line)))
