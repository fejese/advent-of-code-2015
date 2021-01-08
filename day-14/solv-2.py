#!/usr/bin/env python3

import re
from typing import Dict, List

# INPUT_FILE_NAME: str = "test-input"
# DEADLINE: int = 1000
INPUT_FILE_NAME: str = "input"
DEADLINE: int = 2503

LINE_PATTERN: re.Pattern = re.compile(
    r"^(\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.$"
)


class R:
    def __init__(self, line: str) -> None:
        m = LINE_PATTERN.match(line)
        if not m:
            raise Exception(f"Can't parse line: {line}")
        self.name, speed, flight_time, rest_time = m.groups()
        self.speed = int(speed)
        self.flight_time = int(flight_time)
        self.rest_time = int(rest_time)
        self.cycle_time = self.flight_time + self.rest_time
        self.points = 0

    def get_pos(self, time: int) -> None:
        full_flights = (time + self.rest_time) // self.cycle_time
        remainder = max(0, time - full_flights * self.cycle_time)
        total_flight_time = full_flights * self.flight_time + remainder
        return total_flight_time * self.speed

    def __str__(self) -> str:
        return f"[{self.name} / {self.points}]"

    def __repr__(self) -> str:
        return str(self)


rs: List[R]
with open(INPUT_FILE_NAME, "r") as input_file:
    rs = [R(line) for line in input_file]

for time in range(1, DEADLINE + 1):
    max_pos = max(r.get_pos(time) for r in rs)
    for r in rs:
        if r.get_pos(time) == max_pos:
            r.points += 1

print(rs)
