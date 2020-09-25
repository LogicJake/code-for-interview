#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#

# @lc code=start
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        if n == 0:
            return []

        dp = [0] * n
        dp[0] = [nums[0]]

        ans = dp[0]
        for i in range(1, n):
            dp[i] = [nums[i]]

            for j in range(i):

                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j][:]
                        dp[i].append(nums[i])

            if len(ans) < len(dp[i]):
                ans = dp[i]
        return ans


# @lc code=end
