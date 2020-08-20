#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        if nums[0] != 0:
            return 0
        if nums[-1] != len(nums):
            return len(nums)

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                return nums[i - 1] + 1


# @lc code=end
