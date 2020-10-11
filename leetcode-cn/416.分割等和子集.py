#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        n = len(nums)
        maxNum = max(nums)

        if sum_ % 2 != 0:
            return False

        target = sum_ // 2
        if maxNum > target:
            return False

        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return bool(dp[n - 1][target])


# @lc code=end
