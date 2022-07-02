# -*- coding: utf-8 -*-
"""
Created on Jul 01 08:13:27 2022

@author: Jerome Yutai Shen

"""
import unittest
from sudoku import Sudoku


SOLUTIONS = [[[7, 9, 2, 1, 5, 4, 3, 8, 6],
              [6, 4, 3, 8, 2, 7, 1, 5, 9],
              [8, 5, 1, 3, 9, 6, 7, 2, 4],
              [2, 6, 5, 9, 7, 3, 8, 4, 1],
              [4, 8, 9, 5, 6, 1, 2, 7, 3],
              [3, 1, 7, 4, 8, 2, 9, 6, 5],
              [1, 3, 6, 7, 4, 8, 5, 9, 2],
              [9, 7, 4, 2, 1, 5, 6, 3, 8],
              [5, 2, 8, 6, 3, 9, 4, 1, 7]],
             [[5, 5, 5, 5, 5, 5, 5, 5, 5],
              [5, 5, 5, 5, 5, 5, 5, 5, 5],
              [5, 5, 5, 5, 5, 5, 5, 5, 5],
              [5, 5, 5, 5, 5, 5, 5, 5, 5],
              [5, 5, 5, 5, 5, 5, 5, 5, 5],
              [5, 5, 5, 5, 5, 5, 5, 5, 5],
              [5, 5, 5, 5, 5, 5, 5, 5, 5],
              [5, 5, 5, 5, 5, 5, 5, 5, 5],
              [5, 5, 5, 5, 5, 5, 5, 5, 5]],
             [[7, 9, 2, 1, 5, 4, 3, 8, 9],
              [6, 4, 3, 8, 2, 7, 1, 5, 9],
              [8, 5, 1, 3, 9, 6, 7, 2, 4],
              [2, 6, 5, 9, 7, 3, 8, 4, 1],
              [4, 8, 9, 5, 6, 1, 2, 7, 3],
              [3, 1, 7, 4, 8, 2, 9, 6, 5],
              [1, 3, 6, 7, 4, 8, 5, 9, 2],
              [9, 7, 4, 2, 1, 5, 6, 3, 8],
              [5, 2, 8, 6, 3, 9, 4, 1, 7]]]


class TestSudoku(unittest.TestCase):

    def test_init(self):
        for given_solution in SOLUTIONS:
            sudoku = Sudoku(given_solution)
            self.assertEqual(sudoku._filled_board, given_solution)

    def test_check_valid(self):
        sudoku = Sudoku(SOLUTIONS[0])
        self.assertEqual(sudoku.check_valid(), True)

        sudoku.update_filled_board(SOLUTIONS[1])
        self.assertEqual(sudoku.check_valid(), False)

        sudoku.update_filled_board(SOLUTIONS[2])
        self.assertEqual(sudoku.check_valid(), False)


if __name__ == "__main__":
    unittest.main()
