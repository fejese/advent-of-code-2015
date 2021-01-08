#!/usr/bin/env python3

import re
from typing import Callable, Dict, List

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

PARSER: re.Pattern = re.compile(
    r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$"
)
ACTIONS: Dict[str, Callable[[bool], bool]] = {
    "turn on": lambda state: True,
    "turn off": lambda state: False,
    "toggle": lambda state: not state,
}

grid: List[List[bool]] = [[False] * 1000 for _ in range(1000)]

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
                grid[x][y] = action(grid[x][y])

print(sum(sum(line) for line in grid))
