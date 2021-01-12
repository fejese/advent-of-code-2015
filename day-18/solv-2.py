#!/usr/bin/env python3

from typing import List, Tuple
from itertools import product

# INPUT_FILE_NAME: str = "test-input"
# STEPS: int = 5
INPUT_FILE_NAME: str = "input"
STEPS: int = 100


def get_neighbours(grid: List[List[bool]], x: int, y: int) -> List[bool]:
    neigbours: List[bool] = []
    for dx, dy in product(range(-1, 2), range(-1, 2)):
        if dx == 0 and dy == 0:
            continue
        if x + dx < 0 or y + dy < 0:
            continue
        if x + dx >= len(grid) or y + dy >= len(grid):
            continue
        neigbours.append(grid[y + dy][x + dx])

    return neigbours

def step(grid: List[List[bool]], stuck_lights: List[Tuple[int, int]]) -> List[List[bool]]:
    new_grid = [[False] * len(grid) for _ in range(len(grid))]
    for x, y in product(range(len(grid)), range(len(grid))):
        neigbours = get_neighbours(grid, x, y)
        if (x,y) in stuck_lights:
            new_grid[y][x] = True
        elif grid[y][x]:
            new_grid[y][x] = sum(neigbours) in [2, 3]
        else:
            new_grid[y][x] = sum(neigbours) == 3

    return new_grid

def p(title: str, grid: List[List[bool]]) -> None:
    print(f"{title}:")
    for row in grid:
        print("".join(["#" if c else "." for c in row]))
    print()

grid: List[List[bool]]
with open(INPUT_FILE_NAME, "r") as input_file:
    grid = [[c == "#" for c in line.strip()] for line in input_file]

stuck_lights: List[Tuple[int, int]] = [
    (0, 0),
    (0, len(grid) - 1),
    (len(grid) - 1, 0),
    (len(grid) - 1, len(grid) - 1),
]
for x, y in stuck_lights:
    grid[y][x] = True

p("Initial state", grid)

for i in range(STEPS):
    grid = step(grid, stuck_lights)
    p(f"After {i + 1} steps", grid)

on = sum(sum(row) for row in grid)
print("Lights on:", on)
