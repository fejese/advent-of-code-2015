#!/usr/bin/env python3

from math import ceil
from typing import List
from dataclasses import dataclass, field
from itertools import combinations as C

# Equipment rules:
#  - exactly 1 weapon
#  - 0 or 1 armor
#  - 0 to 2 rings
#  - must use all equipment
#  - each item is unique

TEST: bool = False


@dataclass
class Equipment:
    cost: int
    damage: int
    armor: int


WEAPONS: List[Equipment] = [
    Equipment(8, 4, 0),
    Equipment(10, 5, 0),
    Equipment(25, 6, 0),
    Equipment(40, 7, 0),
    Equipment(74, 8, 0),
]
ARMORS: List[Equipment] = [
    Equipment(0, 0, 0),
    Equipment(13, 0, 1),
    Equipment(31, 0, 2),
    Equipment(53, 0, 3),
    Equipment(75, 0, 4),
    Equipment(102, 0, 5),
]
RINGS: List[Equipment] = [
    Equipment(25, 1, 0),
    Equipment(50, 2, 0),
    Equipment(100, 3, 0),
    Equipment(20, 0, 1),
    Equipment(40, 0, 2),
    Equipment(80, 0, 3),
]


@dataclass
class Player:
    hit_points: int
    equipment: List[Equipment] = field(default_factory=list)

    @property
    def damage(self) -> int:
        return sum(e.damage for e in self.equipment)

    @property
    def armor(self) -> int:
        return sum(e.armor for e in self.equipment)


if TEST:
    player: Player = Player(hit_points=8)
    boss: Player = Player(
        hit_points=12, equipment=[Equipment(cost=0, damage=7, armor=2)]
    )
else:
    player: Player = Player(hit_points=100)
    boss: Player = Player(
        hit_points=100, equipment=[Equipment(cost=0, damage=8, armor=2)]
    )

print(boss.damage)

max_cost: int = 0
max_eq: List[Equipment] = []
for weapon in WEAPONS:
    for armor in ARMORS:
        for rings in [[]] + [[r] for r in RINGS] + list(C(RINGS, 2)):
            equipment = [weapon, armor] + list(rings)
            player_damage = max(1, sum(e.damage for e in equipment) - boss.armor)
            boss_damage = max(1, boss.damage - sum(e.armor for e in equipment))
            if ceil(boss.hit_points / player_damage) <= ceil(
                player.hit_points / boss_damage
            ):
                continue
            cost = sum(e.cost for e in equipment)
            if cost > max_cost:
                max_cost = cost
                max_eq = equipment
print(max_cost)
print(max_eq)
