#!/usr/bin/env python3

import math
from typing import List, Set

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    TARGET: int = int(input_file.read().strip()) / 10

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
    # if n != 1:
    #     PRIMES.append(n)
    #     dividers.update([n * dp for dp in dividers])
    #     dividers.add(n)

    return dividers


def get_present_count(n: int) -> int:
    count = sum(get_dividers(n))
    return count

n = 0
max_present_count: int = 0
while max_present_count < TARGET:
    n += 1
    max_present_count = max(max_present_count, get_present_count(n))
    if n % 10000 == 0:
        print("just tried", n, "max present count:", max_present_count)
print("n:", n)
print("dividers:", get_dividers(n))
print("sum:", get_present_count(n))
