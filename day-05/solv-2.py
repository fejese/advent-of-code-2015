#!/usr/bin/env python3

from typing import List

INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


def is_nice(s: str) -> bool:
    rule_1_matches = False
    rule_2_matches = False
    for i in range(len(s) - 1):
        if not rule_1_matches and s[i : i + 2] in s[i + 2 :]:
            rule_1_matches = True
        if not rule_2_matches and i < len(s) - 2 and s[i] == s[i + 2]:
            rule_2_matches = True
        if rule_1_matches and rule_2_matches:
            print(f"{s}: NICE")
            return True
    if not rule_1_matches and not rule_2_matches:
        print(f"{s}: NAUGHTY (neither rule match)")
    elif not rule_1_matches:
        print(f"{s}: NAUGHTY (rule #1 doesn't match)")
    else:
        print(f"{s}: NAUGHTY (rule #2 doesn't match)")
    return False


matches = 0
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        if is_nice(line.strip()):
            matches += 1

print(matches)
