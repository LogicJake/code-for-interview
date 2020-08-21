#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        jsquare = [j**2 for j in range(int(sqrt(n)) + 1)]

        for i in range(1, n + 1):
            dp[i] = i
            for j in jsquare:
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i - j] + 1)

        return dp[n]


# @lc code=end
