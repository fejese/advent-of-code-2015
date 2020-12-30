#!/usr/bin/env python3

import re
from typing import List

INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

CHARS: str = "".join([chr(ascii) for ascii in range(ord("a"), ord("z") + 1)])
VOWELS: str = "aeiou"
BLACKLIST: List[str] = ["ab", "cd", "pq", "xy"]

RAW_PATTERNS: List[str] = [
    f"(?:.*[{VOWELS}]){{3,}}.*",
    "".join([".*(", "|".join([f"{c}{c}" for c in CHARS]), ").*"]),
    "".join(["^(?!.*(?:", "|".join(BLACKLIST), "))"]),
]
PATTERNS: List[re.Pattern] = [re.compile(pattern) for pattern in RAW_PATTERNS]


def is_nice(s: str) -> bool:
    for pi, pattern in enumerate(PATTERNS):
        if not pattern.match(s):
            print(
                f"{s}: NAUGHTY (Pattern #{pi + 1} does not match: {RAW_PATTERNS[pi]})"
            )
            return False
    print(f"{s}: NICE")
    return True


matches = 0
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        if is_nice(line.strip()):
            matches += 1

print(matches)
