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

        max_k = k
        dp = [[[0, 0] for _ in range(max_k + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')

        for i in range(n):
            for k in range(max_k, 0, -1):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[0]
                else:
                    dp[i][k][0] = max(dp[i - 1][k][0],
                                      dp[i - 1][k][1] + prices[i])

                    dp[i][k][1] = max(dp[i - 1][k][1],
                                      dp[i - 1][k - 1][0] - prices[i])

        return dp[-1][max_k][0]


# @lc code=end
