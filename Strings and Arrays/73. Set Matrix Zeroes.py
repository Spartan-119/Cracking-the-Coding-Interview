# medium
"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

from typing import *

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        # set rows to zero
        for row in zero_rows:
            for col in range(cols):
                matrix[row][col] = 0
        
        # set cols to zero
        for col in zero_cols:
            for row in range(rows):
                matrix[row][col] = 0