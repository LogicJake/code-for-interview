from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]],
                            target: int) -> bool:
        n = len(matrix)

        if n == 0:
            return False

        m = len(matrix[0])
        if m == 0:
            return False

        row = 0
        column = m - 1

        while row < n and column >= 0:
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                column -= 1
            else:
                row += 1

        return False