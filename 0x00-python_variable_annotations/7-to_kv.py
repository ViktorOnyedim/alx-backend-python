#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string and the square of the number.
    """
    return (k, float(v**2))
