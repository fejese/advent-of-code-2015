#!/usr/bin/env python3

import re
from typing import List, Set, Tuple

# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    target = [l.strip() for l in input_file][-1]


# #NumSymbols - #Rn - #Ar - 2 * #Y - 1

print(
    len(target)
    - len(list(re.finditer("Rn", target)))
    - len(list(re.finditer("Ar", target)))
    - target.count("Y") * 2
    - 1
)
