# -*- coding: utf-8 -*-
"""
Created on Jun 29 23:39:58 2022

@author: Jerome Yutai Shen

"""
from typing import List


def bisect_right(boundaries: List[float], num: float):
    """
    returns idx where all boundaries[: idx] is less than or equal to num
    :param boundaries:
    :param num:
    :return:
    """

    lo, hi = 0, len(boundaries)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if boundaries[mid] > num:
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    pass
