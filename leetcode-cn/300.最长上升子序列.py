#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [1] * len(nums)

        for i in range(len(nums)):
            max_cnt = 0

            for j in range(0, i):
                if nums[i] > nums[j] and dp[j] > max_cnt:
                    max_cnt = dp[j]

            dp[i] = max_cnt + 1

        return max(dp)


# @lc code=end
