# -*- coding: utf-8 -*-
"""
Created on Jun 29 21:51:02 2022

@author: Jerome Yutai Shen

"""

import unittest
from histogram import Histogram


class TestHistogram(unittest.TestCase):

    def test_init(self):
        boundaries = [0, 5, 10]
        hist = Histogram(boundaries)
        self.assertEqual(hist._boundaries, boundaries)
        self.assertEqual(hist._histogram, [0] * (len(boundaries) + 1))

    def test_add_numbers(self):
        boundaries = [0, 5, 10]
        hist = Histogram(boundaries)

        hist.add_numbers([1, 9, 12, 5, 6])
        self.assertEqual(hist.histogram(), [0, 1, 3, 1])

        hist.add_numbers([4, 11])
        self.assertEqual(hist.histogram(), [0, 2, 3, 2])


if __name__ == "__main__":
    unittest.main()
