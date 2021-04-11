#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            dp[i] = dp[i - 1] + nums[i]
        self.dp = dp
        print(dp)

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end
