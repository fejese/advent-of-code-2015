#!/usr/bin/env python3

import re

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    lines = [l.strip() for l in input_file]
    start = lines[-1]
    replacements = [tuple(l.split(" => ")) for l in lines[:-2]]

print(replacements)
print(start)

molecules = set(
    start[:match_start] + t + start[match_end:]
    for f, t in replacements
    for match_start, match_end in [m.span() for m in re.finditer(f, start)]
)

print(molecules)
print(len(molecules))
