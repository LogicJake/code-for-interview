#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0

        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0][1] = -float('inf')

        for i in range(n):
            for j in range(k, 0, -1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0],
                                      dp[i - 1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1],
                                      dp[i - 1][j - 1][0] - prices[i])

        return dp[-1][-1][0]


# @lc code=end
