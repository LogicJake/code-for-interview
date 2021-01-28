#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#

# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        left = 0
        for i in range(len(nums)):
            right = total - left - nums[i]

            if right == left:
                return i

            left += nums[i]

        return -1


# @lc code=end
