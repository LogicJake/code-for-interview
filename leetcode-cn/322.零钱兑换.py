#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for coin in coins:
                if x - coin >= 0:
                    dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1


# @lc code=end
