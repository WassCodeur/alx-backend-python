#!/usr/bin/env python3

def sum_list(input_list: list[float]) -> float:
    """function sum_list

    params: list of float

    return sum af list as float
    """
    sum_l: float = 0.0
    for i in input_list:
        sum_l += i
    return sum_l
