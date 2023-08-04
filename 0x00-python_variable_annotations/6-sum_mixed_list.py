#!/usr/bin/env python3

def sum_mixed_list(mxd_lst: list[float, int]) -> float:
    """function sum_list

    params: list of float

    return sum af list as float
    """
    sum_l: float = 0.0
    for i in mxd_lst:
        sum_l += i
    return sum_l
