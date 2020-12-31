#!/usr/bin/env python3

import re
from typing import Callable, Dict, List

# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input"

PARSER: re.Pattern = re.compile(
    r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$"
)
ACTIONS: Dict[str, Callable[[int], int]] = {
    "turn on": lambda state: state + 1,
    "turn off": lambda state: max(0, state - 1),
    "toggle": lambda state: state + 2,
}

grid: List[List[int]] = [[0] * 1000 for _ in range(1000)]

with open(INPUT_FILE_NAME, "r") as input_file:
    for lineno, line in enumerate(input_file):
        m = PARSER.match(line)
        if not m:
            raise Exception(f"Line no {lineno} ({line}) is weird")
        action_name = m[1]
        if action_name not in ACTIONS:
            raise Exception(
                f"Line no {lineno} ({line}) has unknown action: {action_name}"
            )
        action = ACTIONS[action_name]

        x_min, y_min, x_max, y_max = [int(n) for n in m.groups()[1:]]

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                # print(f"{action_name} {x} {y} {grid[x][y]} -> {action(grid[x][y])}")
                grid[x][y] = action(grid[x][y])

print(sum(sum(line) for line in grid))
