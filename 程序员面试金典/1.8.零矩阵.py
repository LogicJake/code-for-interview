from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return

        n = len(matrix[0])

        a = []
        b = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    a.append(i)
                    b.append(j)

        for i in range(m):
            for j in range(n):
                if i in a or j in b:
                    matrix[i][j] = 0
