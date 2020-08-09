#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i > -1 and nums[i] >= nums[i + 1]:
            i -= 1

        if i != -1:
            j = len(nums) - 1
            while (nums[j] <= nums[i]) and j >= 0:
                j -= 1

            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp

        nums[i + 1:] = sorted(nums[i + 1:])


# @lc code=end
