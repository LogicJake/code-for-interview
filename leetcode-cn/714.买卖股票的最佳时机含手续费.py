#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[0]
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)

                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]


# @lc code=end
