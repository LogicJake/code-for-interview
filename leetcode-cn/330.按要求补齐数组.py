#
# @lc app=leetcode.cn id=330 lang=python3
#
# [330] 按要求补齐数组
#

# @lc code=start
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, x = 0, 1
        length, index = len(nums), 0

        while x <= n:
            if index < length and nums[index] <= x:
                x += nums[index]
                index += 1
            else:
                x <<= 1
                patches += 1

        return patches


# @lc code=end
