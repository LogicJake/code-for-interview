#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#

# @lc code=start
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)

        if m == 0:
            return

        n = len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = matrix[0][0]

        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + matrix[0][i]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + matrix[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][
                    j - 1] + matrix[i][j]

        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2][col2] - self.dp[row1 - 1][col2] - self.dp[row2][
            col1 - 1] + self.dp[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
