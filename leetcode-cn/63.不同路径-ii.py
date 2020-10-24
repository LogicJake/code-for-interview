#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m == 0:
            return 0

        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] != 1:
                    if i - 1 >= 0:
                        dp[i][j] += dp[i - 1][j]
                    if j - 1 >= 0:
                        dp[i][j] += dp[i][j - 1]

        print(dp)
        return dp[-1][-1]


# @lc code=end
