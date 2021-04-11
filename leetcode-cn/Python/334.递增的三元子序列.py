#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        small = 999999999999999
        mid = 999999999999999

        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            elif num > mid:
                return True

        return False


# @lc code=end
