#!/usr/bin/env python3
""" Complex type modules"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ function to_kv

    params:

    k (str) string

    v (int or float) value

    return

    tuple
    """
    return (k, v**2)
