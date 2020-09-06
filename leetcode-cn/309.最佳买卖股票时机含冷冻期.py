#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp = [[-prices[0], 0, 0]] + [[0, 0, 0] for _ in range(n - 1)]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])

        return max(dp[n - 1][1], dp[n - 1][2])


# @lc code=end
