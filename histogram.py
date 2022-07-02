# -*- coding: utf-8 -*-
"""
Created on Jun 29 17:59:18 2022

@author: Jerome Yutai Shen

"""
from typing import List
from utils import bisect_right


class Histogram:

    def __init__(self, boundaries: List[float]) -> None:
        self._boundaries = boundaries
        self._histogram = [0] * (len(boundaries) + 1)

    def _update_histogram(self, num: float) -> None:
        idx = bisect_right(self._boundaries, num)
        self._histogram[idx] += 1

    def add_numbers(self, numbers: List[float]) -> None:
        """
        O(Nlog(M)), M is the length of boundaries, N is the length of numbers
        :param numbers:
        :return:
        """
        for num in numbers:
            self._update_histogram(num)

    def histogram(self) -> List[float]:
        return self._histogram


if __name__ == "__main__":
    pass