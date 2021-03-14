#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums)

        if nums[right - 1] > nums[left]:
            return nums[0]

        while left < right:
            mid = (left + right) // 2
            if mid + 1 < right and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if mid - 1 > -1 and nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid


# @lc code=end
