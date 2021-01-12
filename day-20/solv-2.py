#!/usr/bin/env python3

import math
from typing import List, Set

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    TARGET: int = int(input_file.read().strip())

with open("first_10m_primes.txt", "r") as prime_file:
    PRIMES: List[int] = [int(line.strip()) for line in prime_file]

def get_dividers(n:int) -> List[int]:
    dividers: Set[int] = set([1])
    for prime in PRIMES:
        while n % prime == 0:
            dividers.update([prime * dp for dp in dividers])
            dividers.add(prime)
            n //= prime
        if prime > n:
            break

    return dividers


def get_present_count(n: int) -> int:
    count = sum(d for d in get_dividers(n) if n / d < 50) * 11
    return count

n: int = 0
count: int = 0
max_present_count: int = 0
while max_present_count < TARGET:
    n += 1
    count = get_present_count(n)
    max_present_count = max(max_present_count, get_present_count(n))
    if n % 10000 == 0:
        print("just tried", n, "count:", count, "max present count:", max_present_count)
print("n:", n)
print("dividers:", get_dividers(n))
print("count:", count)
