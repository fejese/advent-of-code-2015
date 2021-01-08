#!/usr/bin/env python3

import re
from typing import Dict

# INPUT_FILE_NAME: str = "test-input"
# DEADLINE: int = 1000
INPUT_FILE_NAME: str = "input"
DEADLINE: int = 2503

LINE_PATTERN: re.Pattern = re.compile(
    r"^(\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.$"
)


distances: Dict[str, int] = {}
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        m = LINE_PATTERN.match(line)
        if not m:
            raise Exception(f"Can't parse line: {line}")
        name, speed, flight_time, rest_time = m.groups()
        speed = int(speed)
        flight_time = int(flight_time)
        rest_time = int(rest_time)
        cycle_time = flight_time + rest_time
        full_flights = (DEADLINE + rest_time) // cycle_time
        remainder = max(0, DEADLINE - full_flights * cycle_time)
        total_flight_time = full_flights * flight_time + remainder
        distance = total_flight_time * speed
        distances[name] = distance

print(distances)
print(max(distances.values()))
