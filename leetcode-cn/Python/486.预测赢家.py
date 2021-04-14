#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#

# @lc code=start
from typing import List


class Solution:
    # def PredictTheWinner(self, nums: List[int]) -> bool:
    #     def helper(i, j, turn):
    #         if i == j:
    #             return nums[i] * turn

    #         pickI = nums[i] * turn + helper(i + 1, j, -turn)
    #         pickJ = nums[j] * turn + helper(i, j - 1, -turn)

    #         if turn == 1:
    #             return max(pickI, pickJ)
    #         else:
    #             return min(pickI, pickJ)

    #     return helper(0, len(nums) - 1, 1) >= 0

    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [[0] * length for _ in range(length)]

        for i, num in enumerate(nums):
            dp[i][i] = num

        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][length - 1] >= 0


# @lc code=end
