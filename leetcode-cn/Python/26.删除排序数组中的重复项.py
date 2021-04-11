#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        i = -1
        for j in range(0, len(nums)):
            if j == 0 or nums[j] != nums[j - 1]:
                i += 1
                nums[i] = nums[j]

        return i + 1


# @lc code=end
