#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return [-1, -1]
        else:
            start = left

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) >> 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        if nums[left] != target:
            return [-1, -1]
        else:
            end = left

        return [start, end]


# @lc code=end
