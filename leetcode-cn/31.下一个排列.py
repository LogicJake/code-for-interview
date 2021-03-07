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

        # 从后向前搜索找到第一个小于后一个数的值
        n = len(nums)

        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i != -1:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = sorted(nums[i + 1:])


# @lc code=end
