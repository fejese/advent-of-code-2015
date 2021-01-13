#!/usr/bin/env python3

import re
from typing import List, Set, Tuple

# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    lines = [l.strip() for l in input_file]
    target = lines[-1]
    replacements = [tuple(reversed(l.split(" => "))) for l in lines[:-2]]

MUTATIONS_CACHE: Set[str] = set()


def get_mutations(starts: Set[str], replacements: List[Tuple[str, str]]) -> Set[str]:
    return set(
        start[:match_start] + t + start[match_end:]
        for start in starts
        for f, t in replacements
        for match_start, match_end in [m.span() for m in re.finditer(f, start)]
    )


def get_steps(start: str, target: str, replacements: List[Tuple[str, str]]) -> int:
    steps = 0
    while target != start:
        steps += 1
        print("step:", steps, "cache size:", len(MUTATIONS_CACHE))
        print("start:", start)
        mutations = get_mutations(set([start]), replacements)
        print("mutations:", len(mutations))
        mutations -= MUTATIONS_CACHE
        print("new mutations:", len(mutations))
        MUTATIONS_CACHE.update(mutations)
        start = sorted(mutations, key=lambda s: len(s))[0]

    return steps


print(len(target))
steps = get_steps(target, "e", replacements)
print(steps)
