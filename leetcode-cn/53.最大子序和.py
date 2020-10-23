#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)


# @lc code=end
