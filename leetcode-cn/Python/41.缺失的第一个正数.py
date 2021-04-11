#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1

        if min(nums) > 1:
            return 1

        if max(nums) < 1:
            return 1

        start = min(nums)
        if min(nums) < 1:
            start = 1

        end = max(nums) + 2

        for i in range(start, end):
            if i not in nums:
                return i


# @lc code=end
