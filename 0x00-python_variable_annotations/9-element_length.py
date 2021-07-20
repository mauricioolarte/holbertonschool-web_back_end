#!/usr/bin/env python3
''' function’s parameters and return values with the appropriate types'''

from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
