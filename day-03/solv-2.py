#!/usr/bin/env python3

from typing import List, Set, Tuple

Coord = Tuple[int, int]

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        poss: List[Coord] = [(0, 0), (0, 0)]
        pos_idx = 0
        visited: Set[Coord] = set()
        visited.add(poss[0])
        for c in line.strip():
            if c == ">":
                poss[pos_idx] = (poss[pos_idx][0] + 1, poss[pos_idx][1])
            elif c == "<":
                poss[pos_idx] = (poss[pos_idx][0] - 1, poss[pos_idx][1])
            elif c == "^":
                poss[pos_idx] = (poss[pos_idx][0], poss[pos_idx][1] + 1)
            elif c == "v":
                poss[pos_idx] = (poss[pos_idx][0], poss[pos_idx][1] - 1)
            visited.add(poss[pos_idx])
            pos_idx ^= 1
        print(len(visited))
