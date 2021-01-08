#!/usr/bin/env python3

from typing import Set, Tuple

Coord = Tuple[int, int]

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        pos: Coord = (0, 0)
        visited: Set[Coord] = set()
        visited.add(pos)
        for c in line.strip():
            if c == ">":
                pos = (pos[0] + 1, pos[1])
            elif c == "<":
                pos = (pos[0] - 1, pos[1])
            elif c == "^":
                pos = (pos[0], pos[1] + 1)
            elif c == "v":
                pos = (pos[0], pos[1] - 1)

            visited.add(pos)
        print(len(visited))
