#!/usr/bin/env python3

import re
from typing import Callable, Dict, List, Optional, Tuple, Union

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

STATIC_PATTERN = re.compile(r"^(\S+) -> (\S+)$")
UNARY_OP_PATTERN = re.compile(r"^(\S+) (\S+) -> (\S+)$")
BINARY_OP_PATTERN = re.compile(r"^(\S+) (\S+) (\S+) -> (\S+)$")

Logic = Callable[[List[int]], int]
Input = Tuple[Logic, List[Union[str, int]]]

LOGICS: Dict[str, Logic] = {
    "static": lambda l: l[0],
    "AND": lambda l: l[0] & l[1],
    "OR": lambda l: l[0] | l[1],
    "NOT": lambda l: l[0] ^ 65535,
    "LSHIFT": lambda l: l[0] << l[1],
    "RSHIFT": lambda l: l[0] >> l[1],
}


def sanitize_params(matches: List[str]) -> List[Union[str, int]]:
    return [int(m) if m.isdecimal() else m for m in matches]


def solve(override_b: Optional[int] = None) -> int:
    wire_to_signal: Dict[str, int] = {}
    wire_to_input: Dict[str, Input] = {}

    with open(INPUT_FILE_NAME, "r") as input_file:
        for line in input_file:
            static_m = STATIC_PATTERN.match(line)
            if static_m:
                wire = static_m[2]
                params = sanitize_params([static_m[1]])
                wire_to_input[wire] = (LOGICS["static"], params)
                continue

            unary_m = UNARY_OP_PATTERN.match(line)
            if unary_m:
                wire = unary_m[3]
                params = sanitize_params([unary_m[2]])
                wire_to_input[wire] = (LOGICS[unary_m[1]], params)
                continue

            binary_m = BINARY_OP_PATTERN.match(line)
            if binary_m:
                wire = binary_m[4]
                params = sanitize_params([binary_m[1], binary_m[3]])
                wire_to_input[wire] = (LOGICS[binary_m[2]], params)
                continue

            raise Exception(f"Can't parse line: {line}")

    if override_b:
        wire_to_input["b"] = (LOGICS["static"], [override_b])

    while "a" not in wire_to_signal:
        for wire, input in wire_to_input.items():
            logic, params = input
            new_params = [
                wire_to_signal[p] if isinstance(p, str) and p in wire_to_signal else p
                for p in params
            ]
            if new_params != params:
                wire_to_input[wire] = (logic, new_params)
                # print(f"Resolved params for {wire}: {params} -> {new_params}")
                params = new_params

            if all(isinstance(p, int) for p in params):
                wire_to_signal[wire] = logic(params)
                # print(f"Resolved signal for {wire}: {params} -> {wire_to_signal[wire]}")
                del wire_to_input[wire]
                break

    return wire_to_signal["a"]


a = solve()
print(a)
a = solve(a)
print(a)
