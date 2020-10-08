#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            if i > 0:
                dp[0][i] = dp[0][i - 1] + grid[0][i]
            else:
                dp[0][i] = grid[0][i]
        for i in range(m):
            if i > 0:
                dp[i][0] = dp[i - 1][0] + grid[i][0]
            else:
                dp[i][0] = grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        return dp[-1][-1]


# @lc code=end
