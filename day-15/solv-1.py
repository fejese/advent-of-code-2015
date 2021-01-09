#!/usr/bin/env python3

import re
from itertools import accumulate
from typing import Dict, Tuple, List

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

LINE_PATTERN: re.Pattern = re.compile(
    r"(\S+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)$"
)

Properties = Tuple[int, int, int, int]


def get_score(ingredients: Dict[str, Properties], combination: Dict[str, int]) -> int:
    total_props = (0, 0, 0, 0)
    for name, props in ingredients.items():
        cnt = combination[name]
        total_props = tuple(
            total_props[i] + props[i] * cnt for i in range(len(total_props))
        )
    if any(prop < 0 for prop in total_props):
        return 0

    return [x for x in accumulate(total_props, lambda x, y: x * y)][-1]


ingredients: Dict[str, Properties] = {}
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        m = LINE_PATTERN.match(line)
        if not m:
            raise Exception(f"Can't parse line: {line}")
        name = m.group(1)
        ingredients[name] = tuple(int(prop) for prop in m.groups()[1:-1])
names = list(ingredients.keys())

print(ingredients)

max_score = 0
max_comb = {n: 0 for n in names}
for i in range(101):
    for j in range(101 - i):
        for k in range(101 - i - j):
            for l in range(101 - i - j - k):
                counts = [i, j, k, l]
                # counts = [i, j]
                combination = {n: cnt for n, cnt in zip(names, counts)}
                score = get_score(ingredients, combination)
                if score > max_score:
                    max_comb = combination
                    max_score = score

print("max score:", max_score)
print("max combination:", max_comb)
