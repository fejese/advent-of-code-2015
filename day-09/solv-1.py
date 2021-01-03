#!/usr/bin/env python3

import re
from itertools import permutations as P
from typing import Dict, List, Tuple, Set

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

LINE_PATTERN: re.Pattern = re.compile(r"^(\S+) to (\S+) = (\d+)$")

distances: Dict[Tuple[str, str], int] = {}
cities: Set[str] = set()
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        m = LINE_PATTERN.match(line)
        if not m:
            raise Exception(f"Can't parse line: {line}")

        distances[tuple(sorted([m[1], m[2]]))] = int(m[3])
        cities.add(m[1])
        cities.add(m[2])


print(
    min(
        sum(
            distances[tuple(sorted([perm[i], perm[i + 1]]))]
            for i in range(len(perm) - 1)
        )
        for perm in P(cities)
    )
)
