#!/usr/bin/env python3

from copy import deepcopy
from typing import List, Set, Tuple

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


class HashableList(list):
    def __hash__(self) -> int:
        return str(self).__hash__()


def get_quantum_entanglement(packages: List[int]) -> int:
    ent: int = 1
    for package in packages:
        ent *= package
    return ent


def get_best_config(packages: List[int]) -> HashableList:
    sum_packages: int = sum(packages)
    if sum_packages % 3 != 0:
        raise Exception(f"sum of packages ({sum_packages}) is not divisible by 3!")
    bucket_size: int = sum_packages // 4

    old_cache: Set[HashableList] = set()
    cache: Set[HashableList] = set([HashableList()])
    found_solution: bool = False
    while not found_solution:
        print(len(cache))
        old_cache = cache
        cache = set()

        for config in old_cache:
            config_sum = sum(config)

            for package in packages:
                if package in config:
                    continue
                if config_sum + package > bucket_size:
                    continue
                if config_sum + package == bucket_size:
                    print(config, config_sum, package, bucket_size)
                    found_solution = True

                new_config = HashableList(sorted([*config, package]))
                cache.add(new_config)

    solutions = [x for x in cache if sum(x) == bucket_size]

    def config_rank(config: HashableList) -> Tuple[int, int]:
        return (len(config), get_quantum_entanglement(config))

    ranked_configs = sorted(solutions, key=config_rank)

    return ranked_configs[0]


with open(INPUT_FILE_NAME, "r") as input_file:
    packages = [int(line.strip()) for line in input_file]


best_config = get_best_config(packages)
print(best_config)
ent = get_quantum_entanglement(best_config)
print(ent)
