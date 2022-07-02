# -*- coding: utf-8 -*-
"""
Created on Jun 29 23:42:12 2022

@author: Jerome Yutai Shen

"""
from typing import List


class Sudoku:
    N = 9

    def __init__(self, give_solution: List[List[int]]):
        self._filled_board = give_solution
        self._reset_status()

    def update_filled_board(self, give_solution: List[List[int]]):
        self._filled_board = give_solution
        self._reset_status()

    def _reset_status(self):
        self._unique = [False] * (self.N + 1)
        self.error_msg = ""
        self.is_valid = True

    def check_valid(self) -> bool:
        is_valid = self._check_valid()

        if self.error_msg:
            self.error_msg = "Invalid\n" + self.error_msg
            assert not is_valid
            print(self.error_msg)
        else:
            assert is_valid
            print("Valid")

        return is_valid

    def _check_value_range(self):
        """
        check whether each value is in the range
        """
        for idx in range(0, self.N):
            for idx_col in range(0, self.N):
                if ((self._filled_board[idx][idx_col] <= 0) or
                        (self._filled_board[idx][idx_col] > 9)):
                    self.error_msg += f"row {idx} column {idx_col} is out of the range [0, 9)\n"
                    self.is_valid = False

    def _check_row(self):
        for idx in range(self.N):
            self._unique = [False] * (self.N + 1)
            for idx_col in range(self.N):
                Z = self._filled_board[idx][idx_col]
                if self._unique[Z]:
                    self.error_msg += f"The row {idx} has duplicate values\n"
                    self.is_valid = False
                self._unique[Z] = True

    def _check_column(self):
        for idx_col in range(self.N):
            self._unique = [False] * (self.N + 1)
            for idx in range(self.N):
                Z = self._filled_board[idx][idx_col]
                if self._unique[Z]:
                    self.error_msg += f"The column {idx_col} has duplicate values\n"
                    self.is_valid = False
                self._unique[Z] = True

    def _check_block(self):
        for i in range(0, self.N - 2, 3):
            for j in range(0, self.N - 2, 3):
                self._unique = [False] * (self.N + 1)
                for k in range(0, 3):
                    for l in range(0, 3):
                        idx_row = i + k
                        idx_col = j + l
                        Z = self._filled_board[idx_row][idx_col]

                        if self._unique[Z]:
                            self.error_msg += f"The block {idx_row // 3, idx_col // 3} has duplicate values\n"
                            self.is_valid = False

                        self._unique[Z] = True

    def _check_valid(self) -> bool:
        self._check_value_range()
        self._check_row()
        self._check_column()
        self._check_block()

        return self.is_valid


if __name__ == "__main__":
    pass