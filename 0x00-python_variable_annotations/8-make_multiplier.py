#!/usr/bin/env python3
""" Complex type modules"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function multiplier

    params:

    multiplier (float) float
    return function
    """

    def fun(n: float) -> float:
        """ multiplie float by multiplier"""
        return float(n * multiplier)

    return fun
