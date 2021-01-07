#!/usr/bin/env python3

import re
from itertools import permutations as P
from typing import Dict, List, Tuple, Set

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

LINE_PATTERN: re.Pattern = re.compile(
    r"^(\S+) would (lose|gain) (\d+) happiness units by sitting next to (\S+)\.$"
)


def K(pers_a: str, pers_b: str) -> Tuple[str, str]:
    return tuple(sorted([pers_a, pers_b]))


costs: Dict[Tuple[str, str], int] = {}
people: Set[str] = set()
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        m = LINE_PATTERN.match(line)
        if not m:
            raise Exception(f"Can't parse line: {line}")
        pers_a, action, value, pers_b = m.groups()

        key = K(pers_a, pers_b)
        value = int(value)
        if action == "lose":
            value *= -1

        if key in costs:
            costs[key] += value
        else:
            costs[key] = value
            people.add(pers_a)
            people.add(pers_b)

print(costs)

part1 = max(
    sum(
        costs[tuple(sorted([perm[i], perm[(i + 1) % len(perm)]]))]
        for i in range(len(perm))
    )
    for perm in P(people)
)
print("part 1:", part1)

me = "foobar"
for p in people:
    costs[K(me, p)] = 0
people.add(me)

print(costs)

part2 = max(
    sum(
        costs[tuple(sorted([perm[i], perm[(i + 1) % len(perm)]]))]
        for i in range(len(perm))
    )
    for perm in P(people)
)
print("part 2:", part2)
